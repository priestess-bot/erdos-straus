# Agent 7 F3 (m=3,q=5,p^2) Wave-1 Handoff

> Branch: `sol/f3-m3-q5-p2`
>
> Base: `9215f8c92c53c0eb1081849b0a03e5cb922facad`
>
> Status: partial mathematical closure; active-runtime E3 and four mathematical leaves remain open.

## Exact owned domain

This track owns only actual persistent, terminal-first-surviving low proper-root states with

\[
m=3,qquad 5\mid D_*,qquad 2\le h<p,
\]

split into `R1_M3_Q5_PATH_UNBOUND` and `R2_M3_Q5_PATH_BOUND_NO_SERIALIZER`.
The full q5 domain is retained: the nonminimal (v_5(T)\ge2) leaf is not replaced by the
minimal (v_5(D_*)=v_5(T)=1, 5\nmid E) leaf.

## Established mathematics

1. A full actual-persistent parent determines a canonical source-forward raw transcript:
   `universal_p_source_v1`, then two nondecreasing capacity words to ((h,R-h)).
   The transcript is content-bound to parent ID, charged support and source scope. It is an E1
   artifact, not a successor.
2. Pure-dyadic, odd first-child and (omega_{\rm pf}) endpoints use one synchronous
   recanonicalizer. It recomputes complete-excess blocks and
   (L_\omega); it never imports an (L_1) theorem.
3. Every nonterminal target has
   
   \[
   M=A L_\omega>A>B_p,
   \]
   
   so (R_T<p) is impossible. Every strict target is a high-support
   `TYPEI/CHARGED OVERFLOW` and pays the original-parent-to-final
   `LOCAL_DROP` by (c_T<p-1).
4. Odd first-child strict, dyadic/omega strict, (	heta_\omega=-1), and
   (	heta_\omega\notin\{-1,0,1\}) have mathematical E1, E2, identity E4 and final E5.
   They remain unregistered only because the common producer/E3/re-entry is coordinator-owned.
5. In the nonminimal branch, (5\mid E) gives an actual, primitive, p-free q=5 child.
   No selected-side E5 is inferred because the (p-1) overlap can absorb the apparent support drop.

## Exact residual partition

The machine-readable matrix has 12 mutually exclusive leaves:

- R1 path payload missing;
- nonminimal q5 root residue;
- terminal;
- dyadic endpoint strict;
- odd first-child strict;
- full-capacity endpoint strict;
- short endpoint strict;
- (	heta_\omega=-1) raw-source channel;
- (	heta_\omega=1) regeneration channel;
- (	heta_\omega=mathrm{OTHER}) residual-strict channel;
- one-sided (p^2);
- genuine two-sided (p^2).

The proof receipt retains four mathematical open groups:

1. `R2_M3_Q5_NONMINIMAL_ROOT_RESIDUE`: after the established (5\mid E) child reduction,
   (5\nmid E) and all non-strict descendants still need EMPTY/TERMINAL/PAID.
2. `R2_M3_Q5_P_STUTTER_REGENERATION`: countdown is finite, but may return to p-free failure.
3. `R2_M3_Q5_P2_ONE_SIDED`: close
   
   \[
   v=(1+p^2\chi)d,qquad 4uw=c+p+p^3\chi.
   \]
4. `R2_M3_Q5_P2_TWO_SIDED`: close
   
   \[
   E_u,E_v>1,qquad E_uE_v=1+p^2\chi
   \]
   
   under the actual cross-divisor and path constraints.

Higher congruence, a finite scan, or an internal checkpoint is not a closure mode.

## Coordinator interface requirements

1. Attach the full path/scope/prefix payload to a common producer receipt; do not accept
   `raw_path_bound=true` as proof.
2. Register the track producer and target rights for the existing
   `type_i_a_gt_one_overflow_residual` fallback.
3. Run synchronous target normalization and compute owner from final facts. One-/two-sided
   occurrence ownership remains in the edge receipt; H4/C8 atomic arms are not reused.
4. No new persistent family is requested. p-stutter and p² objects remain nonpersistent checkpoints.

## Cross-audit

Agent 4 found and blocked an impossible draft shape `R_T<p, M>B_p`. The final invariant
(M=A L_\omega>A>B_p) deletes that shape entirely. Agent 7 independently reviewed Agent 1 commit
`3e69b4d`: its low-chart result stops at overflow handoff and its H4 owner is recomputed from final
(M_T,c_T,R_T); only wording around active E3 admission was recommended for tightening.

## Artifacts

- `data/t6-wave1/f3-m3-q5-p2-scope-freeze-v1.json`
- `data/t6-wave1/f3-m3-q5-p2-residual-matrix-v1.json`
- `data/t6-wave1/f3-m3-q5-p2-proof-receipt-v1.json`
- `data/interface-requests/f3-m3-q5-p2-target-shapes-v1.json`
- `claims/type-I-t6-f3-m3-q5-source-bound-macro-interface.md`
- `claims/type-I-t6-f3-policy-endpoint-p2-divisor-source-normal-form.md`
- `reproductions/type_i_t6_f3_m3_q5_source_bound_macro.py`
- `reproductions/type_i_t6_f3_policy_endpoint_p2_gate.py`

No README, index, frontier, shared runtime or shared grammar file was edited.
