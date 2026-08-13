---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-s-zero-hensel-height-no-go
title: a=1 的 s=0 Hensel 任意根高度与统一 priority 抢占
statement: >-
  对 p=73 存在同一个完整超额算术固定胞 r(j)=57+73^2 Vj，其中源根 departure
  恒有 73-adic 高度 1、atomic split multiplier 恒满足 L=1 (mod 73^2)；对每个
  f>=2，有无穷多个正参数使条件 split rechart 的算术 target 根 departure 高度为 f。
  但该族在真实 terminal-first selector 下不会成为 atomic split 边：p=73 已有直接
  Type II 终端；即使人为屏蔽该终端，固定容量 (y,K)=3 也会先到 h=3，由小 endpoint
  定理给出 terminal-or-strict 算术动作：j!=5 (mod 11) 时 capacity 为 2，j=5
  (mod 11) 时为 22。只有该单侧 action 自身通过 typed E1--E5 后，它才构成第二层
  实际 priority 抢占。
  目标高度由一个模 73 有唯一简单根的三次整数多项式 H(j) 控制：
  R(r')-74=73H(j)、H(j)=45j+11 (mod 73)。这排除仅由 s=0 算术 normal form 推出
  根 p-adic 高度统一有界或不增；同时它证明当前 selector 的 priority prefix 正好排除
  整个高度族，因而该族不是 admitted-cycle 障碍。它不推出其它素数或其它 receipt cell
  也有同样的 priority 出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-chart-least-coprime-prime-anchor-source
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - split-stutter
  - p-adic
  - hensel-lifting
  - unbounded-height
  - potential-no-go
  - terminal-first
  - priority-preemption
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
    role: s-zero-rechart-normal-form
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: conditional-atomic-split-admission
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: canonical-anchor-source
  - reproduction: reproductions/type_i_s_zero_hensel_height_no_go.py
    role: fixed-cell-height-controls-and-terminal-endpoint-priority-preemption
visibility: public
last_checked: '2026-08-13'
---

# \(a=1\) 的 \(s=0\) Hensel 任意根高度与统一 priority 抢占

## 1. 固定完整超额胞

固定

\[
p=73,\qquad g=37,\qquad
V=\operatorname{lcm}(72,197210,199911)=12\,786\,307\,560,
\tag{1}
\]

并令

\[
r(j)=57+73^2Vj,\qquad j\ge0.
\tag{2}
\]

相应图表量可写成

\[
R=777888r-5401,\qquad K=14196456r-98568.
\tag{2a}
\]

特别地，

\[
\frac{R-1}{74}=10512r-73,\qquad
\frac K{74}=191844r-1332.
\tag{2b}
\]

右侧两线性式的行列式绝对值为 \(2628\)。步长 \(73^2V\) 被 \(2628\) 整除，而
\(j=0\) 时两商互素；故对所有 \(j\ge0\)

\[
\boxed{(R-1,K)=74.}
\tag{2c}
\]

若相应图表已是 persistent state，最小互素素数 source 先给出 chart-local
\(\{1,R-1\}\) anchor。再把 \(R-1\) 中相对 \(K\) 超容量的每个素数按完整指数逐次
raw 除去；每步 primitive 性由 \((R-1,R)=1\) 保持，(2c) 因而使路径精确停在
\(\{74,R-74\}\)。这不是静态选择一个 \(K\) 的因子。本卡也不由 formal source 反向
制造 persistent parent。

在 \(a=1,d=1\) 图表中，根 \(h=74\) 的一层 \(p\)-peel 给

\[
\begin{aligned}
x(j)&=52\,277\,832\,771\,266\,119\,680j+43\,726\,898,\\
y(j)&=726\,081\,010\,712\,029\,440j+607\,317,\\
A(j)&=13\,435\,019\,812\,793\,072\,520j+11\,237\,492,
\end{aligned}
\tag{3}
\]

且 \(K(j)=72A(j)\)。两条消元行列式为

\[
767232(-1369)-197173(-5326)=-197210,
\tag{4}
\]

\[
10656(-1369)-197173(-75)=199911.
\tag{5}
\]

因为 \(r(j)-57\) 被 \(72,197210,199911\) 整除，(4)--(5) 和 \(j=0\) 的 gcd
对所有 \(j\ge0\) 给出

\[
(x,A)=2,\quad(y,A)=1,\quad(x,K)=2,\quad(y,K)=3.
\tag{6}
\]

所以整个参数族的完整超额分解固定为

\[
x=2Q_x,\qquad y=3Q_y,\qquad
(A,Q_x)=(A,Q_y)=1,
\tag{7}
\]

\[
\begin{aligned}
Q_x(j)&=26\,138\,916\,385\,633\,059\,840j+21\,863\,449,\\
Q_y(j)&=242\,027\,003\,570\,676\,480j+202\,439.
\end{aligned}
\tag{8}
\]

源根 departure 还满足

\[
R(r)-74=73\bigl(2(73^2-1)r-75\bigr).
\tag{9}
\]

括号模 73 恒为 \(30\)，所以每个源状态都恰有
\(\nu_{73}(R-74)=1\)。又 \(73\nmid K\)，因此从该真实 endpoint 出发的
\(73\)-edge 恰好多剥一层，并无 gcd reduction；其输出正是 (3) 的 primitive
\(\{x,y\}\)。

## 2. \(s=0\) relay 与高度多项式

联合 multiplier 为

\[
\begin{aligned}
L(j)=Q_xQ_y
={}&6\,326\,323\,609\,399\,226\,524\,762\,256\,681\,120\,563\,200j^2\\
&+10\,583\,081\,143\,381\,474\,116\,929\,280j\\
&+4\,426\,014\,752\,111.
\end{aligned}
\tag{10}
\]

三个系数模 \(73^2\) 分别为 \(0,0,1\)，故

\[
L(j)\equiv1\pmod {73^2}.
\tag{11}
\]

写 \(t=(L-1)/73^2\)，则

\[
\begin{aligned}
t(j)
={}&1\,187\,150\,236\,329\,372\,588\,621\,177\,834\,700\,800j^2\\
&+1\,985\,941\,291\,683\,519\,256\,320j
+830\,552\,590,
\end{aligned}
\tag{12}
\]

并且 \(t(j)\equiv45j+54\pmod {73}\)。令 \(T=73^2r-37\)。在 atomic split
已通过 E1--E4 的前提下，既有 \(s=0\) 正规形给出

\[
r'=r+tT,\qquad T'=LT.
\tag{13}
\]

定义

\[
H(j)=2(73^2-1)r'(j)-75.
\tag{14}
\]

其精确式为

\[
\begin{aligned}
H(j)={}&
4\,593\,423\,440\,403\,964\,545\,177\,479\,339\,766\,882\,217\,819\,365\,187\,780\,608\,000j^3\\
&+11\,526\,264\,542\,696\,077\,825\,044\,476\,203\,856\,387\,727\,360\,000j^2\\
&+9\,640\,941\,085\,434\,912\,999\,813\,015\,586\,560j\\
&+2\,687\,998\,488\,683\,439\,957.
\end{aligned}
\tag{15}
\]

目标 departure 精确满足

\[
R(r')-74=73H(j),
\tag{16}
\]

而

\[
H(j)\equiv45j+11\pmod {73},\qquad
H'(j)\equiv45\not\equiv0\pmod {73}.
\tag{17}
\]

唯一模 73 根是 \(j\equiv3\)。在此类上 \(t\equiv43\not\equiv0\pmod {73}\)，
所以还恒有

\[
\nu_{73}(L-1)=2.
\tag{18}
\]

## 3. 任意算术目标根高度

由 (17) 的简单根 Hensel 提升，对每个 \(m\ge1\) 有唯一根类
\(j_m\bmod73^m\)。在该类的 73 个模 \(73^{m+1}\) lift 中，恰一个继续为下一层根，
其余 72 个都满足

\[
\nu_{73}(H(j))=m.
\tag{19}
\]

每个这样的类包含无穷多个非负整数。因此对每个 \(f=m+1\ge2\)，都有无穷多个
算术候选 \(j\ge0\) 同时保持固定完整超额胞、(18)，并满足

\[
\boxed{\nu_{73}(R(r')-74)=f.}
\tag{20}
\]

对其中任一 \(j\)，若 persistent source、独立 target validation 与 adapter receipt
通过 E1--E4，则 (20) 才是相应合法 checkpoint 的高度。

前六个控制为

| \(m\) | \(j\) | \(r(j)\) | \(\nu_{73}(H(j))\) |
|---:|---:|---:|---:|
| 1 | 3 | 204,414,698,961,777 | 1 |
| 2 | 1,536 | 104,660,325,868,400,697 | 2 |
| 3 | 65,484 | 4,461,964,048,936,424,217 | 3 |
| 4 | 3,566,637 | 243,024,342,886,910,711,937 | 4 |
| 5 | 883,912,108 | 60,228,209,155,146,445,501,977 | 5 |
| 6 | 79,660,632,642 | 5,427,934,746,871,531,913,488,137 | 6 |

所以源高度恒为 1，而同一固定胞中的条件 rechart 算术候选可产生任意大的
目标根高度。这严格排除仅依赖 \(s=0\) normal-form 算术、且未使用 admission gate
额外限制来证明“根 \(p\)-进高度统一有界”或“\(s=0\) 下高度不增”的方案。

## 4. 真实 selector 对整个族的统一抢占

上述高度族只看了 split normal form；现有 selector 在生成 atomic split 之前必须先跑
terminal/endpoint priority prefix。对 \(p=73\)，首先有直接 Type II 终端

\[
\boxed{
\frac4{73}=\frac1{20}+\frac1{219}+\frac1{4380}.}
\tag{21}
\]

它只依赖 \(p\)，所以对所有 \(j\) 都先于任何 chart-local split 返回 terminal leaf。
因此本族没有一个实例会被真实 selector 选择成 atomic split edge。

即使为分析局部机制而人为屏蔽 (21)，式 (6) 的

\[
(y,K)=3
\tag{22}
\]

也强制容量剥离先到 \(h=3\)：由 \(y=3Q_y\)、\((Q_y,K)=1\)，逐个除去 \(Q_y\)
的实际素因子，且 primitive 性沿 raw 除法保持。由于 \(3^2<73\)，小 endpoint 定理给出 direct Type I
或 strict 单侧 action。这里还可把后一动作显式化：

\[
R-3=4Q_3,
\tag{23}
\]

\[
Q_3(j)=13\,250\,978\,445\,494\,537\,280j+11\,083\,553.
\tag{24}
\]

消元行列式为

\[
194472(-1369)-197173(-1351)
=148555=5\cdot11\cdot37\cdot73.
\tag{25}
\]

模 11 有

\[
A(j)\equiv2+4j,
\qquad
Q_3(j)\equiv8+5j.
\tag{26}
\]

两者同时为零恰在 \(j\equiv5\pmod {11}\)。其余素因子由固定非零余数排除，所以当
\(j\not\equiv5\pmod {11}\) 时

\[
(A,Q_3)=1,\qquad Q_3\equiv17\pmod {72},\qquad Q_3\equiv36\pmod {73},
\tag{27}
\]

并且 \(12\mid K\)。特别地 \((Q_3,72)=1\)，故 \((Q_3,K)=1\)；完整超额分解精确为

\[
R-3=Q_3\cdot4,
\qquad Q=Q_3,
\qquad \beta=4,
\qquad g_A=1.
\tag{27a}
\]

所以该 h=3 receipt 的 canonical target capacity 精确为

\[
\boxed{c=-36^{-1}\equiv2<72\pmod {73}.}
\tag{28}
\]

剩下的 \(j\equiv5\pmod {11}\) 也不是算术例外。行列式 (25) 的 11-adic 指数恰为 1，
其余素因子仍被固定非零余数排除，故

\[
(A,Q_3)=11.
\tag{29}
\]

写 \(a=\nu_{11}(A)\)、\(e=\nu_{11}(Q_3)\)，则 \(\min(a,e)=1\)。若 \(e>a\)，
完整超额块收入整个 \(11^e\)，并有 \(g_A=11\)；若 \(e\le a\)，则 \(e=1\)，这一层
11 留在 residual。两种情况都给相同的 canonical 数据

\[
E=\frac{Q_3}{11},
\qquad
D=44.
\tag{30}
\]

由 \(Q_3\equiv36\pmod {73}\) 与 \(11^{-1}\equiv20\pmod {73}\)，

\[
E\equiv63\pmod {73},
\qquad
\boxed{c=-63^{-1}\equiv22<72\pmod {73}.}
\tag{31}
\]

所以屏蔽直接终端后，全族都有 h=3 strict 算术动作：\(j\not\equiv5\pmod {11}\) 时
\(72\to2\)，\(j\equiv5\pmod {11}\) 时 \(72\to22\)。

对高度 \(f=m+1\)，每个 Hensel 精确高度类是模 \(73^{m+1}\) 的非空类；由
\((11,73)=1\)，CRT 还可任意指定上面的两个模 11 分支。所以对每个 target 高度
\(f\ge2\)，两种 strict capacity 都各有无穷多个候选。把它升级成完整 priority 宏仍须
该单侧 action 自身的 E1--E5；在未完成这些回执时，它不能单独使 atomic split
priority admission 失败。全族的实际 split admission 已由直接终端 (21) 无条件排除。

## 5. 量词边界

本定理证明两件必须分开的事：normal-form 算术 target 高度无统一上界；当前真实
selector 又因 (21) 统一终止；在屏蔽 (21) 的局部实验中，(22)--(28) 则给出
endpoint-first 算术候选，只有单侧 E1--E5 完整时才实际抢占。它不绕过 atomic split
的 persistent path、typed validator 和 E1--E4 合同；全族不能满足“priority prefix
全部 miss”只由已验证的 (21) 保证。

六个高度控制和 \(j=5\) 控制验证固定胞、算术高度 \(2,\ldots,7\) 与 h=3 的两个
strict receipt；一般高度由 (17)--(20) 的 Hensel 论证承担，与任一模 11 分支的同时性
由 CRT 承担。

因此仅靠该 normal form 限制 \(p\)-block 深度或根高度不足以证明终止；但本族也不能
再作为 admitted-height no-go 的证据。它给出的正面方法论是：先证明 terminal/endpoint
priority 的统一覆盖，再讨论 stutter 势。尚未解决的是其它核心素数、其它完整超额胞在
priority prefix 全部 miss 后的合法 \(s=0\) checkpoint。

## 6. 聚焦回执

运行
\( \texttt{python3 reproductions/type_i_s_zero_hensel_height_no_go.py --verify} \)。

脚本只派生 (3)、(8)、(10)、(12)、(15)、(24)，核对固定 gcd 胞、六个 Hensel 控制、
直接 Type II 恒等式及 h=3 priority receipt；不扫描素数、分母、selector history、
证书菜单或历史结果。
