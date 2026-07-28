---
kind: claim
claim_id: ghermoul-2025-core-residual-reduction
title: Ghermoul 2025 多项式覆盖的核心残余恰为 p 等于 1 模 24
statement: Ghermoul 的四个多项式族中，已显式证明的代入覆盖全部 q 不等于 0 模 6；剩余 q=6c 正好给出 Erdős--Straus 的核心 p=4q+1=24c+1。对素数输出，第一、第三（除其退化到第二族的情形）和第四族只给出合数，因此第二族 p2=x(4yz-z-1)-yz 在 q=6c 上的覆盖是该文真正未解决的必要分支。论文将四族全覆盖明确列为 Conjecture 2，并只报告有限计算，故不构成主猜想或混合终端选择引理的证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- literature-audit
- polynomial-family
- core-primes
- type-I
- proof-gap
sources:
- paper: ghermoul2025
  locator: Equations (4)--(7), (14)--(21), Conjecture 2, Theorems 2--4
  role: polynomial-family-source
visibility: public
last_checked: '2026-07-28'
---

# Ghermoul 2025 多项式覆盖的核心残余恰为 \(p\equiv1\pmod{24}\)

## 审计对象

Ghermoul 的预印本定义

\[
\begin{aligned}
p_1(x,y,z)&=x(4yz-1)-yz,\\
p_2(x,y,z)&=x(4yz-z-1)-yz,\\
p_3(x,y,z)&=x(8y-3)-6y+2,\\
p_4(x,y,z)&=x^2-x,
\end{aligned} \tag{1}
\]

其中变量为正整数，并研究 \(a=4q+1\) 是否由 \(q=p_i(x,y,z)\) 覆盖。该文证明
各个前 3 族的输出有显式单位分数分解，却把四族覆盖所有正整数 \(q\) 明确表述为
Conjecture 2。

## 已证明部分的精确并集

不用任何计算，可由论文自身的特化直接得到：

\[
\begin{aligned}
p_2(1,1,z)&=2z-1,\\
p_2(c+1,2,1)&=6c+4,\\
p_1(2c+1,1,1)&=6c+2.
\end{aligned} \tag{2}
\]

故所有奇数、所有 \(6c+4\) 和所有 \(6c+2\) 都被这些已证明的代入覆盖。换言之，
它们已无条件处理恰好是

\[
q\not\equiv0\pmod6 \tag{3}
\]

的全部正整数。

剩余类写为 \(q=6c\)，相应的 Erdős--Straus 参数就是

\[
p=4q+1=24c+1. \tag{4}
\]

这正是经典约化以及本库混合终端选择引理中的核心素数类。因此这套多项式并没有绕开
当前主缺口；它把缺口精确重述为自己 Conjecture 2 在 \(q\equiv0\pmod6\) 上的覆盖问题。

## 为什么素数不能由其余三族替代

直接展开论文给出的恒等式：

\[
\begin{aligned}
4p_1+1&=(4x-1)(4yz-1),\\
4p_3+1&=(8y-3)(4x-3),\\
4p_4+1&=(2x-1)^2.
\end{aligned} \tag{5}
\]

第一和第四式对正 \(q\) 均为合数。第三式在 \(x>1\) 时也为合数；当 \(x=1\) 时，

\[
p_3(1,y,z)=2y-1=p_2(y,1,1). \tag{6}
\]

所以若 \(4q+1\) 是素数，任何由四族联合覆盖推出的表示都必可归到第二族：

\[
\boxed{
q=x(4yz-z-1)-yz.} \tag{7}
\]

特别地，针对核心 \(q=6c\) 的第二族覆盖不是前三/第四族可以接管的旁支，而是该预印本
全称路线的必要未解环节。

## 对主计划的含义

该文报告到 \(q\le10^9\) 的联合覆盖，并报告第二族对相应素数的更大范围计算；这些都是
有限经验。论文也明确说明形式证明仍然开放。即使将 (7) 的全称覆盖补上，它首先给出的是
一类单位分数参数化，仍需单独验证它是否能统一产生本项目要求的 Type I 正规形与偶终端
因子或严格递降。

因此本库将该文列为“计算报告加覆盖猜想”，而不是关于 Erdős--Straus 猜想、混合终端
选择引理，或当前证明程序的已证全称结果。
