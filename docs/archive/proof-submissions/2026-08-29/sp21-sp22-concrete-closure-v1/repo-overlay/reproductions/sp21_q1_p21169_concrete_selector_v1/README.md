# SP-21/SP-22 signed q=1,G selector reproduction

Run from repository root on base commit `e6e9e4a8c41b90a330b9ef333e542c18c2cb7be4` after applying this overlay:

```bash
python scripts/t6_sp21_q1_p21169_concrete_selector_v1.py \
  --repo-root . \
  --output reproductions/sp21_q1_p21169_concrete_selector_v1/evidence-v1.json

python scripts/t6_sp21_q1_p21169_independent_replayer_v1.py \
  --repo-root . \
  --evidence reproductions/sp21_q1_p21169_concrete_selector_v1/evidence-v1.json \
  --output reproductions/sp21_q1_p21169_concrete_selector_v1/independent-replay-v1.json

python -m unittest tests.test_t6_sp21_q1_p21169_concrete_selector_v1 -v
```

The constructor first verifies the external signature and complete artifact lock. It proves the signed policy skeleton's universal case split, executes terminal and successor regression witnesses, performs the complete predicate-domain census below 100000, emits the full `p=21169` edge, and records the gap-31 later-terminal control.

The independent program imports no repository-local module. It regenerates source states, source-prefix decisions, complementary-divisor screens, projection, target policy, E1--E5/R, admission, queue/re-entry trace, bounded census and content-addressed seals.

Key positive trace:

```text
p = 21169
M23 = all MISS
selected action = 6
R = 14115
K = 74700109
re-entry = ENTERED_TYPE_I_FULL_CARRIER_POST_G_BODY
global_exhaustion = false
gap 31 later certificate = (5300, 3619899, 19185464700)
```

Bounded audit expected values:

```text
domain sources with 2 <= p < 100000: 606
selected action counts 0..6: 0, 475, 83, 11, 16, 15, 6
successor p: 21169, 61681, 67369, 87481, 94441, 99961
```

The generated evidence and replay JSON are outputs, not inputs to the authority signature. They may be deleted and regenerated.
