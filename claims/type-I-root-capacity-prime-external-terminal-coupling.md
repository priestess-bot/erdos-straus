---
kind: claim
claim_id: type-I-root-capacity-prime-external-terminal-coupling
title: 根容量素因子的 q 关联最小正源 Type I 终端菜单
statement: >-
  对核心素数 p≡1 mod24，令 M=(p^2+p+1)/3、u=gcd(2r+1,M)，并取素数
  q|u。若 rho 是 p mod q 的最小正剩余、i=q-rho，则 q≡1 mod3、2<=i<=q-2，
  且所有固定 source i、gap 含 q 的外部源 Type I 终端恰由有限菜单
  T_{p,q}={t|(p+i)/q: t≡-p q^{-1} mod4i} 参数化，gap 为 m=qt。每个菜单命中
  自动落在 3<=m<=p-2，并给出显式三分母。该菜单可以为空；p=457,q=7 是严格
  负控制。若 q≡-1 mod gcd(24,4i)，相容 CRT 类则给出无穷多个以 t=1、m=q
  终止的核心素数；q=7,rho=2,i=5 时该类为 p≡793 mod840。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - external-source-type-I-certificate
  - type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
topics:
  - type-I
  - external-source
  - terminal-first
  - common-root
  - capacity-factor
  - cyclotomic
  - finite-divisor-menu
  - dirichlet-ray
  - proof-boundary
sources:
  - claim: external-source-type-I-certificate
    role: external-source-and-type-I-divisor-equivalence
  - claim: type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
    role: exact-root-capacity-layer
  - reproduction: reproductions/type_i_root_capacity_prime_external_terminal_coupling.py
    role: finite-menu-positive-negative-and-dirichlet-class-controls
visibility: public
last_checked: '2026-08-13'
---

# 根容量素因子的 \(q\) 关联最小正源 Type I 终端菜单

## 1. 容量素因子强制一个最小外部源

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
M=\frac{p^2+p+1}{3},
\qquad
u=(2r+1,M),
\tag{1}
\]

并取素数 \(q\mid u\)。令 \(\rho\in\{1,\ldots,q-1\}\) 是 \(p\bmod q\) 的
最小正剩余，置

\[
i=q-\rho.
\tag{2}
\]

因为 \(p\equiv1\pmod3\)，有 \(M\equiv1\pmod3\)，故 \(q\ne3\)。又

\[
p^2+p+1\equiv0\pmod q.
\tag{3}

若 \(p\equiv1\pmod q\)，则 (3) 强制 \(q=3\)，矛盾；\(p\equiv-1\pmod q\)
也会使 (3) 的左边等于 1。因此 \(p\) 在
\((\mathbb Z/q\mathbb Z)^\times\) 中的阶恰为 3，从而

\[
q\equiv1\pmod3,
\qquad
\rho^2+\rho+1\equiv0\pmod q,
\qquad
2\le i\le q-2.
\tag{4}

由定义，\(i\) 正是满足 \(q\mid p+i\) 的最小正整数。这里的“最小”只相对于固定
容量因子 \(q\)，不声称它是所有成功外部源中的全局最小者。特别地
\((q,4i)=1\)。

## 2. 精确有限菜单

定义

\[
N=\frac{p+i}{q},
\qquad
\tau=\left\langle-pq^{-1}\right\rangle_{4i},
\tag{5}

其中尖括号表示模 \(4i\) 的最小非负剩余。则对每个正整数 \(t\)，

\[
\boxed{
t\mid N,\qquad t\equiv\tau\pmod {4i}}
\tag{6}

当且仅当令 \(m=qt\) 后有

\[
\boxed{
m\mid p+i,\qquad 4i\mid p+m.}
\tag{7}

确实，第一条整除等价于 \(qt\mid qN=p+i\)，第二条同余可消去模 \(4i\)
可逆的 \(q\)。因此，固定最小源 \(i\) 且 gap 含容量素因子 \(q\) 的外部源
Type I 终端，恰由有限除子残数菜单

\[
\boxed{
\mathcal T_{p,q}
=\left\{t\mid N:t\equiv\tau\pmod {4i}\right\}}
\tag{8}

参数化。该集合只对固定 \((p,q)\) 有限；它不提供关于 \(p\) 一致有界的菜单，因为
\(q,i,N\) 都可随 \(p\) 变化。

### 定理 1（菜单命中自动是合法短证书）

若 \(t\in\mathcal T_{p,q}\)，置

\[
m=qt,
\qquad
x=\frac{p+m}{4},
\qquad
d=ix,
\qquad
B=\frac{p+i}{m}.
\tag{9}

则 \(m\) 自动满足

\[
3\le m\le p-2,
\qquad m\equiv3\pmod4,
\tag{10}

且 \((m,d)\) 是 Type I 除子证书。

**证明。** 由 (7) 有 \(m\equiv-p\equiv3\pmod4\)，且 \(m\ge q\ge7\)。
只需排除 \(B=1\)。若 \(B=1\)，则 \(m=p+i\)，而
\(4i\mid p+m=2p+i\) 给出 \(i\mid2p\)。由 \(p\) 为素数及 (4)，只可能有
\(i=2,p,2p\)。它们分别要求

\[
8\mid2(p+1),
\qquad 4p\mid3p,
\qquad 8p\mid4p,
\tag{11}

均不可能；第一项使用 \(p\equiv1\pmod4\)。故 \(B\ge2\)，于是

\[
p-m=m(B-1)-i\ge q-i=\rho\ge2,
\tag{12}

得到 (10)。

另一方面，\(4i\mid p+m=4x\) 给出 \(i\mid x\)，所以

\[
d=ix\mid x^2.
\tag{13}

再由 \(m\mid p+i\) 得

\[
m\mid x(p+i)=px+d.
\tag{14}

这正是 Type I 除子判据。相应三分母可显式写成

\[
\boxed{
\frac4p=
\frac1x+
\frac1{xB}+
\frac1{pxB/i}.}
\tag{15}

最后一项为整数，因为 \(i\mid x\)；直接通分并使用
\(p+i=mB\)、\(p+m=4x\) 即验证 (15)。证毕。

## 3. 容量耦合的准确含义

式 (1) 给出

\[
q\mid u
\quad\Longleftrightarrow\quad
q\mid M\ \text{且}\ q\mid2r+1.
\tag{16}

反过来，若 \(q\mid M\)，取

\[
r=\frac{q-1}{2},
\tag{17}

则 \((2r+1,M)=(q,M)=q\)，所以根容量层精确为 \(u=q\)。这说明根容量因子
与外部源的来源可以取成同一个 \(q\)，但 (16) 本身不保证 (8) 非空。

## 4. 一个无限固定 gap 子域

固定素数 \(q\equiv1\pmod3\)、(3) 的一个非平凡根 \(\rho\)，并仍令
\(i=q-\rho\)。若

\[
q\equiv-1\pmod{(24,4i)},
\tag{18}

则 CRT 系统

\[
p\equiv1\pmod {24},
\qquad p\equiv\rho\pmod q,
\qquad p\equiv-q\pmod {4i}
\tag{19}

给出一个模

\[
L=\operatorname{lcm}(24,q,4i)
\tag{20}

的剩余类。(18) 正是前后两个非互素模数的相容条件；\(q\) 与另两个模数互素。
该剩余类还是本原的：模 24 的素因子上它等于 1，模 \(q\) 非零，而模 \(i\)
等于 \(-q\)，也非零。Dirichlet 定理因此给出 (19) 中无穷多个素数。

对每个满足 \(p>q+2\) 的这样的素数取 (17)，便有 \(u=q\)，且 \(t=1\)
同时满足 (6)。所以固定 gap \(m=q\) 给出 Type I 终端。

最小例为

\[
(q,\rho,i)=(7,2,5),
\qquad
\boxed{p\equiv793\pmod {840}}.
\tag{21}

该进程中大于 9 的每个素数在取 \(r=3\) 后都有 \(u=7\)、\(t=1\)，并满足

\[
x=\frac{p+7}{4},
\qquad
\frac4p=
\frac1x+
\frac1{x(p+5)/7}+
\frac1{px(p+5)/35}.
\tag{22}

前三个素数项为 \(2473,3313,4153\)。例如

\[
\frac4{2473}
=\frac1{620}+\frac1{219480}+\frac1{108554808}.
\tag{23}

## 5. 非平凡菜单命中与严格负控制

取 \(p=2137,r=3\)。此时

\[
M=1522969,
\quad u=7,
\quad(q,\rho,i,N,\tau)=(7,2,5,306,9).
\tag{24}

菜单以 \(t=9\) 命中，给出

\[
(m,x,d,B)=(63,550,2750,34),
\tag{25}

\[
\boxed{
\frac4{2137}
=\frac1{550}+\frac1{18700}+\frac1{7992380}.}
\tag{26}

相反，取 \(p=457,r=3\)，则

\[
M=69769=7\cdot9967,
\quad u=7,
\quad i=5,
\quad N=66,
\quad\tau=9\pmod {20}.
\tag{27}

66 的所有正除子均不等于 \(9\pmod {20}\)，所以
\(\mathcal T_{457,7}=\varnothing\)。更强地，gap \(m=7\) 自身也没有任意 Type I/II
除子证书：此时 \(x=116\)，\(x^2\) 的除子模 7 只能落在
\(\{1,2,4\}\)，而 Type I、Type II 分别要求

\[
d\equiv-px\equiv6\pmod7,
\qquad
d\equiv-x\equiv3\pmod7.
\tag{28}

因此新结论不是“\(q\mid u\) 自动终止”。CRT 子域给出的直接证书不要求相应
\(r\)-图表先由合法 lineage 到达，也不能称为 hard-root 全覆盖；固定 \(q\) 而
\(p\) 充分大时，\(9q^2<p\) 已属于既有 small-endpoint 区。新结论把指定
\((p,q,i)\) 的问题准确缩成有限集合 (8)：
真正仍需攻克的是证明 hard 容量层中至少一个这样的自适应菜单命中，或把空菜单
转化成可提升的严格递降。

## 6. 聚焦回执

```bash
python3 reproductions/type_i_root_capacity_prime_external_terminal_coupling.py --verify
```

脚本只核对 (21)--(28) 的固定正负控制和精确分数恒等式；无穷性与全称等价由正文的
CRT、Dirichlet 与整除证明承担。它不扫描素数范围、分母范围、selector history 或
历史结果。
