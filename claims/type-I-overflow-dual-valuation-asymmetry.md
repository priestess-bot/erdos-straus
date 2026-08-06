---
kind: claim
claim_id: type-I-overflow-dual-valuation-asymmetry
title: overflow 双通道不等赋值的加权相位正规形与首层分离
statement: 设 verified overflow 满足 \(pn=4Md+1\)、\(M=kp+r\)，且 \(q^a\parallel A\)。令 d/r determinant 标签为 \(L_d=k+1\)、\(L_r=dn-1\)，其 q-进赋值为 \(\beta_d,\beta_r\)，载体赋值为 \(u_d,u_r\)，未支付高度为 \(h_t=(a-u_t-\beta_t)_+\)。在 \(\beta=\min(\beta_d,\beta_r)\) 归一化后，有 \(p(q^{\beta_d-\beta}\eta_d-q^{\beta_r-\beta}\eta_r)\equiv(2p-r-d)/q^\beta\pmod{q^{a-\beta}}\)。因此若 \(\beta_d\ne\beta_r\) 且两侧高度均正，加权相位必在首层分裂并且 \(v_q(2p-r-d)=\beta\)；若 \(\beta_d=\beta_r\)，则退化为已有的 \(2p-r-d\) 精确相位间隙判据。该命题补齐不等赋值分支，但不产生递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-qadic-obstruction-transfer
  - type-I-overflow-dual-phase-gap-criterion
  - type-I-overflow-dual-channel-first-layer-phase-separation
topics:
- type-I
- overflow
- dual-channel
- q-adic
- valuation-asymmetry
- weighted-phase
- phase-separation
- capacity
- proof-program
sources:
  - claim: type-I-overflow-qadic-obstruction-transfer
    role: carrier-and-label-payment-heights
  - claim: type-I-overflow-dual-phase-gap-criterion
    role: equal-valuation-specialization
  - reproduction: reproductions/type_i_overflow_dual_valuation_asymmetry.py
    role: bounded-weighted-phase-replay
visibility: public
last_checked: '2026-08-05'
---

# overflow 双通道不等赋值的加权相位正规形与首层分离

## 1. 设置

设一个有来源回执的 overflow 满足

\[
pn=4Md+1,\qquad M=kp+r,\qquad 1\le r<p,
\tag{1}
\]

并携带旧支撑 \(A\mid M\)，且两个 determinant 标签 \(L_d,L_r\) 非零
（在当前正 overflow 回执中 \(L_d>0,L_r>0\)）。固定

\[
q^a\parallel A,
\qquad q\ne p.
\tag{2}
\]

记两个对偶 determinant 标签为

\[
L_d=k+1,
\qquad L_r=dn-1,
\tag{3}
\]

并令

\[
\beta_d=v_q(L_d),\quad \beta_r=v_q(L_r),
\qquad
u_d=v_q(d),\quad u_r=v_q(r),
\tag{4}
\]

\[
h_d=(a-u_d-\beta_d)_+,
\qquad h_r=(a-u_r-\beta_r)_+.
\tag{5}
\]

当 \(h_t>0\) 时定义完整整数单位

\[
\eta_d=L_d/q^{\beta_d},
\qquad
\eta_r=L_r/q^{\beta_r},
\tag{6}
\]

它们在实际相位树中再分别截断到 \(q^{h_t}\)。令

\[
\beta=\min(\beta_d,\beta_r),
\qquad
\zeta_d=q^{\beta_d-\beta}\eta_d,
\qquad
\zeta_r=q^{\beta_r-\beta}\eta_r.
\tag{7}
\]

\(\zeta_t\) 是由两个 determinant 标签共同基准化后的**加权相位**；当两侧赋值不同，
较高赋值的一侧不再是 q-进单位，这正是不能直接套用单位相位树的原因。

## 2. 加权相位恒等式

由 \(q^a\mid M\) 和 \(M=kp+r\)，有

\[
pL_d=p(k+1)\equiv p-r\pmod {q^a}.
\tag{8}
\]

由 \(pn=4Md+1\)，有

\[
pL_r=p(dn-1)=4Md^2+d-p\equiv d-p\pmod {q^a}.
\tag{9}
\]

相减得到

\[
p(L_d-L_r)\equiv G:=2p-r-d\pmod {q^a}.
\tag{10}
\]

因为 \(L_d-L_r=q^\beta(\zeta_d-\zeta_r)\)，且 \(p\) 是 q-进单位，(10) 首先给出

\[
q^\beta\mid G,
\tag{11}
\]

再除以 \(q^\beta\) 得到精确形式

\[
\boxed{
p(\zeta_d-\zeta_r)
\equiv G/q^\beta
\pmod {q^{a-\beta}}.
}
\tag{12}
\]

因此对任意 \(0\le j\le\min(h_d,h_r)\)，都有逐层等价

\[
\boxed{
q^{\beta+j}\mid G
\iff
q^j\mid(\zeta_d-\zeta_r).
}
\tag{13}
\]

这里 \(\min(h_d,h_r)\le a-\beta\)，所以局部账本提供的相位高度完全落在 (12) 的
有效模数内。

### 证明

(8) 使用 \(q^a\mid M\) 消去 \(M\) 项；(9) 直接展开 \(p(dn-1)\)。两式相减给出
(10)。当两侧高度均正时，\(\beta_d,\beta_r<a\)，所以 \(\beta<a\)，并且
\(L_d-L_r=q^\beta(\zeta_d-\zeta_r)\)；除以 \(q^\beta\) 即得 (12)。再因 \(p\) 为单位，
对每个 \(j\) 取模得到 (13)。证毕。

## 3. 不等赋值分支：加权首层必分裂

假设 \(h_d,h_r>0\) 且

\[
\beta_d\ne\beta_r.
\tag{14}
\]

不妨设 \(\beta_d=\beta<\beta_r\)。则 \(\eta_d\) 是 q-进单位，而

\[
\zeta_d=\eta_d\not\equiv0\pmod q,
\qquad
\zeta_r=q^{\beta_r-\beta}\eta_r\equiv0\pmod q.
\tag{15}
\]

所以

\[
\boxed{\zeta_d\not\equiv\zeta_r\pmod q.}
\tag{16}
\]

同时 \(\zeta_d-\zeta_r\) 是 q-进单位。由 (12) 和 \(p\) 为单位，得到

\[
\boxed{v_q(G)=\beta.}
\tag{17}
\]

这给出一个不依赖 q 奇偶性的首层分离证书：对于不等赋值状态，任何声称双通道共享
一个相位前缀的容量扣除，都必须先说明它如何吸收权重 \(q^{|\beta_d-\beta_r|}\)；
直接把 \(\eta_d,\eta_r\) 当成同一层单位标签是不合法的。

建议的 typed 分派为：

* 'DUAL_PHASE_VALUATION_ASYMMETRY'：记录 \((\beta_d,\beta_r)\) 和较低赋值侧；
* 'DUAL_PHASE_WEIGHTED_FIRST_LAYER_SPLIT'：记录 (16)、\(v_q(G)=\beta\)，禁止无条件
  的双通道相位去重；
* 若另有显式仿射 source-map 能抵消权重，必须把该映射作为独立 E1--E4 证书，而不能
  从局部支付账本直接推定。

这比“q=2 首层可能相同”的原始单位相位判断更精确：在 q=2 且
\(\beta_d\ne\beta_r\) 时，原始单位都可能为 1，但加权相位仍在首层分裂。

## 4. 等赋值分支：恢复间隙判据

若 \(\beta_d=\beta_r=\beta\)，则 \(\zeta_d=\eta_d\)、\(\zeta_r=\eta_r\)，(13) 变成

\[
\eta_d\equiv\eta_r\pmod {q^j}
\iff
q^{\beta+j}\mid(2p-r-d),
\tag{18}
\]

正是已有的 \(2p-r-d\) 精确间隙判据；最大共同深度为

\[
\min\bigl(h_d,h_r,v_q(2p-r-d)-\beta\bigr),
\tag{19}
\]

并约定 \(v_q(0)=+\infty\)。因此本卡不是另一个独立的 equal-valuation容量公式，而是
把已有公式嵌入一个覆盖全部赋值分支的加权正规形。

## 5. 统一的加权相位树计数

令

\[
m=\min(h_d,h_r),\qquad H=\max(h_d,h_r),
\]

并定义加权共同前缀深度

\[
s_w=\min\bigl(m,v_q(\zeta_d-\zeta_r)\bigr),
\tag{20}
\]

其中相等时约定 \(v_q(0)=+\infty\)。对双通道的逐层相位胞数，\(1\le j\le H\)，有

\[
D_j^{(w)}=
\begin{cases}
1,&j\le s_w,\\
2,&s_w<j\le m,\\
1,&m<j\le H.
\end{cases}
\tag{21}
\]

这只是对每层同余类的精确计数：低于两侧共同高度时，两条记录落在同一个胞当且仅
当 \(q^j\mid(\zeta_d-\zeta_r)\)；超过较短高度后只剩一侧。由 (13)，\(s_w\) 可直接
由 \(G=2p-r-d\) 计算：

\[
s_w=\min\bigl(m,v_q(G)-\beta\bigr).
\tag{22}
\]

特别地：

* \(\beta_d\ne\beta_r\) 时 \(s_w=0\)，所以所有共同债务层都缴纳双胞分裂税；
* \(\beta_d=\beta_r\) 时 \(s_w\) 恢复 (19) 的共同前缀深度。

若加权相位整数代表落在长度为 \(L\) 的区间、每个胞的重复度至多为 \(\mu\)，则任意
相位树容量账本都必须满足

\[
h_d+h_r\le
\mu\sum_{j=1}^{H}
D_j^{(w)}
\left(\left\lfloor\frac{L}{q^j}\right\rfloor+1\right).
\tag{23}
\]

相对于把两侧误合并成一个胞的粗界，额外分裂税精确为

\[
\operatorname{Tax}^{(w)}_q
=\mu\sum_{j=s_w+1}^{m}
\left(\left\lfloor\frac{L}{q^j}\right\rfloor+1\right).
\tag{24}
\]

式 (23)--(24) 仍以真实整数相位映射、区间长度和重复度为前提；本卡只保证双通道
overflow 坐标产生的加权相位胞数，不替代这些外部容量假设。

## 6. 具体例子与边界

### 不等赋值、二进也分裂

取

\[
(p,M,d,n,r,k,q^a)=(73,675,1,37,18,9,5^2).
\]

此时

\[
(\beta_d,\beta_r)=(1,0),
\qquad (h_d,h_r)=(1,2),
\]

而

\[
\eta_d=2,
\qquad \eta_r=36,
\qquad (\zeta_d,\zeta_r)=(10,36).
\]

所以加权相位模 5 为 \(0,1\)，首层分裂；同时

\[
2p-r-d=127,\qquad v_5(127)=0=\min(\beta_d,\beta_r).
\]

### 等赋值、奇 q 载体分支

若 \(q\mid d\) 且 \(q\mid r\)，则通常有 \(\beta_d=\beta_r=0\)，本卡的等赋值式退化为
首层 \(2p-r-d\) 判据；例如

\[
(p,M,d,n,r,k,A,q^a)=(73,225,3,37,6,3,3^2)
\]

给出两侧单位相位 \(1,-1\pmod3\)。这是已有奇 q 首层分离引理的坐标化表达。

## 7. 逻辑边界

本卡关闭的是双通道 q-进支付账本中“标签赋值不相等”这一缺失的算术分支。它仍然
不证明：

1. 加权相位一定映入一个非空 marked solution set；
2. 相位首层分裂必然产生 Type I/II 终端；
3. 忽略旧支撑后的状态拥有全局良基外层秩；
4. 任意两个分裂胞之间存在合法 source-switch 或解提升。

因此它是表示—对偶—容量选择器的精确 'phase_dispatch' 输入：不等赋值行必须先付
“加权首层分裂税”，等赋值行才可使用已有相位间隙和双胞容量公式；它不是 Erdős--Straus
猜想的全称证明。

## 复现

    python3 reproductions/type_i_overflow_dual_valuation_asymmetry.py --verify

脚本会同时扫描有限 overflow 小样本和四个手工边界，输出位于
reproductions/type-i-overflow-dual-valuation-asymmetry-results.json。
