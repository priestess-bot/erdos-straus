---
kind: claim
claim_id: type-I-root-capacity-stutter-reduced-divisor-product
title: 根容量 stutter 的约化除子与双因子结果式约束
statement: >-
  对核心素数 p≡1 mod24 的实际根容量回执，令
  C=(p^2-1)/2、T=p^2r-(p+1)/2、z=R-h=ED、D|CT，并假设
  D|ph+1、D≡1-h (mod p)。置 H=h^2-1、D*=D/gcd(D,H)、
  m=(D+h-1)/p、S=h^2-h-2r。则 D*|T、D*|S，并且
  D* 整除 J=2h^2r-hm-4hr-m^3-2m^2r-m^2+m+2r。
  由于 J+((h-1)^2-m^2)S=(h^2-h+m)(h^2-2h-m^2-m+1)，
  必有 D*|(h^2-h+m)(h^2-2h-m^2-m+1)。这是由 stutter 余式得到的必要
  恒等式；由于第一因子恰为 D a（a=em-h），该乘积本身不是独立的排除筛选。
  独立的算术增量是 D*|J 及其容量约分来源；它仍不构造 Type I/II 证书、解提升或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-finite-curve-constraint
topics:
  - type-I
  - overflow
  - common-root
  - capacity-endpoint
  - stutter
  - resultant
  - divisor-filter
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: actual-receipt-cyclotomic-and-C/T-factor-split
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: stutter-parameterization-and-root-cyclotomic-condition
  - reproduction: reproductions/type_i_root_capacity_stutter_reduced_divisor_product.py
    role: fixed-arithmetic-controls-and-identity-checks
visibility: public
last_checked: '2026-08-13'
---

# 根容量 stutter 的约化除子与双因子结果式约束

## 1. 设置

沿用根容量回执的记号

\[
C=\frac{p^2-1}{2},\qquad T=p^2r-\frac{p+1}{2},\qquad K=CT,
\]

\[
R=2p^3r-p^2-2pr-p+1,
\qquad z=R-h.
\]

取一个实际 maximal complete-excess receipt

\[
z=ED,\qquad D\mid K,
\qquad D\mid ph+1,
\qquad D\equiv1-h\pmod p,
\tag{1}
\]

其中 stutter 门使

\[
m=\frac{D+h-1}{p}\in\mathbb Z_{>0},
\qquad D=mp+1-h.
\tag{2}
\]

定义

\[
H=h^2-1,
\qquad D_* =\frac{D}{(D,H)},
\qquad S=h^2-h-2r.
\tag{3}
\]

注意 \(D_*\) 是把 \(D\) 中与 \(h^2-1\) 重合的全部指数删去后的除子；它不等同于
已有的 \(D_T=D/(D,C)\)，但二者有逐素数的容量关系。

## 2. \(D_*\) 保留在 \(T\) 中

先由 \(D_C=(D,C)\mid D\) 和 \(D_C\mid C\) 得

\[
p^2\equiv1\pmod {D_C},
\qquad ph\equiv-1\pmod {D_C},
\]

从而

\[
\boxed{D_C\mid h^2-1.}
\tag{4}
\]

下面按素数 \(q\) 计算指数。记

\[
\alpha=v_q(D),\quad \beta=v_q(H),\quad
\gamma=v_q(C),\quad \tau=v_q(T).
\]

因为 \(D\mid CT\)，有 \(\alpha\le\gamma+\tau\)；由 (4)，
\(\min(\alpha,\gamma)\le\beta\)。若 \(\alpha\le\beta\)，则 \(q\) 在 \(D_*\) 中的指数为
零。若 \(\alpha>\beta\)，则必有 \(\gamma\le\beta\)，故

\[
v_q(D_*)=\alpha-\beta\le\gamma+\tau-\beta\le\tau.
\]

因此

\[
\boxed{D_*\mid T.}
\tag{5}
\]

这一步是必要的：不能把 \(D_T\mid T\) 直接替换成 \(D_*\mid T\)，必须使用
\(D_C\mid H\) 的指数信息。

## 3. \(D_*\) 的两个整除式

由 \(D_*\mid D\) 和 (1)，有 \(ph\equiv-1\pmod {D_*}\)。于是

\[
2T h^2
=2p^2rh^2-h^2(p+1)
\equiv2r-(h^2-h)=-S\pmod {D_*}.
\]

结合 (5)，得到

\[
\boxed{D_*\mid S.}
\tag{6}
\]

再考虑 \(z\) 关于 \(p\) 的整数多项式。由 \(mp\equiv h-1\pmod D\)，直接展开可得

\[
m^3z\equiv(h-1)J\pmod D,
\tag{7}
\]

其中

\[
J=2h^2r-hm-4hr-m^3-2m^2r-m^2+m+2r.
\tag{8}
\]

由于 \(D\mid z\)，式 (7) 给出 \(D\mid(h-1)J\)。令
\(g_1=(D,h-1)\)。标准约分得到 \(D/g_1\mid J\)。而

\[
g_1\mid (D,h^2-1)\quad\Longrightarrow\quad
D_*\mid D/g_1,
\]

所以

\[
\boxed{D_*\mid J.}
\tag{9}
\]

## 4. 约化除子的双因子约束

纯整数恒等式为

\[
\boxed{
J+\bigl((h-1)^2-m^2\bigr)S
=(h^2-h+m)(h^2-2h-m^2-m+1).}
\tag{10}
\]

由 (6)、(9) 立即推出

\[
\boxed{
D_*\mid(h^2-h+m)(h^2-2h-m^2-m+1).}
\tag{11}
\]

这比单独的 \(D_C\mid h^2-1\)、\(D_T\mid S\) 多出一个由根回执 \(z\) 和 stutter
线性式共同产生的恒等式；但它仍只是必要条件。由此前的 stutter 恒等式

\[
a=em-h>0,\qquad Da=m+h(h-1)=h^2-h+m,
\]

第一因子已经满足 (h^2-h+m=Da)，所以 (D_*\mid h^2-h+m) 早已自动成立；
式 (11) 的乘积形式不能被解释为额外排除第二因子的筛选。真正新增的是第 3 节的
约化余式 (D_*\mid J)，以及由容量指数约分得到 (D_*\mid T,S) 的精确来源。

## 5. 证明边界

式 (11) 没有给出 \(D_*\mid h^2-h+m\) 的全称结论，也不能排除第二因子

\[
h^2-2h-m^2-m+1.
\]

因此当前 hard root 仍没有获得短证书或合法递降。要把 (11) 升级为全局出口，至少还需
把两个因子的素因子归属与 actual source/path provenance、容量素因子 external-source
菜单或全域解提升合同联立。抽象满足式 (1)--(11) 的元组不能被当作真实递归边。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_reduced_divisor_product.py --verify
```

脚本固定重算一个核心同余合数控制和两个非核心素数算术控制，分别核对 \(D_*\mid T\)、
\(D_*\mid S\)、\(D_*\mid J\) 与 (10)--(11)；它不声称这些控制是核心素数的 actual
stutter receipt，也不执行范围搜索。
