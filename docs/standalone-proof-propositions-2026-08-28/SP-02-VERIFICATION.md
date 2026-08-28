# SP-02 Verification Report

Date: 2026-08-28

## Scope

This report verifies the finite-model implementation of the conditional SP-02
theorem. It does not verify that the repository's concrete constructor census
is complete, and it does not alter the F1 residual inventory.

## Commands

~~~text
python3 reproductions/sp02_constructor_source_completeness.py --verify
python3 -m unittest tests/test_sp02_constructor_source_completeness.py -v
ruff check reproductions/sp02_constructor_source_completeness.py tests/test_sp02_constructor_source_completeness.py
python3 -m py_compile reproductions/sp02_constructor_source_completeness.py tests/test_sp02_constructor_source_completeness.py
~~~

## Results

The good finite model returned:

~~~json
{
  "reachable": ["a", "r"],
  "labels": {
    "k": "NONRUNTIME_CONTROL",
    "p": "ACTIVE_PRODUCER",
    "t": "TERMINAL_ONLY",
    "u": "OBSOLETE_OR_UNREACHABLE"
  },
  "unknown_count": 0,
  "status": "PASS"
}
~~~

All seven negative controls returned the expected rejection:

~~~text
NC-1 STATE_CHANGE_REGISTRY
NC-2 TERMINAL_SUCCESSOR_CONFLICT
NC-3 SUCCESSOR_OWNER_CONFLICT
NC-4 CONTROL_SUCCESSOR
NC-5 SELECTOR_NOT_TOTAL
NC-6 TERMINAL_UNVERIFIED
NC-7 TARGET_ILLEGAL
~~~

The focused unittest result was:

~~~text
Ran 4 tests
OK
~~~

Ruff, Python compilation and git diff --check passed.

## Interpretation

The report establishes the finite algorithm, its fixed-point computation and
the listed fail-closed controls under the explicit model assumptions. It is
evidence for the conditional SP-02 meta-lemma only. Selector totality,
state-change registry completeness and owner uniqueness remain assumptions
when a concrete system is instantiated; therefore U-A0-01, F1 and T6 remain
open.
