---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h5-top-capacity-d-one-handoff
title: q=1 高 C=2 19 相位 H5 顶容量的 d=1 handoff 与唯一 a=1 p-free 残余
statement: >-
  在 q=1 high C=2 19 相位中，设 H4=>H5 的 fifth-anchor complete-excess receipt
  已通过其 source/path、p-free、terminal-first 与 typed guards，并且 H5 的 canonical
  capacity c5=p-1。则 M5=(pn5-1)/4、R5=(p-1)n5-1、K5=M5(p-1)，其中
  n5=(4M5+1)/p>1 且 n5=1 (mod 4)，所以 H5 精确落入完整乘积 d=1 饱和行。令
  (p+1)/2=ga、(n5+1)/2=gb、(a,b)=1、E=(p-1)b-a、eta=v_p(E-1)，并令
  omega=(E-1)/p^eta (mod p)。那么 a=1 当且仅当 (p+1)/2 整除 M5；有限次
  d=1 canonical regeneration 保持 a 并使 eta 每步减一。若其末态是 raw p-source
  failure，最小互素素数 source 给出 residual capacity <p-1；若末态为非 p-free
  非 regeneration 类，canonical capacity 也 <p-1；若末态为 p-free failure 且 a>1，
  真实 p-primary 剥离--小锚 complete-excess route 给出 capacity <p-1。因此在所有
  checkpoint 的 terminal/type/source guards 与 serializer 均通过时，原 persistent parent
  P 的 (0,p-1) 容量可直接比较到该最终端点，组成 strict guarded macro。唯一未被该
  handoff 清除的算术类是 a=1 且 omega=-1 (mod p) 的 p-free return；等价地，
  (p+1)/2|M5 且 finite d=1 suffix 的末态满足 R=1 (mod p)。本结果不证明该残余
  必有短证书或 n<p 递降，亦不把尚未验证的 checkpoints 登记为递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-fifth-anchor-parent-macro-gate
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-chart-least-coprime-prime-anchor-source
  - type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
  - type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fifth-anchor
  - top-capacity
  - d-one
  - p-adic-regeneration
  - p-free-failure
  - small-anchor
  - guarded-macro
  - residual-classification
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-fifth-anchor-parent-macro-gate
    role: H4-to-H5-parent-receipt-and-top-capacity-case
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: d-one-normal-form-regeneration-and-strict-capacity-map
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: raw-p-source-failure-repair
  - claim: type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
    role: a-greater-than-one-p-free-strict-small-anchor-exit
  - claim: type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
    role: a-one-terminal-digit-and-p-free-return-classification
  - concept: denominator-escape-state-contract
    role: guarded-E1-E5-requirements
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h5_top_capacity_d_one_handoff.py
    role: top-capacity-normal-form-and-suffix-classification-receipts
visibility: public
last_checked: '2026-08-15'
---

# q=1 高 \(C=2\) 19 相位 H5 顶容量的 \(d=1\) handoff

## 1. 顶容量不是新的自由图表

保留 H4 \(\Rightarrow\) H5 fifth-anchor receipt 的记号。令

\[
K_5=M_5c_5,
\qquad
pR_5+1=4K_5,
\qquad
c_5=p-1.
\tag{1}
\]

H4 的 high-support 边界给出 \(M_5>M_4>B_p=(p-1)^2/4\)。由 (1) 模 \(p\)
得到

\[
4M_5\equiv-1\pmod p.
\tag{2}
\]

所以

\[
\boxed{n_5:=\frac{4M_5+1}{p}\in\mathbb N.}
\tag{3}
\]

又 \(p\equiv1\pmod4\)，故 \(n_5\equiv1\pmod4\)。将 (3) 代回 (1) 得到精确
正规形

\[
\boxed{
M_5=\frac{pn_5-1}{4},\qquad
R_5=(p-1)n_5-1,\qquad
K_5=M_5(p-1).
}
\tag{4}
\]

特别地，\(n_5>1\)，因为 \(M_5>B_p\)。所以 \(c_5=p-1\) 并非一张新的
untyped high-support chart：它精确是已有 full-product \(d=1\) 饱和行的入口。

## 2. d=1 坐标与顶容量的支持判别

写

\[
\alpha=\frac{p+1}{2}=ga,
\qquad
v=\frac{n_5+1}{2}=gb,
\qquad
(a,b)=1,
\tag{5}
\]

并令

\[
E=(p-1)b-a,
\qquad
\eta=\nu_p(E-1),
\qquad
\omega\equiv\frac{E-1}{p^\eta}\pmod p.
\tag{6}
\]

这里 \(E>1\)，故 \(\eta\) 与 \(\omega\) 均有定义。顶容量 state 的三个 immediate
门仍是

\[
\begin{array}{c|c|c}
b\pmod p & \text{等价状态检测} & \text{分派}\\ \hline
0 & n_5\equiv-1,\ R_5\equiv0 & \text{raw }p\text{-source failure}\\
-a & n_5\equiv-2,\ R_5\equiv1 & p\text{-free failure}\\
-a-1 & E\equiv1 & d=1\text{ regeneration}\\
\text{其它} & E\not\equiv0,1 & \text{strict canonical capacity}.
\end{array}
\tag{7}
\]

例如第二行只用 \(2ga=p+1\equiv1\pmod p\)：

\[
b\equiv-a
\iff n_5=2gb-1\equiv-2
\iff R_5=(p-1)n_5-1\equiv1\pmod p.
\tag{8}
\]

还有一个对 H5 residual 很有用、但以前没有记录的精确支持判别：

\[
\boxed{
a=1
\iff \frac{p+1}{2}\mid M_5.
}
\tag{9}
\]

事实上，\(a=1\iff p+1\mid n_5+1\)。由 \(pn_5=4M_5+1\) 在模 \(p+1\)
下化简，右式等价于 \(p+1\mid4M_5\)。核心素数满足
\(p\equiv1\pmod8\)，所以 \((p+1)/2\) 为奇数；因而
\(p+1\mid4M_5\iff(p+1)/2\mid M_5\)，得到 (9)。

## 3. 所有非 a=1 p-free 后缀都严格离开顶容量

若 (7) 的第三行发生，\(d=1\) regeneration 产生下一完整乘积行，并保持 \(g,a\)，
同时使 \(\eta\) 恰减一。故至多 \(\eta\) 次后到达 (7) 的非 regeneration 行。

该终行有三种可能：

1. 若 \(b\equiv0\pmod p\)，最小互素素数 source 代替失效的 raw \(p\)-source，
   到达同一 complete-excess anchor；其 canonical capacity 是
   \(\langle2g\rangle_p\le p-2\)。
2. 若 \(b\not\equiv0,-a,-a-1\pmod p\)，canonical multiplier 不为 \(0\) 或 \(1\)
   模 \(p\)，故 target capacity 已严格小于 \(p-1\)。
3. 若 \(b\equiv-a\pmod p\)，这是 p-free failure。若 \(a>1\)，真实
   \(p\)-primary peeling 到小锚的 complete-excess route 是 p-free，且其
   canonical capacity 严格小于 \(p-1\)。

因为 regeneration 保持 \(a\)，第三种在初始 \(a>1\) 时也不会离开已闭合的
\(a>1\) 分支。因此

\[
\boxed{
a>1\quad\Longrightarrow\quad
\text{H5 top-capacity suffix 在有限步后有 residual capacity }<p-1.
}
\tag{10}
\]

式 (10) 是算术 handoff；每个实际 checkpoint 仍必须依序重放 terminal-first、
typed reclassification、source/path 与 state serializer。

## 4. 唯一残余的精确数字标签

现在设 \(a=1\)。此时已有 terminal-digit 正规形适用：经过恰 \(\eta\) 次
regeneration 后，末个 non-regeneration multiplier 满足

\[
E_{\eta}\equiv1+\omega\pmod p.
\tag{11}
\]

它是 p-free failure 当且仅当 \(\omega\equiv-1\pmod p\)；\(\omega\equiv-2\)
给 raw-source failure，其余 residue 给 strict capacity。因此 H5 top capacity 的精确
未清除类为

\[
\boxed{
\frac{p+1}{2}\mid M_5
\quad\text{且}\quad
\omega\equiv-1\pmod p.
}
\tag{12}
\]

若 \(\eta=0\)，(12) 只是 immediate p-free failure；若 \(\eta>0\)，它表示有限
regeneration suffix 的 p-free return。两者都进入已有 \(a=1\) real-reach hard branch；
这里没有把它伪称为 terminal 或 strict descent。对本 q=1 H5 receipt，这个残余先由
[H4 全重叠有限素因子筛](type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-finite-sieve.md)
压缩到显式有限菜单，再由其
[有限筛完成](type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-sieve-completion.md)
证明没有实际 H3--H4 predecessor。因此 \(a=1\) 在这个 19-phase H5 top-capacity 域内
为空；本卡保留的 generic \(a=1\) real-reach boundary 不因此自动推广到其它来源。

## 5. Guarded macro 的作用域

设 H4 \(\Rightarrow\) H5 的 parent 为 \(P\)，且

\[
\Lambda_p^\sharp(P)=(0,p-1).
\tag{13}
\]

对不在 (12) 中的输入，取第 3 节产生的最终 strict capacity endpoint \(T\)。每个
H5/d=1 checkpoint 都只作为 macro 内部记录，而不单独入队。若以下 guards 都通过：

1. H4/H5 和所有 suffix checkpoint 的 terminal-first、实际 source/path、完整
   complete-excess receipt；
2. 每个 target 的独立 typed reclassification 与 normal-form verifier；
3. 从 \(P\) 的同一 persistent scope 继承，并使用图表无关
   \(\operatorname{Sol}(p)\) 的 identity lift；

则 E1--E4 可逐段复合，而由 \(M_5>B_p\) 及最终 \(c_T\le p-2\)，有

\[
\Lambda_p^\sharp(P)=(0,p-1)>(0,c_T)=\Lambda_p^\sharp(T).
\tag{14}
\]

这支付该固定 H5 suffix 的 E5。它不是 G/Type I 全局势函数：式 (12) 仍需独立的
short-certificate 或 \(n<p\) lift；未通过上述 guards 的算术路径只保留为
`analysis_evidence`。

## 6. 定向回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h5_top_capacity_d_one_handoff.py --verify
```

该回执检查八个固定 high-support top-capacity \(d=1\) 正规形：直接 strict、raw-source
repair、\(a>1\) p-free handoff、\(a=1\) p-free residual、以及通向 strict/raw/p-free
末态的 regeneration suffix。它们是 (1)--(12) 的整数控制，不声称其中任一个是实际
19-phase H5 witness，也不扫描素数或完整 selector history。
