# T6 F2/F3 第四轮数学边界

> 日期：2026-08-25
>
> 状态：本轮没有新增 terminal、actual source receipt、registered producer 或
> `VERIFIED_SUCCESSOR`。所有结果都是精确的 terminal-search 或 complete-excess
> 分流定理，目的是把下一次证明的量词压到可审计的最小剩余。

## 1. F2 R=3 hard core：D 因子不能直接解决问题

设 \(D=2p-3\)。最自然的 Type II 尝试是让 AC normal form 的 defining factor
\(h=4ACK-1\) 自身整除 \(D\)。这个分支已完全耗尽：连同 \(h\mid Kp+A\) 会强制

\[
h\mid3K+2A,
\tag{1}
\]

因而只剩 \(h=7\) 或 \(h=11\)。前者已有 gap-7 terminal，后者会使
\(11\mid p+4\)，与 hard core 矛盾。故不能把 \(D\) 整体作为新的 Type II 因子。

真正剩余的 Type II 搜索现在有明确的 mixed-completion 形式：若 \(q\mid D\) 只作为
\(h\) 的真因子，则必须同时满足

\[
3K+2A\equiv0\pmod q,\qquad8A^2C+3\equiv0\pmod q,
\tag{2}
\]

并额外完成 \(h/q\) 的整除、正性和有序条件。Type I 的对应接触也不再是自由度：
\(m\mid D\) 等价于 \(m\mid2A+3B\)。因此下一步不是扫描 \(D\) 的素因子，而是
证明 (2) 的 mixed completion terminal，或给出该 completion 的 structural no-go。

完整命题见
[`type-I-f2-r-three-d-contact-terminal-boundary`](../claims/type-I-f2-r-three-d-contact-terminal-boundary.md)。

## 2. Canonical root：direct landing 的真正算术门

对 canonical root support \(A_\star\)，任何 ordinary same-phase single-side 或 atomic
complete-excess direct landing 必满足 \(A_\star=aL\) 与

\[
c=p-\langle L\rangle_p,\qquad Q_{\rm tot}=dL,
\tag{3}
\]

其中 \(d\) 是 source support 在 \(L\)-prime 上的部分。每个 \(q^e\Vert L\) 都要通过
\(v_q(c)<e\) 的最大性门。这个条件已转化成 single-side 的有限 factor-pair kernel 和
atomic 的双色整数 kernel。

直接 E5 更强地强制 \(a\le B_p\)。由此，若 \(A_\star\) 含有某个
\(q^e\ge(p-1)^2\)，则这种 direct landing 为空。但这不是全域 no-go：\(p=73\) 存在一个
静态 atomic chart 同时满足所有 lcm/maximality/E5 等式。因此剩下的是 root prime powers
全都较小的 smooth-root sector，且必须从真实前驱正向构造 receipt。

这条结果直接否定“用 capacity bound 排除 atomic”的路线，但给出了未来 E1 verifier
必须执行的精确整数门。详见
[`type-II-q-one-canonical-root-direct-complete-excess-landing-gate`](../claims/type-II-q-one-canonical-root-direct-complete-excess-landing-gate.md)。

## 3. TR1 dyadic-fresh：从模糊因子变为四路 child 分流

在 \(2\mid(D_*,E)\) 的低 proper-root stutter 子域，设
\(\lambda=v_2(p-1)\)。现已证明

\[
v_2(A)\ge\lambda+2,\qquad v_2(h^2-1)=\lambda+1,\qquad
v_2(m+2)=\lambda.
\tag{4}
\]

dyadic child 不会耗尽 selected complete-excess：它保留 \(E_x>1\)，并有
strict cofactor \(\langle-2^\mu\rangle_p<p-1\)。child terminal-first miss 后仅剩：

```text
one-sided strict complete-excess
atomic strict complete-excess
atomic companion stutter
```

最后一项是真正的唯一 companion gate；现有 residue 信息不能排除其第二 child 获得
\(p\)-block。于是 TR1 的下一步可精确集中为：为该四路分流补充 source transcript、
child terminal receipts 与 atomic companion 的最终 recanonicalization，而不是继续研究裸
\(D_*\) 因子。

完整命题见
[`type-I-t6-f3-tr1-dyadic-fresh-child-normalization`](../claims/type-I-t6-f3-tr1-dyadic-fresh-child-normalization.md)。

## 4. 下一阶段的最小有效目标

三条结果共同指向同一顺序：

1. 在一个具体 actual source family 中，实现
   `f3_proper_root_endpoint_path_receipt_v1` 的 parent/scope/raw-prefix/terminal binding；
2. 优先选择 TR1 dyadic-fresh 或 canonical-root smooth sector 的一个分流，正向重算其
   complete-excess child；
3. 只有当该 child 通过 terminal priority、target type、E4 和 parent-to-final E5 后，才接入
   common E3 admission。

F2 的 mixed \(D\)-completion 则应独立走 terminal proof，不应以 raw source 或 F3
receipt 代替 Type II certificate。
