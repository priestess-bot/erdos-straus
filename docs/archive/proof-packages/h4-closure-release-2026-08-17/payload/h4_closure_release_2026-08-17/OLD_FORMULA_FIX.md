# 旧 H4 clean-q claim 的公式修正

文件：
`claims/type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge.md`

将按分支定义的旧公式

```tex
M_q=
\begin{cases}
\operatorname{lcm}(M_4,Q_x), & \text{恰一块非平凡},\\
\operatorname{lcm}(M_4,Q_x,Q_y), & \text{双侧非平凡}
\end{cases}
```

统一替换为

```tex
\boxed{M_q=\operatorname{lcm}(M_4,Q_x,Q_y)}.
```

理由：actual single-side 已由后续结果收缩为
\[
Q_x=1<Q_y.
\]
若仍用第一行，则 \(M_q=\operatorname{lcm}(M_4,1)=M_4\)，完全漏掉唯一非平凡的 \(Q_y\) block，与“非平凡 complete-excess block 产生严格 support enlargement”的下一句矛盾。

同时把后续 multiplier 文本改为：

```tex
L_q=M_q/M_4,
\qquad
E_x=Q_x/(M_4,Q_x),
\qquad
E_y=Q_y/(M_4,Q_y).
```

并说明在 actual endpoint 中 \(Q_y>1\)，故修正后的 \(M_q>M_4\)、\(L_q>1\)。后续 `complete-excess-stutter-reduction` 已经使用这一统一公式，因此该修复是对旧卡的接口一致性修正，不改变后续 stutter 证明。
