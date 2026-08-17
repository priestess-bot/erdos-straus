---
kind: claim
claim_id: type-I-root-capacity-stutter-k-one-universal-exclusion
title: actual proper-root stutter 的 k=1 全称排除
statement: >-
  对核心素数 p≡1 mod24 的任意 actual proper-root stutter receipt，令
  b=e-1、N=a^2-ab+b^2=hk。则 k不等于1。证明先用 actual root 条件
  h|p^2+p+1 排除 gcd(a,b)>1；随后把抽象 k=1 整数曲线参数化为
  e=dx^2、a=dxy-1、gcd(x,y)=1，并由 p 的整性门得到
  a|(x-y)(x^2-xy-y^2)。共同因子排除把它收紧为
  x^2-xy-y^2=c(dxy-1)。保持 d,c 的两步 Vieta 无限下降强制 c=1，
  但 actual 模3条件给出 d≡2、3不整除x、3整除y，故等式两边分别为
  1与2 mod3，矛盾。该结论闭合 proper-root quotient 的 QC0 空域；
  它不 physicalize k>1 的 quotient carrier，也不闭合 proper-root 或 T6 totality。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-positive-definite-norm-bound
  - type-I-root-capacity-stutter-eisenstein-support
topics:
  - type-I
  - root-capacity
  - stutter
  - eisenstein-quotient
  - k-one
  - infinite-descent
  - universal-exclusion
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_root_capacity_stutter_k_one_universal_exclusion.py
    role: symbolic-identities-and-descent-invariant
visibility: public
last_checked: '2026-08-17'
---

# actual proper-root stutter 的 \(k=1\) 全称排除

## 1. 设置与结论

固定一个 actual proper-root stutter receipt。沿用

\[
p\equiv1\pmod {24},\qquad h=3u,\qquad (u,3)=1,
\qquad 2\le h<p,
\qquad h\mid p^2+p+1,
\tag{1}
\]

\[
b=e-1,\qquad a=em-h,\qquad
pa=e(h-1)+1,
\tag{2}
\]

以及

\[
1\le a<e,\qquad
N=a^2-ab+b^2=hk.
\tag{3}
\]

本卡证明

\[
\boxed{k\ne1.}
\tag{4}
\]

证明不枚举参数范围。actual 条件只在共同因子排除和最后的模 \(3\) 输入中使用；
中间的无限下降是一个纯整数命题。

## 2. Actual root 排除 \(\gcd(a,b)>1\)

反设 \(k=1\)，于是 \(h=N\)。令

\[
g_0=(a,b),\qquad a=g_0A,\qquad b=g_0B,
\qquad H=A^2-AB+B^2.
\tag{5}
\]

于是 \(h=g_0^2H\)。由 (2) 的等价形式 \(pa+b=eh\)，约去 \(g_0\) 得

\[
pA+B=eg_0H.
\tag{6}
\]

把 \(pA=eg_0H-B\) 代入 \(A^2(p^2+p+1)\)，直接展开得到精确恒等式

\[
\boxed{
A^2(p^2+p+1)
=H\left(e^2g_0^2H+eg_0(A-2B)+1\right).
}
\tag{7}
\]

另一方面，(1) 与 \(h=g_0^2H\) 给出某个正整数 \(v\) 使

\[
p^2+p+1=g_0^2Hv.
\]

代入 (7) 并约去正整数 \(H\)，括号必须等于 \(g_0^2A^2v\)，因而被
\(g_0^2\) 整除。但该括号模 \(g_0\) 恒等于 \(1\)。所以

\[
\boxed{(a,b)=g_0=1.}
\tag{8}
\]

这一步不能从抽象 stutter 曲线单独推出；它精确使用了 actual root 的
\(h\mid p^2+p+1\)。

## 3. 模 \(3\) 输入与 \(k=1\) 参数化

由 \(3\mid h=N\)，在 \(\mathbf F_3\) 中

\[
N=a^2-ab+b^2=(a+b)^2,
\]

所以 \(a+b\equiv0\pmod3\)。又 \(a\equiv em\pmod3\)、\(b=e-1\)，并且
(8) 排除 \(3\mid a,b\)。逐一检查 \(e\pmod3\)：

* \(e\equiv0\) 会给出 \(a\equiv0,b\equiv2\)，与 \(a+b\equiv0\) 矛盾；
* \(e\equiv1\) 会给出 \(a\equiv b\equiv0\)，与 (8) 矛盾；
* 因而只能有

\[
\boxed{e\equiv a\equiv2\pmod3,\qquad m\equiv1\pmod3.}
\tag{9}
\]

现在只使用 \(h=N=em-a\)。展开后有

\[
m=\frac{(a+1)^2}{e}+e-a-2,
\]

故 \(e\mid(a+1)^2\)。标准平方因子分裂给出正整数 \(d,x,y\)，使

\[
\boxed{
e=dx^2,\qquad a=dxy-1,\qquad (x,y)=1,\qquad 1\le y\le x.
}
\tag{10}
\]

具体地，若 \(g=(e,a+1)\)，写 \(e=gx,a+1=gy,(x,y)=1\)，则
\(e\mid(a+1)^2\) 强制 \(x\mid g\)，写 \(g=dx\) 即得 (10)。
由 (9)--(10)，

\[
\boxed{d\equiv2\pmod3,\qquad 3\nmid x,\qquad 3\mid y.}
\tag{11}
\]

特别地

\[
d\ge2,\qquad y\ge3,\qquad x>y.
\tag{12}
\]

令 \(Q=x^2-xy+y^2\)。代回可得完整闭式

\[
\boxed{
m=dQ-1,\qquad
h=d^2x^2Q-dx(x+y)+1,
}
\tag{13}
\]

\[
\boxed{
p=\frac{d^3x^4Q-d^2x^3(x+y)+1}{dxy-1}.
}
\tag{14}
\]

## 4. 整性门收紧为单个二次式

由 (2)，\(p\) 为整数要求

\[
a\mid e(h-1)+1.
\tag{15}
\]

因为 \((a,y)=1\)，在模 \(a=dxy-1\) 下有 \(e\equiv xy^{-1}\)。又
\(h=N\equiv(e-1)^2\pmod a\)，所以把 (15) 的被除数乘以 \(y^3\) 后得到

\[
\boxed{
a\mid x^3-2x^2y+y^3
=(x-y)(x^2-xy-y^2).
}
\tag{16}
\]

另一方面，\(b=dx^2-1\) 满足两个精确线性恒等式

\[
b-a=dx(x-y),
\qquad
xa-yb=y-x.
\tag{17}
\]

第一式说明 \((a,x-y)\mid(a,b)\)，第二式给出反向整除，故由 (8)

\[
\boxed{(a,x-y)=(a,b)=1.}
\tag{18}
\]

由 (16)--(18)，

\[
a\mid P_2,\qquad P_2=x^2-xy-y^2.
\tag{19}
\]

这里 \(P_2\ne0\)：否则 \(y\mid x^2\) 和 \((x,y)=1\) 先迫使 \(y=1\)，
继而 \(x^2-x-1=0\)，无整数解。若 \(P_2<0\)，则由 (12)

\[
0<-P_2=xy+y^2-x^2<xy<dxy-1=a,
\]

也不可能是 \(a\) 的非零倍数。因此 \(P_2>0\)，存在正整数 \(c\) 使

\[
\boxed{x^2-xy-y^2=c(dxy-1).}
\tag{20}
\]

## 5. 保持 \((d,c)\) 的无限下降

先证明

\[
0<c<x.
\tag{21}
\]

左侧来自 (20)。右侧由下列严格正分解得到：

\[
\begin{aligned}
x(dxy-1)-(x^2-xy-y^2)
&=(d-1)x^2y+(y-1)(x^2+x)+y^2\\
&>0.
\end{aligned}
\]

把 (20) 写成

\[
E(x,y):=x^2-(dc+1)xy-y^2+c=0.
\tag{22}
\]

若 \(y=1\)，则 (22) 模 \(x\) 给出 \(c\equiv1\pmod x\)，结合 (21) 立即得到
\(c=1\)。以下设 \(y>1\)，并令

\[
L=dc+1,
\qquad
q=\frac{y^2-c}{x}.
\tag{23}
\]

由 (22) 模 \(x\)，\(q\) 是整数。若 \(q<0\)，则正整数
\(c-y^2\) 是 \(x\) 的倍数，却由 (21) 严格小于 \(x\)，矛盾。若 \(q=0\)，
则 (22) 给出 \(x=Ly\)，从而 \((x,y)=y>1\)，仍矛盾。因此

\[
0<q=\frac{y^2-c}{x}<\frac{y^2}{x}<y,
\qquad x=Ly+q.
\tag{24}
\]

特别地 \((q,y)=(x,y)=1\)。再令

\[
r=\frac{q^2+c}{y}.
\tag{25}
\]

因为 \(q\equiv x\pmod y\)，而 (22) 模 \(y\) 给出
\(x^2+c\equiv0\pmod y\)，所以 \(r\) 是正整数。把 \(x=Ly+q\) 代回
(22)，还得到

\[
r=y-Lq,\qquad (q,r)=1.
\tag{26}
\]

这两次 Vieta 变换保持同一个方程：直接展开有

\[
\boxed{E(q,r)=E(x,y)=0.}
\tag{27}
\]

等价地，

\[
q^2-qr-r^2=c(dqr-1).
\tag{28}
\]

若 \(dqr-1=0\)，正整数性迫使 \(d=q=r=1\)，但 (28) 左边为 \(-1\)，
矛盾。所以 \(dqr-1>0\)，(28) 左边为正，进而 \(0<r<q\)。因此

\[
(x,y)\longmapsto(q,r)
\]

产生同一 \((d,c)\)、互素且满足同型方程的新正整数对，并且

\[
0<r<q<y<x.
\tag{29}
\]

同一个正分解 (21) 应用于新对 \((q,r)\)，还重新给出 \(c<q\)，所以 (23)--(29)
可按完全相同的条件继续迭代。反复应用会严格降低正整数首坐标，必在有限步后到达
第二坐标为 \(1\) 的情形；
该端点已经证明强制

\[
\boxed{c=1.}
\tag{30}
\]

## 6. 最终模 \(3\) 矛盾与边界

由 (20)、(30) 有 \(P_2=a\)。但 (11) 给出

\[
P_2=x^2-xy-y^2\equiv x^2\equiv1\pmod3,
\]

而 (9) 给出 \(a\equiv2\pmod3\)，矛盾。这证明 (4)。

因此 proper-root quotient 路线的 \(k=1\) 子域为空，QC0 已全称闭合。剩余的
proper-root quotient-carrier 量词严格位于 \(k>1\)：本卡没有把任何
\(q\mid k\) physicalize 为 actual occurrence 或 E1--E5 successor，也没有处理
transverse \(D_*\) 的全称出口。故它不是 proper-root 子域或 T6 的 totality claim。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_k_one_universal_exclusion.py --verify
```

脚本在一个标准库整数多项式环中核对 (7)、(13)--(17)、(21) 的正分解以及
Vieta 不变量 (27)。它不执行有限范围扫描；全称次序与严格不等式由上面的证明承担。
