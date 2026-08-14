---
kind: claim
claim_id: type-I-root-capacity-stutter-c-side-m-localization
title: proper-root stutter 的 C-side m 局部化与非平凡 T 余量
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，令
  C=(p^2-1)/2、D_C=gcd(D,C)、D_T=D/D_C，且
  m=(D+h-1)/p。则
  D_C=lcm(gcd(D,p+1),gcd(D,p-1))，并且
  D_C|lcm(m,m+2)=m(m+2)/gcd(m,2)。结合既有 D_C|h^2-1，得到
  D_C|gcd(h^2-1,lcm(m,m+2))。再由 actual proper-root 的 m≥3、
  m<1+sqrt(h)、h<p，可知 D_C<D，故 D_T>1；既有 C/T 因子分裂于是给出
  1<D_T|gcd(T,h^2-h-2r)。这排除了 actual proper-root stutter 的 D 完全停留在
  C-side；D_T 仍可与 C 共享素因子，结论本身不构造 Type I/II 证书、解提升或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-actual-small-root-exclusion
  - type-I-root-capacity-stutter-positive-definite-norm-bound
topics:
  - type-I
  - overflow
  - root-capacity
  - stutter
  - cyclotomic
  - divisor-filter
  - finite-menu
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: actual-C-T-factor-split-and-T-residual-divisibility
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: stutter-parameter-m-and-D-linearization
  - claim: type-I-root-capacity-stutter-actual-small-root-exclusion
    role: actual-m-at-least-three
  - claim: type-I-root-capacity-stutter-positive-definite-norm-bound
    role: proper-root-square-root-bound-for-m
  - reproduction: reproductions/type_i_root_capacity_stutter_c_side_m_localization.py
    role: fixed-localization-and-proper-shape-controls
visibility: public
last_checked: '2026-08-14'
---

# proper-root stutter 的 C-side \(m\) 局部化与非平凡 \(T\) 余量

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}.
\]

考虑 terminal-first 后的一个 actual maximal complete-excess proper-root stutter
receipt。沿用已有记号

\[
C=\frac{p^2-1}{2},\qquad
D_C=(D,C),\qquad D_T=\frac{D}{D_C},
\tag{1}
\]

以及 stutter 参数

\[
D=mp+1-h,\qquad D\mid ph+1,\qquad 2\le h<p.
\tag{2}
\]

这里的 \(D\) 仍必须是 actual receipt 的 canonical divisor，不能以任意满足 (2) 的
抽象整数替代。下面先证明一个只依赖 (2) 和 \(p\equiv1\pmod4\) 的局部化；随后才使用
actual proper-root 的 \(m\) 界。

## 2. \(p-1\) 与 \(p+1\) 部分由 \(m,m+2\) 控制

定义

\[
d_-= (D,p+1),\qquad d_+=(D,p-1).
\tag{3}
\]

由 \(D\mid ph+1\) 得到

\[
h\equiv1\pmod {d_-},\qquad h\equiv-1\pmod {d_+}.
\tag{4}
\]

将其代回 \(D=mp+1-h\)，分别在 \(p\equiv-1\pmod{d_-}\) 与
\(p\equiv1\pmod{d_+}\) 下化简，便有

\[
\boxed{d_-\mid m,\qquad d_+\mid m+2.}
\tag{5}
\]

接着逐素数比较 \(C=(p-1)(p+1)/2\) 的赋值。若 \(q\) 为奇素数，\(q\) 至多整除
\(p-1,p+1\) 中的一个，故 \(q\) 在 \(D_C\) 中的全部指数恰由 \(d_-\) 或 \(d_+\)
中的一个提供。对 \(q=2\)，写

\[
v_2(p-1)=a\ge2,\qquad v_2(p+1)=1,
\]

则 \(v_2(C)=a\)。若 \(\alpha=v_2(D)\)，有

\[
v_2(d_+)=\min(\alpha,a),\qquad
v_2(d_-)=\min(\alpha,1),
\]

其最大值仍是 \(\min(\alpha,a)=v_2(D_C)\)。因此得到精确恒等式

\[
\boxed{D_C=\operatorname{lcm}(d_-,d_+).}
\tag{6}
\]

由 (5) 立刻推出

\[
\boxed{
D_C\mid\operatorname{lcm}(m,m+2)
=\frac{m(m+2)}{(m,2)}.}
\tag{7}
\]

既有 C/T 因子分裂已给出 \(D_C\mid h^2-1\)，故完整的 C-side 必要条件为

\[
\boxed{
D_C\mid\gcd\!\left(h^2-1,\operatorname{lcm}(m,m+2)\right).}
\tag{8}
\]

与此前只使用 \(D_C\mid h^2-1\) 相比，(8) 把 C-side 容量从 \(h^2\) 级直接压到
\(m^2\) 级；proper-root 中 \(m\) 又处在平方根菜单内。

## 3. actual proper-root 不能完全停在 C-side

actual proper-root stutter 的已有结论给出

\[
m\ge3,\qquad m<1+\sqrt h,\qquad h<p.
\tag{9}
\]

由 (2) 和整数范围 \(h\le p-1\)，有

\[
D\ge(m-1)p+2.
\tag{10}
\]

先设 \(m=3\)。核心素数 \(p\equiv1\pmod{24}\) 满足 \(p\ge73\)，故

\[
D\ge2p+2\ge148>15=\operatorname{lcm}(3,5)\ge D_C.
\tag{11}
\]

若 \(m\ge4\)，由 (9) 有

\[
p>(m-1)^2.
\tag{12}
\]

于是

\[
D>(m-1)p>(m-1)^3\ge m(m+2)
\ge\operatorname{lcm}(m,m+2)\ge D_C.
\tag{13}
\]

其中最后的非平凡比较可写为

\[
(m-1)^3-m(m+2)=(m-4)(m^2+1)+3>0
\qquad(m\ge4).
\]

两种情形合并得到

\[
\boxed{D_C<D,\qquad D_T=\frac{D}{D_C}>1.}
\tag{14}
\]

已有 actual C/T 分裂还给出 \(D_T\mid T\) 与
\(D_T\mid h^2-h-2r\)，所以

\[
\boxed{1<D_T\mid\gcd(T,h^2-h-2r).}
\tag{15}
\]

这不是在声称 \((D_T,C)=1\)：\(D_T\) 可以与 \(C\) 共享素因子，只是其指数不能再被
\(D_C=(D,C)\) 完全吸收。准确的结论是 actual proper-root stutter 的 \(D\) 不可能
整除 \(C\)，并且它留下一段非平凡、可同时被 \(T\) 与 \(h^2-h-2r\) 检验的 residual。

## 4. 对全局出口的作用范围

式 (15) 去掉了“纯 cyclotomic C-side stutter”这一整类可能性，也为把 high-root
残余接到 \(T\)-侧的实际 valuation、约化除子 \(D_*\) 或容量素因子 external-source
菜单提供了必经输入。但它没有保证 \(D_T\) 的任一素因子会命中既有外部源菜单；更没有给出
typed target、E1--E5、全域 identity lift 或严格全局势。因此不能把 (14)--(15) 记作
Type I/II 短证书或合法递降。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_c_side_m_localization.py --verify
```

脚本只重算四个固定 stutter 算术控制：一个非 proper 的奇 C-side 控制，以及三个核心素数
proper-shape 控制（其中后者明确缺少 root provenance）。它核对 (5)--(8) 的逐赋值等式、
\(m=3\) 与 \(m\ge4\) 的数值比较和 \(D_T>1\)；不扫描素数、根层、分母或历史图表，
也不把控制冒充 actual receipt。
