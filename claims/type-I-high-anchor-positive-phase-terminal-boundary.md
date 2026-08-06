---
kind: claim
claim_id: type-I-high-anchor-positive-phase-terminal-boundary
title: 高锚点正相位的余量终端接口边界
statement: 设通过 gate 的高锚点 direct cofactor r-chart 具有正相位 \(h\in\{1,2\}\)。令 \(q=h+1\)、\(e=c-q\)、\(d=p-K/A\)、\(d_T=p-t\)。则 \(c d_T=d+pe\) 且 canonical 余量满足 \(n_T=n+4Ae\equiv1\pmod4\)。若 \(e\ge1\)，则 \(n_T>p\)；若 \(e=0\)，则必有 \(a=1,c=q,d=q d_T,A_T=qA,n_T=n\)，即精确的 fixed-n shadow。故相位余量本身永远不能作为现有 Bradford \(3\pmod4\) gap 或偶的 generalized-dyadic predecessor；非最小相位还离开 \(0<n<p\) 域。\(p=1201\) 有 \(h=1\) 与 \(h=2\) 的合法算术 r-chart 实例，且其所有 Bradford gaps \(3,7,11,15,19\) 都无 Type I/II 证书，而首个命中为 gap \(23\) 的 Type I。因而正相位算术本身不强迫 gap \(<23\) 的短终端；该反例没有 source/path/F/G provenance，不能升级为递归边或 Erdos--Straus 反例。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-high-anchor-three-phase-nonreturn-window
  - type-I-overflow-cofactor-r-chart-support
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-generalized-dyadic-standard-even-lift-boundary
topics:
  - type-I
  - type-II
  - high-carrier
  - r-chart
  - positive-phase
  - fixed-n
  - terminal-first
  - Bradford-gap
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_positive_phase_terminal_boundary.py
    role: targeted p=1201 arithmetic charts and exact small-gap audit
  - result: reproductions/type-i-high-anchor-positive-phase-terminal-boundary-results.json
    role: frozen targeted replay receipt
visibility: public
last_checked: '2026-08-06'
---

# 高锚点正相位的余量终端接口边界

## 1. 设置

固定 \(p\equiv1\pmod4\)。设一个高 canonical anchor 与一个已通过代数 gate 的
direct cofactor r-chart 满足

\[
pR+1=4K,\qquad K=AB,\qquad p<R<4A,
\tag{1}
\]

\[
g=(A,C),\qquad A=ga,\qquad C=gc,\qquad r=at,
\tag{2}
\]

\[
A_T=\operatorname{lcm}(A,C)=Ac,\qquad
K_T=rC=Act,
\tag{3}
\]

并令

\[
h=\frac{K_T-K}{pA}\in\{1,2\}.
\tag{4}
\]

三相引理已经给出

\[
ct=B+ph,\qquad c\ge ha+1.
\tag{5}
\]

定义 anchor 与 target 的补量和 canonical 余量

\[
d=p-B,\qquad d_T=p-t,
\qquad n=4A-R,\qquad n_T=4A_T-R_T.
\tag{6}
\]

这里 \(d,d_T>0\)：高 canonical chart 有 \(B<p\)，而 target 仍是 canonical
chart，故 \(t<p\)。

令

\[
q=h+1\in\{2,3\},\qquad e=c-q.
\tag{7}
\]

正相位支撑界保证 \(e\ge0\)。

## 2. 余量恒等式与二分

由 (5) 及 \(B=p-d\)，

\[
ct=pq-d.
\tag{8}
\]

故

\[
c d_T=c(p-t)=cp-ct=d+p(c-q)=d+pe.
\tag{9}
\]

另一方面，两个 canonical chart 分别给出

\[
pn=4Ad+1,
\qquad
pn_T=4Ac d_T+1.
\tag{10}
\]

将 (9) 代入，得到本卡的基本恒等式

\[
\boxed{n_T=n+4Ae.}
\tag{11}
\]

又因 \(p\equiv1\pmod4\)，(10) 立刻给出

\[
\boxed{n\equiv n_T\equiv1\pmod4.}
\tag{12}
\]

这导致两个严格不同的情形。

### 2.1 非最小正相位

若 \(e\ge1\)，高 anchor 的 \(A>p/4\) 与 (11) 给出

\[
n_T\ge n+4A>p.
\tag{13}
\]

因此 \(n_T\) 不在标准 Bradford gap 的范围

\[
3\le m\le p-2,\qquad m\equiv3\pmod4,
\tag{14}
\]

之内；即使忽略范围，(12) 也排除把 \(n_T\) 本身当作这种 gap。它同样不属于
现有 generalized-dyadic terminal interface 的偶前驱域 \(0<n<p\)、\(n\equiv0\pmod2\)。

### 2.2 最小正相位

若 \(e=0\)，则 \(c=q=h+1\)。结合 (5)，

\[
h+1=c\ge ha+1
\quad\Longrightarrow\quad
a=1.
\tag{15}
\]

所以

\[
\boxed{
c=q,\quad a=1,\quad d=q d_T,\quad A_T=qA,\quad n_T=n.
}
\tag{16}
\]

这不是新终端，而是精确的 fixed-\(n\) shadow：\(L=qA\mid A(p-B)\)，且以
\(L\) 重图表的 \((R_L,K_L)\) 正是 \((R_T,K_T)\)。它属于既有 fixed-\(n\)
支撑分支的同一算术对象，而不是一个从相位余量直接得到的 Type I/II 叶；\(L\le B_p\)、
来源 provenance 与外层秩支付等条件仍须由该分支独立验证。

即使恰有 \(0<n<p\)，(12) 仍说明 \(n\) 是奇数且 \(1\pmod4\)，不是偶前驱；若
\(|p-n|\) 为正，则它又是 \(0\pmod4\)，也不是 Bradford gap。故这个结论关闭的是
**从 canonical residual 或其与 \(p\) 的直接距离进入既有终端接口**的尝试，不声称
原素数没有其它 Type I/II 终端。

## 3. 一个精确的受限 terminal 分支

正相位不控制 \(p\bmod7\)，但可与已有 terminal-first 分派组合。令

\[
x=\frac{p+7}{4}.
\tag{17}
\]

当 \(p\equiv1\pmod{24}\) 且满足下表任一剩余类时，gap \(7\) 已给出直接证书：

| \(p\pmod7\) | 类型 | 选择的除子 |
|---:|---|---:|
| \(3\) | Type II | \(1\) |
| \(5\) | Type I | \(2x\) |
| \(6\) | Type II | \(2\) |

确实，\(p\equiv1\pmod8\) 使 \(x\) 为偶数；逐行代入即可得到 Type I 的
\(7\mid px+2x\)，或 Type II 的 \(7\mid x+1\)、\(7\mid x+2\)。这是一个
对正相位也适用的受限 terminal 分支，但它来自 \(p\) 的剩余类，而非 (5) 的相位算术。
例如已有 \(p=3793\) 与 \(p=60913\) 的正相位控制例均为 \(6\pmod7\)。

## 4. \(p=1201\) 的针对性反例

下面两行都满足高 anchor、完整的**算术** overflow r-chart 正规形及 cofactor gate。
为显式给出 source chart，表中 \(M=kp+r\)、\(C=p-d_{\rm src}\)，并满足

\[
p n_{\rm src}=4M d_{\rm src}+1,
\qquad pR_{\rm src}+1=4MC.
\tag{18}
\]

| \(h\) | \(A\) | \(B\) | anchor \((R,K)\) | \(C\) | \(r\) | \(M=kp+r\) | \(d_{\rm src},n_{\rm src}\) | target \((A_T,R_T,K_T,n_T)\) |
|---:|---:|---:|---|---:|---:|---|---|---|
| \(1\) | \(319\) | \(1185\) | \((1259,378015)\) | \(638\) | \(1193\) | \(163328=135p+1193\) | \((563,306257)\) | \((638,2535,761134,17)\) |
| \(2\) | \(346\) | \(1096\) | \((1263,379216)\) | \(1038\) | \(1166\) | \(99648=82p+1166\) | \((163,54097)\) | \((1038,4031,1210308,121)\) |

两行都有 \(g=A\)、\(a=1\)、\(c=h+1\)、\(t=r\)，故

\[
2\cdot1193=1185+1201,
\qquad
3\cdot1166=1096+2\cdot1201.
\tag{19}
\]

它们正是 (16) 的 \(h=1\) 与 \(h=2\) 最小相位：分别有
\(d=16=2\cdot8\) 与 \(d=105=3\cdot35\)，并保持 \(n=17\) 与 \(n=121\)。

这些是 E2/算术 normal-form 反例，**没有**被声称为 source/path/charged-parent
provenance、F/G 纤维提升或 `candidate_transition`；更不可能成为递归边。

### 4.1 小 gap 的完整有限检查

对每个 Bradford gap \(m\)，令 \(x=(p+m)/4\)。Type I 和 Type II 的完整
除子判据分别要求某个 \(d\mid x^2\) 落在

\[
d\equiv-px\pmod m,
\qquad
d\equiv-x\pmod m\quad(d\le x).
\tag{20}
\]

对于 \(p=1201\)，所有小于 \(23\) 的可用 gap 都已由 (20) 穷尽。表中的第三列是
所有 \(d\mid x^2\) 的残数集合，因此已经强于 Type II 的 \(d\le x\) 限制。

| \(m\) | \(x\) 的分解 | \(\{d\bmod m:d\mid x^2\}\) | Type I 目标 | Type II 目标 |
|---:|---|---|---:|---:|
| \(3\) | \(301=7\cdot43\) | \(\{1\}\) | \(2\) | \(2\) |
| \(7\) | \(302=2\cdot151\) | \(\{1,2,4\}\) | \(3\) | \(6\) |
| \(11\) | \(303=3\cdot101\) | \(\{1,2,3,4,6,7,9\}\) | \(10\) | \(5\) |
| \(15\) | \(304=2^4\cdot19\) | \(\{1,2,4,8\}\) | \(11\) | \(11\) |
| \(19\) | \(305=5\cdot61\) | \(\{1,4,5,6,16\}\) | \(15\) | \(18\) |

所以这五个 gaps 都没有 Type I 或 Type II 证书。首个命中是

\[
m=23,\quad x=306,\quad d=34,\quad
(y,z)=(15980,172727820),
\tag{21}
\]

它是 Type I，且直接验证

\[
\frac4{1201}
=\frac1{306}+\frac1{15980}+\frac1{172727820}.
\tag{22}
\]

因此该例否定的只是“由 \(h=1,2\) 正相位算术强迫 gap \(<23\) 的短 terminal”这一
明确命题；它不是 Erdos--Straus 猜想的反例，\(p=1201\) 本身已由 (22) 终止。

## 5. 结论与下一接口

正相位留下的严格结构是：最小相位进入已有 fixed-\(n\) 秩，非最小相位离开现有
residual terminal interface。任何更强的 terminal-or-descent 定理都必须额外使用
source/path provenance、F/G 纤维、\(p\) 的因子化信息或一条新的可提升桥；不能从
\(ct=B+ph\) 与 \(n_T=n+4Ae\) 单独推出。
