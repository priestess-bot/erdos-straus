# T6 q=1 Registered Terminal Prefix Through 23: Next Plan

Date: 2026-08-27

## Decision Required by Gate 4/5

The q=1 phase-root producer cannot use the existing gaps `[3,7,11]` MISS and
place gap 23 after the producer. Under the Gate 4/5 terminal-first rule, every
terminal family registered as prior for this owner must execute before producer
selection.

Adding gap 23 also forces the intervening natural gaps 15 and 19 into the same
prefix. The non-contiguous policy `[3,7,11,23]` is unsound as a natural
precedence schedule: `p=12721` reaches a Type II terminal at gap 19 with
`d=7`.

The minimum proposed source schedule is therefore:

```text
gaps = [3,7,11,15,19,23]
family at each gap = complete Bradford Type I/II divisor screen
order = gap, divisor, Type I before Type II
next_unchecked_gap = 27
coverage = REGISTERED_PRIORITY_ONLY
global_exhaustion = false
```

This schedule is requested, not registered. Gate 4 and Gate 5 remain open.

## Exact Source Partition

Let `D_G` be the exact domain of separately authenticated, parentless ordinary
q=1 G V1 root states with common owner `type_ii_relation_g_endpoint`. This
domain cannot be created from an owner label alone; it must eventually come
from the V5/V6 source chain plus the V7 external trust boundary.

For each registered gap `m`, the full screen factors
`x_m=(p+m)/4`, enumerates every divisor of `x_m^2`, and checks both Bradford
types. The canonical earliest hit is terminal. Define `D_23` as the subset on
which all six screens miss. Then the mathematical partition is

```text
D_G
  = disjoint union of six-gap canonical earliest-terminal leaves
  + D_23.
```

This is a legal owner-domain narrowing only if every excluded `D_G` source is
retained as a verified terminal leaf. Defining the producer owner as a bare
"terminal-first survivor", selecting a convenient prime, or dropping hit
states from the domain would change the quantifier and is forbidden.

The general proof and its `B=23` specialization are in
`t6-q-one-finite-bradford-prefix-through-23-partition-v1`.

## Controls and Changed Pilot Input

The required source controls are:

| p | Result before producer |
|---:|---|
| 241441 | gap 11 Type II, canonical `d=27` |
| 12721 | gap 19 Type II, `d=7` |
| 1201 | gap 23 Type I, `d=34` |
| 2521 | gap 23 Type II, `d=8` |
| 21169 | all six registered gaps MISS; phase-root anchor-sink also MISS |

Consequently `p=1201` and `p=2521` are no longer positive producer controls.
They must terminate before phase-root selection. `p=21169` is the first
arithmetic guard control for the proposed six-gap source residual; actual
membership still requires a separately authenticated source in `D_G`.

It is also the mandatory anti-global control. It has the later Type II
certificate

```text
p = 21169
gap = 31
x = 5300
d = 1
denominators = [5300, 3619899, 19185464700]
```

Thus a six-gap MISS is not a proof that no direct decomposition exists.

## The Semantic Fork

There are two incompatible meanings of "complete terminal schedule".

### Versioned registered-prefix completeness

The coordinator freezes a finite ordered family set and proves that every
candidate inside those registered families was checked. A MISS is
`MISS_REGISTERED_PRIORITY_COMPLETE`, is bound to its exact scope, and keeps
`global_exhaustion=false`.

Under this meaning, the six-gap partition is a viable Gate 4 building block and
`D_23` is a viable narrow Gate 5 producer domain. It is still necessary to
prove that these six families are exactly the coordinator-prior families in
that schedule version.

### Complete terminal-universe semantics

The full natural Bradford range is `3,7,...,p-2`. By
`short-certificate-equivalence`, a HIT in this range is equivalent to
`Sol(p)` being nonempty. A semantically verified full-range MISS is therefore
a candidate counterexample report, not an ordinary producer-continuation
receipt.

If Gate 5 required every possible direct terminal certificate to precede the
pilot producer, every known solvable control would terminate and the remaining
producer domain would be precisely the unknown counterexample domain. Merely
renaming that domain would be circular. The pilot architecture therefore needs
the first, explicitly versioned registered-prefix meaning; it must never state
or imply the second.

## Remaining Mathematical Obligations

1. Obtain independent review of the parameterized `FiniteBradfordPrefix(B)`
   proof and of the reverse direction in `short-certificate-equivalence`.
2. Instantiate one six-gap coverage theorem, including complete
   factorizations, divisor lattices, both Type I/II reconstructions and the
   canonical earliest-hit order.
3. Prove a source-bound partition theorem after the V7 source context exists;
   a self-sealed schedule object is not source membership.
4. Freeze a coordinator theorem saying which terminal families are prior for
   this exact q=1 pilot version. A claim existing elsewhere in the repository
   does not silently become a registered family, and a registered family may
   not be placed after the producer.
5. Build a distinct target schedule. The six Bradford predicates are p-only
   and may be independently transported, while the full-carrier anchor-sink is
   target-projection-specific and must run after E2 but before admission.
6. Only after source and target terminal receipts exist may structured E1,
   deterministic E2, common E3, universal E4, fixed E5 and re-entry be joined.

## Implementation Order After Review

```text
independent theorem review
-> exact-HEAD six-gap scheduler and independent semantic verifier
-> coordinator-owned schedule registry and production issuer
-> V7 authenticated source binding
-> source partition / terminal preemption
-> branch-scoped E1
-> target six-gap transport plus anchor-sink schedule
-> E2/E3/E4/E5 bundle
-> admission and recursive re-entry
```

No step above is established merely by this planning document. In particular,
the new theorem does not register a schedule or producer, and it does not close
Gate 4, Gate 5, F1, F2, F3, T6, or the Erdos-Straus conjecture.
