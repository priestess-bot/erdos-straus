---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-p-primary-chain-no-go
title: 完整乘积 d=1 的 a=1 任意长 p-primary 链与单轨道势 no-go
statement: >-
  在完整乘积 d=1 的 p-free failure 余类中，a=1 当且仅当
  g=(p+1)/2、b=2pr-1。令 H_j=1+p+...+p^j。对任意容量锚 h|K 和
  p^f||(R-h)，真实剥离 p^f 后两侧为 y=(R-h)/p^f、x=R-y，并有
  4K=p^(f+1)y+ph+1；故两侧后续容量分别由 gcd(y,4K)=gcd(y,ph+1)
  与 gcd(x,4K)=gcd(x,py+1) 控制；其奇素数部分精确，2-adic 部分仍按 K
  读取。更强地，对每个有限 N，存在正整数 r
  使 H_0->H_1->...->H_N 是真实容量剥离链，每个 departure bundle 都含恰一个
  p-block 且非 terminal。因此任何只按连续 p-peeling 深度或主侧 H_j 链计数的统一
  有界倒计时均不成立。固定 p=73,r=4796963 还给出真实四周期
  1->74->5403->394420->1，四个 bundle 均含 p。该 no-go 只否定单侧
  p-primary 策略：完整 Reach 在 peeled node 还可选择互补侧，固定周期中该侧到达
  5330->3<->20，而 3、20 的对侧 bundle 已 p-free。它不是全局 selector no-go，
  更不是 Erdős--Straus 反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - p-primary-peeling
  - capacity-orbit
  - arbitrary-transient
  - strict-counterexample
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
    role: a-one-residual-and-small-anchor-entry
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: actual-capacity-peeling-semantics
  - reproduction: reproductions/type_i_overflow_d_one_a_one_p_primary_chain_no_go.py
    role: focused-cycle-binary-branch-and-long-transient-receipts
visibility: public
last_checked: '2026-08-12'
---

# 完整乘积 \(d=1\) 的 \(a=1\) 任意长 \(p\)-primary 链与单轨道势 no-go

## 1. \(a=1\) 的单参数正规形

固定核心素数 \(p\equiv1\pmod {24}\)，并考虑完整乘积 \(d=1\) 饱和行

\[
A=\frac{pn-1}{4},
\qquad
R=(p-1)n-1,
\qquad
K=A(p-1).
\tag{1}
\]

在 \(p\)-free failure 类中写

\[
\frac{p+1}{2}=ga,
\qquad
\frac{n+1}{2}=gb,
\qquad
(a,b)=1,
\qquad
b\equiv-a\pmod p.
\tag{2}
\]

现在取上一卡留下的唯一边界 \(a=1\)。于是

\[
g=\frac{p+1}{2},
\qquad
b\equiv-1\pmod p.
\tag{3}
\]

因为 \(p,g,b\) 都是奇数，唯一可写

\[
b=2pr-1,
\qquad
r\ge1.
\tag{4}
\]

代回得到单参数正规形

\[
\boxed{
n=(p+1)(2pr-1)-1,
}
\tag{5}
\]

\[
\boxed{
R=2p^3r-p^2-2pr-p+1.
}
\tag{6}
\]

若令

\[
C=\frac{p^2-1}{2},
\qquad
T=p^2r-\frac{p+1}{2},
\tag{7}
\]

则

\[
A=\frac{p+1}{2}T,
\qquad
K=CT.
\tag{8}
\]

## 2. 一次真实 \(p^f\)-剥离后的二叉容量公式

取任意真实容量锚点

\[
h\mid K,
\qquad
(h,R)=1,
\qquad
p^f\parallel R-h,\qquad f\ge1.
\tag{9}
\]

沿 \(R-h\) 侧做 \(f\) 次真实 \(q=p\) raw peeling，得到

\[
y=\frac{R-h}{p^f},
\qquad
x=R-y.
\tag{10}
\]

每一步都保持 primitive bottom node；特别地 \(p\nmid y\)。由
\(R=p^fy+h\) 和 \(4K=pR+1\)，有

\[
\boxed{
4K=p^{f+1}y+ph+1.
}
\tag{11}
\]

所以

\[
\boxed{
(y,4K)=(y,ph+1).
}
\tag{12}
\]

另一方面 \(R=x+y\)，故

\[
\boxed{
(x,4K)=(x,py+1).
}
\tag{13}
\]

式 (12)--(13) 精确决定两侧容量的全部奇素数部分。实际容量仍是
\((y,K)\)、\((x,K)\)；它们和 (12)--(13) 只可能相差一个至多为 4 的 2-adic
修正，直接比较 \(\nu_2(y),\nu_2(x),\nu_2(K)\) 即可读取。因而剥掉 \(p\) 后不是只有
一个“继续主侧”，而是有两个都可沿真实 raw 边压到各自 \(K\)-容量的分支。忽略
(13) 会丢掉后面固定例中的实际 \(p\)-free 出口。

## 3. 任意长有限 \(H_j\) 主链

定义 repunit 型容量

\[
H_j=1+p+\cdots+p^j=\frac{p^{j+1}-1}{p-1},
\qquad
H_{j+1}=pH_j+1.
\tag{14}
\]

### 引理 1（整除即精确下一锚）

若

\[
H_{j+1}\mid K,
\tag{15}
\]

则

\[
\boxed{
(R-H_j,K)=H_{j+1}.
}
\tag{16}
\]

**证明。** 写 \(K=H_{j+1}k\)。因为 \(H_{j+1}\equiv1\pmod p\) 且
\(4K=pR+1\equiv1\pmod p\)，有

\[
s=\frac{4k-1}{p}\in\mathbb Z.
\tag{17}
\]

直接重排得到

\[
R-H_j=H_{j+1}s.
\tag{18}
\]

若整数同时整除 \(s,k\)，也整除 \(ps=4k-1\) 和 \(k\)，故只能为 1。因此
\((s,k)=1\)，式 (16) 得证。\(\square\)

### 定理 2（任意长有限 \(p\)-block transient）

对任意 \(N\ge1\)，存在正整数 \(r\)，使

\[
H_0\longmapsto H_1\longmapsto\cdots\longmapsto H_N
\tag{19}
\]

是实际容量剥离链；每个 \(H_j\) 的 departure side 都含恰一个完整 \(p\)-block，且
不是 terminal。

**证明。** 对 \(1\le m\le N\)，令

\[
d_m=\frac{H_m}{(H_m,C)},
\qquad
D_N=\operatorname{lcm}_{1\le m\le N}d_m.
\tag{20}
\]

因为 \(K=CT\)，条件 \(H_m\mid K\) 等价于 \(d_m\mid T\)。又
\(H_m\equiv1\pmod p\)，所以 \((D_N,p)=1\)。因此同余

\[
p^2r\equiv\frac{p+1}{2}\pmod {D_N}
\tag{21}
\]

有解，并可与任意允许的模 \(p\) 类用 CRT 联立。选择模 \(p\) 的类同时避开

\[
r\equiv-\frac12\pmod p,
\qquad
r\equiv-1\pmod p.
\tag{22}
\]

再取足够大的正代表。式 (21) 使 \(H_1,\ldots,H_N\) 全部整除 \(K\)，故引理 1
逐步给出 (19)。

由 (6)、(14) 直接模 \(p^2\) 计算：

\[
R-H_0\equiv-p(2r+1)\pmod {p^2},
\tag{23}
\]

而所有 \(j\ge1\) 满足

\[
R-H_j\equiv-2p(r+1)\pmod {p^2}.
\tag{24}
\]

式 (22) 因而保证每个 departure side 的 \(p\)-进估值恰为 1。又取 \(r\) 足够大
使 \(R-H_j>H_{j+1}\)，便排除 terminal。先做真实 \(p\)-edge，再剥离其它超容量
素数，最终精确到达 (16) 的 \(H_{j+1}\)。证毕。

式 (19) 的量词是

\[
\forall N\ \exists r,
\tag{25}
\]

不是固定一个 \(r\) 后的无限链；固定 \(K\) 的因子有限，而 \(H_j\to\infty\)。但
(25) 已足以全称否定任何只以“连续主侧 \(p\)-block 次数”为第三坐标的统一有界倒计时。

## 4. 一个真实四周期

取

\[
p=73,
\qquad
r=4\,796\,963.
\tag{26}
\]

由 (4)--(8) 得

\[
b=700\,356\,597,
\qquad
n=51\,826\,388\,177,
\tag{27}
\]

\[
A=945\,831\,584\,230,
\quad
R=3\,731\,499\,948\,743,
\quad
K=68\,099\,874\,064\,560.
\tag{28}
\]

容量轨道精确为

\[
\boxed{
1\longmapsto74\longmapsto5403\longmapsto394420\longmapsto1.
}
\tag{29}
\]

四条 departure side 的 complete-excess bundle 依次为

\[
50\,425\,674\,983,
\quad
690\,634\,823,
\quad
9\,460\,727,
\quad
3\,731\,499\,554\,323,
\tag{30}
\]

并且四者都被 73 整除。每条宏都先做唯一一次真实 \(q=73\) edge，再剥离余下超容量
素数，且中间不存在 gcd reduction；四个 departure node 都不是 bottom Type I
terminal。因此 (29) 是同一图表 raw/capacity policy 的真实局部 stutter，而不是静态
gcd 图的伪周期。

## 5. no-go 的严格作用域与正确下一命题

固定例不否定完整 Reach。比如从 \(h=74\) 的 departure side 剥掉 73 后，式 (13)
给出的互补容量为

\[
(x,K)=5330.
\tag{31}
\]

继续真实容量轨道得到

\[
5330\longmapsto3\longmapsto20\longmapsto3.
\tag{32}
\]

在 \(h=3,20\) 上，对侧不被 73 整除，因而 complete-excess bundle 为
\(p\)-free；固定回执还给出相应 canonical target capacities \(10,4<72\)。所以：

1. (19)、(29) 否定“主侧 \(p\)-primary 链自身必有限退出”；
2. 它们不否定 peeled node 的互补侧可能退出；
3. 它们不否定 Type I/II terminal-first。事实上 \(p=73\) 本身已有直接证书
   \(4/73=1/20+1/219+1/4380\)；
4. 它们不是 Erdős--Straus 反例，也不是完整 G/Type I selector 的 no-go；
5. 后续的
   [双侧容量树 no-go](type-I-overflow-full-product-d-one-a-one-two-sided-capacity-tree-no-go.md)
   进一步否定了任何固定深度的二叉容量退出；正确接口必须检查中间 raw 节点的
   terminal 或 split-excess 结构，而不能只增加二叉搜索深度。

## 6. 聚焦回执

```bash
python3 reproductions/type_i_overflow_d_one_a_one_p_primary_chain_no_go.py --verify
```

回执只重放固定 \(p=73,r=4\,796\,963\) 的四周期、每条真实 raw 分解、四个
\(p\)-containing bundle、互补侧 (31)--(32) 及其两个严格容量出口；另固定核对一个
八步 \(H_j\) transient。任意 \(N\) 的结论由第 3 节 CRT 证明承担，脚本不扫描素数、
分母、历史 selector 或一般 \(r\)。
