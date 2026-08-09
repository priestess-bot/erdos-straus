---
kind: claim
claim_id: type-i-target-odd-dprime-typeii-terminal
title: target-odd D'>1 canonical 标签到 Type II 直接终端
statement: 固定核心素数 p、来源层 D 与目标纤维 (D',A)，其中 D'>1。若 target-odd canonical D-格 route 的实际 shared-q 混合因子 h>1 同时整除 p+4Da 与 p+4AD'，且 h=-1 (mod 4D')，则令 C=D'/A、K=(h+1)/(4D')、B=(Kp+A)/h；有 B>A，m=(A+B)/K、x=BD'、d=AD' 给出显式 Type II 短证书。该分支是 D'>1 的直接终端，不是递降边；h 的来源整除只负责 target-odd source provenance。p=97 的 (D,a,D',A,h)=(4,4,2,1,7) 与 p=313 的 (6,3,2,2,7) 是正控制，p=73 的 (4,2,2,1,3) 因模 8 残数错误而不能进入该终端。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-target-odd-d-lattice-affine-menu-completion
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-raw-ray-certificate
  - short-certificate-equivalence
topics:
  - type-I
  - target-odd
  - D-lattice
  - Type-II
  - direct-terminal
  - shared-q
  - source-provenance
  - affine-offset
  - short-certificate
  - proof-program
sources:
  - claim: type-i-target-odd-d-lattice-affine-menu-completion
    role: target-odd-label-and-route-source
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: smaller-modulus-type-ii-generator
  - claim: type-II-raw-ray-certificate
    role: certificate-reconstruction
  - reproduction: reproductions/type_i_target_odd_dprime_typeii_terminal.py
    role: positive-and-residue-negative-controls
visibility: public
last_checked: '2026-08-09'
---

# target-odd \(D'>1\) canonical 标签到 Type II 直接终端

## 条件

固定核心素数 \(p\equiv1\pmod {24}\)、来源层 \(D\)，以及

\[
a\in\mathcal A_D(p),\qquad
(D',A)\in\mathcal L_D(p),\qquad
D'>1.
\tag{1}
\]

target-odd 的 \(q\)-primary 相位为 \(\gamma=0\)。对一组 canonical D-格 route，
目标标签是

\[
s=AD'.
\tag{2}
\]

把实际通过 shared-\(q\) ledger 的互素素数幂块合成为 \(h>1\)，并假设它们同时保留
来源与目标整除：

\[
h\mid p+4Da,\qquad
h\mid p+4AD',
\qquad
h\equiv-1\pmod {4D'}.
\tag{3}
\]

这里 \(h\) 是已经过重复 \(q\) 高度、CRT 和物理 token 计数的实际混合因子；不能把
同一 \(q\) 的多条来源行无条件相乘。

## \(D'>1\) 直接终端定理

置

\[
C=\frac{D'}A,\qquad
K=\frac{h+1}{4D'},\qquad
B=\frac{Kp+A}{h}.
\tag{4}
\]

则 \(C,K\in\mathbb N\)，并且 \(B\in\mathbb N\)。事实上，

\[
h=4AD'K-1=4ACK-1,
\tag{5}
\]

而

\[
K(p+4AD')=(Kp+A)+Ah.
\tag{6}
\]

由 (3) 得 \(h\mid Kp+A\)。同时

\[
B-A=\frac{K(p-4AD')+2A}{h}>0,
\tag{7}
\]

因为 \(4AD'<p\)。因此 \(B>A\)。

令

\[
m=\frac{A+B}{K},\qquad
x=ABC=BD',\qquad
d=A^2C=AD'.
\tag{8}
\]

由于 \(h\equiv-1\pmod K\)，(4) 模 \(K\) 给出 \(A+B\equiv0\pmod K\)，所以
\(m\in\mathbb N\)。由 Type II 因子射线正规形，

\[
\boxed{\frac4p=
\frac1{BD'}
+\frac1{pD'K}
+\frac1{pBCK}.}
\tag{9}
\]

等价地，按缺口证书的标准恢复式，

\[
y=\frac{p(x+d)}m=pD'K,\qquad
z=\frac{p(x+x^2/d)}m=pBCK.
\tag{10}
\]

这里 \(d\mid x^2\)、\(d\le x\)，且

\[
x+d=D'(A+B)=D'Km
\]

被 \(m\) 整除。因此 (9) 是原素数 \(p\) 的直接 Type II 短证书，不产生较小实例，
也不需要解提升或递降边。

## target-odd 接线

target-odd 相位只提供 \(\gamma=0\)；真正进入 Type II 的非零算术标签是 (2)。
选择器的这一分支应记录为

\[
\text{target-odd }\gamma=0
\to
\text{canonical label }AD'
\to
\text{shared-q factor }h
\to
h\equiv-1\pmod {4D'}
\to
\text{direct Type-II terminal}.
\]

第一条整除式 \(h\mid p+4Da\) 只证明 route 有来源；第二条整除式与模 \(4D'\)
残数才完成 (4)--(10) 的整数回译。若 (3) 的最后一个条件失败，不能把该 route
当作 Type II 证书，必须转入 raw Type II、其它 \(D'\)/\(A\) 纤维或严格递降菜单。

## 控制

### \(p=97\)：\(D'=2\) 且 \(A=1\)

取

\[
(D,a,D',A)=(4,4,2,1).
\]

来源数与目标数为

\[
p+4Da=161=7\cdot23,\qquad
p+4AD'=105=7\cdot15.
\]

取 \(h=7\)，有 \(h\equiv-1\pmod8\)。公式 (4)、(8) 给出

\[
(A,C,K,B)=(1,2,1,14),\qquad
(m,x,d)=(15,28,2),
\]

以及

\[
\frac4{97}=\frac1{28}+\frac1{194}+\frac1{2716}.
\]

### \(p=313\)：\(D'=2\) 且 \(A=2\)

取

\[
(D,a,D',A)=(6,3,2,2).
\]

此时

\[
p+4Da=385=5\cdot7\cdot11,\qquad
p+4AD'=329=7\cdot47.
\]

\(h=7\) 仍满足 \(h\equiv-1\pmod8\)，并得到

\[
(A,C,K,B)=(2,1,1,45),\qquad
(m,x,d)=(47,90,4),
\]

从而

\[
\frac4{313}=\frac1{90}+\frac1{626}+\frac1{14085}.
\]

### \(p=73\)：错误残数的负控制

取 \((D,a,D',A)=(4,2,2,1)\)。来源数和目标数分别为

\[
105=3\cdot5\cdot7,\qquad81=3^4.
\]

唯一共同的素因子块可取 \(h=3\)，但
\(3\not\equiv-1\pmod8\)。因此 \(K=(h+1)/8\) 不是整数，这一 route 不能进入
\(D'=2\) 的直接终端。该负控制只说明残数门失败，不说明 \(p=73\) 没有其它
Type I/II 证书。

## 边界

本卡把 D=1 的 target-odd shared-q 终端推广到 \(D'>1\) 的任意已声明目标纤维，
但条件 (3) 仍是一个输入门：它没有证明每个 target-odd 角色都能产生这样的 \(h\)，
也没有覆盖 \(h\equiv1\pmod {4D'}\)、raw source 或跨状态的 E1--E5 递降。空菜单或
错误残数只能输出当前分支的有限障碍，不能升级为全局 no-local-lift。

## 聚焦复现

```bash
python3 reproductions/type_i_target_odd_dprime_typeii_terminal.py --verify
```
