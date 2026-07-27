---
kind: claim
claim_id: type-II-fan-lift-nondeterminism
title: Type II 扇扩张的同余状态分支不可判定性
statement: 设Q为24的倍数，r=1 mod24且gcd(r,Q)=1；令ell>=5为不整除Q与旧移位s的素数。则在同一旧核心同余状态p=r modQ中，存在无穷多个核心素数满足ell|p+4s，也存在无穷多个满足ell不整除p+4s。因此把扇从Q扩张到ell Q时，仅由旧同余状态不能确定旧移位s的强制因子是否新增ell；H22到H23中同一状态p=529 mod77597520的两支分别给出强制因子69与3。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-II
- canonicalization
- multishift
- state-transition
- congruence
- Dirichlet-theorem
- obstruction
- proof-program
sources:
- paper: linnik1944
  locator: least-prime theorem in arithmetic progressions
  role: arithmetic-progression-prime-existence-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-28'
---

# Type II 扇扩张的同余状态分支不可判定性

## 定理

令

\[
24\mid Q,\qquad r\equiv1\pmod {24},\qquad \gcd(r,Q)=1,
\]

并令 \(\ell\ge5\) 是不整除 \(Q\) 与正整数 \(s\) 的素数。旧扇状态只记录

\[
p\equiv r\pmod Q. \tag{1}
\]

则有两个互不相同的既约 CRT 提升 \(R_+,R_-\pmod{\ell Q}\)，均满足

\[
R_+\equiv R_-\equiv r\pmod Q,
\]

但

\[
R_+\equiv-4s\pmod\ell,
\qquad
R_-\not\equiv-4s\pmod\ell. \tag{2}
\]

因而 Dirichlet 算术级数定理给出无穷多个核心素数 \(p\equiv R_+\pmod{\ell Q}\)，
以及无穷多个核心素数 \(p\equiv R_-\pmod{\ell Q}\)。第一类满足
\(\ell\mid p+4s\)，第二类满足 \(\ell\nmid p+4s\)。

特别地，定义旧与新强制因子

\[
D_s=\gcd(Q,r+4s),\qquad
D'_s=\gcd(\ell Q,R+4s), \tag{3}
\]

则同一旧状态 (1) 的两种扩张分别满足

\[
\ell\mid D'_s\quad\text{和}\quad\ell\nmid D'_s. \tag{4}
\]

所以旧模数、旧残数以及旧移位本身不能决定扇扩张后的因子状态。

## 证明

令 \(a=-4s\bmod\ell\)。假设保证 \(a\ne0\)。取

\[
R_+\equiv r\pmod Q,\quad R_+\equiv a\pmod\ell.
\]

由于 \(r\) 与 \(Q\) 互素、\(a\ne0\)，CRT 给出的 \(R_+\) 与 \(\ell Q\) 互素。
又因 \(\ell\ge5\)，单位群中至少存在一个 \(b\ne a\)。取

\[
R_-\equiv r\pmod Q,\quad R_-\equiv b\pmod\ell.
\]

同样 \(\gcd(R_-,\ell Q)=1\)。Dirichlet 定理于是分别给出两个既约进程中的无穷多个素数。
它们都因 \(24\mid Q\) 而为 \(1\bmod24\) 的核心素数。式 (2) 立即给出这两个进程对
\(\ell\mid p+4s\) 的相反结论，进而得到 (4)。证毕。

## H22 到 H23 的具体分支

既有 H22 状态为

\[
Q=77{,}597{,}520,\qquad r=529,
\]

H23 新增 \(\ell=23\)，考察旧移位 \(s=5\)。CRT 给出

\[
R_+=1{,}474{,}353{,}409\equiv3\equiv-20\pmod {23},
\]

和

\[
R_-=1{,}086{,}365{,}809\equiv1\pmod {23}.
\]

两个残数都约化到同一个 \(529\bmod77{,}597{,}520\)，但

\[
\gcd(Q,529+20)=3,
\]

而扩张后分别为

\[
\gcd(23Q,R_++20)=69,
\qquad
\gcd(23Q,R_-+20)=3. \tag{5}
\]

作为完全显式的素数实例，两个进程中最先找到的核心素数是

\[
15{,}752{,}297{,}089=R_++8(23Q),
\]

与

\[
4{,}655{,}851{,}729=R_-+2(23Q).
\]

前者的 \(p+20\) 被 \(23\) 整除，后者不被 \(23\) 整除。

## 含义与边界

这一定理加强了[扇扩张的模数强制因子精确更新律](type-II-fan-extension-forced-factor-update.md)：
不只是某个储存的 CRT 提升会重启，任何只以旧同余状态为输入的确定性更新规则都不可能在
一般情形下正确。一个可归纳的状态必须至少按新提升分支，或直接携带 \(p+4s\) 的实际因子
信息；它不能只保存固定扇的模数与残数。

该结论仍然不产生 Type II 因子对、Type I 偶桥或严格下降边。它排除的是一种状态设计，
并没有证明任何有限状态扩张都不可能成功；实际素因子、碰撞标签和可重选的 AC 因子对仍可能
提供更强的非同余转移机制。

可复现命令：

~~~bash
python3 reproductions/type_ii_fan_lift_nondeterminism.py
python3 -m unittest tests/test_type_ii_fan_lift_nondeterminism.py -q
~~~
