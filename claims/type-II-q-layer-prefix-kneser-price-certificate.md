---
kind: claim
claim_id: type-II-q-layer-prefix-kneser-price-certificate
title: Type II q 层前缀匹配到纤维 Kneser 价格的规范压缩
statement: 在固定候选参数纤维和固定 q 残数方向中，若每个请求的合法 q 层邻域都是前缀 {1,...,h_r}，则任意 Hall 匹配可规范化为按高度排序的前缀匹配。n 个匹配请求因此恰由一个高度 n 的真实 q 幂块承载，而不是 n 个重复 q 槽；其最终稳定子价格为 min(n,ord(qT)-1)。若 n+1 达到最终商阶则该方向已被最终稳定子吸收；只有在插入时稳定子上才输出 q^ord∈T 的 Q_PREFIX_ORDER_FOLD 回执。若不同纤维的前缀价格无法集中到同一目标群，则输出带逐纤维价格表的碎片化证书，不能把跨纤维请求直接相加。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-qheight-kneser-bridge
  - type-II-source-fiber-shared-q-ledger
  - type-II-cross-state-source-demand-hall-capacity-bridge
  - type-II-multiblock-kneser-active-capacity-dichotomy
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-final-stabilizer-q-fold-collapse
topics:
- type-II
- q-adic
- prefix-matching
- Hall
- Kneser
- source-fiber
- shared-q
- finite-order
- cross-fiber
- capacity
- proof-program
sources:
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: exact-q-height-to-block
  - claim: type-II-source-fiber-shared-q-ledger
    role: repeated-q-prefix-capacity
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: typed-request-graph
visibility: public
last_checked: '2026-08-05'
---

# Type II q 层前缀匹配到纤维 Kneser 价格的规范压缩

## 1. 固定纤维和前缀请求

固定核心素数 \(p\)、原始 \(D\)，以及一个候选参数纤维
\[
f=(D_*,A),\qquad s_f=AD_*,
\qquad A\mid D_*,\quad D_*/A\text{ 平方自由},\quad 4s_f<p.
\tag{1}
\]

令
\[
H_f\le U(4D_*),\qquad u_q=q\bmod 4D_*,
\tag{2}
\]
并要求
\[
q\nmid 4D_*.
\tag{3}
\]

同一个原始 q 的来源标签 \(b_i=Da_i\) 满足
\(q^{e_i}\mid p+4b_i\)。经过共同 q 账本后，纤维可用的最大连续深度记为
\[
d_f(q)=
\min\left(
  \sum_{i:q_i=q}\min(e_i,v_q(s_f-b_i)),
  v_q(p+4s_f)
\right).
\tag{4}
\]
若源边还带有额外的 CRT、SNF、范围或 \(B'>A\) 条件，它们必须在进入本引理前
通过；(4) 只表示整数 q 层的上界，不替代这些门。

一个请求 \(r\) 在 \((f,q)\) 上若有一个整数
\[
1\le h_r\le d_f(q)
\tag{5}
\]
并且其所有层
\[
\mathcal I_r(f,q)=\{1,\ldots,h_r\}
\tag{6}
\]
都通过同纤维 source-switch 和 shared-q 账本，则称 \(r\) 有 **Q-PREFIX** 边。
这里禁止把 \(\{j\}\) 的孤立高层标签当作前缀边；缺少低层来源时必须记录
\(\mathrm{Q\_PREFIX\_EDGE\_OBSTRUCTED}\)。

## 2. 前缀 Hall 规范化

设 \(R\) 是选择使用同一 \((f,q)\) 的请求族，\(|R|=n\)，每个请求带阈值
\(h_r\) 并有前缀邻域 (6)。将阈值升序排列为
\[
h_{(1)}\le h_{(2)}\le\cdots\le h_{(n)}.
\tag{7}
\]

则下列条件等价：

\[
\boxed{
\begin{array}{c}
\text{存在把 }R\text{ 匹配到不同 q 层的合法匹配};\\[1mm]
h_{(k)}\ge k\quad(1\le k\le n);\\[1mm]
\text{存在规范匹配 }r_{(k)}\longmapsto k,
\text{ 其使用层为 }\{1,\ldots,n\}.
\end{array}}
\tag{8}
\]

### 证明

对任意 \(k\)，取阈值最小的 \(k\) 个请求。它们的联合前缀邻域至多为
\(\{1,\ldots,h_{(k)}\}\)，所以 Hall 必要性给出 \(h_{(k)}\ge k\)。反之，按
(7) 的顺序把第 \(k\) 个请求分配到层 \(k\)，由 \(k\le h_{(k)}\) 可知每条边
合法，得到规范匹配。证毕。

因此，任意前缀匹配的 \(n\) 个请求都可以压缩为一个连续 q 幂块
\[
B_{f,q}(n)=\{1,u_q,u_q^2,\ldots,u_q^n\}\subseteq H_f.
\tag{9}
\]
它不是 \(n\) 个相同 q 的独立块；同一个 q 方向只出现一次，源层的总深度恰为
\(n\)。由 \(n\le d_f(q)\) 和 (4)--(5) 有
\[
q^n\mid p+4s_f,
\tag{10}
\]
所以 (9) 的每个指数都有真实整数整除回译。

## 3. Kneser 价格和有限阶折叠

本节的最终价格应按当前稳定子商中的实际陪集数计费。统一的递归账本是
[Type II 稳定子塔的加权价格与逐层缺陷守恒](type-II-stabilizer-tower-weighted-defect-conservation.md)；
下述 q 前缀公式正是其 \(\kappa=|BT/T|-1\) 特例。

把 (9) 与该纤维的其它已经通过回译的源块相乘，记完整积集为 \(P_f\)，最终稳定子为
\[
T_f=\operatorname{Stab}_{H_f}(P_f),
\qquad
o_{f,q}=\operatorname{ord}_{H_f/T_f}(u_qT_f).
\tag{11}
\]

q 前缀族的精确活跃价格为
\[
\boxed{
\kappa_{f,q}(R)
=|B_{f,q}(n)T_f/T_f|-1
=\min(n,o_{f,q}-1).
}
\tag{12}
\]

由[Type II 最终稳定子下 q 幂折叠的吸收塌缩](type-II-final-stabilizer-q-fold-collapse.md)，
这里的 \(T_f\) 是完整积集的最终稳定子；若 \(n+1\ge o_{f,q}\)，必有
\(o_{f,q}=1\)。因此最终账本中的非平凡商阶只能满足
\(n+1<o_{f,q}\)，不能把中间插入稳定子的阶数直接代入最终价格。

最终稳定子下有两个互斥分支：

1. **Q\_PREFIX\_FULL\_PRICE**：若 \(o_{f,q}>1\)（等价于
   \(n+1<o_{f,q}\)），则
   \(\kappa_{f,q}(R)=n\)。匹配的每一层都支付一个新的商陪集，且这 \(n\) 个请求
   可作为一个真实幂块的 Kneser 价格进入目标纤维账本；
2. **Q\_PREFIX\_FINAL\_STABILIZER\_ABSORBED**：若
   \(n+1\ge o_{f,q}\)，则折叠塌缩给出 \(o_{f,q}=1\) 和
   \(\kappa_{f,q}(R)=0\)。该 q 方向已经被最终稳定子吸收，不产生最终价格。

若同样的请求是在中间稳定子 \(T^{\mathrm{ins}}_f\) 上处理，折叠条件应写成
\(n+1\ge\operatorname{ord}_{H_f/T^{\mathrm{ins}}_f}(u_qT^{\mathrm{ins}}_f)\)；
此时才记录 **Q\_PREFIX\_ORDER\_FOLD** 并进入稳定子塔，必须保留插入时稳定子和
来源标签，不能把中间价格与最终 \(T_f\) 下的 (12) 再相加。原先形式若写成
\(n\ge o_{f,q}\)，会漏掉 \(n=o_{f,q}-1\) 的整循环边界。

### 插入层补充分支：Q\_PREFIX\_ORDER\_FOLD

在中间稳定子上若
\(n+1\) 达到其商阶，则有
\[
u_q^{o^{\mathrm{ins}}_{f,q}}\in T^{\mathrm{ins}}_f.
\tag{13}
\]
该有限阶关系由稳定子塔的插入时账本处理；多出的层转入商、二幂/primary 或
关系 Fourier，不能继续按请求数收费。

若同一纤维有多个 q 族，先按商方向 \(u_qT_f\) 去重；相同方向的族必须合并成一个
前缀块，否则输出
\(\mathrm{Q\_DIRECTION\_DUPLICATE\_OBSTRUCTED}\)。在去重后，多集合 Kneser 给出
\[
|P_f|
\ge |A_{0,f}T_f|
 +|T_f|\sum_{q\text{ direction}}\kappa_{f,q}.
\tag{14}
\]
若目标 \(t_f\notin P_f\)，则
\[
\sum_q\kappa_{f,q}
\le
\left\lfloor
\frac{|H_f|-1-|A_{0,f}T_f|}{|T_f|}
\right\rfloor.
\tag{15}
\]
若反之左侧超过 (15)，则直接得到该纤维的 Type II 命中。

## 4. 跨纤维碎片化回执

一个跨状态 Hall 匹配可能把请求分配给不同纤维
\(f_1,\ldots,f_t\)。这时不能把不同 \(H_f\) 的价格相加。对每个纤维单独记录
\[
\mathsf P_f=\sum_q\kappa_{f,q},\qquad
\mathsf G_f=
\left\lfloor
\frac{|H_f|-1-|A_{0,f}T_f|}{|T_f|}
\right\rfloor-\mathsf P_f,
\tag{16}
\]
以及每个 q 族的 \((n_{f,q},o_{f,q},\kappa_{f,q})\)。

若所有纤维都满足 \(\mathsf G_f\ge0\)，且至少有两个纤维携带非空请求，则输出
\[
\boxed{
\mathrm{Q\_PREFIX\_PRICE\_FRAGMENTED}
=\{(f,\mathsf P_f,\mathsf G_f,\text{fold ledger})\}_f.
}
\tag{17}
\]
该回执严格说明当前匹配没有产生一个共同目标积集的 Kneser 价格；它不声称原猜想
失败。后续只能选择某一纤维的完整匹配、构造保持标签的 source-switch、进入稳定子
塔，或把未实现的跨纤维边记录为算术障碍。

若某个纤维满足 \(\mathsf G_f<0\)，则 (14)--(15) 给出
\(\mathrm{Q\_PREFIX\_TYPEII\_HIT}\)；若某个 q 族的前缀 Hall 条件失败，则输出
\[
\mathrm{Q\_PREFIX\_MATCHING\_DEFICIT}
=(f,q,\{h_{(k)}<k\},n,\ d_f(q)).
\tag{18}
\]
这比普通 Hall 缺口更精确：它指出第一个无法由连续 q 层支付的高度。

## 5. 与 q 进 Hall 和稳定子塔的接线

对一个 q 进请求子集，先执行 layered-Rado 的 q 层上界和本引理的前缀排序：

1. 若总深度不满足 \(n\le d_f(q)\)，输出
   \(\mathrm{Q\_PREFIX\_MATCHING\_DEFICIT}\) 或
   \(\mathrm{Q\_PREFIX\_EDGE\_OBSTRUCTED}\)，不进入 Kneser 价格；
2. 若前缀匹配通过且最终 \(o_{f,q}>1\)（因而 \(n+1<o_{f,q}\)），把 \(B_{f,q}(n)\) 放入同一纤维的
   PRICE-INJECTION 序列，价格恰为 \(n\)；
3. 若在中间稳定子上 \(n+1\) 达到其商阶，使用 (13) 的有限阶关系进入稳定子塔；
   最终稳定子下的同一 q 方向则只记录吸收，吸收块和折叠层不在商中重新收费；
4. 若请求跨纤维，先生成 (17) 的逐纤维账本，不能把 FULL_MATCH 直接解释为一个
   Type II 目标积集。

这样，Hall 的“q 层槽”到 Kneser 的“幂块价格”有一个规范中间对象
\(B_{f,q}(n)\)，消除了逐槽复制同一 q 的歧义。

## 6. 构造性边界

### 6.1 前缀匹配失败而总槽数看似足够

取一个共享 q 账本的最大深度 \(d=2\)，三个请求阈值为
\[
(h_1,h_2,h_3)=(1,2,2).
\]
逐层总槽计数若错误地把两个深度二标签相加，会得到三个名义单位；但升序条件
\(h_{(3)}=2<3\)，式 (8) 说明不存在三请求的合法前缀匹配。回执是
\(\mathrm{Q\_PREFIX\_MATCHING\_DEFICIT}\)，不能生成高度三的 q 幂块。

### 6.2 插入层有限阶折叠

在 \(H_f=C_4\) 中取插入前稳定子 \(T_f^{\mathrm{ins}}=1\)、\(u_q=3\)，其阶为
\(2\)。一个高度 \(n=1\) 的前缀块已经满足
\[
B_{f,q}(1)=\{1,3\}=\langle3\rangle.
\]
它在插入层记录 \(\mathrm{Q\_PREFIX\_ORDER\_FOLD}\)；插入后最终稳定子至少包含
\(\langle3\rangle\)，所以最终商阶变为 \(1\)，最终价格为 \(0\)。即使把同一方向的
请求重复到 \(n=3\)，也不能把三请求当成三单位容量；重复层必须在插入账本和最终
稳定子中同时去重。

### 6.3 跨纤维不能合并

令两个纤维各有 \(H_f=C_4\)、\(T_f=1\)，每个纤维各自收到一个前缀请求，且目标
在各自积集外。每个纤维的价格为 \(1\)，但没有共同的 \(H\) 或共同的
source-switch；两单位不能相加成一个 \(C_4\) 的 Kneser 命中。回执必须是
\(\mathrm{Q\_PREFIX\_PRICE\_FRAGMENTED}\)，除非另有保持标签的纤维合并构造。

## 7. 证明

前缀匹配的三项等价由排序后的 Hall 条件证明。规范匹配使用层
\(1,\ldots,n\)，所以 \(n\le d_f(q)\)；(4) 的共同 q 账本和 (10) 给出每个指数
\(q^j\) 的整数整除，得到真实块 (9)。有限循环商中的连续幂段基数为
\(\min(n+1,o_{f,q})\)，减一即得 (12)。多集合 Kneser 应用于去重后的 q 方向和
其它源块，得到 (14)；目标缺失时目标陪集缺口给出 (15)。

不同纤维的积集位于不同目标群和不同参数合同中，不能使用同一个 Kneser积集；
逐纤维计算只得到 (16)，于是 (17) 是跨纤维未合并的精确回执。若前缀排序失败，
第一个 \(h_{(k)}<k\) 给出 (18)。所有分支均由有限排序、有限群阶和有限来源合同
确定，证毕。

## 研究边界

本引理完成了一个新的严格容量映射：q 进 Hall 层在同一纤维中自动压缩成单个真实
幂块，价格精确为 \(\min(n,\operatorname{ord}(qT)-1)\)，并把有限阶折叠、方向重复
和跨纤维碎片化分别类型化。它仍不证明每个核心素数都有一个满足前缀条件的共同纤维；
也不把 \(\mathrm{Q\_PREFIX\_MATCHING\_DEFICIT}\) 或碎片化回执自动升级为严格递降。
下一步决定性接口是：证明剩余 q 请求必进入某个共同纤维，或把第一个失败高度
转成保持标签的 source-switch、广义 \(2^j\) 终端或稳定子塔下降。
