#!/usr/bin/env python3
"""SP-04 constructor/replay emitter.

This implementation constructs divisor lists from a complete factorization of x,
using the Cartesian product of exponent ranges for x^2.  It emits evidence but
is not the independent verifier; see sp04_verifier.py.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Iterable, Sequence

B = 23
GAPS = (3, 7, 11, 15, 19, 23)
TYPE_ORDER = ("I", "II")
CONTROL_PRIMES = (73, 241441, 2689, 12721, 1201, 2521, 21169)
EXTERNAL_CONTROLS = ((21169, 31),)
ROOT = Path(__file__).resolve().parent
REPLAY_DIR = ROOT / "replays"
BINDING_DIR = ROOT / "bindings"


@dataclass(frozen=True)
class Hit:
    m: int
    d: int
    kind: str
    x: int
    y: int
    z: int


@dataclass(frozen=True)
class DivisorRow:
    d: int
    i_residue: int
    i_hit: bool
    ii_eligible: bool
    ii_residue: int
    ii_hit: bool
    i_y: int | None
    i_z: int | None
    ii_y: int | None
    ii_z: int | None
    i_lhs: int | None
    i_rhs: int | None
    ii_lhs: int | None
    ii_rhs: int | None


def nat(n: int) -> bytes:
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"expected a nonnegative integer, got {n!r}")
    return str(n).encode("ascii")


def frame(payload: bytes) -> bytes:
    return nat(len(payload)) + b":" + payload


def record(tag: str, fields: Sequence[tuple[str, bytes]]) -> bytes:
    out = bytearray()
    out += frame(tag.encode("ascii"))
    out += frame(nat(len(fields)))
    for name, value in fields:
        out += frame(name.encode("ascii"))
        out += frame(value)
    return bytes(out)


def list_value(items: Sequence[bytes]) -> bytes:
    out = bytearray()
    out += frame(b"SP04.LIST.v1")
    out += frame(nat(len(items)))
    for item in items:
        out += frame(item)
    return bytes(out)


def text(s: str) -> bytes:
    return s.encode("utf-8")


def boolean(v: bool) -> bytes:
    return b"1" if v else b"0"


def sha256_hex(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    for r in range(2, math.isqrt(n) + 1):
        if n % r == 0:
            return False
    return True


def factor_trial(n: int) -> tuple[tuple[int, int], ...]:
    if n < 1:
        raise ValueError("factorization requires n >= 1")
    remaining = n
    q = 2
    factors: list[tuple[int, int]] = []
    while q * q <= remaining:
        if remaining % q == 0:
            exponent = 0
            while remaining % q == 0:
                remaining //= q
                exponent += 1
            factors.append((q, exponent))
        q = 3 if q == 2 else q + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def divisors_of_square_from_factorization(
    factors: Sequence[tuple[int, int]],
) -> tuple[int, ...]:
    pools = [tuple(q**e for e in range(2 * a + 1)) for q, a in factors]
    if not pools:
        return (1,)
    values = [math.prod(choice) for choice in product(*pools)]
    values.sort()
    if len(values) != len(set(values)):
        raise AssertionError("factor-exponent construction emitted a duplicate divisor")
    return tuple(values)


def exact_identity(p: int, x: int, y: int, z: int) -> tuple[int, int]:
    return 4 * x * y * z, p * (y * z + x * z + x * y)


def make_gap(p: int, m: int, scope: str) -> dict:
    if (p + m) % 4 != 0:
        raise ValueError(f"x is not integral for p={p}, m={m}")
    x = (p + m) // 4
    factors = factor_trial(x)
    divisors = divisors_of_square_from_factorization(factors)
    rows: list[DivisorRow] = []
    hits: list[Hit] = []

    for d in divisors:
        i_residue = (p * x + d) % m
        i_hit = i_residue == 0
        ii_eligible = d <= x
        ii_residue = (x + d) % m
        ii_hit = ii_eligible and ii_residue == 0

        i_y = i_z = i_lhs = i_rhs = None
        if i_hit:
            if (p * x + d) % m != 0 or x * x % d != 0:
                raise AssertionError("invalid Type-I hit")
            i_y = (p * x + d) // m
            numerator = p * (x + p * x * x // d)
            if numerator % m != 0:
                raise AssertionError("Type-I z is not integral")
            i_z = numerator // m
            i_lhs, i_rhs = exact_identity(p, x, i_y, i_z)
            if i_lhs != i_rhs:
                raise AssertionError("Type-I identity failure")
            hits.append(Hit(m, d, "I", x, i_y, i_z))

        ii_y = ii_z = ii_lhs = ii_rhs = None
        if ii_hit:
            numerator_y = p * (x + d)
            numerator_z = p * (x + x * x // d)
            if numerator_y % m != 0 or numerator_z % m != 0:
                raise AssertionError("Type-II denominator is not integral")
            ii_y = numerator_y // m
            ii_z = numerator_z // m
            ii_lhs, ii_rhs = exact_identity(p, x, ii_y, ii_z)
            if ii_lhs != ii_rhs:
                raise AssertionError("Type-II identity failure")
            hits.append(Hit(m, d, "II", x, ii_y, ii_z))

        rows.append(
            DivisorRow(
                d=d,
                i_residue=i_residue,
                i_hit=i_hit,
                ii_eligible=ii_eligible,
                ii_residue=ii_residue,
                ii_hit=ii_hit,
                i_y=i_y,
                i_z=i_z,
                ii_y=ii_y,
                ii_z=ii_z,
                i_lhs=i_lhs,
                i_rhs=i_rhs,
                ii_lhs=ii_lhs,
                ii_rhs=ii_rhs,
            )
        )

    hits.sort(key=lambda h: (h.m, h.d, 0 if h.kind == "I" else 1))
    return {
        "scope": scope,
        "p": p,
        "m": m,
        "x": x,
        "factors": factors,
        "divisors": divisors,
        "rows": tuple(rows),
        "hits": tuple(hits),
    }


def factor_record(q: int, a: int) -> bytes:
    return record(
        "SP04.FACTOR.v1",
        (("prime", nat(q)), ("exponent_in_x", nat(a))),
    )


def hit_record(hit: Hit) -> bytes:
    return record(
        "SP04.HIT.v1",
        (
            ("m", nat(hit.m)),
            ("d", nat(hit.d)),
            ("type", text(hit.kind)),
            ("x", nat(hit.x)),
            ("y", nat(hit.y)),
            ("z", nat(hit.z)),
        ),
    )


def optional_nat(n: int | None) -> bytes:
    return b"" if n is None else nat(n)


def row_record(row: DivisorRow) -> bytes:
    return record(
        "SP04.DIVISOR-ROW.v1",
        (
            ("d", nat(row.d)),
            ("I_residue", nat(row.i_residue)),
            ("I_hit", boolean(row.i_hit)),
            ("II_eligible", boolean(row.ii_eligible)),
            ("II_residue", nat(row.ii_residue)),
            ("II_hit", boolean(row.ii_hit)),
            ("I_y", optional_nat(row.i_y)),
            ("I_z", optional_nat(row.i_z)),
            ("I_identity_lhs", optional_nat(row.i_lhs)),
            ("I_identity_rhs", optional_nat(row.i_rhs)),
            ("II_y", optional_nat(row.ii_y)),
            ("II_z", optional_nat(row.ii_z)),
            ("II_identity_lhs", optional_nat(row.ii_lhs)),
            ("II_identity_rhs", optional_nat(row.ii_rhs)),
        ),
    )


def definition_bytes() -> bytes:
    schedule_code = (
        "for m in [3,7,11,15,19,23]:x=(p+m)/4;"
        "D=sort(all_positive_divisors(x^2));"
        "for d in D:test_I_then_test_II;"
        "on_first_hit_return_terminal;"
        "after_all_tests_return_registered_scope_miss;"
        "producer_may_run_only_after_that_miss"
    )
    return record(
        "SP04.DEFINITION.v1",
        (
            ("B", nat(B)),
            ("registered_gaps", list_value([nat(m) for m in GAPS])),
            ("candidate_order", text("lexicographic(m,d,type),I<II")),
            ("type_order", list_value([text(t) for t in TYPE_ORDER])),
            ("x_formula", text("x=(p+m)/4")),
            ("I_predicate", text("d|x^2&&(p*x+d)%m=0")),
            ("II_predicate", text("d|x^2&&d<=x&&(x+d)%m=0")),
            ("I_denominators", text("(x,(p*x+d)/m,p*(x+p*x^2/d)/m)")),
            ("II_denominators", text("(x,p*(x+d)/m,p*(x+x^2/d)/m)")),
            ("schedule_code", text(schedule_code)),
            ("miss_status", text("MISS_REGISTERED_PRIORITY_COMPLETE")),
            ("coverage", text("REGISTERED_PRIORITY_ONLY")),
            ("next_unchecked_gap", nat(27)),
            ("global_exhaustion", boolean(False)),
        ),
    )


def replay_bytes(gap: dict, definition_digest: str) -> bytes:
    status = "HIT_PRESENT" if gap["hits"] else "GAP_MISS"
    return record(
        "SP04.GAP-REPLAY.v1",
        (
            ("definition_digest_sha256", text(definition_digest)),
            ("scope", text(gap["scope"])),
            ("p", nat(gap["p"])),
            ("m", nat(gap["m"])),
            ("x", nat(gap["x"])),
            (
                "factorization_of_x",
                list_value([factor_record(q, a) for q, a in gap["factors"]]),
            ),
            ("divisor_count", nat(len(gap["divisors"]))),
            ("divisor_rows", list_value([row_record(r) for r in gap["rows"]])),
            ("all_gap_hits", list_value([hit_record(h) for h in gap["hits"]])),
            ("gap_status", text(status)),
        ),
    )


def miss_outcome_record() -> bytes:
    return record(
        "SP04.OUTCOME.MISS.v1",
        (
            ("status", text("MISS_REGISTERED_PRIORITY_COMPLETE")),
            ("coverage", text("REGISTERED_PRIORITY_ONLY")),
            ("next_unchecked_gap", nat(27)),
            ("global_exhaustion", boolean(False)),
            ("producer_eligible", boolean(True)),
        ),
    )


def terminal_outcome_record(hit: Hit) -> bytes:
    return record(
        "SP04.OUTCOME.TERMINAL.v1",
        (
            ("status", text("TERMINAL_HIT")),
            ("producer_eligible", boolean(False)),
            ("hit", hit_record(hit)),
        ),
    )


def control_source_payload(p: int) -> bytes:
    return record(
        "SP04.CONTROL-SOURCE.v1",
        (("source_id", text(f"control-p-{p}")), ("p", nat(p))),
    )


def binding_bytes(
    p: int,
    definition_digest: str,
    registered_replay_digests: Sequence[str],
    outcome: Hit | None,
) -> bytes:
    return record(
        "SP04.SOURCE-BINDING.v1",
        (
            ("definition_digest_sha256", text(definition_digest)),
            ("domain_adapter", text("SP04.PRIME-SOURCE-DOMAIN.v1")),
            ("source_payload", control_source_payload(p)),
            ("bound_p", nat(p)),
            (
                "registered_replay_digests_sha256",
                list_value([text(d) for d in registered_replay_digests]),
            ),
            (
                "schedule_outcome",
                miss_outcome_record() if outcome is None else terminal_outcome_record(outcome),
            ),
        ),
    )


def run_registered_schedule(gaps: Sequence[dict]) -> Hit | None:
    for gap in gaps:
        for row in gap["rows"]:
            if row.i_hit:
                assert row.i_y is not None and row.i_z is not None
                return Hit(gap["m"], row.d, "I", gap["x"], row.i_y, row.i_z)
            if row.ii_hit:
                assert row.ii_y is not None and row.ii_z is not None
                return Hit(gap["m"], row.d, "II", gap["x"], row.ii_y, row.ii_z)
    return None


def factorization_text(factors: Iterable[tuple[int, int]]) -> str:
    items = list(factors)
    return "1" if not items else "*".join(f"{q}^{a}" for q, a in items)


def main() -> None:
    REPLAY_DIR.mkdir(parents=True, exist_ok=True)
    BINDING_DIR.mkdir(parents=True, exist_ok=True)
    for old in REPLAY_DIR.glob("*.rec"):
        old.unlink()
    for old in BINDING_DIR.glob("*.rec"):
        old.unlink()

    definition = definition_bytes()
    definition_digest = sha256_hex(definition)
    (ROOT / "definition.rec").write_bytes(definition)

    transcript_rows: list[dict[str, str | int]] = []
    primality_rows: list[dict[str, int]] = []
    outcomes: list[dict[str, object]] = []
    replay_index: list[dict[str, object]] = []

    for p in CONTROL_PRIMES:
        if not is_prime_trial(p):
            raise AssertionError(f"control p={p} is not prime")
        if p % 4 != 1 or B > p - 2:
            raise AssertionError(f"control p={p} is not legal for B={B}")
        for r in range(2, math.isqrt(p) + 1):
            primality_rows.append({"p": p, "trial_divisor": r, "remainder": p % r})

        registered_gaps = [make_gap(p, m, "REGISTERED_B23") for m in GAPS]
        registered_digests: list[str] = []
        for gap in registered_gaps:
            payload = replay_bytes(gap, definition_digest)
            digest = sha256_hex(payload)
            filename = f"p{p}-m{gap['m']}-registered.rec"
            (REPLAY_DIR / filename).write_bytes(payload)
            registered_digests.append(digest)
            replay_index.append(
                {
                    "scope": gap["scope"],
                    "p": p,
                    "m": gap["m"],
                    "filename": f"replays/{filename}",
                    "sha256": digest,
                    "divisor_count": len(gap["divisors"]),
                }
            )
            factors_str = factorization_text(gap["factors"])
            for row in gap["rows"]:
                transcript_rows.append(
                    {
                        "scope": gap["scope"],
                        "p": p,
                        "m": gap["m"],
                        "x": gap["x"],
                        "factorization_x": factors_str,
                        "d": row.d,
                        "I_residue": row.i_residue,
                        "I_hit": int(row.i_hit),
                        "II_eligible": int(row.ii_eligible),
                        "II_residue": row.ii_residue,
                        "II_hit": int(row.ii_hit),
                        "I_y": "" if row.i_y is None else row.i_y,
                        "I_z": "" if row.i_z is None else row.i_z,
                        "I_identity_lhs": "" if row.i_lhs is None else row.i_lhs,
                        "I_identity_rhs": "" if row.i_rhs is None else row.i_rhs,
                        "II_y": "" if row.ii_y is None else row.ii_y,
                        "II_z": "" if row.ii_z is None else row.ii_z,
                        "II_identity_lhs": "" if row.ii_lhs is None else row.ii_lhs,
                        "II_identity_rhs": "" if row.ii_rhs is None else row.ii_rhs,
                    }
                )

        outcome = run_registered_schedule(registered_gaps)
        outcomes.append(
            {
                "p": p,
                "status": "MISS_REGISTERED_PRIORITY_COMPLETE" if outcome is None else "TERMINAL_HIT",
                "coverage": "REGISTERED_PRIORITY_ONLY" if outcome is None else None,
                "next_unchecked_gap": 27 if outcome is None else None,
                "global_exhaustion": False if outcome is None else None,
                "earliest": None
                if outcome is None
                else {
                    "m": outcome.m,
                    "d": outcome.d,
                    "type": outcome.kind,
                    "x": outcome.x,
                    "y": outcome.y,
                    "z": outcome.z,
                },
            }
        )
        binding = binding_bytes(p, definition_digest, registered_digests, outcome)
        (BINDING_DIR / f"p{p}-binding.rec").write_bytes(binding)

    for p, m in EXTERNAL_CONTROLS:
        gap = make_gap(p, m, "EXTERNAL_BOUNDARY_CONTROL")
        payload = replay_bytes(gap, definition_digest)
        digest = sha256_hex(payload)
        filename = f"p{p}-m{m}-external.rec"
        (REPLAY_DIR / filename).write_bytes(payload)
        replay_index.append(
            {
                "scope": gap["scope"],
                "p": p,
                "m": m,
                "filename": f"replays/{filename}",
                "sha256": digest,
                "divisor_count": len(gap["divisors"]),
            }
        )
        factors_str = factorization_text(gap["factors"])
        for row in gap["rows"]:
            transcript_rows.append(
                {
                    "scope": gap["scope"],
                    "p": p,
                    "m": m,
                    "x": gap["x"],
                    "factorization_x": factors_str,
                    "d": row.d,
                    "I_residue": row.i_residue,
                    "I_hit": int(row.i_hit),
                    "II_eligible": int(row.ii_eligible),
                    "II_residue": row.ii_residue,
                    "II_hit": int(row.ii_hit),
                    "I_y": "" if row.i_y is None else row.i_y,
                    "I_z": "" if row.i_z is None else row.i_z,
                    "I_identity_lhs": "" if row.i_lhs is None else row.i_lhs,
                    "I_identity_rhs": "" if row.i_rhs is None else row.i_rhs,
                    "II_y": "" if row.ii_y is None else row.ii_y,
                    "II_z": "" if row.ii_z is None else row.ii_z,
                    "II_identity_lhs": "" if row.ii_lhs is None else row.ii_lhs,
                    "II_identity_rhs": "" if row.ii_rhs is None else row.ii_rhs,
                }
            )

    transcript_fields = [
        "scope",
        "p",
        "m",
        "x",
        "factorization_x",
        "d",
        "I_residue",
        "I_hit",
        "II_eligible",
        "II_residue",
        "II_hit",
        "I_y",
        "I_z",
        "I_identity_lhs",
        "I_identity_rhs",
        "II_y",
        "II_z",
        "II_identity_lhs",
        "II_identity_rhs",
    ]
    with (ROOT / "divisor_transcript.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=transcript_fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(transcript_rows)

    with (ROOT / "primality_transcript.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=("p", "trial_divisor", "remainder"),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(primality_rows)

    (ROOT / "outcomes.json").write_text(
        json.dumps(outcomes, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (ROOT / "replay_index.json").write_text(
        json.dumps(replay_index, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    report = {
        "definition_sha256": definition_digest,
        "registered_gap_records": len(CONTROL_PRIMES) * len(GAPS),
        "external_gap_records": len(EXTERNAL_CONTROLS),
        "divisor_rows": len(transcript_rows),
        "primality_trial_rows": len(primality_rows),
    }
    (ROOT / "constructor_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
