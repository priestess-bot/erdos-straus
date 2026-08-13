---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-endpoint-s-zero-p-free-return
title: a=1 endpoint s=0 的精确 p-free 回返与任意根高度边界
statement: >-
  在完整乘积 d=1 的 a=1 hard state 中，若真实 endpoint 的完整超额 multiplier
  E_0=1+p^2t，则 canonical checkpoint 精确保持 a=1，且
  r_1=r+tT、T_1=E_0T、A_1=E_0A、K_1=E_0K。其下一 ordinary multiplier 必为
  E_1=pF_1，其中 F_1=2(p-1)r_1-1；故该 checkpoint 必返回普通 p-free failure，
  而不是立即严格。写 e=nu_p(F_1)、F_1=p^eu，则从 anchor 剥尽 p^(e+1) 后两侧为
  y=(p+1)u、x=1+(p^(e+1)-1)y，容量精确为 p+1 与
  gcd(x,p^(e+1)-p-1)，再沿 y 到根锚 h=p+1，下一容量整除 p^2+p+1。根锚 departure
  的高度则为 1+nu_p((p+1)F_1-1)，与 ordinary p-free block 高度 e+1 不同。
  更强地，在 p=97 存在一个从 canonical anchor 可实际重放的 chart-local raw
  endpoint s=0 参数族，
  使 conditional target 的每个形式根 departure 高度 f>=2 都出现无穷多次，并可同时
  令根容量饱和到 p^2+p+1；这排除任何只靠 s=0、ordinary block 高度、固定根高度界或
  根容量真因子下降的终止论证。相应 chart 仍须先有 persistent lineage，target 仍须
  通过 terminal-first 与 E1--E5 才能成为递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
  - type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
  - type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
  - type-I-chart-least-coprime-prime-anchor-source
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - capacity-endpoint
  - p-free-failure
  - p-adic
  - hensel-lifting
  - unbounded-height
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
    role: actual-endpoint-stutter-and-four-way-relay
  - claim: type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
    role: actual-p-block-peeling-and-a-one-root-anchor
  - claim: type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
    role: exact-a-one-root-capacity-formula
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: target-independent-formal-source-to-canonical-anchor
  - reproduction: reproductions/type_i_endpoint_s_zero_p_free_return.py
    role: anchor-local-actual-endpoint-return-height-two-and-post-return-strict-control
  - reproduction: reproductions/type_i_endpoint_s_zero_actual_unbounded_height.py
    role: anchor-local-actual-endpoint-generated-unbounded-root-height-family
visibility: public
last_checked: '2026-08-13'
---

# \(a=1\) endpoint \(s=0\) 的精确 \(p\)-free 回返与任意根高度边界

## 1. 精确回返正规形

固定核心素数 \(p\equiv1\pmod {24}\)，并写

\[
g=\frac{p+1}{2},\qquad b=2pr-1,\qquad n=(p+1)b-1,
\tag{1}
\]

\[
T=p^2r-g,\qquad A=gT,\qquad K=A(p-1),\qquad R=(p-1)n-1.
\tag{2}
\]

设一条绑定于真实 persistent source 的 raw path 到达 primitive endpoint
\(\{h,R-h\}\)，其单侧完整超额 receipt 通过来源、maximality 与 \(p\)-free 门，并有

\[
E_0=1+p^2t.
\tag{3}
\]

这正是单侧 relay 中 \(s=(E_0-1)/p=pt\) 的 hard 类。canonical checkpoint
\(U\) 的参数为

\[
b_1=E_0b-pt,\qquad n_1=E_0n-pt.
\tag{4}
\]

定义

\[
\boxed{r_1=r+tT.}
\tag{5}
\]

由 \(2pg=p(p+1)\) 直接计算得

\[
b_1=2pr_1-1,
\tag{6}
\]

进而

\[
\boxed{T_1=p^2r_1-g=E_0T,\qquad A_1=E_0A,\qquad K_1=E_0K.}
\tag{7}
\]

所以 \(U\) 不是一个未知图表：它精确返回同一个 \(a=1,d=1\) 正规形。

## 2. 必然返回 ordinary \(p\)-free failure

令 \(U\) 的下一 ordinary multiplier 为

\[
E_1=(p-1)b_1-1.
\tag{8}
\]

把 (6) 代入并定义

\[
F_1=2(p-1)r_1-1,
\tag{9}
\]

得到精确分解

\[
\boxed{E_1=pF_1.}
\tag{10}
\]

因此 endpoint \(s=0\) checkpoint 必落入 ordinary \(p\)-free failure；它不是
\(p\)-free canonical action，更不能直接登记严格边。这把单侧 relay 留下的第一类
余项接回既有 p-block peeling 接口。

更精确地，

\[
R_1-1=p(p+1)F_1.
\tag{11}
\]

写

\[
e=\nu_p(F_1),\qquad F_1=p^eu,\qquad p\nmid u.
\tag{12}
\]

从 anchor \(\{1,R_1-1\}\) 真实剥尽 \(p^{e+1}\) 后得到

\[
\boxed{
y=(p+1)u,\qquad
x=1+(p^{e+1}-1)y.}
\tag{13}
\]

既有 p-free peeled-node 定理在 \(a=1\) 上给出

\[
\boxed{
(y,K_1)=p+1,\qquad
(x,K_1)=\bigl(x,p^{e+1}-p-1\bigr).}
\tag{14}
\]

继续沿 \(y\) 的完整容量剥离真实到达根锚 \(h=p+1\)。根锚对侧容量满足

\[
\boxed{
D_1=(R_1-p-1,K_1)\mid p^2+p+1.}
\tag{15}
\]

由于 \(a=1\)，根锚对侧的新完整超额块仍含 \(p\)，所以 (15) 是新的
\(O(p^2)\) root box，不是 strict exit。

## 3. 两种 \(p\)-进高度必须区分

ordinary anchor 的 block 高度由 (10)--(12) 给出，为 \(e+1\)。根锚 departure
却满足

\[
R_1-(p+1)=pH_1,
\quad
\boxed{H_1=(p+1)F_1-1.}
\tag{16}
\]

所以根高度为

\[
\boxed{
\nu_p(R_1-p-1)=1+\nu_p(H_1),}
\tag{17}
\]

并不等于 \(e+1\)。特别地，哪怕 \(p\nmid F_1\)，仍可有 \(p\mid H_1\)。因此
“ordinary p-block 只剩一层”不能推出“根锚也只剥一层”。

## 4. 一个锚点局部实际 raw endpoint 的高度二控制

取

\[
p=97,\qquad r=66\,988\,440.
\tag{18}
\]

源图表为

\[
\begin{aligned}
b&=12\,995\,757\,359,& n&=1\,273\,584\,221\,181,\\
A&=30\,884\,417\,363\,639,& K&=2\,964\,904\,066\,909\,344,\\
R&=122\,264\,085\,233\,375.&&
\end{aligned}
\tag{19}
\]

从 canonical anchor 出发，六条实际 raw 边的标签为

\[
97,67,131,3,42101,2107984905029,
\tag{20}
\]

并到达 \(h=58\)。终点有

\[
R-58=331\cdot369\,377\,901\,007,
\tag{21}
\]

且完整 receipt 精确为

\[
Q=369\,377\,901\,007,\qquad \beta=331,\qquad (A,Q)=1,\qquad E_0=Q,
\tag{22}
\]

\[
E_0=1+97^2\cdot39\,257\,934.
\tag{23}
\]

由 (5) 得 target 参数

\[
r_1=24\,744\,049\,357\,009\,720\,314.
\tag{24}
\]

本例 \(F_1\equiv1\pmod {97}\)，所以 ordinary failure 只有一层 \(97\)；但是

\[
\nu_{97}(R_1-98)=2.
\tag{25}
\]

从根锚 \(98\) 剥尽这两层并继续实际容量剥离，可到达 \(h=3\)。其完整 receipt 为

\[
R_1-3=4Q_3,\qquad (A_1,Q_3)=1,\qquad Q_3\equiv48\pmod {97},
\tag{26}
\]

故下一 canonical capacity 是

\[
c=-48^{-1}\equiv2<96\pmod {97}.
\tag{27}
\]

式 (27) 仍只是通过整数 gates 的严格算术候选；只有来源连续性、target validation、
priority prefix、identity lift 与 E5 全部通过后，才成为合法 guarded macro。

## 5. 锚点局部实际 endpoint 生成的条件 target 任意根高度族

固定 \(p=97,h=58\)，并令

\[
r(k)=66\,988\,440+
4\,243\,815\,461\,730\,835\,674\,059\,638\,914\,706\,837\,844\,637k,
\quad k\ge0.
\tag{28}
\]

这个步长不是只冻结 endpoint 方程；它同时冻结一条从 canonical anchor 出发的真实
raw prefix。对每个 \(k\)，
依次使用

\[
97,67,131,3,42101
\tag{29}
\]

都是唯一选中、超出容量、gcd reduction 为 1 的合法 raw 边；五次超容量差依次为
\(1,1,1,2,1\)。五步后含 \(58\) 的一侧为

\[
58q(k),
\tag{30}
\]

其中

\[
q(k)=2\,107\,984\,905\,029+
133\,543\,920\,917\,590\,341\,086\,691\,816\,028\,640\,377\,650\,310\,464k.
\tag{31}
\]

逐线性行列式核对给出

\[
(q(k),K(k))=1.
\tag{32}
\]

所以不需要、也不能假设 \(q(k)\) 是素数。由于 \((q(k),K(k))=1\)，对它的每个实际
素因子 \(\ell\)，\(58q(k)\) 一侧的 \(\ell\)-容量都是零；按完整指数逐次使用
\(\ell\)-raw 除法时，primitive 性由 \((58q(k),R(k))=1\) 保持。故存在一条长度随
\(k\) 变化的非空 raw suffix，从 (30) 真正到达 \(h=58\)。这不是固定六步或有界证书。
endpoint 对侧精确为

\[
R(k)-58=331E(k),
\tag{33}
\]

\[
E(k)=369\,377\,901\,007+
23\,400\,629\,237\,489\,299\,674\,263\,740\,436\,419\,983\,401\,253\,504k.
\tag{34}
\]

同一组行列式余数给出

\[
(E(k),A(k))=(E(k),K(k))=1,\qquad E(k)\equiv1\pmod {97^2}.
\tag{35}
\]

又 \(58\cdot331\mid K(k)\)，故对每个 \(k\)，完整超额 receipt 都精确为

\[
Q=E(k),\qquad \beta=331,\qquad g_A=1,\qquad D=331.
\tag{36}
\]

因此，对任一已由独立 root policy 赋予 persistent lineage 的相应 chart，最小互素
素数源先到 canonical anchor，随后上述 prefix 与 capacity suffix 给出可实际重放的
anchor-to-endpoint analysis receipt；它不只是静态因子方程，也不反向制造 persistent
chart。这里的“实际”只修饰 raw 路径可逐边重放，不表示本族已经获得统一的 admitted
source lineage。

令 \(r_1(k)\) 为 (5) 的 target 参数，并定义

\[
H(k)=\frac{R_1(k)-98}{97}.
\tag{37}
\]

直接展开得到二次整数多项式

\[
\begin{aligned}
H(k)={}&
1\,868\,578\,428\,073\,766\,217\,858\,525\,191\,856\,689\,368\,432\,694\,029\,295\,254\,181\,783\,788\,414\,861\,243\,374\,903\,854\,993\,031\,168k^2\\
&+58\,990\,856\,239\,305\,572\,631\,703\,764\,704\,555\,659\,300\,682\,708\,034\,054\,096\,000k\\
&+465\,584\,032\,701\,494\,897\,428\,125.
\end{aligned}
\tag{37a}
\]

其模 97 化简为

\[
\boxed{H(k)\equiv27k\pmod {97}.}
\tag{38}
\]

并且 \(\nu_{97}(H(0))=1\)、\(H'(0)\equiv27\ne0\pmod {97}\)。Hensel 提升于是
给出：对每个 \(m\ge1\)，有唯一根类模 \(97^m\)；它的 97 个下一层 lift 中恰一个
继续为根，其余 96 个满足精确估值 \(m\)。每个这样的剩余类含无穷多个非负整数，故

\[
\boxed{
\text{对每个 }f\ge2，\text{有无穷多个 chart-local actual raw endpoint receipt 满足 }
\nu_{97}(R_1-98)=f.}
\tag{39}
\]

式 (39) 的 anchor-local endpoint path 是实际可重放的；\(H\) 控制的是 conditional target
图表在形式根 \(h=98\) 处的 departure，不声称该 target root 已被 selector 实际访问。
事实上 \(p=97\) 已有直接 Type II 终端
\[
\frac4{97}=\frac1{28}+\frac1{194}+\frac1{2716},
\tag{40}
\]
所以 terminal-first 会更早停止。即使暂时屏蔽这个全局终端，target checkpoint 是否
可入队仍取决于 typed validation 和 E1--E5。该族否定统一 normal-form 根高度势，但
不否定 selector 在 target 上发现 terminal 或其它严格动作。

这个族还能把高度与根容量饱和同时实现。一般 \(a=1\) 根容量公式在这里给出

\[
D_1=3\gcd(2r_1(k)+1,3169).
\tag{41}
\]

因此 target 根容量等于 \(N=97^2+97+1=9507\) 当且仅当

\[
2r_1(k)+1\equiv0\pmod {N/3}.
\tag{42}
\]

这里 \(N/3=3169\)，而左侧模 3169 为

\[
1264+1783k+1641k^2.
\tag{43}
\]

其两个根类为

\[
\boxed{k\equiv1224,1633\pmod {3169}.}
\tag{44}
\]

由于 \((3169,97)=1\)，可把 (44) 的任一饱和类与 (38) 的每个精确 Hensel 高度类
用 CRT 合并。故 (39) 可加强为

\[
\boxed{
\forall f\ge2，\text{存在无穷多个 chart-local actual raw endpoint receipts，使 conditional
target 同时满足 }
\nu_{97}(R_1-98)=f,\qquad D_1=9507.}
\tag{45}
\]

这说明“大高度”与“容量变小”之间不存在自动补偿；二者最坏情形可以同时出现。

## 6. 当前边界

本卡把 endpoint \(s=0\) 与 ordinary regeneration 最终 p-free failure 统一到同一个
\(a=1\) root interface：真实剥离后到 \(h=p+1\)，下一容量整除 \(p^2+p+1\)。
它同时证明根高度无统一上界，因而不能再把“控制 p-adic 层数”作为主证明目标。

剩余的正确问题是：在根盒的两侧完整容量、terminal-first 菜单与 admitted lineage
之间，证明至少一条严格/terminal 出口；或者构造一个在 rechart 下不可重置的全局势。

## 7. 聚焦回执

```bash
python3 reproductions/type_i_endpoint_s_zero_p_free_return.py --verify
python3 reproductions/type_i_endpoint_s_zero_actual_unbounded_height.py --verify
```

第一张回执重放固定 anchor-local actual raw path 与高度二控制；第二张核验
(28)--(45) 中的参数恒等式、
线性 gcd 证书、前五条固定 raw 边、饱和同余类与高度 2--6 的有限控制。任意
\(f\ge2\) 的无穷族由正文的 simple-root Hensel 与 CRT 论证承担；脚本不扫描素数、
分母、selector history 或历史结果。
