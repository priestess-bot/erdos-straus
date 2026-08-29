# SP-21/SP-22 signed q=1,G selector domain v1

**Status:** ESTABLISHED in the exact signed predicate-policy scope.  
**Base commit:** `e6e9e4a8c41b90a330b9ef333e542c18c2cb7be4`.

The source domain is not a finite fixture. It contains every externally admitted parentless root whose integer parameter satisfies

```text
p is prime
p = 24t + 1
q = 1
X = 6t + 1 = (p+3)/4
every prime factor of X is 1 mod 3
```

The frozen policy is:

```text
0 gap 3 terminal    PRIOR
1 gap 7 terminal    PRIOR
2 gap 11 terminal   PRIOR
3 gap 15 terminal   PRIOR
4 gap 19 terminal   PRIOR
5 gap 23 terminal   PRIOR
6 phase-root        SELECTED PRODUCER
7 gap 31 terminal   LATER
```

All registered terminal predicates overlap the producer domain and are exhaustively classified by the signed coordinator manifest. There is no reject action. For every admitted source, the earliest M23 HIT terminates; after six MISS records the producer guard is true and the uniform phase-root construction satisfies E1--E5/R, common admission, unique pilot queue ingress and actual re-entry.

For `p=21169` the complete positive trace has

```text
t = 882
X = 5293 = 67 * 79
R = 14115
K = 74700109
4K = pR + 1
source potential = (21169, 3, 0, 0, 0, 0, 0)
target potential = (21169, 2, 4, 112021056, 74700109, 0, 0)
re-entry = ENTERED_TYPE_I_FULL_CARRIER_POST_G_BODY
```

The later gap-31 certificate remains present:

```text
4/21169 = 1/5300 + 1/3619899 + 1/19185464700
```

Hence the M23 receipt is scope-bound and is never `MISS_COMPLETE`.

The constructor and independent replayer use different divisor-enumeration algorithms. A bounded audit below 100000 covers all 606 predicate-domain roots and obtains six successors:

```text
21169, 61681, 67369, 87481, 94441, 99961
```

The bounded audit is regression evidence, not the basis of the universal proof.

The offline coordinator signs the exact policy and artifact-lock digests. Runtime code pins the public-key fingerprint, contains no private key, accepts no caller authority boolean, and gives the producer no policy-mutation power. The independent prefix replayer does not import or invoke the selected producer or its edge verifier.

This claim does not establish production-wide SP-03, post-G body totality, F1/F2/F3, T6, or the Erdős--Straus conjecture.
