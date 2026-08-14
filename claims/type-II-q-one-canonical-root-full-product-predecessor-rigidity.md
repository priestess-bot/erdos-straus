---
kind: claim
claim_id: type-II-q-one-canonical-root-full-product-predecessor-rigidity
title: q=1 规范根的一步完整乘积前驱刚性
statement: >-
  令 p=24t+1 为核心素数，取 q=1 的规范 Type-I 根 r=t，记
  g=(p+1)/2、T=p^2t-g、A=gT 与 n=(4A+1)/p。任何以完整乘积
  quotient-fold 一步精确到达该根的 determinant source，都且只由一个
  d|A、1<=d<p 给出：M=A/d、K=M(p-d)、R=4M-n。每个此类 source 都是
  high-R overflow，且其 carrier M>B_p；d=1 只是同 determinant chart 的
  uncharged support rebase，d>1 才是不同 chart 的前驱。特别地 d=g 给出
  一个固定的 p-only 规范 pre-root：(M,d,R,K)=(T,g,p[2t(p-1)-1],T(p-1)/2)。
  节点 {C,R-C}、C=(p-1)/2 是 primitive 且 gcd(C,K)=C，故只要有独立的
  actual raw receipt 到达该节点，就能无歧义解码此 determinant source，并由
  full-product fold 严格支付 A_s=1 到 A 的外层秩。该算法身份、E2、E4 和 E5
  并不产生 E1 或 typed E3：目前没有全称的、target-independent raw-entry
  证明。更精确地，每个 inverse predecessor 都满足
  gcd(X,K_d)=gcd(X,d+3)<X，X=(p+3)/4；若 q=1 endpoint 为 G，则每个
  inverse predecessor 对完整 X source box 的 carrier loss X/gcd(X,K_d) 至少为 7，且该常数
  在 p=1033,d=330 达到；规范 root 自身与 X 互素，故第二腿把全部 X-carrier
  清零。因而 q=1 source 的完整带幂 carrier 不能在一步 bridge 中原样保留，甚至
  从完整 X box 出发的 partial transfer 也至少丢失一个大小不小于 7 的因子；个别素数层仍可能相交。故本卡
  不是全局 Type-I exit 或 verified edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-canonical-root-slice-support-disjointness
  - type-I-overflow-unbounded-full-product-quotient-fold
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-raw-universal-p-parent-root-policy-boundary
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - type-I
  - canonical-root
  - overflow
  - full-product
  - inverse-classification
  - determinant
  - root-entry
  - source-provenance
  - E1-E5
  - proof-boundary
sources:
  - claim: type-II-q-one-canonical-root-slice-support-disjointness
    role: canonical-q-one-root-data-and-strict-follow-up-carry
  - claim: type-I-overflow-unbounded-full-product-quotient-fold
    role: forward-full-product-fold-and-ranked-admission-contract
  - claim: type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
    role: d-equals-one-same-chart-boundary
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: raw-parent-does-not-create-E1-policy
  - reproduction: reproductions/type_ii_q_one_canonical_root_full_product_predecessor.py
    role: focused-inverse-classification-full-carrier-obstruction-and-pre-root-controls
visibility: public
last_checked: '2026-08-15'
---

# q=1 规范根的一步完整乘积前驱刚性

## 1. 问题与规范根

固定核心素数

\[
p=24t+1,
\qquad t\ge3.
\tag{1}
\]

q=1 Type II exit 的规范根取 \(r=t\)。沿用已有根切片的记号，令

\[
g=\frac{p+1}{2},
\qquad
T=p^2t-g,
\qquad
A=gT,
\tag{2}
\]

\[
n=\frac{4A+1}{p}=2pt(p+1)-p-2.
\tag{3}
\]

于是 root determinant 是

\[
pn=4A\cdot1+1,
\qquad
K_{\rm root}=A(p-1),
\qquad
R_{\rm root}=4A-n.
\tag{4}
\]

已有结果已给出该根后的 strict carry。这里不再寻找 root endpoint 的 raw word，而是
反向问一个严格限定的问题：哪一些 overflow determinant state 可以经一次完整乘积
fold 精确到达 (4)？

## 2. 逆分类是精确的

设一个合法的 full-product source 有 determinant 数据

\[
pn_s=4Md+1,
\qquad 1\le d<p,
\tag{5}
\]

并在完整乘积 \(S=Md\) 上应用既有 fold。其 target 为

\[
(M_T,d_T,n_T;A_T)=(S,1,n_s;S).
\tag{6}
\]

因此 target 恰为 (4) 当且仅当

\[
\boxed{n_s=n,\qquad Md=A.}
\tag{7}
\]

等价地，这些 source 与整数集合

\[
\boxed{d\mid A,\qquad 1\le d<p}
\tag{8}
\]

一一对应；给定一个 source 时，其 \(d\) 唯一，且该 source 为

\[
\boxed{
M_d=\frac{A}{d},
\qquad C_d=p-d,
\qquad K_d=M_dC_d,
\qquad R_d=4M_d-n.
}
\tag{9}
\]

反过来，任意 (8) 的 \(d\) 都满足

\[
pn=4M_dd+1,
\qquad
pR_d+1=4K_d,
\tag{10}
\]

并由 (6) 在算术上精确送到 root。故 (8)--(9) 不是一个候选菜单，而是所有一步
full-product bridge 的完整分类。

这个分类还立即分出一个容易混淆的退化情形。\(d=1\) 时

\[
(M_1,1,R_1,K_1)=(A,1,R_{\rm root},K_{\rm root}),
\tag{11}
\]

determinant chart 本身没有改变；若 source 的 charged support 是 \(1\)，它只是
同图表的 support rebase。只有 \(d>1\) 才给出不同的 pre-root chart，因为此时
\(M_d<A\) 从而 \(R_d<R_{\rm root}\)。

## 3. 所有一步前驱都是 high-carrier overflow

这些前驱不可能隐藏在低载体入口中。先注意

\[
T>p^2.
\tag{12}
\]

确实，\(t\ge3\) 且 \(g=(p+1)/2<2p^2\)。于是对所有 (8)，

\[
M_d=\frac{A}{d}>\frac{A}{p}
 =\frac{gT}{p}
 >\frac{p(p+1)}2
 >\frac{(p-1)^2}{4}=B_p.
\tag{13}
\]

同样，\(R_d\) 随 \(d\) 递减，所以只需检查 \(d=p-1\)：

\[
p(p-1)(R_{p-1}-p)
=4A-(p-1)(p^2+1)>0.
\tag{14}
\]

最后一个严格不等式由

\[
4A=4gT>2(p+1)p^2>(p-1)(p^2+1)
\tag{15}
\]

给出。因此每个 (9) 都有

\[
\boxed{R_d>p,\qquad M_d>B_p.}
\tag{16}
\]

这把一步 bridge 的形状压到一个明确边界：它若存在，必须是带低 charged support 的
**高 carrier overflow**，不能是当前 \(R<p\) 的默认 entry state，也不能把
\(M_d\) 本身当作 \(A\le B_p\) 的原有 bounded support。

## 4. 固定的 p-only 规范 pre-root

在分类 (8) 中，\(g\mid A\) 总成立。取

\[
d=g=\frac{p+1}{2},
\qquad
C=p-d=\frac{p-1}{2},
\qquad
b=2t(p-1)-1.
\tag{17}
\]

代入 (9) 得到一个完全由 \(p\) 预先决定的 source：

\[
\boxed{
M_g=T,
\qquad
R_g=pb,
\qquad
K_g=TC.
}
\tag{18}
\]

其关键恒等式为

\[
4T-pb=n,
\qquad
p(pb)+1=4TC,
\qquad
pn=4Tg+1.
\tag{19}
\]

因此这个 pre-root 的完整乘积正好是

\[
M_gd=Tg=A,
\tag{20}
\]

而 fold 后的 chart 为

\[
R_T=(p-1)n-1=4A-n=R_{\rm root},
\qquad
K_T=A(p-1)=K_{\rm root}.
\tag{21}
\]

它没有参数选择，也没有从某个 raw endpoint 反求 \(r\)：\(r=t\)、\(d=g\) 都是
q=1 exit 的固定 \(p\)-函数。

## 5. 一个可验证但尚未入队的 determinant seed

令

\[
P_g=\{C,R_g-C\}.
\tag{22}
\]

因为 \(p=2C+1\)、\(b=4tC-1\)，有

\[
R_g=pb\equiv-1\pmod C.
\tag{23}
\]

所以

\[
\boxed{(C,R_g-C)=1,\qquad (C,K_g)=C,\qquad K_g/C=T.}
\tag{24}
\]

换言之，任何已经验证的 raw receipt 若到达 (22)，其末端无需猜测即可解码出

\[
(M,d,n)=(T,g,n).
\tag{25}
\]

这是一个良好的 physical determinant seed；它不是“某个因子恰好相符”的静态观察。
不过，(24) 只证明 node 的 primitive/determinant 算术。它**不**证明一个已授权的
source tree 真能到达该 node。

## 6. q=1 完整 source carrier 不能穿过一步 bridge

上节的 \(d=g\) 选择与 \(X\) 互素，但其它 \(d\) 不能据此一概排除。所有
inverse predecessor 的精确交集其实是

\[
\begin{aligned}
(X,K_d)
&=\left(X,\frac{A}{d}(p-d)\right)\\
&=(X,p-d)\\
&=\boxed{(X,d+3)},
\end{aligned}
\tag{26}
\]

其中第二步使用已有 \((X,A)=1\)，第三步使用 \(p\equiv-3\pmod X\)。

我们现在证明完整带幂 carrier 不会原样穿过。若 \(X\mid K_d\)，则由 (26)
有 \(X\mid d+3\)。因为

\[
1\le d<p=4X-3,
\tag{27}
\]

只能写作

\[
d+3=mX,
\qquad m\in\{1,2,3\}.
\tag{28}
\]

三个情形都与 \(d\mid A\) 矛盾。

### \(m=3\)

此时 \(d=3X-3=18t\)。但

\[
p\equiv g\equiv1\pmod t,
\qquad T\equiv-1\pmod t,
\qquad A=gT\equiv-1\pmod t.
\tag{29}
\]

所以 \((t,A)=1\)，不可能有 \(18t\mid A\)。

### \(m=2\)

此时 \(d=2X-3=12t-1\)。它是奇数且

\[
(d,g)=(12t-1,12t+1)=1.
\tag{30}
\]

因此 \(d\mid A\) 会强制 \(d\mid T\)。但模 \(d\) 有 \(p\equiv3\)、
\(g\equiv2\)，从而

\[
4T\equiv4(9t-2)=36t-8\equiv-5\pmod d.
\tag{31}
\]

这会给出 \(d\mid5\)，而 \(d=12t-1\ge35\)，矛盾。

### \(m=1\)

令 \(d=X-3=6t-2=2e\)，其中 \(e=3t-1\)。此时

\[
p\equiv9,\qquad g\equiv5,\qquad T\equiv e+22\pmod {2e},
\]

故

\[
A=gT\equiv5e+110\pmod {2e}.
\tag{32}
\]

若 \(2e\mid A\)，则 \(e\mid110\)，且 \(110/e\) 必为奇数。因此

\[
e\in\{2,10,22,110\}.
\tag{33}
\]

再与 \(e=3t-1\) 合并，只剩 \((t,e)=(1,2)\) 或 \((37,110)\)，对应
\(p=25\) 或 \(889=7\cdot127\)，都不是核心素数。

所以对每个核心素数和每个 (8) 的 inverse predecessor，

\[
\boxed{(X,K_d)<X.}
\tag{34}
\]

### 6.1 G source 的定量最小损失

现在额外假设 q=1 endpoint 是 G。于是 \(X\) 的每个素因子都满足

\[
\ell\equiv1\pmod3,
\qquad \ell\mid X,
\tag{35}
\]

故它们全都至少为 \(7\)。对任一 inverse predecessor 定义其保留 carrier 与缺失倍率

\[
H_d=(X,K_d)=(X,d+3),
\qquad
\mathcal L_X(d)=\frac{X}{H_d}.
\tag{36}
\]

式 (34) 说明 \(H_d\) 是 \(X\) 的真因子。因此 \(\mathcal L_X(d)>1\)，而且
\(\mathcal L_X(d)\) 的每个素因子仍来自 \(X\)。于是有统一且 sharp 的容量界

\[
\boxed{\mathcal L_X(d)\ge7.}
\tag{37}
\]

逐素数幂地，若 \(\ell^e\Vert X\)，则 \(\ell\nmid A\)，从而

\[
v_\ell(K_d)=v_\ell(p-d),
\qquad
\min\{e,v_\ell(K_d)\}=\min\{e,v_\ell(d+3)\},
\tag{38}
\]

其中使用 \(p\equiv-3\pmod{\ell^e}\)。所以 (37) 等价于 source 的指数缺口

\[
\sum_{\ell\mid X}
\bigl(e-\min\{e,v_\ell(K_d)\}\bigr)\log\ell
=\log\mathcal L_X(d)\ge\log7.
\tag{39}
\]

这不是仅说“至少少一层”：任何以完整 \(X\) source box 为输入、并在 \(K_d\) 的物理
carrier 账本上登记其保留部分的一步 adapter，都至少要消去一个乘法大小不小于 \(7\)
的 block。界是 sharp 的。取

\[
p=1033,\qquad X=259=7\cdot37,\qquad d=330\mid A,
\tag{40}
\]

则 \(d+3=333=9\cdot37\)，故

\[
H_{330}=37,
\qquad
\mathcal L_X(330)=7.
\tag{41}
\]

另一方面，fold 的 root target 满足既有 \((X,K_{\rm root})=1\)。因此这条完整
two-leg bridge 的第二腿将所有尚存的 \(X\)-carrier 清零：partial overlap 只能是
pre-root 的瞬时容量，不能作为到 root 的 support-preserving payload。

这个结论不排除某个新 adapter 预先只声明 \(H_d\) 的子盒为其来源 universe；但那已经
不是完整 \(X\) box 的保留，而是需要独立 E1 receipt 的 genuine source-switch，不能沿用
原 Type II endpoint 的完整 provenance。

### 6.2 provenance 的边界

这正好扩展了 root 本身的互素障碍，但它是一个**带幂 carrier**结论，不能被夸大为
所有单素数层都互素。更具体地，q=1 Type II endpoint 的真实 source box 以

\[
X=\prod_{\ell\mid X}\ell^{e_\ell}
\]

作为逐素数的指数预算。任何试图把这个**完整** source factorization 原样保留到
\(K_d\) 的 E1 adapter 都必须满足

\[
e_\ell\le v_\ell(K_d)\quad(\ell\mid X),
\]

这等价于 \(X\mid K_d\)，已被 (34) 排除。因此一步 bridge 不存在完整 q=1 source
box 的 identity-on-factorization transfer；任何 partial overlap 都必须明确丢弃或
source-switch 至少一个 \(q\)-进层，并重新支付 provenance，而不能沿用旧 E1。

例如 q=1 G 的局部控制

\[
p=673,
\qquad X=169=13^2,
\qquad d=75\mid A
\tag{42}
\]

给出

\[
(X,K_{75})=(169,78)=13,
\qquad v_{13}(K_{75})=1<v_{13}(X)=2.
\tag{43}
\]

故一个 \(13\)-层仍相交，而完整 \(13^2\) source carrier 不可保留。这个例子不是
E1 bridge，也未通过 terminal-first；它只是说明后续工作必须以逐素数、逐幂容量处理
partial overlap，不能把 (34) 错读为全面 source-disjointness。

## 7. 条件性的严格付款与精确剩余

若将来有一个独立、terminal-first 的 fresh entry 创建 (18)，且其 charged support 是
\(A_s=1\)，则完整乘积 fold 有

\[
\Lambda_p^\sharp:
\left(B_p,K_g\right)
\longmapsto
\left(0,p-1\right),
\tag{44}
\]

第一坐标严格下降。式 (19)--(21) 支付 E2；解集采用图表无关的
\(\operatorname{Sol}(4,p)\) 恒等 map 时支付 E4；(44) 支付 E5。fold 后根的既有
strict carry 还可继续把 \((0,p-1)\) 降到 \((0,c)\)。

但这里尚缺的不是一个算术因子，而是完整的 E1/E3 准入：

1. 一个在选择目标前就声明的 `fresh_source_tree_only` high-carrier entry；
2. 从该 entry 到 (22) 的 actual ordered raw transcript，或另一条同样独立的
   physical provenance；
3. entry 与 root target 的 terminal-first、F/G/hit、normal form 和内容地址重算；
4. 将 (44) 与 Type II exit phase 合并到不可 reset 的全局势。

任意 primitive node 都可反向补造 formal \(p\)-parent 的事实不能代替第 1--2 项。
因此本卡的可复用成果是：所有一步 determinant bridge 已被分类，并且一个固定的
q=1 pre-root 已被缩为 (18)、(22) 这一条明确的 high-carrier entry 问题；(34) 又排除
了完整 q=1 carrier 的一步原样转移，但保留了逐层 overlap 的较窄问题；它没有声称
该 entry 已经存在，更没有证明 Erdős--Straus 猜想。

## Focused reproduction

```bash
python3 reproductions/type_ii_q_one_canonical_root_full_product_predecessor.py --verify
```

验证器只重放六个固定核心素数、每个根 support 的全部 \(d<p\) 因子、规范
\(d=g\) seed 恒等式，以及 \(p=673\) 的 partial-overlap 与 \(p=1033\) 的 sharp
source-loss 控制；不做素数范围、
分母范围或 raw-reach 搜索。
