---
kind: claim
claim_id: type-I-r47-cycle-nonempty-support-short-selector
title: R=47 非空周期支撑的短 Type I/II 选择器
statement: 设 p≡1 (mod 24) 为素数、K=(47p+1)/4，并令 T=Supp(K)∩{5,13,31,43}。若 T 非空，则可按 31、5、13、43 的固定优先级构造一张 Type I 或 Type II 除子证书，其首分母缺口统一满足 m≤(p+32)/15<p-2：31|K 时使用 H=93 的 Type I 比 1/93；否则分别由 5、13、43 触发射线因子 15、39、43，唯一序条件例外 p=73 由因子 15 的 Type II 直接补齐。因此 R=47 平方自由周期相图的 15 个非空掩码全部有周期内或周期外短出口，只剩空掩码 MISS_EXTERNAL 未由该选择器处理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-r47-cycle-lattice-capacity-three-phase-boundary
  - type-I-general-b-centered-square-spectrum
  - type-II-raw-ray-certificate
topics:
  - type-I
  - type-II
  - short-certificate
  - cycle
  - support-mask
  - affine-ray
  - selector
  - escape-lemma
  - proof-program
sources:
  - claim: type-I-r47-cycle-lattice-capacity-three-phase-boundary
    role: exact-R47-support-mask-phase
  - claim: type-I-general-b-centered-square-spectrum
    role: Type-I-certificate-reconstruction
  - claim: type-II-raw-ray-certificate
    role: fixed-affine-Type-II-ray
visibility: public
last_checked: '2026-07-31'
---

# \(R=47\) 非空周期支撑的短 Type I/II 选择器

## 定理

设

\[
p\equiv1\pmod{24},
\qquad p\text{ 为素数},
\qquad K=\frac{47p+1}{4},
\]

并记

\[
T=\operatorname{Supp}(K)\cap\{5,13,31,43\}.
\]

若 \(T\ne\varnothing\)，则 \(p\) 有一张显式 Type I 或 Type II 除子证书，且其
首分母缺口 \(m\) 满足

\[
\boxed{
m\le H_{47}(p):=\frac{p+32}{15}<p-2.}
\tag{1}
\]

因此在
[R=47 五周期的表示格容量三相](type-I-r47-cycle-lattice-capacity-three-phase-boundary.md)
中，十五个非空支撑掩码全部有短出口。周期格的九个 HIT 可以直接恢复 Type I；更强地，
下面的固定优先级选择器也独立覆盖所有非空掩码：

\[
31\succ5\succ13\succ43.
\tag{2}
\]

## 四条显式分支

为避免与核心量 \(K=(47p+1)/4\) 混淆，Type II 原始射线中的参数记为
\(\kappa\)，射线因子记为

\[
q_0=4AC\kappa-1.
\]

选择器如下；只有 \(13\mid K\) 的最小点 \(p=73\) 需要单独一行。

| 触发条件 | 类型 | 固定参数或尾比 | 缺口 | 恢复的三个分母 |
|---|---|---|---|---|
| \(31\mid K\) | Type I | \((A,B,C,H)=(2,1,K/93,93)\) | \((p+2)/93\) | \(2C,186C,pK\) |
| \(31\nmid K,\ 5\mid K\) | Type II | \((A,C,\kappa,q_0)=(1,2,2,15)\), \(B=(2p+1)/15\) | \((p+8)/15\) | \(2B,4p,4pB\) |
| \(31\nmid K,\ 5\nmid K,\ 13\mid K,\ p>73\) | Type II | \((A,C,\kappa,q_0)=(5,2,1,39)\), \(B=(p+5)/39\) | \((p+200)/39\) | \(10B,10p,2pB\) |
| \(p=73\) | Type II | \((A,B,C,\kappa,q_0)=(2,5,2,1,15)\) | \(7\) | \(20,292,730\) |
| \(31\nmid K,\ 5\nmid K,\ 13\nmid K,\ 43\mid K\) | Type II | \((A,C,\kappa,q_0)=(11,1,1,43)\), \(B=(p+11)/43\) | \((p+484)/43\) | \(11B,11p,pB\) |

表中整除符号的优先级只表示前面的素数分支已经排除；例如第三行的条件意为
\(31\nmid K\)、\(5\nmid K\)、\(13\mid K\)。

## Type I 分支的核验

若 \(31\mid K\)，则 \(47\equiv16\pmod{31}\) 给出

\[
p\equiv-2\pmod{31}.
\]

又因 \(p\equiv1\pmod3\)，有 \(3\mid K\) 且 \(93\mid p+2\)。置

\[
C=\frac K{93},
\qquad
(A,B,H,h)=\left(2,1,93,\frac{p+2}{93}\right).
\]

则

\[
A=\frac{B+H}{47},
\qquad
4B^2C+1=47h,
\qquad
Bp+A=Hh.
\tag{3}
\]

这正是 \(1/93\) 尾比的 Type I 正规形。其分母满足

\[
\frac1{2C}+\frac1{186C}+\frac1{pK}
=\frac{47}{K}+\frac1{pK}
=\frac4p.
\tag{4}
\]

## 三条 Type II 射线的核验

对任一表中 Type II 行，定义

\[
B=\frac{\kappa p+A}{4AC\kappa-1},
\qquad
m=\frac{A+B}{\kappa},
\qquad
x=ABC,
\qquad
d=A^2C.
\tag{5}
\]

只要 \(B\) 为正整数且 \(A\le B\)，
[非互素 Type II 因子射线定理](type-II-raw-ray-certificate.md)就给出

\[
p=4ABC-m,
\quad
d\mid x^2,
\quad
d\le x,
\quad
m\mid x+d,
\tag{6}
\]

以及单位分数恒等式

\[
\frac4p
=\frac1x+\frac1{pAC\kappa}+\frac1{pBC\kappa}.
\tag{7}
\]

现在逐项验证整数性和序条件。

### \(5\mid K\)

由 \(47p+1\equiv0\pmod5\) 得 \(p\equiv2\pmod5\)，而
\(p\equiv1\pmod3\)。故

\[
15\mid2p+1.
\]

取 \((A,C,\kappa)=(1,2,2)\) 即得表中数据；核心素数 \(p\ge73\) 使
\(B=(2p+1)/15>A\)。

### \(13\mid K\)

由 \(47\equiv8\pmod{13}\) 得 \(p\equiv8\pmod{13}\)，再结合
\(p\equiv1\pmod3\)，有

\[
39\mid p+5.
\]

取 \((A,C,\kappa)=(5,2,1)\)。此时 \(A\le B\) 等价于 \(p\ge190\)。联合同余为

\[
p\equiv73\pmod{312},
\]

所以低于 \(190\) 的唯一素数候选是 \(p=73\)。该点改取
\((A,B,C,\kappa)=(2,5,2,1)\)，直接得到表中的 \(m=7\) 证书。

### \(43\mid K\)

由 \(47\equiv4\pmod{43}\) 得 \(p\equiv32\pmod{43}\)，故 \(43\mid p+11\)。
取 \((A,C,\kappa)=(11,1,1)\)。写 \(p=43B-11\)，再模 \(24\) 使用
\(p\equiv1\)，得到

\[
19B\equiv12\pmod{24},
\qquad B\equiv12\pmod{24}.
\]

所以 \(B\ge12>11=A\)，序条件自动成立。

## 统一短界

四类缺口分别为

\[
\frac{p+2}{93},
\qquad
\frac{p+8}{15},
\qquad
\frac{p+200}{39},
\qquad
\frac{p+484}{43},
\tag{8}
\]

以及特例 \(p=73,m=7\)。前三个一般式在相应允许范围内都不超过
\((p+32)/15\)；特例恰有

\[
7=\frac{73+32}{15}.
\]

对 \(43\) 分支，联合同余给出 \(p\equiv505\pmod{1032}\)，故 \(p\ge505\)，并有

\[
\frac{p+484}{43}\le\frac{p+32}{15}.
\]

最后，\(p\ge73\) 立即给出 \((p+32)/15<p-2\)，证明 (1)。

## 边界与下一余核

这个选择器闭合的是 \(R=47\) 周期相图中的**非空可选支撑**，不是任意 \(R\) 的逃逸
定理。它也不能把周期格三相直接改名为完整环境中的 F/G 三分；后者还必须读取
\(K\) 中所有周期外素因子。

唯一未由本选择器处理的是

\[
T=\varnothing,
\]

即周期格的 MISS_EXTERNAL 相。该相不能由 \(p=313\) 的个例证书外推，也不存在一条
固定 \((A,C,\kappa)\) 的 Type II 原始射线覆盖仓库选定的整条 CRT 素数进程。下一步应
只针对这个空掩码族检验一个可证伪的有限析取：普通 \(p-1\) 双尾递降、完整 Type I
\(p-1\) 桥，或 \(A,C\in\{1,2\}\) 的四类可变 \(\kappa\) Type II 射线。

符号恒等式、样本单位分数恢复和全部十六个掩码的选择分支由
reproductions/type_i_r47_nonempty_support_short_selector.py 重放，冻结结果为
reproductions/type-i-r47-nonempty-support-short-selector-results.json。
