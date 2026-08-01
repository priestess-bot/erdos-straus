---
kind: claim
claim_id: type-I-universal-p-source-capacity-anchor-orbit
title: 通用 p 源、容量锚点轨道与周期对偶证书
statement: 对每个合法核心图表 p=1 (mod 24)、4K=pR+1、3<=R<=p-2，三元组 (p,R(p-1)-p,p-1) 是一个位长 O(log p) 的规范形式源；其唯一 p-边以 t=1、无 gcd 约分一步到达 (1,R-1,1)。因此裸 G 不再存在 source 缺口：若 R-1|K 则 anchor 直接给 Type I，否则 anchor 的完整超额块给出 path-anchored bundle，并严格进入 marked absorb 或 overflow。更一般地，任一 primitive bottom side u 可沿真实 raw 边、与顺序无关地剥离到 gcd(u,K)。由此得到有限确定轨道 h_0=1、h_{i+1}=gcd(R-h_i,K)；每一步满足 R-h_i=e_i h_{i+1}、h_i h_{i+1}|K、(h_i,h_{i+1})=1，周期上有 product e_i=(-1)^ell (mod R)。G 分离角色在每条周期边上读取 chi(e_i)=chi(-1)，但该周期证书本身不保证终端或下降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-ranked-pruning-and-external-gap-selector
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-marked-support-accumulation-rechart-saturation
topics:
  - type-I
  - formal-source
  - universal-source
  - G-state
  - complete-excess-bundle
  - q-adic-capacity
  - capacity-anchor
  - finite-orbit
  - lattice-certificate
  - Fourier-character
  - proof-boundary
sources:
  - claim: type-I-formal-ranked-pruning-and-external-gap-selector
    role: raw-formal-transition-definition
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: path-anchored-bundle-and-marked-overflow-dichotomy
  - claim: type-I-marked-support-accumulation-rechart-saturation
    role: absorbed-support-state-and-potential
visibility: public
last_checked: '2026-08-01'
---

# 通用 \(p\) 源、容量锚点轨道与周期对偶证书

## 1. 设置

固定

\[
p\equiv1\pmod {24},
\qquad
4K=pR+1,
\qquad
3\le R\le p-2,
\tag{1}
\]

其中 \(p\) 为素数。形式源是正整数三元组

\[
U+V=Rm,
\qquad
(U,V)=1.
\tag{2}
\]

若 \(q\mid U\)、\(v_q(U)>v_q(K)\)，raw 迁移选择唯一的
\(1\le t\le q\) 使 \(q\mid m+t\)，并把三元组变为

\[
\left(\frac Uq,\frac{V+Rt}{q},\frac{m+t}{q}\right),
\tag{3}
\]

随后只做实际 gcd 约分。本卡使用完整 raw 定义，不附加“\(q\mid K\)”或“源必须来自
目标纤维”的隐藏限制。

## 2. 每个核心图表都有一个规范实际源

定义

\[
\boxed{
(U,V,m)=\bigl(p,\ R(p-1)-p,\ p-1\bigr).
}
\tag{4}
\]

由 \(R\ge3\)、\(p\ge73\) 得 \(V>0\)，并且

\[
U+V=R(p-1)=Rm.
\tag{5}
\]

又因 \(p\nmid R\)，

\[
(U,V)=(p,R(p-1)-p)=(p,R)=1.
\tag{6}
\]

式 (1) 给出 \(4K\equiv1\pmod p\)，所以 \(p\nmid K\)。于是 \(q=p\) 是 (3) 的
合法超容量边。由 \(m=p-1\)，唯一 shift 为 \(t=1\)，且

\[
\left(
\frac Up,
\frac{V+R}{p},
\frac{m+1}{p}
\right)
=
(1,R-1,1).
\tag{7}
\]

两坐标互素，故 gcd reduction 等于 \(1\)。公式 (4) 只含 \(O(\log p)\) 位整数，定义
`universal_p_source_v1`；(4)--(7) 是它的完整 verifier。

这一步只提供 source/path provenance，不是递归状态边，也不要求势下降。

## 3. anchor 的规范三分

在节点 \(\{1,R-1\}\) 上，若

\[
R-1\mid K,
\tag{8}
\]

则 \(1\cdot(R-1)\mid K\)，已有 sink 正规形直接恢复原 \(p\) 的 Type I 证书。
否则写

\[
R-1=Q\beta,
\qquad
Q=\prod_{v_q(R-1)>v_q(K)}q^{v_q(R-1)}.
\tag{9}
\]

逐素数立刻得到

\[
Q>1,
\qquad
\beta\mid K,
\qquad
(Q,\beta)=1,
\qquad
Q\nmid K,
\qquad
Q<R<p.
\tag{10}
\]

因此 (7) 与 (9) 是一个完整 `path_anchored` receipt。对当前 charged support
\(A\mid K\)，令

\[
M=\operatorname{lcm}(A,Q).
\tag{11}
\]

现有 complete-excess 定理将它严格分成

\[
R_M<p
\Longrightarrow
\text{identity-lift marked absorb},
\tag{12}
\]

\[
R_M>p
\Longrightarrow
\text{bundle overflow}.
\tag{13}
\]

所以所有 F、G 和 hit 图表都有同一个实际 source 接口。特别地，旧的“裸 G 没有
\(K\)-支撑形式源”只是一个对更窄源类的观察，不再是完整形式 Reach 的余项。

## 4. 容量剥离定理

更一般地，设 \(\{u,R-u\}\) 是一条已验证路径上的 bottom 节点，且

\[
(u,R)=1.
\tag{14}
\]

对每个满足 \(v_q(u)>v_q(K)\) 的素数，沿 raw 边把所选侧除以 \(q\)，恰好重复
\(v_q(u)-v_q(K)\) 次。每一步仍有

\[
\left(\frac{u'}q,R-\frac{u'}q\right)=1,
\tag{15}
\]

所以不会发生额外 gcd 约分。不同素数的除法可交换，终点与顺序无关，并且

\[
\boxed{
\{u,R-u\}
\leadsto
\{(u,K),R-(u,K)\}.
}
\tag{16}
\]

式 (16) 是实际 raw 路径，不是静态因子替换。它把任意一侧精确压到当前 \(K\) 能承担
的最大容量。

## 5. 确定容量锚点轨道

定义

\[
h_0=1,
\qquad
h_{i+1}=(R-h_i,K).
\tag{17}
\]

若 \(R-h_i\mid K\)，则 \(h_i(R-h_i)\mid K\)，直接 Type I。否则把该侧完整分解为

\[
R-h_i=Q_i\beta_i
\tag{18}
\]

并令

\[
G_i=(Q_i,K),
\qquad
e_i=Q_i/G_i.
\tag{19}
\]

由于 \(Q_i\) 取 offending 素数的完整幂块，

\[
h_{i+1}=\beta_iG_i,
\qquad
R-h_i=e_i h_{i+1}.
\tag{20}
\]

归纳地 \(h_i\mid K\)，且

\[
(h_i,h_{i+1})\mid(h_i,R-h_i)=1.
\tag{21}
\]

故

\[
\boxed{
h_i h_{i+1}\mid K,
\qquad
(h_i,h_{i+1})=1.
}
\tag{22}
\]

所有 \(h_i\) 都是 \(K\) 的因子，因此 (17) 在至多 \(\tau(K)+1\) 个 macro step 后终端
或进入周期。这给出规范、有限、与路径 tie-break 无关的容量状态压缩。

## 6. 周期的格与 Fourier 证书

若 (17) 有长度 \(\ell\) 的周期，式 (20) 在 \((\mathbb Z/R\mathbb Z)^\times\) 中给出

\[
e_i h_{i+1}\equiv-h_i\pmod R.
\tag{23}
\]

沿周期相乘并约去全部 \(h_i\)，得到

\[
\boxed{
\prod_{i=0}^{\ell-1}e_i\equiv(-1)^\ell\pmod R.
}
\tag{24}
\]

若 \(\chi\) 是在 \(K\) 支撑上平凡的 G 分离角色，则 \(\chi(h_i)=1\)，由 (23)
逐边得到

\[
\boxed{\chi(e_i)=\chi(-1).}
\tag{25}
\]

因此缺失的 G 相位精确落在外部容量商 \(e_i\) 上。(24) 是加法/格证书，(25) 是它的
Fourier 对偶读法；二者都不自动提供 marked absorb 或严格下降。

## 7. 周期不是良基势

聚焦状态

\[
(p,R,K;A)=(409,251,25665;5)
\tag{26}
\]

的轨道为

\[
1\longmapsto5\longmapsto3\longmapsto1.
\tag{27}
\]

三步 bundle 分别给出

\[
(Q,M,R_M)=(250,250,511),(82,410,1231),(248,1240,1431),
\tag{28}
\]

全部 overflow，且

\[
50\cdot82\cdot248\equiv-1\pmod {251}.
\tag{29}
\]

所以容量锚点轨道完成了规范压缩和对偶定位，却不能单独作为递降证明。下一步必须使用
overflow-derived support、同一 Reach 的 alternate receipt，或有独立外层秩支付的换相位边。

## 8. 聚焦复现

~~~bash
python3 reproductions/type_i_universal_anchor_overflow_dual.py --verify
~~~

结果文件为
`reproductions/type-i-universal-anchor-overflow-dual-results.json`。对应 SHA-256 为

~~~text
94fb9625361e8184ee6cb6991aef03d8d806f623a1e8123952e8c8ff2f667e21  reproductions/type_i_universal_anchor_overflow_dual.py
1fceb021f77ea88ac391b09cee9aafe0eee9348d98b75779c94b0ec45d71d025  reproductions/type-i-universal-anchor-overflow-dual-results.json
~~~

脚本只验证通用源公式、容量剥离、一个三周期和少量 overflow receipt；不重跑历史普查。
全称结论由第 2--6 节的整数证明承担。
