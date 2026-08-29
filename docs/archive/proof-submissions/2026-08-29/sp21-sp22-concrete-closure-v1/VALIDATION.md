# Validation record

Validated against the overlay contents on 2026-08-29.

## Signed identities

```text
base HEAD: e6e9e4a8c41b90a330b9ef333e542c18c2cb7be4
policy payload SHA-256: 470b9d787eab4af3ecb05fd32764cf09937cb52f4837d5a2cde9b0a8be5945f8
artifact-lock payload SHA-256: f3384a43f94a8687bc762d0be305671287631d92e230a83ab07ebb9ec2312311
authority statement SHA-256: abd31d6f89e95aea8f431e46d50c48cce784a9e70d41a4113f133320c2af989d
trusted public-key fingerprint: e03c0a9f1fd62668f5f89742aea49c16e68648e2e471480c3d9907d50346da65
```

The detached RSA-3072 PKCS#1 v1.5 / SHA-256 signature was independently verified with OpenSSL and by both repository programs.

## Generated receipts

```text
evidence ID: 7eb2bdbc44d67acba8c4357a917b4ed4d446ceb46bf1de468f34f36d83b7da99
independent replay ID: fec547d83b6af59c2785968d67f6ec285174c1e381b61b883e6c7f81eefee69d
```

## Bounded dual-implementation audit

For every signed-domain source with `2 <= p < 100000`:

```text
domain source count: 606
selected action counts 0..6: 0, 475, 83, 11, 16, 15, 6
successor roots: 21169, 61681, 67369, 87481, 94441, 99961
rejects: 0
fallthroughs: 0
```

Constructor and independent replayer produce the same content-addressed audit receipt while using different divisor-enumeration algorithms. This bounded run is regression evidence; the universal result is proved by the finite-action/total-producer case split and uniform edge formulas in the dossiers.

## Positive edge

For `p=21169`:

```text
t=882, X=5293=67*79
M23 prior result: six MISS records
selected producer index: 6
R=14115, K=74700109, 4K=pR+1
target potential: (21169,2,4,112021056,74700109,0,0)
re-entry: ENTERED_TYPE_I_FULL_CARRIER_POST_G_BODY
```

The later gap-31 certificate is retained and `global_exhaustion=false`.

## Tests

`python -m unittest tests.test_t6_sp21_q1_p21169_concrete_selector_v1 -v` completed 37/37 tests successfully. The suite covers policy/order/overlap, signature and artifact lock, predicate-domain local totality, actual source and E1 binding, E2--E5/R, target-local replay, common admission, queue/re-entry, gap-31 scope control, generic independent prefix replay, and fail-closed mutation controls.

## Status

SP-21 and SP-22 are established only in the signed ordinary q=1,G predicate-policy scope. Production-wide SP-03, F1, F2, F3, T6 and the conjecture remain open.
