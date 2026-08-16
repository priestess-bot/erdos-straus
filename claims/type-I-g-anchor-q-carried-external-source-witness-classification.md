---
kind: claim
claim_id: type-I-g-anchor-q-carried-external-source-witness-classification
title: G-anchor Q-carried external-source witness 的完整分类
statement: >-
  对核心素数 p=1 (mod 24)，令 Q=(p-3)/2。对每个正整数 k|(p-1)/4，令
  q=4k-1、n=(qp+1)/(q+1)、M=kn。总有 gcd(Q,M)=gcd(Q,3q+1)。
  若 k>=2，则不存在正整数 g 满足 g|Q、g|M、g=-1 (mod q)。若 k=1，则这样的
  g 存在当且仅当 p=73 (mod 120)，且唯一为 g=5；它满足 g|n、g<=n，并给出
  显式 q=3 external-source 的 marked strict descent 与 Type I 证书。因此，G-anchor
  的 actual Q carrier 在完整 ordinary mixed/adaptive external-source 菜单中只有这一条
  Q-carried 例外；所有 k>=2 的该类 witness 必须来自 Q 以外。该结论不排除
  非 Q-carried witness、平方因子 e|M^2、其它 terminal 或其它 G exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - type-I-g-anchor-q-carried-external-source-witness-no-go
  - mixed-factor-external-source-descent
  - adaptive-external-source-descent
topics:
  - type-I
  - G-state
  - G-anchor
  - complete-excess-bundle
  - external-source
  - marked-descent
  - q-3
  - gcd-intersection
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: actual-Q-carrier
  - claim: type-I-g-anchor-q-carried-external-source-witness-no-go
    role: raw-label-special-case
  - claim: mixed-factor-external-source-descent
    role: witness-to-marked-lift-and-Type-I-certificate
  - claim: adaptive-external-source-descent
    role: k-one-adaptive-subfamily
  - reproduction: reproductions/type_i_g_anchor_q_carried_external_source_witness_classification.py
    role: fixed-q-three-exception-and-k-ge-two-controls
visibility: public
last_checked: '2026-08-16'
---

# G-anchor \(Q\)-carried external-source witness 的完整分类

## 1. 问题与结论

固定核心素数

\[
p\equiv1\pmod{24},\qquad Q=\frac{p-3}{2}.
\tag{1}
\]

对任意正整数

\[
k\mid\frac{p-1}{4},\qquad q=4k-1,\qquad
n=\frac{qp+1}{q+1},\qquad M=kn,
\tag{2}
\]

mixed-factor external-source 的 witness 条件为

\[
g\mid M,\qquad g\le n,\qquad g\equiv-1\pmod q.
\tag{3}
\]

这里仅考察其中能从 G-anchor 的 actual complete-excess carrier \(Q\) 重复取到的
witness，即再加 \(g\mid Q\)。结论是完整的：

\[
\boxed{
\begin{array}{c|c}
k&\text{\(Q\)-carried witness}\\
\hline
1&\text{当且仅当 }p\equiv73\pmod{120}\text{，唯一为 }g=5\\
k\ge2&\text{不存在}
\end{array}}
\tag{4}
\]

第一行不是纯粹的分类余项：它给出一条显式严格递降。第二行则说明所有较大尺度
ordinary mixed/adaptive external-source 若要成功，都必须使用 \(Q\) 以外的因子。

## 2. 不依赖 \(q\mid Q\) 的精确 gcd 恒等式

令

\[
a=\frac{p-1}{q+1}=\frac{p-1}{4k}.
\tag{5}
\]

由 (2)，\(a\) 是正整数，且

\[
p=(q+1)a+1,\qquad n=qa+1,\qquad Q=2ka-1.
\tag{6}
\]

因此

\[
(Q,k)=1,\qquad (Q,q+1)=1.
\tag{7}
\]

另一方面，

\[
(q+1)n=qp+1=2qQ+3q+1.
\tag{8}
\]

所以

\[
\begin{aligned}
(Q,M)
&=(Q,kn)\\
&=(Q,n)\\
&=(Q,(q+1)n)\\
&=\boxed{(Q,3q+1)}.
\end{aligned}
\tag{9}
\]

此前的 raw-label 交集公式是 (9) 在 \(q\mid Q\) 时的特例；推导中实际上完全没有
使用 \(q\mid Q\)。这使它成为整个 variable-\(k\) external-source 菜单的容量公式。

## 3. 所有 \(k\ge2\) 的 \(Q\)-内路径均为空

若 \(k\ge2\)，则 \(q=4k-1\ge7\)。设有正整数 \(g\) 满足

\[
g\mid Q,\qquad g\mid M,\qquad g\equiv-1\pmod q.
\tag{10}
\]

由 (9)，\(g\mid3q+1\)。故

\[
g=jq-1\qquad(j\ge1).
\tag{11}
\]

又 \(g\le3q+1\)，只可能 \(j=1,2,3\)。但：

\[
q-1\mid3q+1\quad\Longrightarrow\quad q-1\mid4,
\tag{12}
\]

这与 \(q\ge7\) 矛盾；以及

\[
0<q+2=(3q+1)-(2q-1)<2q-1,
\tag{13}
\]

\[
0<2=(3q+1)-(3q-1)<3q-1.
\tag{14}
\]

后二式分别排除 \(2q-1\) 与 \(3q-1\) 整除 \(3q+1\)。故 (10) 不可能。
注意这个论证甚至没有使用 \(g\le n\)，因此它同时覆盖 mixed-factor 以及更窄的
adaptive 外部源菜单。

## 4. 唯一的 \(q=3\) 例外与实际递降

若 \(k=1\)，则 \(q=3\) 且 \(M=n\)。由 (9)，

\[
(Q,n)=(Q,10).
\tag{15}
\]

\(Q\) 是奇数，因此一个同时满足 \(g\mid Q\)、\(g\mid n\) 及
\(g\equiv-1\pmod3\) 的正整数只能是 \(g=5\)。这样的 \(g\) 存在当且仅当
\(5\mid Q\)，即

\[
p\equiv3\pmod{10}.
\tag{16}
\]

与 \(p\equiv1\pmod{24}\) 合并，得到

\[
5\mid Q
\quad\Longleftrightarrow\quad
p\equiv73\pmod{120}.
\tag{17}
\]

写 \(p=120t+73\)。则

\[
n=\frac{3p+1}{4}=90t+55,\qquad
u=\frac{n+5}{3}=30t+20,\qquad
v=\frac{nu}{5}=(18t+11)(30t+20).
\tag{18}
\]

特别地 \(5\mid n\) 且 \(5\le n\)，所以 \(g=5\) 是 (3) 的实际 witness。直接有

\[
\frac4n=\frac1n+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p=\frac1{np}+\frac1u+\frac1v.
\tag{19}
\]

这是一条到 \(n<p\) 的显式 marked strict descent；由
mixed-factor-external-source-descent，它同时产生自然范围的 Type I 除子证书。这里该证书
可直接写为

\[
m=\frac{4g+1}{3}=7,\qquad D=\frac{u^2}{5}.
\tag{20}
\]

## 5. G/Type I 选择器的准确接口

\[
\text{actual \(Q\) carrier}
\ \longrightarrow\
\begin{cases}
q=3,\ p\equiv73\pmod{120}:&g=5\text{，显式 marked descent};\\
k\ge2:&\text{\(Q\)-carried external witness 空};\\
\text{其余 \(q=3\) 点}:&\text{\(Q\)-carried external witness 空}.
\end{cases}
\tag{21}
\]

因此，\(Q\) 不能被当作所有 ordinary external-source 分支的通用 witness 仓库。
这个容量门没有否定 external-source family：非 \(Q\)-carried 因子仍可能命中；
一般平方因子机制中的 \(e\mid M^2\) 也不受本卡排除。它只把全局选择器的
\(Q\)-内接口精确压缩为 (20)，避免把不存在的 \(Q\)-内 lift 计入递降势。

## 6. 定向回执

~~~bash
python3 reproductions/type_i_g_anchor_q_carried_external_source_witness_classification.py --verify
~~~

回执只检查四个固定控制：\(p=73,k=1\) 的正 \(q=3\) 例外；
\(p=97,k=1\) 的 \(q=3\) 未命中；\(p=97,k=2\) 的非 raw \(q=7\) 未命中；
以及 \(p=1873,k=3\) 的非平凡交集 \((Q,M)=17\) 仍未命中。它不扫描素数、
分母或 Reach history。
