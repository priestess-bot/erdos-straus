---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-native-raw-type-II-menu
title: 横向 stutter 约化除子的原生 Type II raw-ray 终端菜单
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，令
  D*=D/gcd(D,h^2-1)，其中 D|ph+1。定义 M_raw(p,h,D*)={Q|D*:Q≡-1 mod4h}。
  每个 Q∈M_raw（Q 不必为素数）令 C=(Q+1)/(4h)、B=(ph+1)/Q，则
  m=(B+1)/h、x=BC、d=C 是一张 Type II 证书，并恢复为
  4/p=1/(BC)+1/(phC)+1/(phBC)。这与所有 raw Type II 射线中 A=1、K=h、
  且生成模数整除 D* 的切片一一对应；菜单可为空，故不构成全局出口或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-II-raw-ray-certificate
  - short-certificate-equivalence
topics:
  - type-I
  - type-II
  - root-capacity
  - stutter
  - transverse-residual
  - raw-ray
  - divisor-menu
  - terminal-dispatch
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: actual-D-star-input-and-divides-ph-plus-one
  - claim: type-II-raw-ray-certificate
    role: Type-II-raw-ray-certificate-reconstruction
  - claim: short-certificate-equivalence
    role: direct-Type-II-certificate-verifier
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_native_raw_type_ii_menu.py
    role: root-shape-prime-and-composite-menu-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 约化除子的原生 Type II raw-ray 终端菜单

## 1. 原生除子菜单

固定核心素数

\[
p\equiv1\pmod {24}.
\]

在 terminal-first 后，设一个 actual proper-root stutter receipt 仍存在。沿用

\[
D\mid ph+1,
\qquad
D_*=\frac{D}{(D,h^2-1)}.
\tag{1}
\]

特别地，\(D_*\mid ph+1\)。定义有限的、允许合数因子的菜单

\[
\boxed{
\mathcal M_{\mathrm{raw}}(p,h,D_*)
=\{Q:Q\mid D_*,\ Q\equiv-1\pmod {4h}\}.
}
\tag{2}
\]

这不是对 \(D_*\) 的任意因子都适用的陈述；剩余类 \(-1\pmod{4h}\) 是下述
Type II raw-ray 坐标的精确生成模数条件。

## 2. 每个命中的直接 Type II 终端

取 \(Q\in\mathcal M_{\mathrm{raw}}(p,h,D_*)\)，并定义

\[
C=\frac{Q+1}{4h},
\qquad
B=\frac{ph+1}{Q}.
\tag{3}
\]

两者都是正整数。由 \(QB=ph+1\) 模 \(h\) 化简，并使用 \(Q\equiv-1\pmod h\)，
有

\[
B\equiv-1\pmod h.
\tag{4}
\]

因此

\[
m=\frac{B+1}{h},
\qquad
x=BC,
\qquad d=C
\tag{5}
\]

都是整数。更精确地，令 Type II raw-ray 的参数为

\[
(A,C,K)=(1,C,h),
\qquad H_{\mathrm{ray}}=4ACK-1=4Ch-1=Q.
\tag{6}
\]

式 (1)--(3) 恰给出

\[
H_{\mathrm{ray}}\mid Kp+A,
\qquad
B=\frac{Kp+A}{H_{\mathrm{ray}}}\ge A.
\tag{7}
\]

所以 `type-II-raw-ray-certificate` 逐项给出 (5) 的 Type II 除子证书。其显式恢复为

\[
\boxed{
\frac4p=
\frac1{BC}+
\frac1{phC}+
\frac1{phBC}.
}
\tag{8}
\]

也可直接检查：\(d=C\mid x^2\)、\(d\le x\)，且

\[
x+d=C(B+1)=Chm,
\tag{9}
\]

故 \(m\mid x+d\)。raw-ray 引理同时保证 \(3\le m\le p-2\) 及
\(m\equiv3\pmod4\)。

## 3. 该 raw-ray 切片的完备性

反过来，考虑所有参数满足

\[
A=1,
\qquad K=h,
\qquad H_{\mathrm{ray}}=4Ch-1,
\qquad H_{\mathrm{ray}}\mid D_*
\tag{10}
\]

的 Type II raw-ray。令 \(Q=H_{\mathrm{ray}}\)。则自动有

\[
Q\mid D_*,
\qquad Q\equiv-1\pmod {4h},
\]

即 \(Q\in\mathcal M_{\mathrm{raw}}(p,h,D_*)\)；而 (3) 唯一恢复 \(C\) 与 \(B\)。
因此 (2) 精确参数化的不是所有 Type II 证书，而是这个与 root height \(h\) 原生对齐的
\(A=1,K=h\) raw-ray 切片。

精确菜单不应预先把 \(Q\) 限为素数。root-shape 控制

\[
(p,h,Q)=(10369,21,335),
\qquad 335=5\cdot67,
\tag{11}
\]

满足 \(h\mid p^2+p+1\)、\(Q\mid ph+1\) 和 \(Q=4\cdot21\cdot4-1\)。由此

\[
(B,C,m,x,d)=(650,4,31,2600,4)
\tag{12}
\]

给出一张直接 Type II 证书。这里仅验证 root-shape 与 raw-ray 算术，**不**声称
\(335\) 是某个 actual receipt 的 \(D_*\) 因子。

## 4. 与二次移位扇的区别

二次移位扇把某个 \(q\mid D_*\) 用作 Type II 正规形中的 \(B\)-侧因子，并寻找
\(m+K(K-1)\) 的正支；本菜单则把 \(Q\mid D_*\) 用作 raw-ray 的生成模数
\(4ACK-1\)，且固定 \((A,K)=(1,h)\)。二者在一个 \(ph+1\) 的因子对恰好匹配时
可以给出同一张证书，但没有一般的包含关系。

所以 terminal-first 可先检查 (2)：它直接读取 actual \(D_*\)，不需要把该因子误投递到
旧的 \(q\mid u\) external-source 菜单。

## 5. 边界

菜单 (2) 仍可能为空；它没有证明：

* \(D_*\) 或其因子必落在 \(-1\pmod{4h}\)；
* 菜单未命中时存在另一张 Type I/II 证书；
* 任何由此证书恢复的小分母都形成可提升的递降边；
* G/Type I global exit 的全域良基势。

故该结论是一个 exact terminal menu，而不是 global proof。未命中的 \(D_*\) 因子仍须进入
二次移位、其他 Type I/II 图表，或具有 identity lift 的递降适配器。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_native_raw_type_ii_menu.py --verify
```

脚本重放一个素数和一个合数 \(Q\) 的 root-shape/raw-ray 控制，逐项检查除子、自然
缺口与恢复分母；它不扫描素数、根层、实际 receipt 或历史 selector。
