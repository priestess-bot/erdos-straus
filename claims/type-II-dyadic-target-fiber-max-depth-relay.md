---
kind: claim
claim_id: type-II-dyadic-target-fiber-max-depth-relay
title: Type II 二进目标纤维最大深度的商约化—顶层对合终端
statement: 设 K=<kappa> 同构于 C_{2^a}，S 是对称有限指数盒的源像，t 是二阶目标且 t+K 命中而 t 本身未命中。令 F_t={k in K:t+k in S}，并取 F_t 中非零元素的最大二进深度 d。则 F_t 与 L=2^{d+1}K 不相交，故 H/L 中的目标像仍缺失；当 d<a-1 时得到严格较小的 C_{2^{d+1}} 顶层目标纤维，包含规范的二进最高位，当 d=a-1 时任何非零 K-子群都会吸收该最高位，只能输出顶层二进终端。对 t 不在 K 的反足源对，非顶层偏移的两倍差向量精确生成 2^{e+1}K，并二分为预算内短关系或有符号盒外需求。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-cyclic-digit-deficit-quotient-kernel-relay
  - type-II-source-fiber-highest-deficit-tail-compression
  - type-II-top-kernel-pair-overflow-capacity
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-annihilator-congruence-fiber-lift-criterion
  - type-I-target-fiber-neighbor-dyadic-normalization
topics:
  - type-II
  - dyadic
  - target-fiber
  - maximum-depth
  - quotient-descent
  - generalized-dyadic
  - source-relation
  - signed-overflow
  - Fourier
  - source-switch
  - proof-program
sources:
  - claim: type-II-source-fiber-cyclic-digit-deficit-quotient-kernel-relay
    role: cyclic-primary-quotient-interface
  - claim: type-II-source-fiber-highest-deficit-tail-compression
    role: primary-tail-descent-boundary
  - claim: type-II-top-kernel-pair-overflow-capacity
    role: antipodal-source-pair-overflow-interface
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: source-relation-fourier-lift
  - claim: type-II-annihilator-congruence-fiber-lift-criterion
    role: arithmetic-source-switch-menu
  - reproduction: reproductions/dyadic_target_fiber_max_depth.py
    role: C2xC8-strict-and-top-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II 二进目标纤维最大深度的商约化—顶层对合终端

## 1. 目标纤维

使用加法记号。令 \(H\) 为有限阿贝尔群，令

\[
K=\langle\kappa\rangle\cong C_{2^a},
\qquad a\ge1,
\]

并令 \(t\in H\) 满足 \(2t=0\)。取对称指数盒和映射

\[
\mathcal B_\nu=\prod_{i=1}^{r}[-\nu_i,\nu_i]\cap\mathbb Z^r,
\qquad
\phi(z)=\sum_i z_i g_i,
\qquad
S=\phi(\mathcal B_\nu)=-S.
\tag{1}
\]

假设

\[
t\notin S,
\qquad
S\cap(t+K)\ne\varnothing.
\tag{2}
\]

定义目标纤维的核截面

\[
F_t=\{k\in K:t+k\in S\}.
\tag{3}
\]

由 (2) 有 \(F_t\ne\varnothing\)，且 \(0\notin F_t\)。由于 \(S=-S\) 和
\(t=-t\)，有

\[
F_t=-F_t.
\tag{4}
\]

对非零 \(k\in K\)，定义其二进深度

\[
\operatorname{dep}_2(k)
=\max\{0\le j\le a-1:k\in 2^jK\}.
\tag{5}
\]

记

\[
d=\max_{k\in F_t}\operatorname{dep}_2(k),
\qquad
L=2^{d+1}K,
\tag{6}
\]

其中 \(2^aK=\{0\}\)，所以 \(L=\{0\}\) 在 \(d=a-1\) 时成立。

## 2. 最大深度商约化定理

令 \(\bar H=H/L\)、\(\bar S\) 和 \(\bar t\) 分别为 \(S\) 和 \(t\) 的像，
\(\bar K=K/L\simeq C_{2^{d+1}}\)。则：

\[
\boxed{F_t\cap L=\varnothing,\qquad \bar t\notin\bar S.}
\tag{7}
\]

### 证明

若非零 \(k\in L=2^{d+1}K\)，则
\(\operatorname{dep}_2(k)\ge d+1\)，与 \(d\) 的最大性矛盾；而
\(0\notin F_t\)。故 \(F_t\cap L=\varnothing\)。

若 \(\bar t\in\bar S\)，则存在 \(s\in S\) 使 \(s-t\in L\)。由于 \(L\subseteq K\)，
可写成 \(s=t+k\)，其中 \(k\in F_t\cap L\)，矛盾。这证明 (7)。证毕。

最大深度层在商中给出一个规范的顶位。取 \(k=2^d u\kappa\in F_t\)，其中
\(u\) 为奇数。模 \(L=2^{d+1}K\) 有

\[
k\equiv 2^d\kappa\pmod L.
\tag{8}
\]

所以

\[
\boxed{2^d\kappa+L\in\bar F_t,
\qquad
\bar F_t=\{\bar k:k\in F_t\}\subseteq\bar K,
\qquad
0\notin\bar F_t.}
\tag{9}
\]

其中 \(2^d\kappa+L\) 是 \(\bar K\simeq C_{2^{d+1}}\) 的唯一非零二阶元。

这给出严格二分：

1. 若 \(d<a-1\)，则 \(L\ne\{0\}\)，
   \(|\bar H|=|H|/|L|<|H|\)，(7) 是严格的
   DYADIC_TARGET_FIBER_QUOTIENT_DESCENT；商中的目标纤维含有规范最高二进位。
2. 若 \(d=a-1\)，则 \(L=\{0\}\)，没有非平凡的 \(K\)-二进子群可以继续商掉；
   (9) 给出 TOP_DYADIC_TARGET_FIBER。事实上，\(K\simeq C_{2^a}\) 的每个
   非零子群都包含 \(2^{a-1}\kappa\)，所以任何非零子群商都会把该顶位偏移吸收到
   目标中，不能保持目标缺失。

注意这里的 \(d\) 取自目标纤维 \(F_t\)，而不是源块的层计数。它因此补充了
循环 primary 源块缺口引理：即使源块层数尚未被组织成独立二点块，目标纤维本身也
能给出一个规范的二进商或不可再压缩的顶位终端。

## 3. 反足源关系与溢出二分

定义指数纤维

\[
\mathcal Z_{tK}=\{z\in\mathcal B_\nu:\phi(z)\in t+K\}.
\tag{10}
\]

若 \(t\notin K\)，则 \(z\mapsto-z\) 在 \(\mathcal Z_{tK}\) 上无固定点：固定点只能是
\(z=0\)，但 \(\phi(0)=0\in t+K\) 会推出 \(t\in K\)。从每个反足对
\(\{z,-z\}\) 选一个代表，并写

\[
\phi(z)=t+k,\qquad k\in F_t,
\qquad
\delta(z)=2z,\qquad
\rho(z)=\phi(\delta(z))=2k.
\tag{11}
\]

若 \(e=\operatorname{dep}_2(k)<a-1\)，则 \(2k\ne0\)，且

\[
\operatorname{dep}_2(\rho(z))=e+1,
\qquad
\langle\rho(z)\rangle=2^{e+1}K.
\tag{12}
\]

因此每个非顶位反足对都产生一个精确标记的二进源关系，而不是泛化成“某个
非零频率”。对坐标预算定义

\[
o_i(z)=\bigl(2|z_i|-\nu_i\bigr)_+,
\qquad
\epsilon_i(z)=\operatorname{sgn}(z_i)o_i(z).
\tag{13}
\]

于是有构造性二分：

* 若 \(2|z_i|\le\nu_i\) 对所有 \(i\)，输出
  SHORT_DYADIC_SOURCE_RELATION，并携带关系层 \(e+1\)；
* 否则 \(\sum_i o_i(z)\ge1\)，输出带方向的
  DYADIC_SOURCE_OVERFLOW_DEMAND。

当 \(e=a-1\) 时，\(k=2^{a-1}\kappa\) 且 \(2k=0\)。这类反足对不是源生成关系，
而是 TOP_DYADIC_OFFSET_PAIR，必须保留给第 2 节的顶位终端，不能把零关系计入
容量。

若 \(t\in K\)，则 \(t\) 必是 \(K\) 的顶位二阶元。此时 \(z=0\in\mathcal Z_{tK}\)，
对应 \(k=t\) 的顶位偏移，自动进入 TOP_DYADIC_TARGET_FIBER；其余非固定反足对
仍按 (11)--(13) 处理。这一分支解释了为什么不能无条件套用 \(t\notin K\) 时的
固定点自由配对。

对多个状态，把每个溢出单位记为

\[
u=(s,\{z,-z\},i,j),
\qquad 1\le j\le o_i(z),
\tag{14}
\]

并把关系层 \(e+1\)、来源标签和 q 进槽合同保留在请求载荷中。只有通过同一来源
纤维的 source-switch/SNF/范围门后，\(u\) 才进入 Hall 图；此后沿用“全匹配或
严格容量缺口”二分。未通过提升门的溢出单位必须记为
DYADIC_SOURCE_LIFT_OBSTRUCTED，不能直接当作 q 容量。

## 4. 规范 Fourier 回执

在严格商分支中，

\[
\bar K=K/L\simeq C_{2^{d+1}},
\qquad
\omega_d=2^d\kappa+L
\tag{15}
\]

是 \(\bar K\) 的唯一非零二阶元。取规范角色

\[
\chi_d(\kappa+L)=\exp\!\left(\frac{2\pi i}{2^{d+1}}\right),
\qquad
\chi_d(\omega_d)=-1.
\tag{16}
\]

\(\chi_d\) 保存了最高二进位的相位，但不能仅凭该单个相位断言
\(\widehat{1_{\bar F_t}}(\chi_d)\) 为负；其它纤维点可能抵消它。正确的 Fourier
证书由 Parseval 给出：

\[
\bar F_t\ne\varnothing,\quad 0\notin\bar F_t
\Longrightarrow
\sum_{\chi\ne1}
\left|\widehat{1_{\bar F_t}}(\chi)\right|^2
=|\bar F_t|\bigl(|\bar K|-|\bar F_t|\bigr)>0.
\tag{17}
\]

因此至少存在一个非平凡角色；\(\chi_d\) 作为顶位相位与该非零角色一起保存，
再通过源关系格相容性判定哪些角色可以进入 q 进容量。这个区分避免把一个顶位
符号直接误记为已支付容量。

## 5. 整数提升门与良基势

(7) 是有限群层面的严格商，不自动是 Erdos--Straus 的整数递降。要把它升级为
保持来源标签的后继，必须对投影后的源指数格运行：

1. FIBER_REALIZED：投影源列确实来自同一参数纤维；
2. SNF/CRT：\(L=2^{d+1}K\) 的商关系、目标顶位和来源因子相容；
3. RANGE：低模数 \(D',A\) 的除子、平方自由和 \(B'>A\) 条件；
4. E1--E5：整数解全域提升，且来源势或模数严格下降。

四门通过时登记

~~~text
DYADIC_TARGET_FIBER_SOURCE_SWITCH
quotient_layer = 2^(d+1)
top_digit = 2^d*kappa
strict_potential_drop = true
~~~

任一门失败时登记

~~~text
DYADIC_TARGET_FIBER_LIFT_OBSTRUCTED
failed_gate = FIBER_REALIZED | SNF_CRT | RANGE | E1_E5
quotient_target_missing = true
~~~

顶层 \(d=a-1\) 分支没有严格商，必须转入广义 \(2^a\) 终端、其它 Type I/II
路线或新的源关系；不能把 TOP_DYADIC_TARGET_FIBER 误写成递降。

## 6. \(C_2\times C_8\) 控制

取

\[
H=C_2\times C_8,
\qquad
K=\{0\}\times C_8,
\qquad
t=(1,0).
\]

使用源列 \(g=(1,2)\)。预算 \(\nu=1\) 时，目标 \(t\) 未命中，而
\(F_t=\{2,6\}\)，最大深度 \(d=1\)，所以

\[
L=4K,
\qquad
K/L\simeq C_4,
\qquad
F_t\bmod L=\{2+L\}.
\tag{18}
\]

反足对 \(z=1,-1\) 的差向量为 \(2\)，关系像为 \((0,4)\)，但超出预算一个单位，
输出 DYADIC_SOURCE_OVERFLOW_DEMAND；预算改为 \(\nu=2\) 时同一关系落入盒内，
输出 SHORT_DYADIC_SOURCE_RELATION。

若改取 \(g=(1,4)\)、\(\nu=1\)，则 \(F_t=\{4\}\)，最大深度为 \(a-1=2\)，
\(L=\{0\}\)，反足对的关系像为零；这正是不可再压缩的
TOP_DYADIC_OFFSET_PAIR，而不是一个可收费的源生成元。

若取 \(H=K=C_8\)、\(t=4\)、\(g=1\)、\(\nu=1\)，则 \(t\in K\)，固定指数
\(z=0\) 产生顶位偏移 \(k=4\)，验证了 \(t\in K\) 时必须保留固定点的分支。

复现：

~~~bash
python3 reproductions/dyadic_target_fiber_max_depth.py --verify
~~~

## 研究边界

本引理新增的是目标纤维侧的二进规范化：最大深度 \(d\) 直接给出保持目标缺失的
\(C_{2^{d+1}}\) 商，或在 \(d=a-1\) 时给出不能再压缩的顶位对合。它还把非顶位
反足表示精确接到层 \(e+1\) 的源关系和有符号溢出需求。

它没有证明所有核心素数都满足 FIBER_REALIZED 或整数提升门；商状态若无法回译，
只能保留 DYADIC_TARGET_FIBER_LIFT_OBSTRUCTED，顶层分支仍需广义 \(2^j\)、
Type I/II 短证书或另一条保持标签的严格递降来承接。
