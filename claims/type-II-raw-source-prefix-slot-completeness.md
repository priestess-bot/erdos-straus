---
kind: claim
claim_id: type-II-raw-source-prefix-slot-completeness
title: Type II raw 来源前缀的 K 同余槽完备性
statement: 对 p=1 mod 4 的素数和任意声明的 raw 来源前缀 u>1，利用 Type II 正规形的有限 A/C/K 盒，u | (4ACK-1) 的所有候选 K 恰由 gcd(u,4AC)=1 及 K=(4AC)^(-1) mod u 的有限同余槽给出；再筛 h | Kp+A 与 A <= (Kp+A)/h，所得集合非空当且仅当存在携带前缀 u 的 raw Type II 正规形。槽集为空或 E4/序门对全部槽失败时，给出 raw 分支的完备算术障碍；对有限前缀族按规范化物理记录去重后得到 source-column raw 边的完备菜单，但不能排除非 raw Type I/II 路线。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-raw-normal-form-sqrt-cutoff
  - type-II-raw-ray-certificate
  - type-II-source-column-escape-finite-expansion-relay
  - type-II-hall-fiber-arithmetic-closure-trichotomy
topics:
  - type-II
  - raw-ray
  - source-column
  - source-prefix
  - finite-search
  - congruence
  - capacity
  - arithmetic-obstruction
  - proof-program
sources:
  - claim: type-II-raw-normal-form-sqrt-cutoff
    role: finite-A-C-K-box
  - claim: type-II-raw-ray-certificate
    role: raw-certificate-equivalence
  - claim: type-II-source-column-escape-finite-expansion-relay
    role: source-column-expansion-interface
  - reproduction: reproductions/type_ii_raw_source_prefix_slot_completeness.py
    role: prefix-slot-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II raw 来源前缀的 \(K\) 同余槽完备性

## 1. 前缀槽定义

固定 \(p\equiv1\pmod4\) 素数，并使用
[Type II 正规形的有限 raw 盒](type-II-raw-normal-form-sqrt-cutoff.md) 的记号

本卡的槽枚举暂不要求 \(\gcd(A,B)=1\)：盒的上界只使用 \(A\le B\)。命中后可按
\(g=\gcd(A,B)\) 规范化为
\[
(A_0,B_0,C_0,K_0)=(A/g,B/g,Cg^2,K/g),
\]
且 \(A_0C_0K_0=ACK\)，所以 \(h=4ACK-1\) 和来源前缀不变。

\[
1\le A\le A_{\max}(p),
1\le C\le C_{\max}(p,A),
1\le K\le K_{\max}(p,A,C).
\tag{1}
\]

对一个正整数来源前缀 \(u>1\)，令

\[
h_{A,C,K}=4ACK-1.
\tag{2}
\]

固定 \(A,C\)。若 \(\gcd(u,4AC)>1\)，则

\[
u\nmid h_{A,C,K}
\quad\text{对所有 }K,
\tag{3}
\]

因为 \(u\mid h\) 会强制 \(4ACK\equiv1\pmod u\)，与公共因子矛盾。若
\(\gcd(u,4AC)=1\)，令 \(r_{u,A,C}\in\{1,\ldots,u\}\) 是

\[
r_{u,A,C}\equiv(4AC)^{-1}\pmod u.
\tag{4}
\]

则全部前缀可用 \(K\) 槽恰为

\[
\mathcal K_u(p;A,C)=
\{K:1\le K\le K_{\max}(p,A,C),\quad
K\equiv r_{u,A,C}\pmod u\}.
\tag{5}
\]

其槽数是精确的

\[
S_u(p;A,C)=
\begin{cases}
\max\left(0,1+\left\lfloor
\dfrac{K_{\max}(p,A,C)-r_{u,A,C}}u
\right\rfloor\right),&\gcd(u,4AC)=1,\\[6pt]
0,&\gcd(u,4AC)>1.
\end{cases}
\tag{6}
\]

定义总的 raw 前缀预容量

\[
S_u(p)=\sum_{A=1}^{A_{\max}(p)}
\sum_{C=1}^{C_{\max}(p,A)}S_u(p;A,C).
\tag{7}
\]

这里 \(S_u\) 只是通过 \(u\mid h\) 的预筛槽数，不是 Type II 证书数，也不允许把
不同 \((A,C)\) 的同一物理来源标签直接相加为 q 容量。

## 2. raw 边的精确筛选

在槽 (5) 上再施加真实算术门

\[
h_{A,C,K}\mid Kp+A,
\quad
B_{A,C,K}:=\frac{Kp+A}{h_{A,C,K}}\ge A.
\tag{8}
\]

定义

\[
\mathcal R_u(p)=
\left\{(A,C,K):
\begin{array}{l}
(A,C,K)\text{ 满足 (1)},\\
K\in\mathcal K_u(p;A,C),\\
\text{且 (8) 成立}
\end{array}
\right\}.
\tag{9}
\]

则有充要等价：

\[
\boxed{
\mathcal R_u(p)\ne\varnothing
\quad\Longleftrightarrow\quad
\text{存在 raw Type II 正规形 }(A,B,C,K)\text{ 且 }u\mid(4ACK-1).
}
\tag{10}
\]

当 (9) 非空时，字典序最小元素给出规范 raw edge；令

\[
h=4ACK-1,
m=\frac{A+B}{K},\quad x=ABC,\quad d=A^2C,
\tag{11}
\]

即可构造 Type II 短证书，并保留 \(u\mid h\) 的来源前缀 provenance。

当 \(S_u(p)=0\) 时，(3)--(6) 给出
`RAW_SOURCE_PREFIX_CONGRUENCE_EMPTY`。当 \(S_u(p)>0\) 但
\(\mathcal R_u(p)=\varnothing\) 时，逐个保存所有前缀槽的 E4 整除失败或序条件失败，
输出
`RAW_SOURCE_PREFIX_E4_ORDER_EMPTY`。后者不是单个失败行，而是有限槽全集及其
失败门的集合证书；只保留一个失败样本不足以证明空集。

## 3. 与 source-column 扩张的接线

令 \(\mathcal U\) 是一个已经通过 q-prefix/shared-q 规范化的有限来源前缀集合。把
每个 \(u\in\mathcal U\) 的 \(\mathcal R_u(p)\) 作为 raw source-column edge
菜单，并按规范化物理记录 \((m,x,d,h)\) 去重、按前缀标签保留 provenance。则：

1. 任意携带某个 \(u\in\mathcal U\) 的 raw Type II 边都在该菜单中；
2. 菜单中每条记录都是真实 raw Type II 边，而不是抽象残数乘积；
3. 某个 \(u\) 的菜单为空时，只能把该前缀的 **raw 分支** 标记为
   `RAW_SOURCE_PREFIX_EDGE_OBSTRUCTED`，然后转入非 raw Type I/II、Fourier 或
   source-column 的其它已定义分支，不能把它误写成全局无边或递降。

这里的 \(u\) 必须已有独立的来源标签、q-prefix 或 shared-q 语义；任意事后挑选的
整数因子虽然可以运行 (5)--(9)，但只能是 raw 算术探针，不能自动登记为 owner edge。

因此，原 source-column 有限扩张引理中“已完成同纤维合法边枚举”的假设，在 raw
正规形子分支内可以由 (1)--(9) 独立证明；未闭合处被精确限制为非 raw 来源或
E1--E5 的整数回译接口。

## 4. 证明

由有限 raw 盒定理，任意 raw Type II 参数的 \((A,C,K)\) 满足 (1)。若其 raw 因子
\(h=4ACK-1\) 携带 \(u\)，则 \(4ACK\equiv1\pmod u\)。这首先排除
\(\gcd(u,4AC)>1\) 的情形；在互素情形中，\(K\) 必且只须满足 (4)，故必落入
\(\mathcal K_u(p;A,C)\)。它还满足正规形的 (8)，所以属于 (9)。这证明正向包含。

反过来，(9) 的三元组满足 \(h\mid Kp+A\) 且 \(B\ge A\)，而 \(h=4ACK-1\)。
raw 正规形引理因此直接给出 (11) 的 Type II 证书；(5) 又保证 \(u\mid h\)。
所以 (10) 成立。若输入坐标不是互素，raw 正规形引理的规范化保持
\(ACK\)、\(h\)、\(m\)、\(x\) 和 \(d\)，因此不产生一个遗漏的前缀边；物理菜单
按 \((m,x,d,h)\) 去重即可消除这类坐标重复。

式 (6) 是一个固定首项 \(r_{u,A,C}\) 的等差数列在有限区间
\([1,K_{\max}]\) 中的精确计数。有限前缀族的去重只合并同一个规范化物理记录，不合并
不同来源标签；故第 3 节的三个结论保持 source provenance 和物理容量语义。证毕。

## 5. 控制实例

### \(p=73\) 的两个 raw source edge

对 \(u=7\)，前缀菜单唯一命中

\[
(A,C,K,h,B,m)=(1,1,2,7,21,11).
\tag{12}
\]

对 \(u=15\)，唯一命中为

\[
(A,C,K,h,B,m)=(2,2,1,15,5,7).
\tag{13}
\]

这两个边分别对应直接 \(h=7\) 和旧 D-格空集后的 raw 回退。

### \(p=313\) 的非互素坐标去重

前缀 \(u=47\) 同时出现原始坐标
\((A,B,C,K)=(2,40,1,6)\) 和规范坐标 \((1,20,4,3)\)。二者都有
\(h=47,m=7,x=80,d=4\)，故 raw 菜单只保留一个物理记录，并保留两条
source provenance。

### \(p=97\) 的伪池化前缀空集

对 \(u=143=11\cdot13\)，有限盒中有 6 个预筛 \(K\) 槽，但全部不满足
\(h\mid Kp+A\)，故

\[
S_{143}(97)>0,
\mathcal R_{143}(97)=\varnothing.
\tag{14}
\]

这把 \(11\cdot13\equiv-1\pmod{24}\) 的伪池化直接归类为
`RAW_SOURCE_PREFIX_E4_ORDER_EMPTY`，而不是 Type II 证书。

### \(p=878089\) 的共享 raw edge

对 \(u=19919\)，唯一控制命中为

\[
(A,C,K,h,B,m)=(83,5,12,19919,529,51).
\tag{15}
\]

它保留共享正规形的来源前缀，并落在 \(A_{\max}(p)=468\) 的有限盒中。

## 研究边界

本引理完成了 raw source-column 菜单的算术完备性和有限槽容量映射，但只覆盖
“某个声明前缀 \(u\) 必须整除 raw 因子 \(h\)”的分支。它没有证明每个 Fourier/Rado
源列都能得到这样的整数前缀，也没有把 `RAW_SOURCE_PREFIX_E4_ORDER_EMPTY` 自动
升级为严格递降；后两项仍需非 raw Type I/II、源关系 Fourier 或 E1--E5 回译。

## 定向复现

```bash
python3 reproductions/type_ii_raw_source_prefix_slot_completeness.py --verify
```
