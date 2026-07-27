---
kind: claim
claim_id: type-II-h19-deficit-one-saturated-prime-normal-form
title: 零溢出指数缺陷一的饱和素因子正规形
statement: 设 (M,r)=1 且 M 的普通除子没有命中 -1 mod r。指数缺陷 delta(M,r)=1 当且仅当存在 q^nu||M 与 b|M/q^nu，使 q^(nu+1)b=-1 mod r。等价地，目标只差把已在普通除子 q^nu*b 中用尽的一种素因子 q 再乘一次。十亿 H19 剖面中的75个高溢出 delta=1 首状态全部满足此正规形；其中38个在后续 r<=9999 释放，37个仍未释放。
claim_status: established
topics:
- type-I
- even-source
- overflow
- divisor-residues
- exponent
- normal-form
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# 零溢出指数缺陷一的饱和素因子正规形

令 \((M,r)=1\)，并假设没有普通除子 \(a\mid M\) 满足

\[
a\equiv-1\pmod r. \tag{1}
\]

记 \(\delta(M,r)\) 为[指数补偿距离](type-II-h19-zero-overflow-exponent-deficit.md)：先选
一个普通除子，再允许重复使用 \(M\) 的支持素因子，达到 \(-1\bmod r\) 所需的最少因子数。
则

\[
\delta(M,r)=1
\quad\Longleftrightarrow\quad
\exists q^\nu\mathbin{\Vert}M,\ b\mid\frac{M}{q^\nu}:
q^{\nu+1}b\equiv-1\pmod r. \tag{2}
\]

这里 \(q\) 是素数。换言之，取 \(a=q^\nu b\) 后，\(a\) 已含有 \(M\) 中全部的
\(q\)-幂；目标残数只差再乘一个无法继续从 \(M\) 取出的 \(q\)。

## 证明

若 \(\delta=1\)，按定义存在 \(a\mid M\) 和支持素因子 \(q\mid M\)，使

\(qa\equiv-1\pmod r\)。若 \(qa\mid M\)，则 \(qa\) 本身违反 (1)。因此 \(a\) 中的
\(q\)-指数必等于 \(v_q(M)=\nu\)。写 \(a=q^\nu b\)，即得 (2)，且
\(b\mid M/q^\nu\)。

反之，(2) 给出普通除子 \(a=q^\nu b\)，在其后重复一次支持素因子 \(q\) 即命中目标，
故 \(\delta\le1\)。假设 (1) 排除了 \(\delta=0\)，所以 \(\delta=1\)。

这条正规形把缺陷一状态转成明确的“素因子容量”问题，不涉及模糊的积集补偿。
一个可提升的源转换只要能在保持目标残数的同时使该 \(q\) 获得一份额外指数，或改造为
已含 \(q^{\nu+1}\) 的新 \(M\)，便会强制零溢出尾。

## H19 有限剖面

在 \(p\le10^9\) 的高溢出首 \(r\) 状态中，恰有 75 个 \(\delta=1\) 状态；程序为每个
状态逐项构造 (2) 的见证。其规范首见饱和素因子中，\(q=3\) 有 28 个，\(q=5\) 有 10 个，
\(q=7\) 有 9 个，其余分布在 16 个素数上。

把这些状态继续扫描至 \(r\le9999\) 时，38 个转成普通除子零溢出，37 个仍未转成。
这表明饱和素因子正规形是实际可用的状态压缩，却不保证仅增加 \(r\) 即可修复容量缺口。

更细的释放机制审计否定了一个自然但过强的解释。对每个 \(\delta=1\) 状态，令
\(\mathcal Q\) 是所有能使 (2) 成立的饱和素因子 \(q\)，并比较其在释放后
\(M'=(r'p+1)/4\) 的指数。38 个后续释放中：

| 释放时对初始 \(\mathcal Q\) 的关系 | 状态数 |
| --- | ---: |
| 每个 \(q\in\mathcal Q\) 都不再整除 \(M'\) | 28 |
| 某个 \(q\) 仍出现、但指数未增加 | 5 |
| 某个 \(q\) 的指数增加 | 5 |

因此绝大多数释放并非“把原来耗尽的同一 \(q\) 多补一次”，而是改变 \(M\) 的整个素因子
支撑后重新命中目标残数。任何一般源转换必须允许这种支撑重组；只追踪一个固定 \(q\) 的
指数增长不能解释当前释放机制。

这不是偶然的数值现象。令 \(r'=r+8j\)，则

\[
M(r')=\frac{r'p+1}{4}=M(r)+2pj. \tag{3}
\]

若奇素数 \(q^\nu\mathbin{\Vert}M(r)\)，则 \(q\nmid p\)，并有精确的固定素因子提升律：

\[
q\mid M(r')\quad\Longleftrightarrow\quad q\mid j. \tag{4}
\]

写 \(j=qt\) 后，指数至少增加一即 \(q^{\nu+1}\mid M(r')\)，当且仅当

\[
\frac{M(r)}q+2pt\equiv0pmod {q^\nu}. \tag{5}
\]

因此，对固定 \(q^\nu\) 来说，保持 \(q\) 已把 \(j\) 限在模 \(q\) 的一个类；增幂则把
\(j\) 限在模 \(q^{\nu+1}\) 的唯一类。证明只需将 (3) 模 \(q\)、再在 \(j=qt\) 后除以
\(q\) 即可。它解释了为何“同一 \(q\) 的容量恢复”在可变 \(r\) 搜索中是刚性而稀薄的
子机制，却不解释跨支撑的主导释放。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_deficit_one_saturated_prime_profile.py \
  --input reproductions/type-ii-h19-bounded-r-overflow-profile-1b-results.json \
  --release reproductions/type-ii-h19-zero-overflow-r-release-profile-1b-results.json \
  --output reproductions/type-ii-h19-deficit-one-saturated-prime-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_deficit_one_saturated_prime_profile.py -q
python3 reproductions/type_ii_h19_deficit_one_release_mechanism.py \
  --input reproductions/type-ii-h19-deficit-one-saturated-prime-profile-1b-results.json \
  --output reproductions/type-ii-h19-deficit-one-release-mechanism-1b-results.json
python3 -m unittest tests/test_type_ii_h19_deficit_one_release_mechanism.py -q
~~~
