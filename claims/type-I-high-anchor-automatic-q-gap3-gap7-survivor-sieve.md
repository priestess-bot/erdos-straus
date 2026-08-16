---
kind: claim
claim_id: type-I-high-anchor-automatic-q-gap3-gap7-survivor-sieve
title: 最小 automatic q 来源的 gap-3/gap-7 prefix 生存筛
statement: >-
  在互素 beta_0=2、Q_1=R-1 的 automatic C=qA 来源中，只有 q=2 且 k 为偶数、
  或 q=3 且 k=2 mod3 的行能进入 e=0 fixed-n bridge。对这样的行，令
  x_3=(p+3)/4、x_7=(p+7)/4。若有序 direct terminal prefix [gap 3, gap 7]
  没有输出，则每个 x_3 的素因子都等于 1 mod3，p=1,25,121 mod168，且
  x_7^2 的全部除子分别避开 Type I 目标 -2p^2 mod7 与小于等于 x_7 的
  Type II 目标 -2p mod7。反之，这些 x_3/x_7 条件精确等价于该两 gap prefix
  的 miss。该筛子不把 prefix miss 误报为全 terminal miss 或 verified macro edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-automatic-q-phase-descent-trichotomy
  - gap-seven-congruence-certificates
  - type-I-high-anchor-automatic-q-gap3-gap7-priority-boundary
topics:
  - Erdos-Straus
  - type-I
  - automatic-q
  - terminal-first
  - gap-three
  - gap-seven
  - factor-sieve
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_automatic_q_gap3_gap7_survivor_sieve.py
    role: exact-gap-predicate-and-source-controls
visibility: public
last_checked: '2026-08-16'
---

# 最小 automatic \(q\) 来源的 gap-3/gap-7 prefix 生存筛

## 1. 输入域

只考虑已经通过 automatic phase--descent 三分法的最小相位行：

\[
\begin{array}{c|c|c|c}
q & k\text{ 的条件} & h & e\\
\hline
2 & k\equiv0\pmod2 & 1 & 0\\
3 & k\equiv2\pmod3 & 2 & 0.
\end{array}
\tag{1}
\]

这些是 automatic \(C=qA\) 来源中仅有能保留 \(n_T=n<p\) 并进入既有
fixed-\(n\) bridge 的参数类。令有序 direct terminal prefix 为

\[
\mathcal P_{3,7}=(\text{gap }3,\ \text{gap }7).
\tag{2}
\]

下面只判断这个冻结 prefix 是否输出；它不能代替完整 terminal-first 菜单。

## 2. gap 3 的精确因子判据

写

\[
x_3={p+3\over4}.
\tag{3}
\]

核心条件给 \(x_3\equiv1\pmod3\)。在 gap \(3\) 上，Type I 与 Type II 的
Bradford 除子目标都为 \(2\pmod3\)。所以

\[
\boxed{\quad
\text{gap 3 miss}
\quad\Longleftrightarrow\quad
\forall\,\ell\mid x_3,\ \ell\equiv1\pmod3.
\quad}
\tag{4}
\]

这里 \(\ell=3\) 不会出现。若 \(x_3\) 有一个 \(2\pmod3\) 素因子，选择它在
\(x_3^2\) 中的适当幂即给出所需除子；反向显然。

## 3. gap 7 的精确 divisor 判据

写

\[
x_7={p+7\over4}\equiv2p\pmod7.
\tag{5}
\]

令

\[
\mathcal D_{\rm I}(p)=
\{d:d\mid x_7^2,\ d\equiv-2p^2\pmod7\},
\tag{6}
\]

\[
\mathcal D_{\rm II}(p)=
\{d:d\mid x_7^2,\ d\le x_7,\ d\equiv-2p\pmod7\}.
\tag{7}
\]

因为 Type I 的目标是 \(d\equiv-px_7\pmod7\)，Type II 的目标是
\(d\equiv-x_7\pmod7\)，并且补因子的第二整除式由 \(d(x_7^2/d)=x_7^2\)
自动给出，故

\[
\boxed{\quad
\text{gap 7 miss}
\quad\Longleftrightarrow\quad
\mathcal D_{\rm I}(p)=\mathcal D_{\rm II}(p)=\varnothing.
\quad}
\tag{8}
\]

这保留了 Type II 的 \(d\le x_7\) 范围，不能仅以 \(x_7^2\) 的无界残数替代。

三个固定 gap-7 叶已覆盖

\[
p\equiv3,5,6\pmod7.
\tag{9}
\]

因此 (8) 的 miss 必要地要求 \(p\equiv1,2,4\pmod7\)。与
\(p\equiv1\pmod{24}\) 合并，得到便宜的 CRT 预筛

\[
\boxed{\quad p\equiv1,25,121\pmod{168}.\quad}
\tag{10}
\]

式 (10) 只是 (8) 的必要条件；其余三个残类仍可能有非固定 gap-7 除子证书。

## 4. 自动来源的精确 prefix 筛

对 (1) 中的任意实际来源行，(4) 和 (8) 合起来给

\[
\mathcal P_{3,7}\text{ miss}
\quad\Longleftrightarrow\quad
\left[
\begin{array}{l}
\forall\,\ell\mid x_3,\ \ell\equiv1\pmod3,\\
\mathcal D_{\rm I}(p)=\mathcal D_{\rm II}(p)=\varnothing.
\end{array}
\right.
\tag{11}
\]

特别地，任何值得继续补 parent、typed lift 和 E5 的 automatic 来源都必须同时通过：

\[
\begin{array}{c|c}
q=2 & k\equiv0\pmod2\\
q=3 & k\equiv2\pmod3
\end{array}
\qquad
p\equiv1,25,121\pmod{168},
\tag{12}
\]

以及 (11) 的两条精确因子/除子检查。这把 source construction 的前置筛选压缩成
小模同余、\(x_3\) 的素因子和 \(x_7^2\) 的 divisor residue，而不需要先构造宏。

## 5. 固定控制与边界

| \(p\) | 角色 | \(p\bmod168\) | gap 3 | gap 7 | 结果 |
|---:|---|---:|---|---|---|
| 3793 | actual \(q=2,e=0\) source | 97 | miss | fixed II | prefix terminal |
| 60913 | actual \(q=3,e=0\) source | 97 | miss | fixed II | prefix terminal |
| 34897 | actual \(q=2,e=0\) source | 121 | I | miss | prefix terminal |
| 68713 | actual \(q=2,e=0\) source | 1 | I | nonfixed I | gap 3 先终止 |
| 193 | core boundary | 25 | miss | nonfixed I | 说明 (10) 不充分 |
| 1201 | core boundary | 25 | miss | miss | true prefix miss |

\(p=1201\) 不是 (1) 的 automatic source；它只证明这张有限筛子确有 core
survivor，不能把必要条件误读成 terminal 覆盖，更不能作为 global edge。

## 6. 边界

这个结论不证明存在通过 (11) 的 actual automatic source，也不证明通过者没有其它
terminal。它的作用是把 global 出口研究中的 expensive source/provenance 工作限制在
真正 surviving 的最小相位行；任何后续宏仍须重跑完整 versioned terminal-first menu，
再给出 parent、全域解提升和严格良基势。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_high_anchor_automatic_q_gap3_gap7_survivor_sieve.py --verify
~~~
