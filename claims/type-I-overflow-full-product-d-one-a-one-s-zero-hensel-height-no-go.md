---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-s-zero-hensel-height-no-go
title: a=1 的 s=0 Hensel 任意根高度 no-go
statement: >-
  对 p=73 存在同一个完整超额算术固定胞 r(j)=57+73^2 Vj，其中源根 departure
  恒有 73-adic 高度 1、atomic split multiplier 恒满足 L=1 (mod 73^2)；对每个
  f>=2，有无穷多个正参数使条件 split rechart 的算术 target 根 departure 高度为 f。
  对其中任一参数，只有 persistent source 与完整 E1--E4 receipt 获准后，它才是合法
  checkpoint。
  目标高度由一个模 73 有唯一简单根的三次整数多项式 H(j) 控制：
  R(r')-74=73H(j)、H(j)=45j+11 (mod 73)。这排除仅由 s=0 算术 normal form 推出
  根 p-adic 高度统一有界或不增；它不排除 admission gate 对合法边施加额外限制，
  也不声称这些 target 有相同 endpoint capacity 或 terminal 行为。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-chart-least-coprime-prime-anchor-source
  - type-I-universal-p-source-capacity-anchor-orbit
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
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
    role: s-zero-rechart-normal-form
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: conditional-atomic-split-admission
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: canonical-anchor-source
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: actual-capacity-peeling-to-root-endpoint
  - reproduction: reproductions/type_i_s_zero_hensel_height_no_go.py
    role: fixed-cell-polynomials-and-conditional-target-height-two-through-seven-controls
visibility: public
last_checked: '2026-08-13'
---

# \(a=1\) 的 \(s=0\) Hensel 任意根高度 no-go

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

若相应图表已是 persistent state，则由 canonical anchor source 与容量剥离定理，
chart-local \(\{1,R-1\}\) source/path 可绑定并重放到 primitive endpoint
\(\{74,R-74\}\)，不是静态选择一个 \(K\) 的因子。本卡不由 formal source 反向制造
persistent parent。

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

## 4. 量词边界

本定理证明的是条件 split rechart 的算术 target 高度 no-go，不绕过 atomic split
的 persistent path、typed validator 和 E1--E4 准入合同。admission gate 可能排除该无穷算术族的
部分或全部成员；本卡不证明任一候选已获准，也不证明 (20) 的 target 具有相同
endpoint capacity、terminal menu 或后续 orbit。六个控制只验证固定胞与算术高度
\(2,\ldots,7\)，一般高度由 (17)--(20) 的 Hensel 论证承担。

因此仅靠该 normal form 限制 \(p\)-block 深度或根高度不足以证明终止；完整证明必须
在任意算术高度上构造 terminal/strict guarded macro，证明 admission gate 统一排除高度候选，
或找到能跨合法 \(K\mapsto LK\) stutter checkpoint 严格下降的另一全局资源。

## 5. 聚焦回执

运行
\( \texttt{python3 reproductions/type_i_s_zero_hensel_height_no_go.py --verify} \)。

脚本只派生 (3)、(8)、(10)、(12)、(15)，核对固定 gcd 胞与六个 Hensel 控制；不扫描
素数、分母、selector history、证书菜单或历史结果。
