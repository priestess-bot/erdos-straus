### H4 clean q-bridge E1–E5 相对宏验证器

`type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py` 对已经取得 upstream actual-H4 receipt 与版本化 priority-prefix miss receipt 的 H4 clean-q endpoint 做完整局部重算：canonical q-word、proper-prefix nonterminal、maximal complete-excess blocks、修正后的 `M_target=lcm(M4,Q_x,Q_y)`、stutter miss、canonical target、pending-dispatch serializer、identity lift 和 persistent-parent-to-target strict rank。

```bash
python reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py --input receipt.json
python reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py --verify-controls
```

`--verify-controls` 只重放已有 p=73、241 的局部 arithmetic controls，不重新证明 upstream 19-phase H4 provenance。
