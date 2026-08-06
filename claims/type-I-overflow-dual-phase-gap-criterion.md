---
kind: claim
claim_id: type-I-overflow-dual-phase-gap-criterion
title: overflow 双通道单位相位的 \(2p-r-d\) 精确间隙判据
statement: 设 verified overflow \(pn=4Md+1\)、\(M=kp+r\)，并取 \(q^a\parallel A\) 为旧支撑素数幂。若 \(q\nmid dr\) 且 d/r 两个 determinant 标签 \(k+1\)、\(dn-1\) 具有相同 q-进赋值 \(b\)，则两侧单位相位的共同深度完全由整数间隙 \(2p-r-d\) 决定：对 \(0\le j\le a-b\)，\(\eta_d\equiv\eta_r\pmod{q^j}\) 当且仅当 \(q^{b+j}\mid(2p-r-d)\)。因此相位树的分裂层数可在 overflow 坐标中直接计算，无需假设 alternate/source-map；不同赋值或 q 整除载体的分支不适用此式，转交一般单位相位或首层分离引理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-qadic-obstruction-transfer
  - type-I-overflow-dual-channel-first-layer-phase-separation
  - type-I-overflow-dual-phase-tree-split-capacity
topics:
- type-I
- overflow
- dual-channel
- q-adic
- phase-gap
- arithmetic-coordinate
- phase-tree
- capacity
- proof-program
sources:
  - claim: type-I-overflow-qadic-obstruction-transfer
    role: local-label-payment
  - claim: type-I-overflow-dual-phase-tree-split-capacity
    role: split-layer-capacity
visibility: public
last_checked: '2026-08-05'
---

# overflow 双通道单位相位的 \(2p-r-d\) 精确间隙判据

## 1. 共同赋值分支

设
\[
pn=4Md+1,\qquad M=kp+r,\qquad 1\le r<p,
\tag{1}
\]
并携带旧支撑 \(A\mid M\)。固定
\[
q^a\parallel A,\qquad q\ne p,
\tag{2}
\]
且假设
\[
q\nmid d,\qquad q\nmid r,\qquad
v_q(k+1)=v_q(dn-1)=b<a.
\tag{3}
\]
在这两个条件下，双通道未支付高度相同：
\[
h_d=h_r=a-b.
\tag{4}
\]
定义单位相位
\[
\eta_d=\frac{k+1}{q^b}\pmod{q^{a-b}},
\qquad
\eta_r=\frac{dn-1}{q^b}\pmod{q^{a-b}}.
\tag{5}
\]

## 2. 坐标间隙恒等式

因为 \(q^a\mid M\)，而 p 是 q-进单位，由 \(M=kp+r\) 得
\[
p(k+1)\equiv p-r\pmod{q^a}.
\tag{6}
\]
另一方面由 \(pn=4Md+1\) 得
\[
p(dn-1)=d(pn)-p=4Md^2+d-p
\equiv d-p\pmod{q^a}.
\tag{7}
\]
相减得到
\[
\boxed{
p\bigl((k+1)-(dn-1)\bigr)
\equiv 2p-r-d\pmod{q^a}.
}
\tag{8}
\]
由 (3) 左侧可除以 \(q^b\)，故
\(q^b\mid(2p-r-d)\)，并由 (5)、(8) 得到精确等价：
\[
\boxed{
\eta_d\equiv\eta_r\pmod{q^j}
\iff
q^{b+j}\mid 2p-r-d,
\qquad 0\le j\le a-b.
}
\tag{9}
\]
因此若约定 \(v_q(0)=+\infty\)，最大共同相位深度为
\[
\boxed{
s=\min\bigl(a-b,\ v_q(2p-r-d)-b\bigr).
}
\tag{10}
\]
当 \(v_q(2p-r-d)<a\) 时，(10) 给出第一处分裂层；当
\(q^a\mid2p-r-d\) 时，两侧在全部共同高度上相容。

### 证明

式 (6) 和 (7) 分别由 (1) 的两个整数恒等式取模 \(q^a\) 得到；p 可逆，所以
相减后除以 \(q^b\) 不改变模 \(q^{a-b}\) 的等价性。式 (9) 是
\(q^{a-b}\) 中的单位相位同余逐层展开，(10) 由 q-进赋值定义立即得到。证毕。

## 3. 直接接入相位树

在 (3) 的共同赋值分支中，双通道相位树的层胞数不必重新计算单位代表：
把 (10) 的 \(s\) 送入
[overflow 双通道相位树分裂的精确容量税](type-I-overflow-dual-phase-tree-split-capacity.md)
即可得到 \(D_k\) 和分裂税。特别地：

* \(q\nmid(2p-r-d)\) 时 \(s=0\)，首层立即分成两个胞；
* \(v_q(2p-r-d)=b+c<a\) 时，共享 \(c\) 层，随后在第 \(c+1\) 层分裂；
* \(q^a\mid(2p-r-d)\) 时，两个通道的整个共同高度相容，但仍不能自动扣除
  共同前缀，除非整数 'SHARED_PHASE_PREFIX' 映射和 E1--E5 通过。

这是一条纯 overflow 坐标判据：它不声称两侧可以构造同一个新分母，也不把相位相容
误写成 source-switch 成功。

若 \(v_q(k+1)\ne v_q(dn-1)\)，本卡的单位相位前提不成立；应先使用
[overflow 双通道不等赋值的加权相位正规形与首层分离](type-I-overflow-dual-valuation-asymmetry.md)
把赋值差吸收到 \(\zeta_t\) 中。只有在加权分派确认等赋值后，才允许使用本卡的
共同前缀和相位税。

## 4. 边界例子

### \(p=73,M=75\) 的五进间隙

取
\[
(p,M,d,n,r,k,A,q^a)=(73,75,9,37,2,1,25,5^2).
\]
此时 \(b=0\)，而
\[
2p-r-d=146-2-9=135,\qquad v_5(135)=1.
\]
故共同相位深度 \(s=1\)：单位相位
\(\eta_d=2\)、\(\eta_r=7\pmod{25}\) 在模 5 相同、在模 25 分裂。

### \(p=73,M=96\) 的二进间隙

取
\[
(p,M,d,n,r,k,A,q^a)=(73,96,23,121,23,1,8,2^3).
\]
此时 \(b=1\)，
\[
2p-r-d=100,\qquad v_2(100)=2,
\]
所以 \(s=2-1=1\)，与单位相位 \(1,3\pmod4\) 的共同前缀深度一致。

### 不适用的奇 q 载体分支

在
\[
(p,M,d,n,r,k,A,q^a)=(73,225,3,37,6,3,9,3^2)
\]
中 q=3 同时整除 d、r，条件 \(q\nmid dr\) 失败；此时应使用奇 q 首层分离
\(\eta_d\equiv1\)、\(\eta_r\equiv-1\pmod3\)，不能套用 (9)。

## 5. 研究边界

本引理把一大类双通道相位兼容性从“待证明的 source-map”降为一个精确整数间隙
\(2p-r-d\) 的 q-进计算。它可以直接产生分裂层、相位税和容量障碍，但不保证
这些相位标签进入同一合法标记集，也不提供 outer-rank RESET；剩余分支仍需
SHARED_PHASE_PREFIX、alternate、固定-\(n\)/固定-\(s\) 或 F/G 终端。
