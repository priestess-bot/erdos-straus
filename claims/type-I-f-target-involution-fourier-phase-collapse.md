---
kind: claim
claim_id: type-I-f-target-involution-fourier-phase-collapse
title: F 型目标对合的 target-odd Fourier 能量与 q-primary 相位塌缩
statement: 设 -1 属于有限单位群 H，J subset H 含单位元，且当前固定层乘积在 tau=pi(-1) 处缺失。则 -1 不属于 P=Stab_H(J)，等价于 tau 是 H/P 中的非平凡对合；目标奇角色上的 Fourier 能量精确等于 h/2(C_1-C_tau)。在循环商 C_m 中，所有目标奇角色保留商群的完整二进角色阶。若 tau 属于指数映射的像，则它的直接 q-primary 预像相位 gamma 满足 2gamma=0 mod q^e；故奇 q 时 gamma=0，二进时 gamma 仅为 0 或 2^(e-1)。在独立 direct phase lift 已给出时，这分别给出一胞和至多两胞的相位树容量界；但它不提供 source map、解提升或递降边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-layer-stabilizer-defect-reduction
  - type-I-fixed-layer-cyclic-fourier-profile
  - type-I-fourier-qprimary-phase-lift-capacity-dichotomy
topics:
  - type-I
  - F-state
  - finite-fourier
  - target-involution
  - q-primary
  - phase-lift
  - capacity
  - fixed-layer
  - proof-program
sources:
  - claim: type-I-fixed-layer-stabilizer-defect-reduction
    role: quotient-stabilizer-reduction
  - claim: type-I-fixed-layer-cyclic-fourier-profile
    role: cyclic-target-odd-Fourier-profile
  - claim: type-I-phase-clearing-cell-capacity-contract
    role: conditional-q-primary-cell-capacity
visibility: public
last_checked: '2026-08-07'
---

# F 型目标对合的 target-odd Fourier 能量与 q-primary 相位塌缩

## 1. 固定层商与目标奇角色

令 $H$ 是有限阿贝尔乘法群，$1\in J\subseteq H$，并令

\[
P=\operatorname{Stab}_H(J),\qquad \bar H=H/P,\qquad h=|\bar H|.
\tag{1}
\]

对任意包含零指数的残余盒，令 $c(x)$ 表示其在 $\bar H$ 中的表示数，并令

\[
A(\chi)=\sum_{x\in\bar H}c(x)\chi(x),\qquad
C_s=\sum_{x\in\bar H}c(x)c(xs^{-1}).
\tag{2}
\]

假设 $-1\in H$，且所研究的状态是 F 型，即中心化总谱在 $-1$ 处缺失；或者更一般地，
当前固定层乘积本身满足

\[
\tau=\pi(-1)\in\bar H,\qquad c(\tau)=0.
\tag{3}
\]

零指数和 $1\in J$ 给出 $c(1)\ge1$。若 $-1\in P$，则 $P\subseteq J$ 推出
$-1\in J$，与 (3) 矛盾。因此

\[
-1\notin P,\qquad \tau\ne1,\qquad \tau^2=1,\qquad 2\mid h.
\tag{4}
\]

定义目标奇角色集

\[
X^-:=\{\chi\in\widehat{\bar H}:\chi(\tau)=-1\},
\qquad |X^-|=h/2.
\tag{5}
\]

“目标奇”是相对于实际目标对合 $\tau$ 的有限群条件，不是对源标签或 q-进载体的额外假设。

## 2. 精确 target-odd 能量恒等式

有

\[
\boxed{
c(1)-c(\tau)=\frac2h\sum_{\chi\in X^-}A(\chi)}
\tag{6}
\]

以及

\[
\boxed{
E^-:=\sum_{\chi\in X^-}|A(\chi)|^2
=\frac h2(C_1-C_\tau)
=\frac h4\sum_{x\in\bar H}\bigl(c(x)-c(\tau x)\bigr)^2.}
\tag{7}
\]

**证明。** 角色正交性给出

\[
\sum_{\chi\in X^-}\chi(x)
=\frac h2\bigl(\mathbf1_{x=1}-\mathbf1_{x=\tau}\bigr).
\tag{8}
\]

将 (8) 乘以 $c(x)$ 并求和即得 (6)。将 (8) 代入
$\sum_{\chi\in X^-}A(\chi)\overline{A(\chi)}$ 得到 (7) 的第一个等式；第二个等式只需
展开平方和并使用 $\tau^2=1$。证毕。

F 缺失时，

\[
E^-\ge\frac h2c(1)^2,\qquad
\max_{\chi\in X^-}|A(\chi)|^2
\ge C_1-C_\tau\ge c(1)^2,
\tag{9}
\]

并且至少存在一个 $\chi\in X^-$ 满足

\[
\operatorname{Re}A(\chi)\ge c(1).
\tag{10}
\]

这比“存在某个非平凡角色”的普通 Fourier 下界更有结构：可选择的角色必定直接区分
目标 $-1$。但 (9)--(10) 仍只是状态内对偶证据。

## 3. 循环商的完整二进角色阶

若 $\bar H=C_m$，则 $m$ 为偶数，目标坐标是 $m/2$。写

\[
A_k=\sum_{x\in\mathbb Z/m\mathbb Z}c_x\zeta_m^{kx}.
\]

目标奇角色恰为奇数 $k$，并有

\[
E^-=\frac m2(C_0-C_{m/2}),\qquad
v_2\!\left(\operatorname{ord}\chi_k\right)=v_2(m)
\quad(k\text{ odd}).
\tag{11}
\]

所以 target-odd 选择不会丢失循环商的任何二进角色阶。枚举时可先取

\[
\{1\le k\le m/2:k\text{ odd}\}.
\]

若后续 source map 有方向，仍必须在相容性检查前保留 $k$ 与 $m-k$ 的有向相位。
当 $v_2(m)=1$ 时自反的 $k=m/2$ 要单独处理，不能被误作一对相反方向。

## 4. 直接目标 q-primary 相位塌缩

固定一个目标奇或其它规范商角色 $\bar\chi_i$。仅在
$\tau_i=\pi_i(-1)\in\operatorname{im}\bar\phi_i$ 时，取

\[
\bar\phi_i:\mathbb Z^{r_i}\longrightarrow\bar H_i,\qquad
\bar\phi_i(z_i^0)=\tau_i.
\tag{12}
\]

这里 $z_i^0$ 只是 $\tau_i$ 的**无界群论预像**；F 型有界目标盒本身为空，不能把它称为
一个盒内目标表示。若

\[
d_i=\operatorname{ord}(\bar\chi_i)=q^{e_i}d_i',
\qquad (q,d_i')=1,
\tag{13}
\]

则 q-primary 角色 $\psi_{i,q}=\bar\chi_i^{d_i'}$ 可以写成

\[
\psi_{i,q}(\bar\phi_i(z))
=\zeta_{q^{e_i}}^{\langle b_i,z\rangle},\qquad
\gamma_i=\langle b_i,z_i^0\rangle\pmod {q^{e_i}}.
\tag{14}
\]

由 $\tau_i^2=1$，

\[
\boxed{2\gamma_i\equiv0\pmod {q^{e_i}}.}
\tag{15}
\]

因而

\[
\gamma_i\equiv0\pmod {q^{e_i}}\quad(q\text{ odd}),\qquad
\gamma_i\in\{0,2^{e_i-1}\}\pmod {2^{e_i}}\quad(q=2).
\tag{16}
\]

将 q-primary 生成元换为单位幂不会改变 (16) 中的零类，也不会交换二进的两个可行类。

## 5. 条件容量与 fixed-B 的直接 no-go

设有限状态族有 $e_i>0$，并假设另有一个独立证明的 direct source map，给每个状态一个标签

\[
s_i\in[L,L+M],\qquad s_i\equiv\gamma_i\pmod {q^{e_i}},
\tag{17}
\]

且同一标签的最大重复度为 $\mu$。这一步是额外输入，不能由 Fourier 角色本身推出。

对奇素数 $q$，(16) 使每一个非空层只有零相位胞，故

\[
\boxed{
\sum_i e_i
\le\mu\sum_{k=1}^{H}\left(\left\lfloor\frac M{q^k}\right\rfloor+1\right)
\le\mu\left(\frac M{q-1}+H\right),}
\qquad H=\max_i e_i.
\tag{18}
\]

对 $q=2$，第 $k$ 层至多有 $0,2^{k-1}$ 两个相位类：非零类只可能来自
$e_i=k$ 且 $\psi_{i,2}(\tau_i)=-1$ 的状态。因此

\[
\boxed{
\sum_i e_i
\le2\mu\sum_{k=1}^{H}\left(\left\lfloor\frac M{2^k}\right\rfloor+1\right)
\le2\mu(M+H).}
\tag{19}
\]

这两式是现有相位树容量的严格特化，而不是新的载体存在定理。

固定 $B$ 清分中，若奇 $q$ 满足 $e>0$、
$v_q(B)=v_q(K)+e$ 且 $q\nmid AR$，其同图表相位

\[
\gamma_B=-AR^{-1}\pmod {q^e}
\tag{20}
\]

是单位；而 direct-target Fourier 相位由 (16) 恒为零。因此同一标签不可能同时满足
$s\equiv\gamma_i$ 和 $s\equiv\gamma_B\pmod {q^e}$。现有 fixed-$B$ 卡中的“相等后 gcd
吸收”分支仍适用于独立提供的锚定或仿射相位，但不适用于这里的直接目标相位。

绕开这个冲突需要一个独立的 source map；常见的可验证形式是

\[
s\equiv u\gamma_i+c\pmod {q^e}.
\tag{21}
\]

奇素数的实质算术信息在偏移 $c$，不在目标对合相位中。

## 6. 锚定相位是不同对象

直接目标相位为零并不排除所有奇 q 相位数据。设 $q$ 为奇素数，$t\in\bar H$ 的阶
与 $q$ 互素，并定义

\[
J_t=\{j\in J:tj^{-1}\in\operatorname{im}\bar\phi\}.
\]

令 $1\le k\le e_i$ 并定义

\[
\psi_k=\psi_{i,q}^{q^{e_i-k}}.
\]

若 $j\in J_t$ 且 $\bar\phi(z_j)=tj^{-1}$，则第 $k$ 层的锚定相位是

\[
\psi_k(\bar\phi(z_j))=\zeta_{q^k}^{\gamma_{j,k}},\qquad
\gamma_{j,k}=-\log_{\zeta_{q^k}}\psi_k(j).
\tag{22}
\]

它由 $j$ 决定，可以非零。若 $J_t=\varnothing$，其相位胞数为零。若 $J_t\ne\varnothing$，
则

\[
D_{J_t,k}=|\psi_k(J_t)|,\qquad
D_{J_t,k}=1
\Longleftrightarrow
\langle jj'^{-1}:j,j'\in J_t\rangle\subseteq\ker\psi_k.
\tag{23}
\]

因此锚定/仿射数据可成为未来奇 q 桥接的正确入口，但仍需独立证明它对应实际 source 标签。

## 7. 两个精确控制与边界

中心化 F 控制 $(p,R,K)=(193,63,3040)$ 的商为 $C_6$，其表示向量为

\[
c=(3,2,1,0,1,2),\qquad C_0=19,\quad C_3=8,\qquad E^-=33.
\tag{24}
\]

其中 $k=1,5$ 的精确平方范数均为 $16$，$k=3$ 的平方范数为 $1$。直接目标的
q-primary 相位为 $\gamma_3=0\pmod3$、$\gamma_2=1\pmod2$。

伴随的一般固定层控制 $(p,R,K)=(97,27,655)$ 的商为 $C_{18}$，其表示向量为

\[
c=(1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0),
\quad C_0=6,\quad C_9=2,\quad E^-=36.
\tag{25}
\]

窄复现：

~~~bash
python3 reproductions/type_i_f_target_involution_fourier.py --verify
~~~

这张卡选择目标奇 Fourier 角色、压缩 direct q-primary 相位树，并明确指出 fixed-$B$
的奇相位桥为何不可直接成立。它没有给出完整 source map、E1--E5 解提升或严格良基下降，
故所有输出仍为 analysis_evidence。
