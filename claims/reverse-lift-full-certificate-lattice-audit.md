---
kind: claim
claim_id: reverse-lift-full-certificate-lattice-audit
title: 完整证书格在两万内全部出现最大项反向提升
statement: 对全部 \(p\le20000\) 的267个核心素数，按自然缺口、平方除子和 Type I 后 Type II 的顺序枚举 Bradford 完整证书格，并在每张已检查目标三元组上穷尽所有二分母保留的反向提升。每个素数均在首次命中的 Type I 证书上出现一条边；267条首边都替换最大目标分母，最大缺口为23，且源分母没有一个是 \(1\bmod24\) 的素数。此为精确有限审计，不构成可归纳的选择器。
claim_status: computationally_reproduced
topics:
- descent
- reverse-lift
- marked-solution
- type-I
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-certificate-and-lift-context
visibility: public
last_checked: '2026-07-25'
---

# 完整证书格在两万内全部出现最大项反向提升

## 审计问题

设某个 Bradford Type I/II 证书给出

\[
\frac4p=\frac1x+\frac1y+\frac1z.
\]

固定其中两项，问是否存在 \(2\le n<p\) 与正整数 \(a\)，使

\[
\frac4n=\frac1a+\frac1x+\frac1y. \tag{1}
\]

若有，则把源项 \(a\) 替换为目标最大项 \(z\) 就是真实的二分母保留提升。它由
[二分母保留一项替换判据](two-denominator-lift-criterion.md) 精确检查，不是把目标
三元组改写成缩放表示。

对每个核心素数，程序以缺口 \(m\)、平方除子 \(d\)、Type I、Type II 的固定顺序枚举
全部合法 Bradford 证书；每张已检查证书都穷尽 \(n=2,\ldots,p-1\) 和三个可替换坐标。
命中后记录第一条边；若没有命中，则完成整个证书格的枚举。因此“无遗漏”只适用于所声明
的有限范围和这一个二分母保留模板。

## 精确结果

| 上界 | 核心素数 | 命中 | 漏点 | 检查证书数 | 首边 Type I | 首边替换最大项 |
|---:|---:|---:|---:|---:|---:|---:|
| 10,000 | 143 | 143 | 0 | 876 | 143 | 143 |
| 20,000 | 267 | 267 | 0 | 1,875 | 267 | 267 |

两档范围中，首个命中证书的最大缺口均为 \(23\)。在两万审计的 267 条首边中，206 条源分母
为偶数；其余亦没有一个是 \(1\bmod24\) 的素数。后一点只说明递降终点在已知的非核心区域，
并不自动给出可提升的**标记**源解。

最小的例子已经展示了这个结构：

\[
\frac4{48}=\frac1{35}+\frac1{20}+\frac1{210}
\quad\Longrightarrow\quad
\frac4{73}=\frac1{30660}+\frac1{20}+\frac1{210}. \tag{2}
\]

右侧来自 \(p=73\)、\((m,d)=(7,10)\) 的 Type I 证书。它不是最短缺口证书的反向边，
正是完整格扫描所暴露出的区别。

## 研究含义

这给出目前最明确的正信号：最短证书截面中的提升极稀少，见
[最短证书反向提升审计](reverse-lift-shortest-certificate-audit.md)；但允许非最短的
Type I 因子状态后，有限范围内的每个核心素数都出现同一种几何形状，即保持 \(x,y\) 并替换
\(z\)。

不过当前扫描先选择了目标 \((m,d)\)，再由 (1) 反求 \(n,a\)。所以它不是递降证明：
它已经使用了要构造的目标证书，不能拿“\(n\) 落在已知区域”替代源标记的构造。

因此可证伪的下一引理应是：

\[
\text{从 }(p,m,d)\text{ 的 Type I 因子条件直接构造 }
(n;a,x,y),\quad n<p,\quad
\frac4n=\frac1a+\frac1x+\frac1y, \tag{3}
\]

并且该构造的选择规则只依赖于可在源侧递归维护的因子标记，而非先知道目标三元组。若能
把 (3) 化为有限的因子同余选择器，并证明它覆盖所有 \(p\equiv1\pmod{24}\)，再与
[带标记解的严格递降闭包](marked-solution-descent-closure.md) 合并，才会形成真正的
递降路线。

## 重建

    python3 reproductions/reverse_lift_full_certificate_lattice_audit.py
    python3 reproductions/reverse_lift_full_certificate_lattice_audit.py \
      --limit 20000 \
      --output reproductions/reverse-lift-full-certificate-lattice-20k-results.json
    python3 -m unittest tests/test_reverse_lift_full_certificate_lattice_audit.py -q
