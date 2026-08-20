from __future__ import annotations

import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import verify_controls
import verify_counterexamples
import verify_downstream_formulas
import verify_state_contract
import verify_symbolic


def main() -> None:
    report = {
        "package": "q1_fresh_handoff_proof",
        "base_commit": "47fedc2",
        "scope": "ordinary q=1 Type II G -> fresh Type I handoff and q=1-specific downstream formula checks",
        "results": {
            "symbolic": verify_symbolic.verify(),
            "controls": verify_controls.verify(),
            "counterexamples": verify_counterexamples.verify(),
            "state_contract": verify_state_contract.verify(),
            "downstream": verify_downstream_formulas.verify(),
        },
        "proof_boundary": [
            "not a proof of the Erdos-Straus conjecture",
            "not a global Type I selector",
            "not T5 global well-foundedness",
            "not nontrivial marked-terminal membership",
            "not c=8,q*=103 totality",
        ],
    }
    out = ROOT / "outputs" / "verification_report.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps({"status": "verified", "report": str(out)}, indent=2))


if __name__ == "__main__":
    main()
