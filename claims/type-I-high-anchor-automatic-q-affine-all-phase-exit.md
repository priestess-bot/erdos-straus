---
kind: claim
claim_id: type-I-high-anchor-automatic-q-affine-all-phase-exit
title: automatic q 高锚的全相位仿射 target 与外层秩出口
statement: >-
  对任一严格 automatic high-anchor source，若 complete-excess rechart 满足
  C=qA<p、q>1（因此 q 为 2 或 3），令 r=M mod p、K=AB 与
  h=(qr-B)/p，则 direct cofactor target 精确为
  T=(p,R+4hA,K+hpA;qA)，其 canonical quotient 为
  B_T=r=(B+hp)/q，且仍处于高窗口 p<R_T<4qA。因 qA<p 且 q>=2，
  外层支撑秩严格满足 Pi_p(qA)<Pi_p(A)，不依赖 h 或 residual 是否小于 p。
  因而一旦该宏另行满足 E1--E4、terminal-first guard，所有 automatic-q 相位都是
  已付款的 E5 state exit；q=3 的 h=0,1 非最小相位仅不能由该 direct target
  提供题设要求的字面 n<p 分母递降，并非缺少严格状态势。该结论不建立宏准入、
  typed lift、guarded dispatcher 或最终 terminal/小分母出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-automatic-q-source-template
  - type-I-high-anchor-three-phase-nonreturn-window
  - type-I-high-anchor-cofactor-outer-rank-composition
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - type-I-high-anchor-cofactor-terminal-guarded-adapter
  - type-I-high-anchor-automatic-q-phase-descent-trichotomy
topics:
  - Erdos-Straus
  - type-I
  - high-anchor
  - automatic-q
  - cofactor
  - phase
  - outer-rank
  - well-founded-descent
  - terminal-first
  - proof-boundary
sources:
  - claim: type-I-high-anchor-automatic-q-source-template
    role: automatic C=qA source and phase identities
  - claim: type-I-high-anchor-cofactor-outer-rank-composition
    role: global E5 composition for admitted direct cofactor macros
  - reproduction: reproductions/type_i_high_anchor_automatic_q_affine_rank_exit.py
    role: focused exact replay of q=2 h=1 and q=3 h=0/h=2 fresh-root controls
visibility: public
last_checked: '2026-08-16'
---

# automatic \(q\) 高锚的全相位仿射 target 与外层秩出口

## 1. 范围与结论

固定核心素数 \(p\equiv1\pmod {24}\)。设严格 automatic high-anchor source 为

\[
H=(p,R,K;A),\qquad p<R<4A,\qquad K=AB,
\tag{1}
\]

其 complete-excess carrier \(M\) 的 rechart 满足

\[
C=qA<p,\qquad q>1,\qquad q\in\{2,3\},\qquad r=M\bmod p.
\tag{2}
\]

因为 \((A,C)=A\)，cofactor gate 自动通过，target support 是
\(A_T=\operatorname{lcm}(A,C)=qA\)。automatic congruence 给出
\(qr\equiv B\pmod p\)，故可唯一写成

\[
h={qr-B\over p},\qquad 0\le h<q.
\tag{3}
\]

**定理。** direct cofactor target 的完整 canonical chart 为

\[
\boxed{
T_h=(p,R+4hA,K+hpA;qA),
\qquad B_T={K+hpA\over qA}=r.
}
\tag{4}
\]

它始终仍是高锚：

\[
p<R+4hA<4qA.
\tag{5}
\]

此外，令 \(B_p=(p-1)^2/4\)、\(\Pi_p(X)=\lfloor B_p/X\rfloor\)，则

\[
\boxed{\Pi_p(qA)<\Pi_p(A).}
\tag{6}
\]

因此，在独立满足高锚 cofactor 宏的 E1--E4 和 terminal-first guarded adapter 后，
\(H\Longrightarrow T_h\) 在**每一个** automatic-q 相位都是严格 E5 边。

这里的结论是 state exit，不是对原分母的直接小分母递降。它不改变 residual 恒等式

\[
n_T=n+4A(q-h-1),\qquad n=4A-R.
\tag{7}
\]

所以当 \(q=3\) 且 \(h=0,1\) 时，仍有 \(n_T>p\)，不能用该 target 作为题设所需的
\(n<p\) 递降实例。

## 2. 仿射 target 的证明

由 (3)，有 \(qr=B+hp\)。乘以 \(A\) 得

\[
rC=qrA=AB+hpA=K+hpA.
\tag{8}
\]

左端正是 cofactor target 的 \(K_T\)，故得到 (4) 的第二坐标。两条 chart determinant

\[
pR+1=4K,\qquad pR_T+1=4K_T
\tag{9}
\]

相减后给出

\[
R_T=R+4hA.
\tag{10}
\]

因为 \(0\le h<q\) 且 \(p<R<4A\)，立刻有 (5)。又 (8) 写成
\(K_T=qAr\)，所以 target 是 support \(qA\) 的 canonical chart，且其 quotient
恰为 \(r=(B+hp)/q\)。

代入 \(n=4A-R\)、\(n_T=4qA-R_T\) 则给出 (7)。这也恢复已有最小相位
\(h=q-1\) 的 fixed-\(n\) shadow，却没有假定它是唯一可付款的相位。

## 3. 外层支付不依赖 residual

由 \(qA<p\) 知 \(A<p\)。核心素数满足 \(p\ge73\)，所以
\(A\le p-1\le B_p\)。又 \(q\ge2\)，容量倍增事实直接给

\[
\Pi_p(qA)<\Pi_p(A).
\tag{11}
\]

这正是 direct cofactor 外层秩定理中需要的第一坐标支付。\(h=0\) 时，(4) 特化为

\[
(R_T,K_T)=(R,K),\qquad q\mid B,
\tag{12}
\]

即同图表的严格 support promotion；\(h>0\) 时，target 图表发生仿射平移，但 (11)
仍独立完成付款。因而 `n_T>p` 只说明既有 fixed-\(n\) 小分母桥不可用，不说明 macro
缺少良基 state descent。

## 4. q=3 的精确分支含义

对互素 \(\beta_0=2\) two-anchor 子族，\(h\equiv1-k\pmod3\)。因此：

| \(k\pmod3\) | \(h\) | target | \(n_T\) | 已有可用出口 |
|---:|---:|---|---|---|
| 0 | 1 | \((R+4A,K+pA;3A)\) | \(n+4A>p\) | 条件性 E5 outer-rank exit |
| 1 | 0 | \((R,K;3A)\) | \(n+8A>p\) | 条件性 E5 same-chart support exit |
| 2 | 2 | \((R+8A,K+2pA;3A)\) | \(n\) | 条件性 E5 exit，且可接 fixed-\(n\) bridge |

第一行是 source-compatible parameter class；当前聚焦控制尚未声称找到它的 actual
fresh-root 实例。第二、三行分别由 \(p=41617,93481\) 与 \(p=60913\) 重放；\(q=2\)
的 \(p=3793,h=1\) 控制检验相同仿射公式。所有已有控制均被 terminal-first 叶抢占，
不能由本卡改登记为递归边。

## 5. 边界与下一缺口

本卡收窄了 automatic-q 非最小相位的缺口：不再需要为它们另造一个 E5 势；真正尚未证明的
部分是

\[
\text{actual source/parent} + \text{typed E4} + \text{terminal-first guard}
\Longrightarrow \text{admitted macro},
\tag{13}
\]

以及任意有限 \(\Lambda_p\) state path 的最终 terminal 或可提升小分母出口。式 (6) 不会
单独制造这些合同，也不会把 \(n_T>p\) 误转换成原猜想所需的 \(n<p\) 递降。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_high_anchor_automatic_q_affine_rank_exit.py --verify
~~~
