---
kind: claim
claim_id: type-I-overflow-qadic-dual-unit-phase-nonidentification
title: overflow 双通道 q 缺陷的单位相位非识别反例
statement: q-adic 支撑账本中的 d/r 未支付高度不决定去掉 q 进赋值后的单位相位；即使两个通道在同一 overflow 状态中具有相同的 q-缺陷高度，也可能得到不同的单位残数。因此不能仅按 \((q,a,O_d,O_r)\) 把双通道缺陷合并为共享相位或共享 q 进容量。显式核心例为 \(p=73,M=75,d=9,n=37,A=25,q^a=5^2\)，两个通道的缺陷都为 2，但单位相位分别为 \(2\) 和 \(7\pmod {25}\)。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-qadic-obstruction-transfer
  - type-I-overflow-fixed-s-dual-outer-rank-descent
  - type-I-fixed-layer-fourier-qadic-phase-bridge
topics:
- type-I
- overflow
- q-adic
- dual-channel
- unit-phase
- nonidentification
- capacity
- counterexample
- proof-boundary
sources:
  - claim: type-I-overflow-qadic-obstruction-transfer
    role: exact-dual-payment-heights
visibility: public
last_checked: '2026-08-05'
---

# overflow 双通道 q 缺陷的单位相位非识别反例

## 1. 双通道账本和单位相位

设 verified overflow 满足
\[
pn=4Md+1,\qquad M=kp+r,\qquad 1\le r<p,
\tag{1}
\]
并携带旧支撑 \(A\mid M\)。固定 \(q^a\parallel A\)。由双对偶支撑支付分解，d/r
通道的未支付高度分别为
\[
O_d(q)=\bigl(a-v_q(d)-v_q(k+1)\bigr)_+,
\]
\[
O_r(q)=\bigl(a-v_q(r)-v_q(dn-1)\bigr)_+.
\tag{2}
\]
当 \(O_d(q)>0\) 或 \(O_r(q)>0\) 时，去除相应标签的 q 进赋值，定义单位相位
\[
\eta_d(q)=
\frac{k+1}{q^{v_q(k+1)}}\pmod{q^{O_d(q)}},
\qquad
\eta_r(q)=
\frac{dn-1}{q^{v_q(dn-1)}}\pmod{q^{O_r(q)}}.
\tag{3}
\]
式 (3) 只是对两个通道已有算术标签的规范记录；它不假定两者属于同一载体坐标。

## 2. 同一状态中的严格反例

取
\[
p=73,\qquad M=75,\qquad d=9,\qquad n=37,\qquad
r=M\bmod p=2,\qquad k=1,
\]
以及旧支撑
\[
A=25,\qquad q=5,\qquad a=2.
\]
直接核验
\[
73\cdot37=2701=4\cdot75\cdot9+1,
\qquad
R_M=4M-n=263>73,
\]
所以这是一个真实 overflow 状态，且 \(5^2\parallel A\)。

此时
\[
v_5(d)=v_5(k+1)=v_5(r)=v_5(dn-1)=0,
\]
因为 \(dn-1=9\cdot37-1=332\)。故两通道都没有支付任何旧 q 层：
\[
O_d(5)=O_r(5)=2.
\]
但单位相位为
\[
\eta_d(5)=k+1=2\pmod{25},
\qquad
\eta_r(5)=dn-1=332\equiv7\pmod{25},
\tag{4}
\]
从而
\[
\boxed{\eta_d(5)\ne\eta_r(5)\quad\text{而}\quad
O_d(5)=O_r(5)=2.}
\tag{5}
\]
这排除了在同一状态内把两个相同高度的 q 缺陷当成一个共享相位胞。

## 3. 跨状态同债务也不决定相位

同一核心素数 \(p=73\)、同一 \(q=5\) 和同一一层支撑 \(A=5\) 还给出两个不同
overflow 状态：
\[
\begin{array}{c|c|c|c|c|c}
(M,d,n,r,k)&4Md+1=pn&R_M&O_d(5)&O_r(5)&(\eta_d,\eta_r)\bmod5\\ \hline
(75,9,37,2,1)&2701&263&1&1&(2,2)\\
(155,2,17,5,2)&1241&603&1&1&(3,3)
\end{array}
\tag{6}
\]
两行均满足 (1)，且均为 overflow；债务签名
\((q,a,O_d,O_r)=(5,1,1,1)\) 完全相同，但单位相位不同。

因此任何只读取 \((q,a,O_d,O_r)\) 的跨状态合并规则都不能推出相位嵌套同余。
即使扩展为“同一通道”的规则，也必须额外携带 \(k+1\)、\(dn-1\) 的单位残数或
一个已证明的整数仿射映射。

## 4. 负证书的精确含义

本反例并不说明 d/r 通道不能在某些子族中共享相位；它说明共享必须是额外定理，
不能由支撑债务账本自动推出。统一选择器对这类输入应输出
'DUAL_QADIC_UNIT_PHASE_UNIDENTIFIED'，并保留
\[
(p,M,d,n,A,q^a,O_d,O_r,\eta_d,\eta_r)
\]
作为最小见证。

只有以下任一条件成立，才允许把两条记录放进同一相位树：

1. 显式证明 \(\eta_d\equiv\eta_r\pmod{q^{\min(O_d,O_r)}}\)；
2. 给出把两种标签拉回同一整数载体的仿射同态，并证明嵌套 q 同余；
3. 通过 alternate/source-switch 将其中一条通道转换为另一条已有相位胞。

否则两个高度只能分别进入 d/r 的容量账本；若各自账本都不产生 surplus，就必须转入
固定-\(n\)、固定-\(s\)、F/G Fourier 或不可重置外层秩分支。

## 5. 结论和研究边界

该反例严格收窄了 overflow 相位—容量桥：支撑缺陷高度是必要账本，但不是共享
相位资源。它也解释了为什么现有相位树容量合同必须保存单位残数，而不能只保存
赋值高度。剩余决定性问题变为：在递归可达的 \(A>1\) overflow 子族中，证明某种
alternate 或整数仿射关系强制 (4) 的相位兼容，或者证明双通道中至少一条支付一个
可提升的外层秩/终端。
