---
kind: claim
claim_id: type-II-source-fiber-highest-deficit-tail-compression
title: Type II 循环 primary 最高缺口的饱和尾压缩与严格递降
statement: 在固定参数纤维的循环 \(C_{\ell^a}\) 中，若合法独立二点块按精确 \(\ell\)-进层计数，则取最高的不足层 \(k^*\) 后，所有更高层块的和集必为完整子群 \(\ell^{k^*+1}C_{\ell^a}\)。因此目标缺失可规范地降到严格较小商 \(C_{\ell^{k^*+1}}\)（当 \(k^*<a-1\)），而 \(k^*=a-1\) 给出顶层 primary digit deficit；若所有层饱和则直接命中或输出锚点外置。抽象商仍需 source-switch/SNF/范围/E1--E5 才能升级为整数递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-cyclic-primary-digit-terminal
  - type-II-source-fiber-multiprimary-digit-terminal
  - type-II-source-fiber-qheight-kneser-bridge
topics:
- type-II
- source-fiber
- cyclic
- primary
- highest-deficit
- tail-saturation
- quotient-descent
- generalized-dyadic
- q-height
- source-switch
- proof-program
sources:
  - claim: type-II-source-fiber-cyclic-primary-digit-terminal
    role: saturated-primary-tail-cover
  - claim: type-II-source-fiber-multiprimary-digit-terminal
    role: primary-factor-interface
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: q-height-source-realization
visibility: public
last_checked: '2026-08-05'
---

# Type II 循环 primary 最高缺口的饱和尾压缩与严格递降

## 1. 设置和规范最高缺口

固定一个已经通过 source-switch、SNF、CRT、范围和独立选择门的参数纤维。令
\[
H=C_{\ell^a}
\]
使用加法记号，且有合法二点源块
\[
B_j=\{0,v_j\}\subseteq H,\qquad v_j\ne0.
\tag{1}
\]
对非零 \(v\) 记精确赋值
\[
\nu_\ell(v)=\max\{0\le r<a:v\in\ell^rH\},
\]
并令
\[
c_r=\#\{j:\nu_\ell(v_j)=r\},\qquad 0\le r<a.
\tag{2}
\]
设源和集为
\[
S=\sum_jB_j.
\tag{3}
\]

若某层不足，即 \(c_r\le\ell-2\)，定义规范的最高不足层
\[
k^*=\max\{r:c_r\le\ell-2\}.
\tag{4}
\]
若集合为空，则称所有层饱和。最高层的选择是按层号的内容寻址，不依赖块或标签的
枚举顺序。

## 2. 饱和尾覆盖引理

令
\[
H_{>k^*}=\ell^{k^*+1}H
\]
并令 \(S_{>k^*}\) 是所有满足 \(\nu_\ell(v_j)>k^*\) 的二点块之和。由
\(k^*\) 的最大性，对每个
\[
r=k^*+1,\ldots,a-1
\]
都有 \(c_r\ge\ell-1\)。把 \(H_{>k^*}\) 除以 \(\ell^{k^*+1}\) 同构为
\(C_{\ell^{a-k^*-1}}\)，高层块的精确赋值依次为
\(r-k^*-1\)。因此循环 primary 进位层终端给出
\[
\boxed{
S_{>k^*}=H_{>k^*}.
}
\tag{5}
\]
当 \(k^*=a-1\) 时约定 \(H_{>k^*}=\{0\}\)，(5) 是平凡尾。

### 证明

缩放后的高层块在 \(C_{\ell^{a-k^*-1}}\) 中，每一层的块数仍至少为
\(\ell-1\)。应用循环 \(\ell\)-primary 进位层覆盖定理，得到缩放和集为整个
\(C_{\ell^{a-k^*-1}}\)；乘回 \(\ell^{k^*+1}\) 即得 (5)。证毕。

## 3. 目标缺失的严格商二分

将源和集分成
\[
S=S_{\le k^*}+S_{>k^*},
\]
其中 \(S_{\le k^*}\) 只使用层号不超过 \(k^*\) 的块。由 (5)
\[
S=S_{\le k^*}+H_{>k^*}
 =\pi_{k^*}^{-1}\bigl(\pi_{k^*}(S_{\le k^*})\bigr),
\tag{6}
\]
其中
\[
\pi_{k^*}:H\longrightarrow
H/H_{>k^*}\simeq C_{\ell^{k^*+1}}.
\tag{7}
\]
因此对任意目标锚点 \(\tau\in H\)，若 \(\tau\notin S\)，必有
\[
\boxed{
\pi_{k^*}(\tau)\notin\pi_{k^*}(S_{\le k^*}).
}
\tag{8}
\]

当 \(k^*<a-1\) 时，(7) 是严格较小的循环 primary 商：
\[
|C_{\ell^{k^*+1}}|=\ell^{k^*+1}<\ell^a.
\tag{9}
\]
高层块全部映为单位元，不能在商层再次收费。回执为
'HIGHEST_PRIMARY_DEFICIT_QUOTIENT'，内容包括 \(k^*\)、被吸收的高层列、
投影目标和投影源块。

当 \(k^*=a-1\) 时没有非平凡高层尾，(8) 退化为原群中的
'TOP_PRIMARY_DIGIT_DEFICIT'；其严格见证是
\[
c_{a-1}\le\ell-2.
\tag{10}
\]
这时不得伪造更小商，应该把最高层的所有合法源列和目标数字记录给广义
\(2^j\)/primary 终端。

若不存在最高不足层，则 \(c_r\ge\ell-1\) 对所有 \(r\)，循环 primary 进位层
覆盖定理给出 \(S=H\)。于是：

* \(\tau\in H\) 时直接得到 Type II 目标命中；
* 若锚点本身不在当前差分群，则输出 'ANCHOR_OUTSIDE_DIFFERENCE'，不能把它称为
  层容量失败。

## 4. 递归和良基性

在 \(k^*<a-1\) 的分支中，商状态的指数从 \(a\) 变为 \(k^*+1\)，严格下降；
投影后的块只保留层号不超过 \(k^*\)，高层块永久标记
'ABSORBED_PRIMARY_TAIL'。对商状态重复 (2)--(8)，得到一个按指数严格下降的
有限递归，直到命中、锚点外置、顶层数字缺口或所有层饱和。

如果某个缺口同时出现在多个层，先取最高层使 (5) 可用；较低层的缺口留在严格
较小商内重新计算，不能把高层和低层的容量缺口相加为两个独立目标。这个规范化
消除了“先处理低层会重复收费高层”的分支歧义。

## 5. 与整数 source-switch 和 q-height 的接口

式 (5)--(9) 是有限群层面的精确递降。要把
'HIGHEST_PRIMARY_DEFICIT_QUOTIENT' 升级为原猜想的可提升 Type II relay，必须保存：

1. 被吸收高层块的真实 q-height、来源标签和同一参数纤维证明；
2. 投影源列与目标锚点的 SNF/CRT 关系；
3. 投影后参数 \(D'\)、\(A'\) 的正性、范围和 \(B'>A'\)；
4. E1--E5 全域解提升以及严格算术势下降。

若其中任一门失败，回执为
'PRIMARY_TAIL_LIFT_OBSTRUCTED'，并把 (8) 作为有限 primary/Fourier 输入；
不能将抽象的 \(C_{\ell^{k^*+1}}\) 自动标成整数递降。对 \(\ell=2\)，
(10) 和递归商正是广义 \(2^j\) 终端的规范入口。

## 6. 边界例子

### 严格尾压缩

在 \(H=C_{16}\) 中取一个层 \(2\) 块 \(\{0,4\}\) 和一个层 \(3\) 块
\(\{0,8\}\)，没有层 \(0,1\) 块。此时
\[
(c_0,c_1,c_2,c_3)=(0,0,1,1),
\qquad k^*=1.
\]
高层和集为
\(\{0,4,8,12\}=4C_{16}\)，所以目标 \(1\) 的缺失严格降到
\(C_4=C_{16}/4C_{16}\)，投影高层列全部消失。

### 顶层缺口

在 \(H=C_8\) 中取层 \(0\) 块 \(\{0,1\}\) 和层 \(1\) 块 \(\{0,2\}\)，则
\((c_0,c_1,c_2)=(1,1,0)\)。最高不足层是 \(k^*=2=a-1\)，没有非平凡尾；
\(c_2=0\) 是规范的 'TOP_PRIMARY_DIGIT_DEFICIT'，不能把它误写成严格商。

## 研究边界

本主张把“某个 primary 层不足”进一步规范为饱和高尾吸收、严格较小商或顶层
广义 \(2^j\) 缺口，并给出按指数下降的有限递归。它仍不证明每个实际 Type II 状态
都满足独立二点块和同纤维 source-switch；整数提升门、跨状态标签分派和目标锚点
外置分支仍需由统一选择器的其它证书闭合。
