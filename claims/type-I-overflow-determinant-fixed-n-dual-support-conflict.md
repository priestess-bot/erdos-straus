---
kind: claim
claim_id: type-I-overflow-determinant-fixed-n-dual-support-conflict
title: overflow 行列式的固定 n 对偶图谱与累积支撑冲突
statement: 设 verified complete-excess bundle overflow 满足 R_M>p、pR_M+1=4K_M 且 K_M=MC，写 n=4M-R_M、d=p-C，则 pn=4Md+1。固定 n 时，每个 L|Md 且 n<4L<p+n 都给出合法小图表 R_L=4L-n、K_L=L(p-Md/L)；若旧 charged support A 满足 A|L、L>A，则这是保持 Sol(p)、恒等提升且使 floor((p-1)^2/(4A)) 严格下降的 overflow-derived edge。若另外有 A=1 且 M<p，则 d>=2、L=d 总在该窗口；不加 M<p 时该结论为假，见 A=1 小载体假设边界。一般 overflow 另有由 r=M mod p 与 d 构成的两个对偶图表，其中至少一个 R<p，且相应载体 t<M；但 A>1 时小图表未必保留旧支撑，固定 n 窗口也可为空，lcm 迭代还可成环。故余项已精确收缩为可达累积支撑 overflow 的 alternate/终端/外层重置问题，而非把所有 A=1 算术 overflow 误判为已闭合。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-marked-support-accumulation-rechart-saturation
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-universal-p-source-capacity-anchor-orbit
topics:
  - type-I
  - overflow
  - determinant
  - fixed-n-atlas
  - divisor-window
  - dual-carrier
  - charged-support
  - marked-descent
  - well-founded-potential
  - counterexample
  - proof-boundary
sources:
  - claim: type-I-marked-support-accumulation-rechart-saturation
    role: overflow-determinant-and-absorbed-support-potential
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: verified-bundle-overflow-provenance
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: universal-anchor-and-path-provenance
visibility: public
last_checked: '2026-08-03'
---

# overflow 行列式的固定 \(n\) 对偶图谱与累积支撑冲突

## 1. overflow 行列式正规形

固定一个已经通过 source/path/node provenance 验证的 bundle overflow：

\[
p\equiv1\pmod {24},
\qquad
1\le R_M<4M,
\qquad
R_M>p,
\qquad
pR_M+1=4MC.
\tag{1}
\]

这里 \(M\mid K_M\)、\(K_M=MC\)。定义

\[
n=4M-R_M,
\qquad
d=p-C.
\tag{2}
\]

由 \(R_M<4M\) 得 \(n>0\)。又因

\[
C=\frac{pR_M+1}{4M}<p+\frac1{4M},
\tag{3}
\]

且 \(p\nmid1\)，有 \(1\le C\le p-1\)，从而 \(1\le d\le p-1\)。直接消元得到

\[
\boxed{pn=4Md+1,}
\tag{4}
\]

并且

\[
(M,pn)=1.
\tag{5}
\]

式 (4) 是 `complete_excess_bundle_overflow` 的 determinant receipt。以下所有新边都必须
保留原 bundle receipt 及其可重放路径；不能从一个任意满足 (4) 的四元组反推来源。

## 2. 固定 \(n\) 的完整因子图谱

令

\[
S=Md=\frac{pn-1}{4}.
\tag{6}
\]

对任意因子 \(L\mid S\)，若

\[
n<4L<p+n,
\tag{7}
\]

定义

\[
\boxed{
R_L=4L-n,
\qquad
K_L=L\left(p-\frac SL\right).
}
\tag{8}
\]

左侧不等式保证 \(R_L>0\)，右侧不等式给 \(R_L<p\)。而

\[
pR_L+1
=4pL-pn+1
=4(pL-S)
=4K_L.
\tag{9}
\]

由 (7) 还有 \(S/L<p\)，所以 \(K_L>0\)。又因 \(n\equiv1\pmod4\)，
\(R_L\equiv3\pmod4\)，故

\[
3\le R_L\le p-2,
\qquad
L\mid K_L.
\tag{10}
\]

若当前状态携带 charged support \(A\mid K\)，则保持旧承诺并严格增长的完整候选集恰为

\[
\boxed{
\mathcal W_A(M,d,n)=
\{L:A\mid L,\ L>A,\ L\mid Md,\ n<4L<p+n\}.
}
\tag{11}
\]

对任一 \(L\in\mathcal W_A\)，定义后继

\[
T=(p,R_L,K_L;L).
\tag{12}
\]

它与原状态有同一个

\[
W_T=W_S=\operatorname{Sol}(p),
\tag{13}
\]

所以 E4 是恒等映射。若 \(B_p=(p-1)^2/4\)，则 \(A\mid L\)、\(L>A\) 蕴含
\(L\ge2A\)，因而

\[
\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{14}
\]

取 (11) 的最小元素可得到确定性 `overflow_fixed_n_charged_support_v1`。这里的新支撑来源
是 `overflow_determinant`，不是原节点上的 complete-excess bundle；这是一个新增且必须
显式记录的 E1 provenance。

## 3. 小载体 \(A=1,\ M<p\) overflow 有合法后继

初始层有

\[
A=1,
\qquad
M=Q<R<p.
\tag{15}
\]

这里的 \(M<p\) 是本节的必要假设，不是任意 determinant overflow 的自动性质；因此本节
只关闭小载体子族。

若 \(d=1\)，则由 (4) 及 \(M<p\) 得 \(n<4\)；又 \(n\equiv1\pmod4\)，所以
\(n=1\)。这会给出

\[
M=\frac{p-1}{4},
\qquad
R_M=4M-n=p-2<p,
\tag{16}
\]

与 overflow 矛盾。因此

\[
d\ge2.
\tag{17}
\]

取 \(L=d\)，则

\[
R_d=4d-n,
\qquad
K_d=d(p-M).
\tag{18}
\]

因为 \(R_M=4M-n>p\)，有 \(4M>p+n\)。结合 (4)，

\[
4d=\frac{pn-1}{M}
<\frac{4pn}{p+n}
\le p+n,
\tag{19}
\]

最后一步等价于 \((p-n)^2\ge0\)。式 (18) 的恒等式保证 \(R_d>0\)，故

\[
n<4d<p+n.
\tag{20}
\]

于是 \(d\in\mathcal W_1\)，并有

\[
\boxed{
3\le R_d\le p-2,
\qquad
pR_d+1=4d(p-M),
\qquad
d\mid K_d.
}
\tag{21}
\]

因此

\[
\boxed{
(p,R,K;1)
\longrightarrow
(p,R_d,d(p-M);d)
}
\tag{22}
\]

是完整 E1--E5 identity-lift edge，命名为
`overflow_determinant_charged_support_v1`。即使 \(R_d=R\)，支撑也由 \(1\) 严格增长到
\(d\)，所以 (14) 仍下降。该定理关闭的是初始 overflow 的“一步出口”；后继已经具有
\(A>1\)，仍须继续处理累积层。

若删去 \(M<p\)，上述 \(L=d\) 推论不成立：例如
\((p,M,d,n)=(73,1297,29,2061)\) 满足同一 determinant overflow，但
\(4d-n<0\)，且 \(S=Md\) 在 \(B_p\) 以下没有正候选除子。该负边界及其逻辑范围见
[A=1 overflow 的小载体假设边界](type-I-overflow-a-one-generic-determinant-boundary.md)。

## 4. 任意 overflow 至少有一个小算术对偶图表

将

\[
M=kp+r,
\qquad
1\le r<p
\tag{23}
\]

代入 (4)，并定义

\[
s=n-4kd.
\tag{24}
\]

则

\[
ps=4rd+1,
\qquad
s\equiv1\pmod4.
\tag{25}
\]

定义对称的两个图表

\[
R_d=4d-s,
\qquad
K_d=d(p-r),
\tag{26}
\]

\[
R_r=4r-s,
\qquad
K_r=r(p-d).
\tag{27}
\]

它们满足

\[
pR_d+1=4K_d,
\qquad
pR_r+1=4K_r,
\tag{28}
\]

并且都是正的 \(3\pmod4\) 规范代表。若二者同时大于 \(p\)，则

\[
4d(p-r)>p^2,
\qquad
4r(p-d)>p^2.
\tag{29}
\]

相乘并除以 \(p^4\) 会得到

\[
16\frac dp\left(1-\frac dp\right)
\frac rp\left(1-\frac rp\right)>1,
\tag{30}
\]

与 \(x(1-x)\le1/4\) 矛盾。因此

\[
\boxed{\min(R_d,R_r)<p.}
\tag{31}
\]

这解决了“小算术图表是否存在”，但没有解决旧支撑是否保留。对载体 \(t=d\) 或
\(t=r\)，令 \(L_t=\operatorname{lcm}(A,t)\)。它升级为合法 charged-support edge 当且
仅当

\[
R_t<p,
\qquad
L_t\mid K_t,
\qquad
L_t>A.
\tag{32}
\]

其中整除条件分别等价于

\[
\frac A{(A,d)}\mid p-r,
\qquad
\frac A{(A,r)}\mid p-d.
\tag{33}
\]

不满足 (32) 的小图表只能标为 `candidate_transition`；把旧 \(A\) 直接重置为 \(t\)
会破坏单调势合同。

### 4.1 载体大小严格下降，但 phase 合同仍需补足

原 bundle provenance 给出 \(p\nmid M\)：\(A\mid K\) 且 \(p\nmid K\)，而 \(Q<R<p\)。
因此在 (23) 中 \(r=M\bmod p\) 满足 \(1\le r<p\)。若 \(M>p\)，则

\[
d<p<M,
\qquad
r<p<M.
\tag{34}
\]

若 \(M<p\)，则 \(r=M\)，并且 \(s=n\)、\(R_r=4M-n=R_M>p\)。所以 (31) 的小
图表只能是 \(d\)-图表。又由 overflow

\[
4M>p+n,
\qquad
d=\frac{pn-1}{4M},
\]

得到

\[
d<\frac{p(4M-p)-1}{4M}<M,
\tag{35}
\]

最后一个不等式使用 \(4M^2-p(4M-p)=(2M-p)^2\ge0\)。因此任一满足 \(R_t<p\) 的
对偶载体都满足

\[
\boxed{1\le t<M.}
\tag{36}
\]

这给出新的 `overflow_carrier_reset_v1` 候选：以原 overflow receipt 为 E1 provenance，
取小图表

\[
T_t=(p,R_t,K_t;t),
\qquad
W_{T_t}=W_S=\operatorname{Sol}(p),
\]

并使用外层载体秩 \(\Pi_M(T)=t<M=\Pi_M(S)\)。它完整满足算术正规形、恒等解提升和
载体大小下降。若 \(\operatorname{lcm}(A,t)\nmid K_t\) 或不严格增加旧支撑，它仍不能
作为当前 charged-support phase 的边，只能作为**有条件的 phase reset candidate**。
要把该候选升级为统一递归边，还需定义不可逆 phase 转换，并证明 reset 后允许的
marked/overflow 边不会重新回到较大的 \(M\)；这正是当前剩余的良基调度问题。

### 4.2 允许普通 anchor 重入会产生真实载体环

上面的 phase 警告可以由一个完全算术的回执具体化。对 \(p=73\)，若从 overflow
\(M=38\) 取小图表 \(t=12\)，则

\[
R_{12}=23,\qquad K_{12}=420.
\]

若 RESET 把 \(t\) 重新记作 charged support，并允许随后执行普通 anchor/lcm 吸收，
\(R_{12}-1=22\) 的 complete bundle 为 \(Q=11,\beta=2\)，于是

\[
\begin{array}{c|c|c|c|c}
\text{当前载体 }M&\text{RESET 载体 }t& R_t&Q&\operatorname{lcm}(t,Q)\\
\hline
38&12&23&11&132\\
132&30&23&11&330\\
330&12&23&11&132
\end{array}
\]

对应的新图表分别为
\[
(R_{132},K_{132})=(311,5676),\qquad
(R_{330},K_{330})=(1103,20130),
\]
二者都再次 overflow。因而这是 `RESET -> anchor/lcm -> RESET` 的实际二环；它不否定
小对偶载体的严格下降 (36)，而是证明“每个 RESET 局部降 \(M\)”不能单独提供全局
良基势。统一选择器若采用这一重入方式，必须禁止普通 ABSORB 回边，或在 RESET 之上
引入一个更外层的不可重置 rank。

## 5. 累积支撑层的严格边界

### 5.1 fixed-\(n\) 窗口可以为空

在

\[
(p,R,K;A)=(241,111,6688;38)
\tag{34}
\]

的 receipt \(Q=5\)、\(M=190\) 上，

\[
R_M=719,
\quad
n=41,
\quad
d=13,
\quad
S=Md=2470.
\tag{35}
\]

不存在满足

\[
38\mid L,
\quad L>38,
\quad L\mid2470,
\quad41<4L<282
\tag{36}
\]

的因子，所以 \(\mathcal W_{38}=\varnothing\)。一般 \(A>1\) 时甚至可以有 \(d=1\)：

\[
(p,R,K;A,Q,M,R_M,n,d)
=(73,23,420,7,13,91,359,5,1).
\tag{37}
\]

因此第 3 节不能逐字推广到累积层。

### 5.2 小对偶图表可以丢失旧支撑

真实 F-source 路径可到达

\[
(p,R,K;A)=(241,79,4760;8),
\qquad
\{8,71\},
\tag{38}
\]

其 bundle 有

\[
Q=71,
\quad
M=568,
\quad
R_M=1103,
\quad
n=1169,
\quad
d=124.
\tag{39}
\]

式 (23)--(27) 给出 \(r=86,s=177\) 及

\[
(R_d,K_d)=(319,19220),
\qquad
(R_r,K_r)=(167,10062).
\tag{40}
\]

唯一小图表是 \(r\) 支，但

\[
\operatorname{lcm}(8,86)=344\nmid10062.
\tag{41}
\]

所以 (31) 不能替代 (32)。

### 5.3 lcm/determinant 的朴素迭代可以成环

在 \((p,R,K;A)=(73,47,858;66)\) 上，先取 \(Q=23\)，有

\[
M_0=1518,
\quad R_{M_0}=3743,
\quad n=2329,
\quad d_0=28.
\tag{42}
\]

以 \(\operatorname{lcm}(66,28)=924\) 再算得到

\[
R_{924}=1367,
\quad d_1=46,
\quad
\operatorname{lcm}(66,46)=1518=M_0.
\tag{43}
\]

这是精确二环，故 determinant 本身不提供新的良基量。

### 5.4 从根状态可达的完整菜单冲突

上述边界并非只来自任意填写 \(A\)。根状态

\[
(p,R,K;A)=(73,39,712;1)
\tag{44}
\]

是 Jacobi-G；第 2 节的通用源到达 \(\{1,38\}\)，其
\(Q=19,\beta=2\) 给出合法吸收边

\[
(73,39,712;1)
\longrightarrow
(73,51,931;19).
\tag{45}
\]

从新状态 anchor 出发的完整 bottom Reach 有 \(16\) 个节点、没有 raw terminal。逐个节点
和方向核验后，全部合法 complete-bundle receipt 恰有

\[
Q\in\{2,32,44,50\}.
\tag{46}
\]

它们与 \(A=19\) 合并后全部 overflow；对每张 receipt 检查 (26)--(33)，没有一个小
对偶图表既保留 \(19\) 又严格增加 charged support；四张 receipt 的 fixed-\(n\) 候选集
\(\mathcal W_{19}\) 也全部为空。

式 (44)--(46) 只反驳“通用 anchor Reach + 当前 bundle/双载体菜单必闭合”的机制命题。
它不是 Erdos--Straus 反例，且不排除另一个形式源、不同 marked 状态或直接短证书。

## 6. 精确的新余项

通用源定理和第 3--4 节已经删除两个旧问题，并将第三个拆分为受限子族：

1. 裸 G 是否有实际 source；
2. \(M<p\) 的小载体 \(A=1\) overflow 是否有合法下一边；
3. 任意 overflow 是否至少存在一个 \(R<p\) 的算术对偶图表。

一般 \(A=1\) 的固定-\(n\) 分支仍不能自动闭合，但[A=1 overflow 的对偶外层秩
RESET](type-I-overflow-a-one-dual-outer-rank-reset.md) 已提供另一条算术出口；合并
两者后，剩余全称命题可量化**递归历史可达的 \(A>1\) 状态**，并证明以下至少一项：

\[
\boxed{
\mathcal W_A\ne\varnothing
\quad\lor\quad
\text{某个 source/path/node alternate 通过 (32)}
\quad\lor\quad
\text{直接 Type I/II terminal}
\quad\lor\quad
\text{有独立外层秩支付的 support reset}.
}
\tag{47}
\]

前三项保持当前单调 charged-support phase；最后一项必须先定义新的 phase 和全局良基序，
不能仅因小图表存在就丢弃旧 \(A\)。这就是路线图后续最窄的证明目标。

## 7. 聚焦复现

~~~bash
python3 reproductions/type_i_universal_anchor_overflow_dual.py --verify
~~~

结果文件为
`reproductions/type-i-universal-anchor-overflow-dual-results.json`。对应 SHA-256 为

~~~text
48afe06bed5fa05a8c90b3afcd9f9fc162bb64aca240a171424266283d82f195  reproductions/type_i_universal_anchor_overflow_dual.py
74724ef248bd13b5dbd0977ede341315f22302357b513c3f8b45602036d8101a  reproductions/type-i-universal-anchor-overflow-dual-results.json
~~~

脚本只验证本卡中的代数恒等式、少量正反 receipt 和 (44)--(46) 的局部 Reach；不重跑
历史测试。全称的固定 \(n\)、初始层与对称双图表结论由第 2--4 节证明承担。
