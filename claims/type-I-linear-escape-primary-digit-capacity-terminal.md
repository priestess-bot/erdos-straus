---
kind: claim
claim_id: type-I-linear-escape-primary-digit-capacity-terminal
title: 线性 escaped source 的高阶 primary 幂块进位容量终端
statement: 设当前目标商含有一个循环 ell-primary 因子 H=C_{ell^a}，并有已通过同一参数纤维 source-switch、SNF、CRT、范围且有整数回译的幂块 B_i={1,u_i,...,u_i^{d_i}}。将其投影写成加法块 E_i={0,v_i,...,d_i v_i}，删除 v_i=0 的稳定子吸收块，令 nu_i=nu_ell(v_i)，W_k=sum_{nu_i=k} min(d_i,ell-1)。若所有 W_k>=ell-1，则源块和集覆盖 H；若最高不足层 k*<a-1，则所有高层块精确覆盖 ell^{k*+1}H，目标缺失严格投影到 C_{ell^{k*+1}}，并给出一次性的 primary 稳定子商递降；k*=a-1 时输出顶层幂块进位缺口。E1--E5 只决定有限商结论能否升级为整数证书或严格递降。该结论不把同一循环因子内平行 source 的初等方向错误相乘。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-escape-primary-hole-capacity
  - type-II-source-fiber-cyclic-primary-digit-terminal
  - type-II-source-fiber-highest-deficit-tail-compression
  - type-II-qadic-height-kneser-block-bridge
  - type-II-stabilizer-tower-weighted-defect-conservation
topics:
- type-I
- linear-source
- escape
- primary
- ell-adic
- digit-capacity
- q-height
- tail-compression
- stabilizer
- quotient-descent
- Type-II
- source-switch
- E1-E5
- proof-program
sources:
  - claim: type-I-linear-escape-primary-hole-capacity
    role: elementary-primary-capacity
  - claim: type-II-source-fiber-cyclic-primary-digit-terminal
    role: binary-layer-terminal
  - claim: type-II-source-fiber-highest-deficit-tail-compression
    role: highest-deficit-quotient
visibility: public
last_checked: '2026-08-05'
---

# 线性 escaped source 的高阶 primary 幂块进位容量终端

## 1. 循环 primary 设置

固定已经通过参数纤维、整数 source-switch、SNF、CRT、范围并有可核验整数回译的目标
商；E1--E5 作为最终证书/递降升级门另行检查。取其中一个循环 primary 因子

\[
H=C_{\ell^a}\qquad(\ell\text{ 为素数},\ a\ge1).
\tag{1}
\]

把乘法源块通过该商坐标写成加法块

\[
E_i=\{0,v_i,2v_i,\ldots,d_i v_i\}\subseteq H,
\qquad d_i\ge1.
\tag{2}
\]

这里 \(v_i\) 是 \(u_i\) 的商像；若 \(v_i=0\)，整个块已经落入当前稳定子，删除它，
不能继续收费。对 \(v_i\ne0\) 写

\[
v_i=\ell^{\nu_i}w_i,
\qquad
0\le\nu_i<a,
\qquad
w_i\notin\ell H.
\tag{3}
\]

第 \(k\) 个精确进位层的**加权容量**定义为

\[
W_k
 =\sum_{\nu_i=k}\min(d_i,\ell-1),
\qquad 0\le k<a.
\tag{4}
\]

每个幂块在该层至多提供 \(\ell-1\) 个独立的模 \(\ell\) 增量；同一循环因子内
所有 \(v_i\) 的模 \(\ell\) 像都在一维方向上，所以这里是加法容量，不能使用
前一张初等商卡的坐标乘积。

## 2. 全层覆盖定理

令

\[
S=E_1+\cdots+E_r.
\tag{5}
\]

若对所有 \(k=0,\ldots,a-1\) 有

\[
\boxed{W_k\ge\ell-1,}
\tag{6}
\]

则

\[
\boxed{S=H.}
\tag{7}
\]

因此，在当前稳定子商中，任意目标坐标都被源幂块命中；若每个块的整数回译仍
保留同一参数纤维，则这是 PRIMARY_POWER_LAYER_HIT 的 Type II 短证书入口。

### 证明

先看 \(a=1\)。所有 \(v_i\) 都是模 \(\ell\) 的非零元。第 \(i\) 个像集

\[
\{0,v_i,\ldots,d_i v_i\}\pmod\ell
\]

有 \(m_i=\min(d_i+1,\ell)\) 个元素。反复使用 Cauchy--Davenport，得到

\[
|S|\ge\min\!\left(\ell,1+\sum_i(m_i-1)\right)
 =\min\!\left(\ell,1+W_0\right)=\ell.
\]

故 \(S=C_\ell\)。

对 \(a>1\)，取精确层 \(0\) 的块。它们在 \(H/\ell H\simeq C_\ell\) 中的像集和由同一
个 Cauchy--Davenport 估计覆盖 \(C_\ell\)。其余层 \(\nu_i\ge1\) 的块都落在
\(\ell H\) 中；除以 \(\ell\) 后得到 \(C_{\ell^{a-1}}\) 中的幂块，且原来的
第 \(k+1\) 层变成新的第 \(k\) 层。归纳假设和 (6) 给出这些剩余块的和集为
\(\ell H\)。任取 \(x\in H\)，先用层 0 块取到与 \(x\) 同模 \(\ell\) 的元素，
再用剩余块补足 \(\ell H\) 中的差值，故 \(x\in S\)。证毕。

## 3. 最高不足层与严格尾压缩

若某层不足，取规范的最高不足层

\[
k^*=\max\{k:W_k\le\ell-2\}.
\tag{8}
\]

当 \(k^*<a-1\) 时，由最大性对每个 \(k>k^*\) 有 \(W_k\ge\ell-1\)。把所有
\(\nu_i>k^*\) 的块相加，除以 \(\ell^{k^*+1}\) 后应用上一节的归纳证明，得到

\[
\boxed{
S_{>k^*}=\ell^{k^*+1}H.
}
\tag{9}
\]

设当前已有基集为 \(P_0\subseteq H\)，完整源积集为

\[
P=P_0+S.
\tag{10}
\]

令 \(U=\ell^{k^*+1}H\)，并记低层和集为 \(S_{\le k^*}\)。由 (9)，

\[
P=P_0+S_{\le k^*}+U
 =\pi^{-1}\!\left(\pi(P_0+S_{\le k^*})\right),
\qquad
\pi:H\to H/U\simeq C_{\ell^{k^*+1}}.
\tag{11}
\]

特别地，\(U\le\operatorname{Stab}_H(P)\)。若目标 \(t\) 在 \(P\) 中缺失，则

\[
\boxed{
t\notin P
\iff
\pi(t)\notin\pi(P_0+S_{\le k^*}).
}
\tag{12}
\]

这给出 PRIMARY_POWER_TAIL_STABILIZER_DESCENT(k*)。当 \(k^*<a-1\) 时，商阶从
\(\ell^a\) 严格降为 \(\ell^{k^*+1}\)，高层幂块在新商中全部变成单位，永久标记为
ABSORBED_PRIMARY_TAIL，不能在下一层再次收费。

若 \(k^*=a-1\)，没有非平凡高尾，保留 PRIMARY_POWER_TOP_DIGIT_DEFICIT，其见证是

\[
W_{a-1}\le\ell-2.
\tag{13}
\]

若不存在最高不足层，则由 (7) 直接进入 PRIMARY_POWER_LAYER_HIT。如果所选 \(H\)
只是当前源关系差分群的真子群而目标锚点不在 \(H\)，则输出 ANCHOR_OUTSIDE_DIFFERENCE，
不能把该情形误写成层容量失败。

## 4. 稳定子塔和整数递降接口

在原目标群 \(G\) 中先取当前稳定子 \(T_0\)，再令 \(\bar G=G/T_0\)。若该循环
primary 坐标已经与其它坐标分离，且其它坐标的当前源积集已经饱和，则 (9) 的尾部
\(U\) 可拉回为

\[
\widehat U=\pi_0^{-1}(U),\qquad \pi_0:G\to\bar G,
\]

并满足

\[
T_0<\widehat U\le\operatorname{Stab}_G(P)
\]

（非平凡坐标时严格）。稳定子塔只为这次增长记录一次价格
\(|\widehat U|-|T_0|\)；所有高层块在 \(G/\widehat U\) 中成为单位，不能同时
在 elementary 容量、原层 Kneser 和商层重复计费。若坐标尚未分离或其它坐标未饱和，
只保留 (11)--(12) 的 primary 因子结论，不能自动把 \(U\) 升格为全局稳定子。

将 (12) 升级为 Erdős--Straus 的严格整数递降，还必须保存：

1. 高层 q-height、来源标签和同一参数纤维合同；
2. 投影源列及目标的 SNF/CRT 关系；
3. 新参数的正性、平方自由条件、范围和 \(B'>A\)；
4. 全域标记解的 E1--E5 提升以及严格势下降。

若这些门全部通过，回执为 PRIMARY_POWER_STRICT_RELAY；否则保留
PRIMARY_POWER_TAIL_LIFT_OBSTRUCTED，有限商结论 (11)--(12) 仍然有效。

## 5. 边界例子

### 幂块替代多个二点块

在 \(H=C_9\) 中取两个块

\[
E_1=\{0,1,2\},\qquad E_2=\{0,3,6\}.
\]

第一块给出 \(W_0=\min(2,2)=2\)，第二块给出 \(W_1=2\)，两层均达到
\(\ell-1=2\)，故 \(E_1+E_2=C_9\)。这说明一个高度为 2 的合法幂块可以在
一层替代两个二点块，但仍不能把同一层平行块的容量相乘。

### 最高缺口压缩

在 \(H=C_{16}\) 中取

\[
E_1=\{0,2\},\quad E_2=\{0,4\},\quad E_3=\{0,8\}.
\]

此时 \(W_0=0\)，而 \(W_1=W_2=W_3=1=\ell-1\)，所以
\(k^*=0\)，高层和集是 \(2C_{16}\)，目标缺失严格投影到 \(C_2\)。

### 顶层缺口

在 \(H=C_8\) 中取 \(E_1=\{0,1\}\)、\(E_2=\{0,2\}\)。有
\((W_0,W_1,W_2)=(1,1,0)\)，故 \(k^*=2=a-1\)。这里不能伪造更小 primary
商，只能记录 PRIMARY_POWER_TOP_DIGIT_DEFICIT。

## 6. 研究边界

本卡把 escaped source 的合法 q-height 幂块从初等商容量推广到同一循环
\(\ell^a\) 因子的加权进位层，给出命中、一次性稳定子尾吸收、严格较小 primary
商和顶层缺口的互斥分派。它仍不证明：

* escaped source 菜单本身完备；
* 不同 primary 因子之间可以无条件池化；
* 尾部商一定有整数 source-switch、SNF/CRT 和 E1--E5 提升；
* 顶层缺口必然导出 Type I/II 证书。

这些分支必须分别进入 finite source dispatch、多 primary 终端、稳定子塔或
annihilator/Fourier relay。尤其在同一循环因子内，只能使用 \(W_k\) 的加法容量，
禁止再次使用 \(\prod_i\min(d_i+1,\ell)\) 的独立坐标乘积。
