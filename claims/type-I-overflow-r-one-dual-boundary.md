---
kind: claim
claim_id: type-I-overflow-r-one-dual-boundary
title: overflow 余数 r=1 的对偶边界
statement: 设核心素数 p≡1 (mod 24) 的 overflow 满足 pn=4Md+1、M=kp+r、1≤r<p、1≤d<p，并令 s=(4rd+1)/p=n-4kd。若 r=1，则 s=1、d=(p-1)/4；d 对偶图表恒为 (p-2,(p-1)^2/4)，r 对偶图表恒为 (3,(3p+1)/4)。该参数族可形成真实 overflow，但 r=1 本身不自动给出一般 A>1 的保持累积支撑 E1--E5 递归边；初始 A=1 的 d 侧出口已由既有 determinant 边覆盖，r=1 只应作为对偶分类边界，不应作为新的统一出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-d-one-p-minus-two-g-rechart
topics:
  - type-I
  - overflow
  - determinant
  - symmetric-dual
  - r-one-boundary
  - charged-support
  - proof-boundary
sources:
  - claim: type-I-overflow-determinant-fixed-n-dual-support-conflict
    role: overflow-determinant-and-symmetric-dual-normal-form
  - claim: type-I-overflow-d-one-p-minus-two-g-rechart
    role: universal-p-minus-two-g-chart
  - reproduction: reproductions/type_i_universal_anchor_overflow_dual.py
    role: symmetric-dual-formulas
visibility: public
last_checked: '2026-08-03'
---

# overflow 余数 \(r=1\) 的对偶边界

## 1. 正规形

设 verified overflow 满足

\[
pn=4Md+1,
\qquad M=kp+r,
\qquad 1\le r<p,
\qquad 1\le d<p,
\tag{1}
\]

并令

\[
s=\frac{4rd+1}{p}=n-4kd.
\tag{2}
\]

这里的第二个等式来自把 \(M=kp+r\) 代回 (1)。若 \(r=1\)，则

\[
ps=4d+1.
\tag{3}
\]

因为 \(1\le d<p\)，有

\[
0<4d+1<4p.
\]

另一方面 \(p\equiv1\pmod4\)，而 \(4d+1\equiv1\pmod4\)，所以在

\[
4d+1\in\{p,2p,3p\}
\]

中只有 \(p\) 的倍数保持模 \(4\) 为 \(1\)。因此

\[
\boxed{s=1,\qquad d=\frac{p-1}{4}.}
\tag{4}
\]

代入对称双图表

\[
(R_d,K_d)=(4d-s,d(p-r)),
\qquad
(R_r,K_r)=(4r-s,r(p-d)),
\tag{5}
\]

得到

\[
\boxed{(R_d,K_d)=\left(p-2,\frac{(p-1)^2}{4}\right),}
\qquad
\boxed{(R_r,K_r)=\left(3,\frac{3p+1}{4}\right).}
\tag{6}
\]

所以 \(r=1\) 并不是一个新的自由小载体问题：d 侧退化为已经分类的普适
\(p-2\) G 图表，r 侧退化为单位载体的 \(R=3\) 图表。初始 \(A=1\) 时 d 侧的
determinant 边仍然合法；新的问题只在 \(A>1\) 的支撑保持上。

## 2. 真实 overflow 参数族

该边界不是空集合。对任意 \(k\ge1\)，取

\[
M=kp+1,
\qquad d=\frac{p-1}{4},
\qquad n=k(p-1)+1.
\tag{7}
\]

则

\[
pn=4Md+1,
\qquad
R_M=4M-n=k(3p+1)+3>p,
\tag{8}
\]

且

\[
4M\frac{3p+1}{4}=pR_M+1.
\]

因此 (7) 确实给出每个核心素数上的无限 \(r=1\) overflow 族；它不能被当作
“有限样本没有出现”的伪边界。

## 3. 选择器边界

旧 charged support 为 \(A\mid M\) 时，两张图表仍须逐边检查

\[
\operatorname{lcm}(A,d)\mid K_d,
\qquad
\operatorname{lcm}(A,r)\mid K_r,
\]

以及严格 support gain、正 canonical chart 和外层势下降。\(r=1\) 本身不能提供
\(\operatorname{lcm}(A,r)>A\)：当 \(A=1\) 时载体仍为 \(1\)，当 \(A>1\) 时它
反而丢弃旧支撑。d 侧虽然可能在个别 \(A\) 上满足支撑整除，但这不是由 \(r=1\)
自动保证的；其普适图表是 G 态，目标 \(-1\) 不在 \(K_d\) 支撑生成的 Jacobi
子群中。

因此 \(r=1\) 只删除一类“期待对偶小图表必然提供新边”的错误搜索目标。它不关闭
递归可达的 \(A>1,\ R_M>p\) bundle overflow；剩余任务仍是 support-preserving
alternate、直接 Type I/II 终端，或有独立良基势支付的 support reset。

## 复核边界

代数核验覆盖核心素数 \(p\le10{,}000\) 和 \(1\le k\le8\) 的 1144 个参数状态，
逐项重算 (1)--(8) 及两张 canonical chart。该有限核验只检查正规形；全称结论来自
上述不等式和模 \(4\) 论证，而不是扫描外推。
