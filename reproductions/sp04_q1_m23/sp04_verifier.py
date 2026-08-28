#!/usr/bin/env python3
"""Independent verifier for SP-04 B=23 evidence.

Independence boundary:
  * this file imports no code from sp04_constructor.py;
  * the hit set is recomputed by divisor-pair scanning k=1..x for x^2,
    not from the constructor's factorization/exponent-product output;
  * all equations are checked by exact integer cross multiplication;
  * record bytes are reconstructed from source p and the public definition;
    digest equality is checked only after byte-for-byte object comparison.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

B = 23
GAPS = (3, 7, 11, 15, 19, 23)
CONTROL_PRIMES = (73, 241441, 2689, 12721, 1201, 2521, 21169)
ROOT = Path(__file__).resolve().parent
REPLAY_DIR = ROOT / "replays"
BINDING_DIR = ROOT / "bindings"

EXPECTED_EARLIEST: dict[int, tuple[int, int, str, int, int, int] | None] = {
    73: (7, 1, "II", 20, 219, 4380),
    241441: (11, 27, "II", 60363, 1325511090, 2963400960210),
    2689: (15, 26, "I", 676, 121186, 8472598004),
    12721: (19, 7, "II", 3185, 2137128, 972393240),
    1201: (23, 34, "I", 306, 15980, 172727820),
    2521: (23, 8, "II", 636, 70588, 5611746),
    21169: None,
}
EXPECTED_EXTERNAL_21169_M31 = (31, 1, "II", 5300, 3619899, 19185464700)


@dataclass(frozen=True)
class Hit:
    m: int
    d: int
    kind: str
    x: int
    y: int
    z: int


@dataclass(frozen=True)
class Row:
    d: int
    i_residue: int
    i_hit: bool
    ii_eligible: bool
    ii_residue: int
    ii_hit: bool
    i_y: int | None
    i_z: int | None
    i_lhs: int | None
    i_rhs: int | None
    ii_y: int | None
    ii_z: int | None
    ii_lhs: int | None
    ii_rhs: int | None


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def nat(n: int) -> bytes:
    require(isinstance(n, int) and n >= 0, f"not a natural number: {n!r}")
    return str(n).encode("ascii")


def frame(payload: bytes) -> bytes:
    return nat(len(payload)) + b":" + payload


def record(tag: str, fields: Sequence[tuple[str, bytes]]) -> bytes:
    out = bytearray(frame(tag.encode("ascii")) + frame(nat(len(fields))))
    for name, value in fields:
        out += frame(name.encode("ascii"))
        out += frame(value)
    return bytes(out)


def list_value(items: Sequence[bytes]) -> bytes:
    return b"".join([frame(b"SP04.LIST.v1"), frame(nat(len(items))), *[frame(x) for x in items]])


def text(s: str) -> bytes:
    return s.encode("utf-8")


def boolean(v: bool) -> bytes:
    return b"1" if v else b"0"


def optional_nat(v: int | None) -> bytes:
    return b"" if v is None else nat(v)


def sha256_hex(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def exact_prime_check(n: int) -> tuple[bool, list[tuple[int, int]]]:
    rows: list[tuple[int, int]] = []
    if n < 2:
        return False, rows
    for r in range(2, math.isqrt(n) + 1):
        remainder = n % r
        rows.append((r, remainder))
        if remainder == 0:
            return False, rows
    return True, rows


def independent_factorization(n: int) -> tuple[tuple[int, int], ...]:
    """Separate factorization used only to verify the recorded x factorization.

    Divisor completeness and hit computation below do not depend on this result.
    """
    require(n >= 1, "factorization input must be positive")
    remaining = n
    result: list[tuple[int, int]] = []
    candidate = 2
    while candidate <= remaining:
        if remaining % candidate == 0:
            exponent = 0
            while remaining % candidate == 0:
                remaining //= candidate
                exponent += 1
            prime, _ = exact_prime_check(candidate)
            require(prime, f"recorded factor base {candidate} is composite")
            result.append((candidate, exponent))
        candidate += 1
        if remaining == 1:
            break
    return tuple(result)


def divisors_by_pair_scan(x: int) -> tuple[int, ...]:
    """Enumerate every divisor of x^2 without using a factorization.

    Since sqrt(x^2)=x, each divisor d is either <=x and is visited directly,
    or has complementary divisor x^2/d < x and is inserted as that pair.
    """
    require(x > 0, "x must be positive")
    n = x * x
    found: set[int] = set()
    for k in range(1, x + 1):
        if n % k == 0:
            found.add(k)
            found.add(n // k)
    ordered = tuple(sorted(found))
    require(all(n % d == 0 for d in ordered), "pair scan produced a non-divisor")
    return ordered


def identity_pair(p: int, x: int, y: int, z: int) -> tuple[int, int]:
    return 4 * x * y * z, p * (y * z + x * z + x * y)


def recompute_gap(p: int, m: int, scope: str) -> dict:
    require((p + m) % 4 == 0, f"nonintegral x for p={p},m={m}")
    x = (p + m) // 4
    factors = independent_factorization(x)
    divisors = divisors_by_pair_scan(x)
    rows: list[Row] = []
    hits: list[Hit] = []
    for d in divisors:
        require((x * x) % d == 0, f"d={d} does not divide x^2")
        i_residue = (p * x + d) % m
        i_hit = i_residue == 0
        ii_eligible = d <= x
        ii_residue = (x + d) % m
        ii_hit = ii_eligible and ii_residue == 0

        i_y = i_z = i_lhs = i_rhs = None
        if i_hit:
            require((p * x + d) % m == 0, "bad Type-I congruence")
            i_y = (p * x + d) // m
            z_num = p * (x + p * x * x // d)
            require(z_num % m == 0, "Type-I z nonintegral")
            i_z = z_num // m
            i_lhs, i_rhs = identity_pair(p, x, i_y, i_z)
            require(i_lhs == i_rhs, "Type-I identity failed")
            hits.append(Hit(m, d, "I", x, i_y, i_z))

        ii_y = ii_z = ii_lhs = ii_rhs = None
        if ii_hit:
            y_num = p * (x + d)
            z_num = p * (x + x * x // d)
            require(y_num % m == 0 and z_num % m == 0, "Type-II denominator nonintegral")
            ii_y = y_num // m
            ii_z = z_num // m
            ii_lhs, ii_rhs = identity_pair(p, x, ii_y, ii_z)
            require(ii_lhs == ii_rhs, "Type-II identity failed")
            hits.append(Hit(m, d, "II", x, ii_y, ii_z))

        rows.append(
            Row(
                d,
                i_residue,
                i_hit,
                ii_eligible,
                ii_residue,
                ii_hit,
                i_y,
                i_z,
                i_lhs,
                i_rhs,
                ii_y,
                ii_z,
                ii_lhs,
                ii_rhs,
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
    return record("SP04.FACTOR.v1", (("prime", nat(q)), ("exponent_in_x", nat(a))))


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


def row_record(row: Row) -> bytes:
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
            ("type_order", list_value([text("I"), text("II")])),
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
    return record(
        "SP04.GAP-REPLAY.v1",
        (
            ("definition_digest_sha256", text(definition_digest)),
            ("scope", text(gap["scope"])),
            ("p", nat(gap["p"])),
            ("m", nat(gap["m"])),
            ("x", nat(gap["x"])),
            ("factorization_of_x", list_value([factor_record(q, a) for q, a in gap["factors"]])),
            ("divisor_count", nat(len(gap["divisors"]))),
            ("divisor_rows", list_value([row_record(r) for r in gap["rows"]])),
            ("all_gap_hits", list_value([hit_record(h) for h in gap["hits"]])),
            ("gap_status", text("HIT_PRESENT" if gap["hits"] else "GAP_MISS")),
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
        (("status", text("TERMINAL_HIT")), ("producer_eligible", boolean(False)), ("hit", hit_record(hit))),
    )


def source_payload(p: int) -> bytes:
    return record("SP04.CONTROL-SOURCE.v1", (("source_id", text(f"control-p-{p}")), ("p", nat(p))))


def binding_bytes(p: int, definition_digest: str, replay_digests: Sequence[str], outcome: Hit | None) -> bytes:
    return record(
        "SP04.SOURCE-BINDING.v1",
        (
            ("definition_digest_sha256", text(definition_digest)),
            ("domain_adapter", text("SP04.PRIME-SOURCE-DOMAIN.v1")),
            ("source_payload", source_payload(p)),
            ("bound_p", nat(p)),
            ("registered_replay_digests_sha256", list_value([text(d) for d in replay_digests])),
            ("schedule_outcome", miss_outcome_record() if outcome is None else terminal_outcome_record(outcome)),
        ),
    )


def first_hit(gaps: Sequence[dict]) -> Hit | None:
    for gap in gaps:
        for row in gap["rows"]:
            if row.i_hit:
                require(row.i_y is not None and row.i_z is not None, "missing Type-I denominators")
                return Hit(gap["m"], row.d, "I", gap["x"], row.i_y, row.i_z)
            if row.ii_hit:
                require(row.ii_y is not None and row.ii_z is not None, "missing Type-II denominators")
                return Hit(gap["m"], row.d, "II", gap["x"], row.ii_y, row.ii_z)
    return None


def outcome_json(p: int, hit: Hit | None) -> dict[str, object]:
    if hit is None:
        return {
            "coverage": "REGISTERED_PRIORITY_ONLY",
            "earliest": None,
            "global_exhaustion": False,
            "next_unchecked_gap": 27,
            "p": p,
            "status": "MISS_REGISTERED_PRIORITY_COMPLETE",
        }
    return {
        "coverage": None,
        "earliest": {"d": hit.d, "m": hit.m, "type": hit.kind, "x": hit.x, "y": hit.y, "z": hit.z},
        "global_exhaustion": None,
        "next_unchecked_gap": None,
        "p": p,
        "status": "TERMINAL_HIT",
    }


def factorization_text(factors: Sequence[tuple[int, int]]) -> str:
    return "1" if not factors else "*".join(f"{q}^{a}" for q, a in factors)


def row_as_tsv(scope: str, p: int, gap: dict, row: Row) -> dict[str, str]:
    def s(v: object | None) -> str:
        return "" if v is None else str(v)

    return {
        "scope": scope,
        "p": str(p),
        "m": str(gap["m"]),
        "x": str(gap["x"]),
        "factorization_x": factorization_text(gap["factors"]),
        "d": str(row.d),
        "I_residue": str(row.i_residue),
        "I_hit": str(int(row.i_hit)),
        "II_eligible": str(int(row.ii_eligible)),
        "II_residue": str(row.ii_residue),
        "II_hit": str(int(row.ii_hit)),
        "I_y": s(row.i_y),
        "I_z": s(row.i_z),
        "I_identity_lhs": s(row.i_lhs),
        "I_identity_rhs": s(row.i_rhs),
        "II_y": s(row.ii_y),
        "II_z": s(row.ii_z),
        "II_identity_lhs": s(row.ii_lhs),
        "II_identity_rhs": s(row.ii_rhs),
    }


def correct_orchestrator(
    gaps: Sequence[dict], producer: Callable[[list[str]], str], events: list[str]
) -> tuple[str, Hit | None]:
    for gap in gaps:
        for row in gap["rows"]:
            events.append(f"CHECK:{gap['m']}:{row.d}:I")
            if row.i_hit:
                hit = Hit(gap["m"], row.d, "I", gap["x"], int(row.i_y), int(row.i_z))
                events.append(f"TERMINAL:{hit.m}:{hit.d}:{hit.kind}")
                return "TERMINAL", hit
            events.append(f"CHECK:{gap['m']}:{row.d}:II")
            if row.ii_hit:
                hit = Hit(gap["m"], row.d, "II", gap["x"], int(row.ii_y), int(row.ii_z))
                events.append(f"TERMINAL:{hit.m}:{hit.d}:{hit.kind}")
                return "TERMINAL", hit
        events.append(f"GAP_COMPLETE_MISS:{gap['m']}")
    events.append("REGISTERED_SCOPE_MISS")
    value = producer(events)
    return value, None


def mutant_producer_first(
    gaps: Sequence[dict], producer: Callable[[list[str]], str], events: list[str]
) -> tuple[str, Hit | None]:
    events.append("MUTANT_PRODUCER_FIRST")
    return producer(events), None


def mutant_after_first_gap_miss(
    gaps: Sequence[dict], producer: Callable[[list[str]], str], events: list[str]
) -> tuple[str, Hit | None]:
    first = gaps[0]
    for row in first["rows"]:
        if row.i_hit or row.ii_hit:
            raise AssertionError("negative control assumes first registered gap is a local miss")
    events.append(f"MUTANT_LOCAL_MISS:{first['m']}")
    return producer(events), None


def run_precedence_controls(all_gaps: dict[int, list[dict]]) -> list[str]:
    report: list[str] = []

    def sentinel(events: list[str]) -> str:
        events.append("PRODUCER_CALLED")
        return "PRODUCER_SENTINEL"

    for p, expected in EXPECTED_EARLIEST.items():
        gaps = all_gaps[p]
        events: list[str] = []
        result, hit = correct_orchestrator(gaps, sentinel, events)
        if expected is None:
            require(result == "PRODUCER_SENTINEL" and hit is None, "producer not reached after full registered miss")
            require(events[-2:] == ["REGISTERED_SCOPE_MISS", "PRODUCER_CALLED"], "producer ordering after miss is wrong")
            report.append(f"p={p}: correct schedule calls producer exactly after all six gap misses")
        else:
            require(result == "TERMINAL" and hit is not None, f"p={p}: terminal schedule failed")
            require("PRODUCER_CALLED" not in events, f"p={p}: producer ran before/after terminal")
            report.append(f"p={p}: correct schedule terminal precedes producer; producer_calls=0")

            e1: list[str] = []
            mutant_result, mutant_hit = mutant_producer_first(gaps, sentinel, e1)
            require(mutant_result == "PRODUCER_SENTINEL" and mutant_hit is None, "producer-first mutant did not expose itself")
            require(mutant_result != "TERMINAL", "producer-first mutant unexpectedly matched terminal")

            e2: list[str] = []
            local_result, local_hit = mutant_after_first_gap_miss(gaps, sentinel, e2)
            require(local_result == "PRODUCER_SENTINEL" and local_hit is None, "local-miss mutant did not expose itself")
            report.append(f"p={p}: producer-first and local-miss-as-complete mutants rejected")
    return report


def main() -> None:
    report: list[str] = []

    # Public definition: reconstruct exact bytes, then compare. Digest is only an identifier.
    expected_definition = definition_bytes()
    actual_definition = (ROOT / "definition.rec").read_bytes()
    require(actual_definition == expected_definition, "definition record differs byte-for-byte")
    definition_digest = sha256_hex(expected_definition)
    report.append(f"definition bytes recomputed; sha256={definition_digest}")

    all_registered: dict[int, list[dict]] = {}
    all_replay_index: list[dict[str, object]] = []
    expected_transcript: list[dict[str, str]] = []
    expected_primality_rows: list[dict[str, str]] = []
    expected_outcomes: list[dict[str, object]] = []

    for p in CONTROL_PRIMES:
        prime, prime_rows = exact_prime_check(p)
        require(prime, f"p={p} is not prime")
        require(p % 4 == 1 and 3 <= B <= p - 2 and B % 4 == 3, f"p={p} fails source legality")
        expected_primality_rows.extend(
            {"p": str(p), "trial_divisor": str(r), "remainder": str(rem)} for r, rem in prime_rows
        )
        report.append(f"p={p}: prime by all trial divisors 2..{math.isqrt(p)}; p mod 4=1")

        gaps = [recompute_gap(p, m, "REGISTERED_B23") for m in GAPS]
        all_registered[p] = gaps
        digests: list[str] = []
        for gap in gaps:
            expected_payload = replay_bytes(gap, definition_digest)
            filename = f"p{p}-m{gap['m']}-registered.rec"
            actual_payload = (REPLAY_DIR / filename).read_bytes()
            require(actual_payload == expected_payload, f"replay byte mismatch: {filename}")
            digest = sha256_hex(expected_payload)
            digests.append(digest)
            all_replay_index.append(
                {
                    "divisor_count": len(gap["divisors"]),
                    "filename": f"replays/{filename}",
                    "m": gap["m"],
                    "p": p,
                    "scope": gap["scope"],
                    "sha256": digest,
                }
            )
            expected_transcript.extend(row_as_tsv(gap["scope"], p, gap, row) for row in gap["rows"])

        hit = first_hit(gaps)
        expected = EXPECTED_EARLIEST[p]
        if expected is None:
            require(hit is None, f"p={p}: expected six-layer miss")
            require(all(not gap["hits"] for gap in gaps), f"p={p}: a registered hit exists")
            report.append(f"p={p}: all six registered Type-I/Type-II hit sets are empty")
        else:
            require(hit is not None, f"p={p}: missing expected terminal")
            actual_tuple = (hit.m, hit.d, hit.kind, hit.x, hit.y, hit.z)
            require(actual_tuple == expected, f"p={p}: earliest mismatch {actual_tuple} != {expected}")
            lhs, rhs = identity_pair(p, hit.x, hit.y, hit.z)
            require(lhs == rhs, f"p={p}: terminal identity mismatch")
            report.append(
                f"p={p}: earliest=({hit.m},{hit.d},{hit.kind}); triple=({hit.x},{hit.y},{hit.z}); cross_product={lhs}"
            )

        expected_outcomes.append(outcome_json(p, hit))
        expected_binding = binding_bytes(p, definition_digest, digests, hit)
        actual_binding = (BINDING_DIR / f"p{p}-binding.rec").read_bytes()
        require(actual_binding == expected_binding, f"source binding mismatch for p={p}")

    external = recompute_gap(21169, 31, "EXTERNAL_BOUNDARY_CONTROL")
    expected_external_payload = replay_bytes(external, definition_digest)
    external_filename = "p21169-m31-external.rec"
    actual_external_payload = (REPLAY_DIR / external_filename).read_bytes()
    require(actual_external_payload == expected_external_payload, "external gap-31 replay mismatch")
    external_digest = sha256_hex(expected_external_payload)
    all_replay_index.append(
        {
            "divisor_count": len(external["divisors"]),
            "filename": f"replays/{external_filename}",
            "m": 31,
            "p": 21169,
            "scope": external["scope"],
            "sha256": external_digest,
        }
    )
    expected_transcript.extend(row_as_tsv(external["scope"], 21169, external, row) for row in external["rows"])
    external_hit = next((h for h in external["hits"] if h.d == 1 and h.kind == "II"), None)
    require(external_hit is not None, "missing p=21169,m=31,Type-II,d=1 witness")
    require(
        (external_hit.m, external_hit.d, external_hit.kind, external_hit.x, external_hit.y, external_hit.z)
        == EXPECTED_EXTERNAL_21169_M31,
        "external gap-31 certificate differs from required control",
    )
    ext_lhs, ext_rhs = identity_pair(21169, external_hit.x, external_hit.y, external_hit.z)
    require(ext_lhs == ext_rhs, "external gap-31 identity failed")
    report.append(
        "p=21169,m=31,d=1,Type-II verified: "
        f"(x,y,z)=({external_hit.x},{external_hit.y},{external_hit.z}); cross_product={ext_lhs}"
    )

    # Human-readable transcripts must equal the independent recomputation row for row.
    transcript_fields = (
        "scope", "p", "m", "x", "factorization_x", "d", "I_residue", "I_hit",
        "II_eligible", "II_residue", "II_hit", "I_y", "I_z", "I_identity_lhs",
        "I_identity_rhs", "II_y", "II_z", "II_identity_lhs", "II_identity_rhs",
    )
    with (ROOT / "independent_divisor_transcript.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=transcript_fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(expected_transcript)
    with (ROOT / "divisor_transcript.tsv").open("r", encoding="utf-8", newline="") as f:
        actual_transcript = list(csv.DictReader(f, delimiter="\t"))
    require(actual_transcript == expected_transcript, "divisor transcript differs from independent recomputation")
    report.append(f"constructor and independent divisor transcripts matched exactly: {len(actual_transcript)} rows")

    with (ROOT / "independent_primality_transcript.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=("p", "trial_divisor", "remainder"), delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(expected_primality_rows)
    with (ROOT / "primality_transcript.tsv").open("r", encoding="utf-8", newline="") as f:
        actual_prime_transcript = list(csv.DictReader(f, delimiter="\t"))
    require(actual_prime_transcript == expected_primality_rows, "primality transcript mismatch")
    require(all(int(row["remainder"]) != 0 for row in actual_prime_transcript), "zero primality remainder found")
    report.append(f"constructor and independent primality transcripts matched exactly: {len(actual_prime_transcript)} rows")

    actual_outcomes = json.loads((ROOT / "outcomes.json").read_text(encoding="utf-8"))
    require(actual_outcomes == expected_outcomes, "outcomes.json mismatch")
    actual_index = json.loads((ROOT / "replay_index.json").read_text(encoding="utf-8"))
    require(actual_index == all_replay_index, "replay_index.json mismatch")
    report.append("outcome and replay indexes reconstructed from source integers, not accepted from digests")

    report.extend(run_precedence_controls(all_registered))

    # Semantic boundary: six registered miss plus an unregistered valid natural-gap hit.
    require(first_hit(all_registered[21169]) is None, "boundary premise: p=21169 is not a registered miss")
    require(31 not in GAPS and 31 % 4 == 3 and 31 < 21169, "m=31 is not a valid unregistered natural gap")
    require(external_hit is not None, "boundary witness missing")
    report.append("global_exhaustion=false witnessed by registered MISS at p=21169 plus unregistered m=31 terminal hit")

    output = "SP-04 INDEPENDENT VERIFICATION: PASS\n" + "\n".join(f"- {line}" for line in report) + "\n"
    (ROOT / "verification_report.txt").write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
