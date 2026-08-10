---
kind: claim
claim_id: type-II-raw-normal-form-sqrt-cutoff
title: Type II 正规形的 sqrt(p) 有界 raw 盒
statement: 对每个 p=1 mod 4 的素数及任意 Type II 证书的互素正规形 x=ABC、d=A^2C、K=(A+B)/m，令 h=4ACK-1。则 h 整除 p+4A^2C，且 4A^2C <= p+2A/K；因而 A <= floor((1+sqrt(1+4p))/4)，C <= floor((p+2A)/(4A^2))，并且 K <= floor((p+4A^2C+1)/(4AC))。所有 Type II 正规形都落在这个逐素数有限盒中；盒内满足 h | Kp+A 和 A <= (Kp+A)/h 的三元组由 raw 正规形直接给出 Type II 证书。另有 m <= p/3+(1+sqrt(1+4p))/3 的普适缺口上界。这是有限化与 O(sqrt(p)) 短化，不是全局常数 A 界或猜想证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-coprime-factor-normal-form
  - type-II-raw-ray-certificate
  - type-II-arithmetic-lift-raw-factor-fallback
topics:
  - type-II
  - raw-ray
  - normal-form
  - finite-search
  - sqrt-bound
  - short-certificate
  - arithmetic-lift
  - proof-program
sources:
  - claim: type-II-coprime-factor-normal-form
    role: coprime-normal-form
  - claim: type-II-raw-ray-certificate
    role: raw-certificate-construction
  - claim: type-II-arithmetic-lift-raw-factor-fallback
    role: fixed-factor-finite-fallback
  - reproduction: reproductions/type_ii_raw_normal_form_sqrt_cutoff.py
    role: bounded-box-controls
visibility: public
last_checked: '2026-08-10'
---

# Type II 正规形的 \(\sqrt p\) 有界 raw 盒

## 定理

令 \(p\equiv1\pmod4\) 为素数，并令一张 Type II 证书的互素正规形为

\[
x=ABC,\qquad d=A^2C,\qquad \gcd(A,B)=1,\qquad A\le B,
\]

\[
m=\frac{A+B}{K},\qquad K\in\mathbb N.
\]

由正规形恒等式定义

\[
h=4ACK-1.
\tag{1}
\]

则有

\[
hB=Kp+A,
\tag{2}
\]

\[
h\mid p+4A^2C,
\tag{3}
\]

以及精确的序差公式

\[
B-A=\frac{K(p-4A^2C)+2A}{h}.
\tag{4}
\]

因此

\[
4A^2C\le p+\frac{2A}{K}\le p+2A.
\tag{5}
\]

特别地，定义

\[
A_{\max}(p)=\left\lfloor\frac{1+\sqrt{1+4p}}4\right\rfloor,
\tag{6}
\]

则每一张 Type II 正规形都满足

\[
1\le A\le A_{\max}(p),
\tag{7}
\]

\[
1\le C\le C_{\max}(p,A):=
\left\lfloor\frac{p+2A}{4A^2}\right\rfloor.
\tag{8}
\]

另一方面，因 \(h\mid p+4A^2C\) 且 \(h>0\)，

\[
4ACK=h+1\le p+4A^2C+1,
\]

所以

\[
1\le K\le K_{\max}(p,A,C):=
\left\lfloor\frac{p+4A^2C+1}{4AC}\right\rfloor.
\tag{9}
\]

于是

\[
\mathcal B(p)=
\left\{(A,C,K):
\begin{array}{l}
1\le A\le A_{\max}(p),\\
1\le C\le C_{\max}(p,A),\\
1\le K\le K_{\max}(p,A,C)
\end{array}
\right\}
\tag{10}
\]

是包含全部 Type II 正规形的显式有限盒。盒内三元组若满足

\[
h=4ACK-1\mid Kp+A,
\qquad
A\le B:=\frac{Kp+A}{h},
\tag{11}
\]

则 raw 正规形引理直接给出

\[
m=\frac{A+B}{K},\qquad x=ABC,\qquad d=A^2C
\]

的 Type II 证书；若再有 \(\gcd(A,B)=1\)，它就是互素正规形。故 (10)--(11)
给出所有正规形的有限算术搜索判据，而不需要先固定一个可能遗漏来源的 \(h\) 或
一个无界的 \(K\) 搜索。

## 普适缺口上界

由 (2)，

\[
m=\frac{A+B}{K}
 =\frac p h+\frac A K\left(1+\frac1h\right).
\tag{12}
\]

因 \(A,C,K\ge1\)，有 \(h\ge3\)。结合 \(K\ge1\) 和 (6)，得到

\[
\boxed{
m\le\frac p3+\frac{4A}{3}
 \le\frac p3+\frac{1+\sqrt{1+4p}}3.
}
\tag{13}
\]

所以全部 Type II 正规形都有 \(m\le p/3+O(\sqrt p)\)。这比自然范围
\(m\le p-2\) 有实质的主项收缩，但不能替代需要常数级或 \(o(\sqrt p)\) 缺口的
更强短证书猜想。

后续的线性平方参数化已经在核心素数范围把这里的上界严格加强为
\(m<p/3\)；式 (13) 仍保留为一般 \(p\equiv1\pmod4\) 的 raw 正规形界。见
[Type II 的线性平方因子分配与核心缺口隔离线](type-II-linear-square-gcd-allocation-core-gap-cutoff.md)。

## 证明

由正规形恒等式 \(p=4ABC-m\) 和 \(Km=A+B\)，直接计算

\[
Kp+A=4KABC-(A+B)+A
 =(4ACK-1)B=hB,
\]

得到 (2)。再有

\[
K(p+4A^2C)=Kp+4A^2CK
 =hB-A+A(h+1)=h(A+B).
\]

而 \(h\equiv-1\pmod K\)，故 \(\gcd(h,K)=1\)，从而得到 (3)。将

\[
B=\frac{Kp+A}{h}
\]

代入 \(B-A\) 即得 (4)。由于 \(A\le B\)，式 (4) 的分子非负，得到 (5)。丢去
\(C\ge1\) 和 \(K\ge1\) 分别得到

\[
4A^2-2A-p\le0,
\qquad
4A^2C\le p+2A,
\]

其正根给出 (6)--(8)。又 (3) 给出 \(h\le p+4A^2C\)，与 (1) 合并即得 (9)。

反向部分正是非互素 raw 正规形引理：(11) 使 \(B\) 为正整数且 \(A\le B\)，于是
\(m,x,d\) 满足 Type II 的全部整除、范围和序条件；互素条件只负责把坐标归一化。
最后，(12) 来自 (2)，利用 \(h\ge3\)、\(K\ge1\) 和 (6) 即得 (13)。证毕。

## 控制与边界

### \(p=73\)

三元组

\[
(A,C,K)=(1,1,2),\qquad h=7,\qquad B=21,\qquad m=11
\]

以及

\[
(A,C,K)=(2,2,1),\qquad h=15,\qquad B=5,\qquad m=7
\]

都落在盒 (10) 中，并分别给出直接和 raw 回退 Type II 证书。第二个控制同时展示
旧 D-格候选为空时 raw 三元组仍可能命中。

### \(p=313\) 的非互素原始坐标

\[
(A,B,C,K)=(2,40,1,6),
\]

给出 \(h=47,m=7\) 的 Type II 证书，虽然 \(\gcd(A,B)=2\)。它先由 (11) 被盒
捕获，再归一化到互素坐标；这说明完备搜索不应把互素性当作 raw 证书的必要门。

### \(p=878089\) 的共享正规形

已有共享证书

\[
(A,B,C,K)=(83,529,5,12),
\qquad h=19919,
\qquad m=51
\]

满足 (5)--(9)。这里 \(A=83\) 仍远低于
\(A_{\max}(878089)=468\)，但它同时说明固定常数 \(A\) 盒不能从小规模现象直接
外推；共享选择器的 \(A\le68\) 强化已经被该点否定。

## 研究边界

这个引理把 raw Type II 的未知参数从“任意正整数三元组”压缩为逐素数有限盒，并
给出 \(O(\sqrt p)\) 级的 \(A\) 和缺口控制。它没有给出与 \(p\) 无关的常数 \(A,C\)
上界，也没有证明盒内一定有命中；盒内全空仍需转交 Type I/F/G 容量、raw 关系
Fourier 或严格可提升递降。它也不把有限枚举自动升级为全局选择器证明。

## 定向复现

```bash
python3 reproductions/type_ii_raw_normal_form_sqrt_cutoff.py --verify
```
