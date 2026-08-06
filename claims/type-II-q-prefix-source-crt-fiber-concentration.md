---
kind: claim
claim_id: type-II-q-prefix-source-crt-fiber-concentration
title: Type II q 层请求的来源 CRT 纤维集中与唯一候选
statement: 对一组已经选定来源标签和 q 层高度的请求，任何共同候选纤维 s=AD_* 都满足 s≡Da_i (mod q_i^{h_i}) 的统一同余。广义 CRT 将这些请求压缩为一个模 Q 的来源剩余类；若 Q>D^2，则 admissible 除子格 s≤D^2 至多有一个候选。候选存在时所有请求集中到同一参数纤维并可调用 q 层前缀—Kneser 价格引理；候选为空时输出精确的 CRT/范围纤维障碍，不能把跨纤维请求直接合并。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-source-fiber-shared-q-ledger
  - type-II-cross-state-source-demand-hall-capacity-bridge
topics:
- type-II
- q-adic
- source-CRT
- fiber-concentration
- parameter-fiber
- Hall
- capacity
- source-switch
- arithmetic-obstruction
- proof-program
sources:
  - claim: type-II-q-layer-prefix-kneser-price-certificate
    role: prefix-to-fiber-price
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: admissible-divisor-lattice
  - claim: type-II-source-fiber-shared-q-ledger
    role: repeated-q-source-contract
visibility: public
last_checked: '2026-08-05'
---

# Type II q 层请求的来源 CRT 纤维集中与唯一候选

## 1. 请求来源和共同候选

固定核心素数 \(p\)、原始 \(D\)，以及一组已经选定的 q 层请求
\[
\mathcal R=\{r_1,\ldots,r_m\}.
\tag{1}
\]
每个请求 \(r\) 保存一个具体来源标签 \(a_r\)、来源整数
\[
b_r=Da_r,
\tag{2}
\]
一个奇素数 \(q_r\nmid 4D\)，以及需要的连续高度 \(h_r\ge1\)，并满足原始来源整除
\[
q_r^{h_r}\mid p+4b_r.
\tag{3}
\]
如果一个请求有多个候选来源标签，先对每个有限标签选择分别运行本引理；不能在
未选标签时把不同来源的同余类静默合并。

一个共同的 admissible 候选纤维是
\[
f=(D_*,A),\qquad
s_f=AD_*,
\qquad
A\mid D_*,\quad D_*/A\text{ 平方自由},\quad D_*\mid D,\quad 4s_f<p.
\tag{4}
\]
若 \(r\) 在该纤维上有合法 q-prefix 边，则
\[
q_r^{h_r}\mid p+4s_f.
\tag{5}
\]
由 (3)、(5) 和 \(q_r\nmid4\)，必有
\[
\boxed{
s_f\equiv b_r\pmod {q_r^{h_r}}
\qquad(r\in\mathcal R).
}
\tag{6}
\]
因此，来源同余是共同纤维存在的必要条件，不是事后筛选。

## 2. 广义 CRT 压缩

令
\[
Q=\operatorname{lcm}_{r\in\mathcal R}q_r^{h_r}.
\tag{7}
\]
对同一 q 的请求对 \(r,r'\)，CRT 兼容条件为
\[
b_r\equiv b_{r'}\pmod {q^{\min(h_r,h_{r'})}}.
\tag{8}
\]
由于不同奇素数幂互素，(8) 对所有同 q 请求成立，当且仅当存在一个唯一剩余类
\[
s\equiv \rho_{\mathcal R}\pmod Q
\tag{9}
\]
满足全部 (6)。若 (8) 失败，输出最小二元见证
\[
\mathrm{Q\_PREFIX\_SOURCE\_CRT\_INCONSISTENT}
=(r,r',q,b_r,b_{r'},\min(h_r,h_{r'})).
\tag{10}
\]
此时这组请求不可能由同一候选纤维承载，也不能将其价格放入一个 Kneser 积集。

若 (8) 通过，候选纤维的完整有限列表为
\[
\mathscr F_{\mathcal R}(p,D)
=
\left\{
(D_*,A):
\begin{array}{l}
D_*\mid D,\quad A\mid D_*,\quad D_*/A\text{ 平方自由},\\
AD_*\equiv\rho_{\mathcal R}\pmod Q,\quad 4AD_*<p
\end{array}
\right\}.
\tag{11}
\]
对每个列表元素，还要继续检查 source-switch、SNF、shared-q 和 \(B'>A\) 门；
(11) 只解决共同整数坐标，不替代这些合法性条件。

## 3. 唯一候选和纤维集中

由 \(A\le D_*\le D\)，有
\[
1\le s_f=AD_*\le D^2.
\tag{12}
\]
所以若
\[
\boxed{Q>D^2,}
\tag{13}
\]
同一剩余类 (9) 在区间 \([1,D^2]\) 中至多包含一个整数。由于每个 admissible
\(s=AD_*\) 有唯一的平方自由分解
\[
s=A^2c,\qquad c=D_*/A\text{ 平方自由},\qquad D_*=Ac,
\tag{14}
\]
有：

\[
\boxed{
|\mathscr F_{\mathcal R}(p,D)|\le1
\quad\text{当 }Q>D^2.
}
\tag{15}
\]

若列表含有唯一元素 \(f\)，则所有请求在同一 \(H_f\)、同一参数合同和同一
source-switch 纤维内；此时调用
[Type II q 层前缀匹配到纤维 Kneser 价格的规范压缩](type-II-q-layer-prefix-kneser-price-certificate.md)，
把 q 请求压缩为幂块并进入 Kneser 价格账本。

若列表为空，输出
\[
\mathrm{Q\_PREFIX\_SOURCE\_FIBER\_EMPTY}
=(\mathcal R,Q,\rho_{\mathcal R},\mathscr F_{\mathcal R},
\text{range/CRT/source failure ledger}).
\tag{16}
\]
这是一条该请求族不能集中到共同 admissible 纤维的算术负证书；它不声称原核心
素数没有另一组来源或另一条 Type I/II 路径。

当 \(Q\le D^2\) 时，(11) 仍是有限候选列表；对每个候选单独计算 q-prefix matching
和 Kneser 价格。不同候选之间不能相加，若所有候选均未命中，保留逐候选的
\(\mathrm{Q\_PREFIX\_PRICE\_FRAGMENTED}\) 表。

## 4. 与 q 层价格的精确接线

若 \((D_*,A)\in\mathscr F_{\mathcal R}\)，则 (6) 给出
\[
q_r^{h_r}\mid p+4AD_*,
\qquad
q_r^{h_r}\mid AD_*-Da_r.
\tag{17}
\]
因此每个请求的高度满足共同纤维的 q-prefix 整数门；但同一个 q 的多个请求仍需
执行共同 q ledger，不能由 (17) 自动产生多个独立块。令 \(R_{f,q}\) 为该纤维
选定的同 q 请求族，按高度排序。若
\[
h_{(k)}\ge k\quad(1\le k\le |R_{f,q}|),
\tag{18}
\]
则前缀引理给出一个高度 \(|R_{f,q}|\) 的真实幂块；其价格为
\[
\min\left(
|R_{f,q}|,
\operatorname{ord}_{H_f/T_f}(qT_f)-1
\right).
\tag{19}
\]
若 (18) 失败，输出第一个 \(h_{(k)}<k\) 的
\(\mathrm{Q\_PREFIX\_MATCHING\_DEFICIT}\)，不把 CRT 兼容误报为容量成功。

## 5. 构造性边界

### 5.1 \(p=97\) 的混合请求为空

取 \(D=6\)，来源
\[
(b_1,q_1,h_1)=(6,11,1),\qquad
(b_2,q_2,h_2)=(18,13,1).
\]
则
\[
Q=11\cdot13=143>D^2=36.
\]
CRT 方程 \(s\equiv6\pmod{11}\)、\(s\equiv18\pmod{13}\) 的剩余类在
\([1,36]\) 中没有元素，因此
\(\mathscr F_{\mathcal R}(97,6)=\varnothing\)。这正是把
\(11\cdot13\equiv-1\pmod{24}\) 误当作同一纤维命中的算术边界；回执为
\(\mathrm{Q\_PREFIX\_SOURCE\_FIBER\_EMPTY}\)。

### 5.2 \(p=5113\) 的唯一降模纤维

取 \(D=6\)，来源
\[
(b_1,q_1,h_1)=(18,17,1),\qquad
(b_2,q_2,h_2)=(36,7,1).
\]
此时
\[
Q=119>D^2=36,\qquad
18\equiv1\pmod{17},\qquad
36\equiv1\pmod7.
\]
唯一候选是 \(s=1\)，分解为 \(A=1,D_*=1\)。两个请求集中到同一
\(U(4)\) 纤维，并由 \(17\equiv1\)、\(7\equiv-1\pmod4\) 的 q 块直接给出
\(-1\) 命中；这与已有 \(p=5113\) 的 Type II 降模证书一致。

### 5.3 同 q 不相容

若两个请求使用同一个 q、相同高度 \(h=2\)，但来源标签满足
\(b_1\not\equiv b_2\pmod{q^2}\)，则 (8) 失败。即使它们分别在不同候选纤维上
各有合法边，也不能把两个 \(q^2\) 层拼成一个共同 q-prefix；回执是
\(\mathrm{Q\_PREFIX\_SOURCE\_CRT\_INCONSISTENT}\)，而非 Kneser surplus。

## 6. 证明

由 \(q_r^{h_r}\mid p+4b_r\) 和共同纤维中的 (5)，相减得到
\(q_r^{h_r}\mid4(s_f-b_r)\)，再用 \(q_r\nmid4\) 得 (6)。广义 CRT 的标准判据
给出 (8)--(9)；不同 q 的模数互素，所以没有其它相容条件。候选的范围和
平方自由分解给出 (12)--(15)，唯一性由 \(s=A^2c\) 的分解得到。

若候选存在，(17) 说明 q 层确实是同一纤维的整数前缀；再应用前缀匹配等价和
幂块 Kneser 价格公式得到 (18)--(19)。若候选为空或 CRT 不相容，所有共同纤维
均被排除；若 \(Q\le D^2\)，逐个枚举有限列表即可避免跨候选重复收费。证毕。

## 研究边界

本引理把跨纤维碎片化推进为一个有限来源合同问题：大模数 \(Q>D^2\) 时，选定请求
要么集中到唯一纤维，要么给出 CRT/范围空集；小模数时也只剩有限候选列表。它仍不
证明每个 Hall 请求都能预先选出一组共同来源标签，也不保证候选纤维的前缀匹配或
Kneser 阈值通过。下一步应把请求标签选择与该 CRT 集中引理组合，形成
\(\mathrm{Q\_PREFIX\_SOURCE\_FIBER\_EMPTY}\) 到 Type I/F/G 或稳定子塔的正式闭包。
