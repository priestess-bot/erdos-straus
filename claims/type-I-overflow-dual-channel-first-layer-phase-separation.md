---
kind: claim
claim_id: type-I-overflow-dual-channel-first-layer-phase-separation
title: overflow 双通道奇素数 q 首层单位相位分离
statement: 设 \(pn=4Md+1\)、\(M=kp+r\)、旧支撑 \(A\mid M\)，且 \(q^a\parallel A\) 为奇素数幂。若 \(q\mid d\) 且 \(q\mid r\)，并且 d、r 两通道在 q^a 层都留下正未支付高度，则 d 通道单位相位模 q 必为 \(+1\)，r 通道单位相位模 q 必为 \(-1\)。因此两通道不可能属于同一个首层 q 相位胞；任何合并必须先通过 alternate 或更高层的显式仿射映射。对 q=2，该首层分离消失，必须继续检查更高 2 进层。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-qadic-obstruction-transfer
  - type-I-overflow-qadic-dual-unit-phase-nonidentification
topics:
- type-I
- overflow
- dual-channel
- q-adic
- phase-separation
- unit-phase
- capacity
- countercertificate
- proof-program
sources:
  - claim: type-I-overflow-qadic-obstruction-transfer
    role: dual-payment-and-directionality
  - claim: type-I-overflow-qadic-dual-unit-phase-nonidentification
    role: same-height-nonidentification
visibility: public
last_checked: '2026-08-05'
---

# overflow 双通道奇素数 q 首层单位相位分离

## 1. 设置

设 verified overflow 满足
\[
pn=4Md+1,\qquad M=kp+r,\qquad 1\le r<p,
\tag{1}
\]
并携带旧支撑 \(A\mid M\)。固定奇素数幂
\[
q^a\parallel A,\qquad q\ne p.
\tag{2}
\]
双通道未支付高度和单位相位记为
\[
O_d=(a-v_q(d)-v_q(k+1))_+,
\qquad
O_r=(a-v_q(r)-v_q(dn-1))_+,
\tag{3}
\]
\[
\eta_d=\frac{k+1}{q^{v_q(k+1)}}\pmod{q^{O_d}},
\qquad
\eta_r=\frac{dn-1}{q^{v_q(dn-1)}}\pmod{q^{O_r}},
\tag{4}
\]
其中只有对应 \(O_\bullet>0\) 时才记录相位。

## 2. 首层分离定理

假设
\[
q\mid d,\qquad q\mid r,\qquad O_d>0,\qquad O_r>0.
\tag{5}
\]
由 \(q\mid M=kp+r\)、\(q\ne p\) 得 \(q\mid k\)，所以
\[
k+1\equiv1\pmod q.
\tag{6}
\]
另一方面 \(q\mid d\) 给出
\[
dn-1\equiv-1\pmod q.
\tag{7}
\]
因 (6)--(7) 中两个数都是 q-进单位，(4) 的单位相位满足
\[
\boxed{
\eta_d\equiv1\pmod q,\qquad
\eta_r\equiv-1\pmod q.
}
\tag{8}
\]
当 q 为奇素数时 \(1\not\equiv-1\pmod q\)，从而
\[
\boxed{
\eta_d\not\equiv\eta_r\pmod q.
}
\tag{9}
\]
这是一条不依赖具体 p、M、n 的首层相位分离证书。

### 证明

式 (6) 使用 \(q\mid M\) 和 \(M=kp+r\)：
\(0\equiv M\equiv kp\pmod q\)，而 p 为 q 单位，故 \(q\mid k\)。
式 (7) 直接来自 \(q\mid d\)。由于 \(O_d,O_r>0\)，两标签的 q-进赋值被完全
去除后，模 q 的单位残数仍分别是 (6)、(7) 的右端，得到 (8)。奇 q 下两者不同，
证毕。

## 3. typed 分派

满足 (5) 的状态应输出
'DUAL_QADIC_FIRST_LAYER_SEPARATION'，并将 d/r 记录放在两个不同的首层相位胞：

\[
\mathcal C_d\equiv1\pmod q,\qquad
\mathcal C_r\equiv-1\pmod q.
\]
因此不能把 \(O_d+O_r\) 直接送入一个重复度为 1 的相位树，也不能把两条通道视为
一个共享 q 槽。它们可以分别进入不同容量账本；只有后续证明一个 alternate 将
两种标签拉到同一载体，才允许重新合并。

若 \(q\mid d\) 但 \(q\nmid r\)，或反之，本引理不强行给出相位结论，交由完整
单位残数判据。若 \(O_d=0\) 或 \(O_r=0\)，只有仍有债务的通道产生相位记录。

当 \(q=2\) 时 \(1\equiv-1\pmod2\)，首层不能分离。此时应记录
'DUAL_QADIC_FIRST_LAYER_UNSEPARATED'，继续比较
\(\eta_d,\eta_r\pmod{2^j}\) 的更高层，不能把奇 q 的结论外推到二进层。

更精确地，令
\[
\lambda=\min(O_d,O_r),
\qquad
c_2=v_2(\eta_d-\eta_r),
\]
并约定 \(c_2=+\infty\) 当 \(\eta_d=\eta_r\)（取整数代表计算差值的
2-adic 赋值）。两通道恰能共享的二进前缀深度为
\[
\boxed{s_2=\min(\lambda,c_2).}
\tag{10}
\]
所有 \(j\le s_2\) 层的单位相位相同；若 \(s_2<\lambda\)，则第
\(s_2+1\) 层发生严格分裂。容量账本中两通道的联合相位需求应记为
\[
s_2+(O_d-s_2)+(O_r-s_2)=O_d+O_r-s_2,
\tag{11}
\]
而不是无条件重复收费或无条件合并。输出分别为
'DUAL_2ADIC_COMMON_PREFIX'（记录 \(s_2\)）和
'DUAL_2ADIC_HIGH_LAYER_SPLIT'（当 \(s_2<\lambda\)）。

## 4. 边界例子

前述 \(p=73,M=75,d=9,n=37,A=25,q=5\) 例中 q 不整除 d、r，故属于一般的
'DUAL_QADIC_UNIT_PHASE_UNIDENTIFIED'，而不是本节的强分离分支；这说明条件
\(q\mid d\) 和 \(q\mid r\) 不能省略。

一个满足强分离条件的真实例子是
\[
(p,M,d,n,r,k,A,q^a)=(73,225,3,37,6,3,9,3^2).
\]
这里 \(73\cdot37=4\cdot225\cdot3+1\)、\(R_M=863>73\)，且
\[
O_d(3)=O_r(3)=1,\qquad
\eta_d=4\equiv1\pmod3,\qquad
\eta_r=3\cdot37-1=110\equiv2=-1\pmod3.
\]
所以 (8) 的两个首层相位胞在实际 overflow 中都非空。

二进共同前缀的实际例子是
\[
(p,M,d,n,r,k,A,q^a)=(73,96,23,121,23,1,8,2^3).
\]
这里
\[
O_d=O_r=2,\qquad
\eta_d=1\pmod4,\qquad
\eta_r=1391\equiv3\pmod4,
\]
所以 \(c_2=1\)、\(s_2=1\)：第一层相位相同，第二层必须分裂。原始双债务仍为
\(2+2=4\)；只有在额外证明 'SHARED_PHASE_PREFIX' 映射后，(11) 才将其去重为
\(1+1+1=3\)。

## 5. 研究边界

本引理把一类双通道状态从“等待相位容量”直接分派为不可合并的首层障碍，减少了
错误池化的搜索空间。它不说明每条分离通道都能产生 Type I/II 命中；首层分离后，
仍需 alternate、独立外层秩、固定-\(n\)/固定-\(s\) 递降或 F/G Fourier 终端来支付
各自的 q 缺陷。

若两侧 determinant 标签的 q-进赋值本身不相等，即使 \(q=2\) 的原始单位相位
在模 2 相同，也应改用
[不等赋值加权相位正规形](type-I-overflow-dual-valuation-asymmetry.md)；
加权相位会给出与奇偶性无关的首层分裂。
