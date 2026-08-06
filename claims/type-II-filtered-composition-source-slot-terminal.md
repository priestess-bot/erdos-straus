---
kind: claim
claim_id: type-II-filtered-composition-source-slot-terminal
title: Type II 同纤维过滤合成列源槽终端
statement: 在固定 Type II 参数纤维中，设相对于同一可除性账本而可独立选择的物理源槽，在有限阿贝尔目标群的一个素数阶合成列上逐层提供 ell_j-1 个新商非零块。则这些二点块的积集覆盖整个目标子群；若相对目标为 -1，且最终稳定子商可回放到原群，则得到实际 Type II 短证书。该条件允许块携带已覆盖低层分量，不要求按固定 primary 直和坐标分组。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-multiprimary-digit-terminal
  - type-II-source-fiber-low-rank-lock-cyclic-terminal
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-raw-ray-certificate
topics:
  - type-II
  - source-fiber
  - composition-series
  - finite-abelian-groups
  - cauchy-davenport
  - source-slots
  - stabilizer
  - constructive-certificate
  - proof-boundary
sources:
  - reproduction: reproductions/type_ii_filtered_composition_terminal.py
    role: focused C2-times-C2 filtered-chain and Type-II certificate verifier
  - result: reproductions/type-ii-filtered-composition-terminal-results.json
    role: replayable p-3313 construction receipt
visibility: public
last_checked: '2026-08-06'
---

# Type II 同纤维过滤合成列源槽终端

## 1. 设置和物理源槽

固定一个 Type II 参数纤维

\[
D_*\mid D,\qquad A\mid D_*,
\qquad \frac{D_*}{A}\text{ squarefree},
\qquad 4AD_*<p,
\tag{1}
\]

并记

\[
M=4D_*,
\qquad
N=p+4AD_*.
\tag{2}
\]

可选地先固定一个基积

\[
h_0\mid N,\qquad (h_0,M)=1.
\]

一个**物理源槽**是带来源标签的因子选择 \(q_c\mid N\)、\((q_c,M)=1\)。相对于这个
\(h_0\)，一族槽可独立选择的意思是：任取其中的子集 \(I\)，都有

\[
h_0\prod_{c\in I}q_c\mid N,
\]

并且全部槽属于同一个参数纤维；\(h_0=1\) 是允许的特例。若同一素数出现在多个来源标签
中，独立性必须由实际的 \(v_q(N)\) 账本支付；不能把标签数误作可重复的 \(q\) 槽。

令 \(H\) 是该纤维中由这些可用槽生成的有限阿贝尔目标子群。用乘法记号取一条合成列

\[
1=H_0<H_1<\cdots <H_L=H,
\qquad
H_j/H_{j-1}\simeq C_{\ell_j},
\tag{3}
\]

其中每个 \(\ell_j\) 是素数。对第 \(j\) 层，选择彼此不复用的
\(\ell_j-1\) 个物理槽 \(q_{j,1},\ldots,q_{j,\ell_j-1}\)，并要求其残数满足

\[
q_{j,i}\bmod M\in H_j\setminus H_{j-1}.
\tag{4}
\]

这里不要求 \(q_{j,i}\) 只落在某个固定直和 primary 坐标中。它可以带有已经覆盖的
低层分量；(4) 只要求其在当前素数阶商中非平凡。

## 2. 过滤合成列覆盖定理

设 \(P\) 是所有被选二点块的积集：

\[
P=\prod_{j=1}^{L}\prod_{i=1}^{\ell_j-1}
\{1,q_{j,i}\}\subseteq H.
\tag{5}
\]

则

\[
\boxed{P=H.}
\tag{6}
\]

### 证明

对 \(j\) 归纳。假设前 \(j-1\) 层的块已覆盖 \(H_{j-1}\)。将第 \(j\) 层投影到
\(H_j/H_{j-1}\simeq C_{\ell_j}\)。每一个二点块变为
\(\{0,\bar q_{j,i}\}\)，其中 \(\bar q_{j,i}\ne0\)。Cauchy--Davenport 的逐次形式给出

\[
\left|
\sum_{i=1}^{\ell_j-1}\{0,\bar q_{j,i}\}
\right|
\ge
\min\{\ell_j,\ 1+(\ell_j-1)\}
=\ell_j.
\tag{7}
\]

所以这些投影覆盖整个商。归纳假设已允许乘上任意 \(H_{j-1}\) 元素，故每个商陪集均被
完整覆盖，前 \(j\) 层的积集就是 \(H_j\)。取 \(j=L\) 即得 (6)。

阈值 \(\ell_j-1\) 是尖锐的：在 \(C_{\ell_j}\) 中只给
\(\ell_j-2\) 个非平凡二点块，和集可以仍少一个元素。

### 过滤层缺口推论

对同一基积账本下所有残数非平凡的可用槽，按其唯一的层号定义

\[
c_j=\#\{q_c:\ q_c\bmod M\in H_j\setminus H_{j-1}\}.
\tag{8}
\]

若相对目标 \(t\in H\) 不能由任何账本合法的槽子集命中，则必有

\[
\boxed{\exists j,\qquad c_j\le\ell_j-2.}
\tag{9}
\]

事实上，若所有 \(c_j\ge\ell_j-1\)，就从每一层取 \(\ell_j-1\) 个互不复用槽；
共同账本保证这个选择仍可实际相乘。由 (6) 得到 \(P=H\)，从而命中 \(t\)，矛盾。
所以 (9) 是一个带合成列层号、实际来源标签和 \(q\)-账本的容量缺口，而不是由未命中
反推出的递降或反例。

## 3. 从覆盖到 Type II 短证书

设已有基积的相对目标

\[
t=(-1)\,h_0^{-1}\pmod M
\tag{10}
\]

属于 \(H\)。由 (6) 可选取一个槽子集 \(I\)，令

\[
s=\prod_{c\in I}q_c,\qquad h=h_0s.
\]

由同一账本的独立性，\(h\mid N\)，并且

\[
h\equiv-1\pmod {4D_*}.
\tag{11}
\]

令

\[
K=\frac{h+1}{4D_*},
\qquad
C=\frac{D_*}{A},
\qquad
B=\frac{Kp+A}{h}.
\tag{12}
\]

因为

\[
4D_*(Kp+A)=hp+N,
\tag{13}
\]

且 \((h,4D_*)=1\)，由 \(h\mid N\) 知 \(B\) 为正整数。并且

\[
B-A
=\frac{K(p-4AD_*)+2A}{h}>0.
\tag{14}
\]

又 \(h=4ACK-1\)。因此现有 Type II 因子正规形给出一张实际短证书；不需要在这里
重新假设 \((A,B)=1\)，因为可按既有 raw-ray 规则规范化。

若 (5) 是在稳定子商 \(G/T\) 中验证的，不能仅凭商命中升级。必须对最终完整积集
\(h_0P\) 重算 \(T=\operatorname{Stab}(P)\)，验证所用槽的同纤维来源、完整账本和
\(PT=P\)，再把商中命中回放为原群中的 \(-1\in h_0P\)。缺少这一最终饱和门时，输出
只能是商级分析证书。

## 4. 非冗余性

[多 primary 进位终端](type-II-source-fiber-multiprimary-digit-terminal.md)要求块先按固定
primary 直和因子分组，并要求那些因子的素数彼此不同。这里改用任意素数阶合成列：
同一 primary 的不同秩，或带有已覆盖低层分量的块，都可通过 (4) 被使用。下面的
\(U(12)\simeq C_2^2\) 样例不能写成旧定理所要求的互异 primary 直和，因而是这个
扩张的定点见证，而非仅改变记号。该结论仍是充分条件，不证明每个参数纤维都能提供这些
同纤维物理槽。

## 5. 定点构造

取原始 source-lattice 输入

\[
p=3313,\qquad D=12,\qquad
(a_1,h_1)=(4,5),\qquad (a_2,h_2)=(2,7),
\tag{15}
\]

并在候选纤维取

\[
A=1,\qquad D_*=3,\qquad M=12,\qquad N=3325=5^2\cdot7\cdot19.
\tag{16}
\]

这里取 \(h_0=1\)。

两条来源都属于这个纤维，因为

\[
5\mid3313+4\cdot12\cdot4,\qquad
7\mid3313+4\cdot12\cdot2,
\tag{17}
\]

\[
AD_*=3\equiv12\cdot4\pmod5,\qquad
3\equiv12\cdot2\pmod7.
\tag{18}
\]

在 \(U(12)\simeq C_2^2\) 中取

\[
1<\langle5\rangle<U(12).
\tag{19}
\]

因子 \(5\) 和 \(7\) 是同纤维、互不复用的物理槽；它们分别在两层 \(C_2\) 商中非平凡，
且

\[
\{1,5\}\{1,7\}=U(12),
\qquad
5\cdot7=35\equiv-1\pmod {12}.
\tag{20}
\]

于是

\[
K=3,\qquad B=284,\qquad (A,B,C,K)=(1,284,3,3).
\tag{21}
\]

对应的 Type II 数据为

\[
m=95,\qquad x=852,\qquad d=3,
\tag{22}
\]

\[
\boxed{
\frac4{3313}
=\frac1{852}+\frac1{29817}+\frac1{8468028}.}
\tag{23}
\]

物理账本只使用一个 \(5\) 和一个 \(7\)，分别不超过
\(v_5(N)=2\)、\(v_7(N)=1\)。所有 \(N\) 的单素因子残数均为 \(5\) 或 \(7\pmod {12}\)，
没有单槽已是 \(11=-1\pmod {12}\)。该例是链式终端绕过旧分组限制的正向回归样本，
不声称它来自一个已证明无法三角化的旧阻碍状态。

## 6. 边界

本定理不允许以下跳步：

1. 不能把不同参数纤维的来源槽池化；
2. 不能用同一 \(q\) 的多个标签超过 \(v_q(N)\)；
3. 不能把商中的 \(-1\) 命中当作未经稳定子饱和回放的整数证书；
4. 不能由某层不足 \(\ell_j-1\) 反推递降或猜想反例。

因此它给出的是一条新的、可核验的 Type II 终端充分条件和明确的过滤层缺口接口，而非
Erdős--Straus 猜想的全称闭合。

复现：

~~~bash
python3 reproductions/type_ii_filtered_composition_terminal.py --verify
~~~
