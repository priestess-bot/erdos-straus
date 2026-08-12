---
kind: claim
claim_id: type-I-high-support-c4-canonical-stutter-boundary
title: C=4 最小高支撑正分支的 canonical complete-excess stutter
statement: 对每个核心素数 p=25 (mod 48)，C=4 的最小高支撑正分支为 R=4p+3、A=(pR+1)/16、K=4A。其高 R canonical raw source 一步到达 anchor (1,R-1)，且 R-1=2Q、Q=2p+1。该 anchor 的完整 complete-excess bundle 为 Q、beta=2、M=AQ，并满足 canonical_chart(p,M)=(RQ+2,4M)。因此 source 与 target 的 high-support cofactor 均为 4，既有 sharp potential (floor(B_p/A),K/A) 精确 stutter 为 (0,4)->(0,4)。这给出一个无穷图表级 E5 失败族，故该势函数不能单独证明 complete-excess 全局递降。控制 p=2137 的 source 是 G、当前九路 Type I dispatch 仍 residual，anchor 在唯一 2801 节点 sink SCC 中，且 source/target 都是 centered Type I miss；它表明该 stutter 并不只是已知 terminal 的重复。图表恒等式本身不声称每个 p=25 (mod 48) 分支都是实际 G/F persistent state。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - denominator-escape-state-contract
topics:
  - type-I
  - high-support
  - c4-boundary
  - complete-excess
  - stutter
  - G-state
  - potential-boundary
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_support_c4_g_stutter_boundary.py
    role: canonical-stutter-and-p2137-G-control
visibility: public
last_checked: '2026-08-12'
---

# (C=4) 最小高支撑正分支的 canonical complete-excess stutter

## 1. (C=4) 的正分支

与 (C=2,3) 不同，(C=4) 的最小越界支撑取决于 (p\pmod {16})。这里只取

\[
p\equiv25\pmod {48},
\tag{1}
\]

即 (p\equiv9\pmod {16}) 的正分支。令

\[
R=4p+3,
\qquad
A=\frac{pR+1}{16},
\qquad
K=4A.
\tag{2}
\]

**引理 1。** (A) 是同余 (16A\equiv1\pmod p) 中严格越过

\[
B_p=\frac{(p-1)^2}{4}
\tag{3}
\]

的最小正解，且

\[
A-p<B_p<A,
\qquad
4K=pR+1,
\qquad
K/A=4.
\tag{4}
\]

**证明。** 由 (p\equiv9\pmod {16}) 知 (2) 为整数，且

\[
16A=p(4p+3)+1.
\tag{5}
\]

又

\[
A-B_p=\frac{11p-3}{16},
\tag{6}
\]

严格介于 (0) 与 (p) 之间。全部解相差 (p)，故得到最小性及 (4)。\(\square\)

## 2. canonical stutter 宏

定义

\[
Q=2p+1,
\qquad M=AQ.
\tag{7}
\]

**定理 2（完整 bundle 保持余因子）。** 图表 (2) 的高 (R) canonical raw source

\[
\bigl(p,\ R(p-1)-p,\ p-1\bigr)
\tag{8}
\]

经过其唯一 (p)-edge（shift (=1)，无 gcd reduction）到达

\[
(1,R-1,1)=(1,2Q,1).
\tag{9}
\]

该 anchor 的 complete-excess 分解精确为

\[
Q_{\rm excess}=Q,
\qquad \beta=2,
\qquad x\beta=2.
\tag{10}
\]

并给出 canonical target

\[
\boxed{
\operatorname{canonical\_chart}(p,M)=(RQ+2,4M).}
\tag{11}
\]

特别地，若两端是持久状态，则既有 sharp potential 精确保持：

\[
\boxed{
\Lambda_p^\sharp=(0,K/A)=(0,4)
\longmapsto(0,K_M/M)=(0,4).}
\tag{12}
\]

**证明。** 因 (p\nmid R)，(8) 是 primitive raw source。按 universal source 的
一步约化，有

\[
\frac{R(p-1)-p+R}{p}=R-1,
\qquad
\frac{p-1+1}{p}=1,
\tag{13}
\]

即 (9)。再由 (R-1=4p+2=2Q)。

在 (Q) 模下有 (R=4p+3\equiv1)，所以

\[
16A=pR+1\equiv p+1\pmod Q,
\qquad
32A\equiv1\pmod Q.
\tag{14}
\]

故 ((A,Q)=1)，于是 (M=AQ)。同样，

\[
\gcd(Q,K)=1,
\tag{15}
\]

因为 (4K=16A\equiv p+1\pmod Q)，而
((Q,p+1)=1)。所以 (9) 中 (Q) 的每个完整素数幂都超过 (K) 的容量，全部进入
complete-excess block；剩余 \(\beta=2\)，且 (2\mid K)、((Q,2)=1)。这证明 (10)。

最后，直接计算

\[
p(RQ+2)+1
=Q(pR+1)
=16AQ
=16M.
\tag{16}
\]

且 (RQ+2\equiv3\pmod4)、(0<RQ+2<4M)，所以它正是 (11) 的 canonical chart。
由 (K_M=4M) 立即得到 (12)。\(\square\)

因此 (8)--(11) 支付 raw source、path、full-block bundle、lcm cargo、两个图表的
独立重建与 (operatorname{Sol}(4,p)) 的恒等提升；但它**不能**支付严格 E5。它不是
可递归边，而是当前势函数的明确 stutter 边界。

## 3. 实际 G 控制而非 terminal 重复

取

\[
p=2137,
\qquad R=8551,
\qquad A=1142093,
\qquad K=4568372.
\tag{17}
\]

这是 (1) 的一个核心素数。它满足

\[
K=2^2\cdot337\cdot3389,
\tag{18}
\]

并且每个 (K)-素因子对 (R) 的 Jacobi 符号都是 (+1)，而

\[
\left(\frac{-1}{8551}\right)=-1.
\tag{19}
\]

故 source 是 G 状态；其 centered Type I 盒不含 (-1)。当前九路 Type I terminal
dispatch 也返回 residual。anchor ((1,8550)) 位于唯一的 2801 节点 bottom sink SCC。

这里

\[
Q=4275,
\qquad
M=4882447575,
\qquad
(R_M,K_M)=(36555527,19529790300),
\tag{20}
\]

两端 centered box 都不含 (-1)，而 (12) 仍给出 (4\mapsto4)。这个控制说明：
即使 terminal-first 的当前九路菜单未命中且 source 是实际 G，单独依赖
\(\Lambda_p^\sharp\) 的 complete-excess 策略也会停在 stutter，而非自动得到出口。

## 4. 第二 anchor 的算术压缩

单步 stutter 不是无限循环。令第一张 target 图表为

\[
R_1=RQ+2,
\qquad A_1=AQ,
\qquad K_1=4A_1,
\tag{21}
\]

并在它自己的 high \(R\) canonical raw source 上再次走到 anchor。其完整 excess block 为

\[
\boxed{
Q_1=\frac{R_1-1}{2}=Q+16A,}
\tag{22}

余因子仍为 \(\beta=2\)。而且

\[
(Q_1,A_1)=(Q_1,K_1)=1.
\tag{23}

令 \(A_2=A_1Q_1\)。第二个 anchor 的 canonical target 不是形式大模数
\(R_1Q_1+2\)，而是

\[
\boxed{
R_2=\frac{R_1Q_1+R+2}{2},
\qquad
K_2=2A_2.}
\tag{24}

故这个两 anchor 的纯算术图表链为

\[
\boxed{
(R_0,K_0;A_0):4
\longmapsto
(R_1,K_1;A_1):4
\longmapsto
(R_2,K_2;A_2):2.}
\tag{25}

**证明。** 由 (11)，

\[
Q_1=\frac{RQ+1}{2}=Q+16A.
\tag{26}

在模 \(Q\) 下，\(2Q_1\equiv1\)，所以 \((Q,Q_1)=1\)。若奇素数
\(q\) 同时整除 \(A,Q_1\)，由

\[
16A=pR+1,
\qquad 2Q_1=RQ+1
\tag{27}

可得 \(p\equiv Q\pmod q\)，再由 \(Q=2p+1\) 得
\(p\equiv-1\pmod q\)，随后 \(R\equiv1\pmod q\)。但此时
\(16A=pR+1\equiv2\pmod q\)，与 \(q\mid A\) 矛盾。又 \(Q_1\) 是奇数，
故 (23) 成立。

写 \(R_f=R_1Q_1+2\)。利用

\[
pR_1+1=16A_1,
\qquad Q_1-Q=16A,
\tag{28}

计算得到

\[
pR_f+1=16(A_2-A),
\qquad pR+1=16A.
\tag{29}

相加并除以二即给

\[
p\frac{R_f+R}{2}+1=8A_2.
\tag{30}

右端是 \(4K_2\) 且 \(R_2=(R_f+R)/2\equiv3\pmod4\)；又
\(0<R_2<4A_2\)，故它就是 canonical chart，并证明 (24)--(25)。\(\square\)

这已给出一个可以读取的 reset 方向。单独由 (25) 仍不能推出全局递归边：若没有真实
persistent parent，就不能把内部图表的 \(4\to2\) 回填为未知 source 的 E5，也不能跳过
terminal-first guard。后续的
[C=4 双高锚内部 checkpoint 宏](type-I-high-support-c4-two-anchor-persistent-macro.md)
证明了精确的条件性补强：只要第一个高锚已收费，第一次 target 可保持为同 scope 的
**内部** checkpoint，第二个 universal-source bundle 就给出一条 \(4\to2\) 的 E1--E5
宏；它不创建 fresh root，也不声称每个本图表都已具有这样的 parent。

对 \(p=2137\)，该压缩具体为

\[
4\longmapsto4\longmapsto2,
\tag{31}
\]

其中

\[
Q_1=18277763,
\quad A_2=89240219635774725,
\quad
(R_2,K_2)=(334076629427327,178480439271549450).
\tag{32}
\]

## 5. 对全局出口目标的影响

本卡不否认 (p=2137) 或任意 (1) 中的素数有其他 Erdős--Straus 证书；也不把全部
图表级 stutter 误称为实际 persistent state。严格结论只有两点：

1. (C=4) 不能按 (C=2,3) 的方式继续得到 complete-excess strict no-go；
2. 当前势 \(\Lambda_p^\sharp\) 对可由 canonical raw source 显式构造的 macro 不严格，
   因而无法作为目标所要求的全局严格良基势。

后续仍必须覆盖没有已收费 parent 的高图表，并补齐全局 terminal-first 与其它 reset 的
良基拼接。对不满足已收费 parent 前提的 stutter，仍需要 terminal/alternate/paid reset，或为状态加入一个能在

\[
(A,K/A)\longmapsto(AQ,K_M/M)=(AQ,4)
\tag{33}
\]

严格下降、同时与其它所有合法宏兼容的新良基坐标。把支撑单调增加直接当作势函数并不可行，
因为它本身不是良基的下降方向。式 (25) 的局部修复现已在“已收费 parent”前提下完成；
不能据此把所有算术 \(4\to2\) 都当作全局严格递降。

## 6. 聚焦复核

```bash
python3 reproductions/type_i_high_support_c4_g_stutter_boundary.py --verify
```
