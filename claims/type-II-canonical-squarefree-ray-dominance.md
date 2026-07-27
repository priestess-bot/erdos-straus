---
kind: claim
claim_id: type-II-canonical-squarefree-ray-dominance
title: 同移位 Type II AC 射线的平方自由规范化支配
statement: 令 s=A^2C，并唯一写成 s=a_0^2c_0（c_0 平方自由）。则 A 整除 a_0，且 4a_0c_0 整除 4AC。若 p>=4s 且 h|p+4s、h= -1 mod 4AC，则以 K_0=(h+1)/(4a_0c_0) 构造的规范 (a_0,c_0,K_0) 也是有效 Type II 射线证书。因而在序条件自动的范围内，同一移位只需保留平方自由规范射线。半径 14 的 196 条原始射线压缩为 169 条规范射线；结合既有 p<=5*10^8 全覆盖审计及 p<10976 的独立有限检查，这 169 条规范射线仍覆盖该范围内全部核心素数。
claim_status: established
topics:
- type-II
- factorization
- canonicalization
- short-certificate
- computation
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 2 and 4 (statements; the paper leaves their proofs to the reader)"
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 同移位 Type II AC 射线的平方自由规范化支配

## 规范坐标

对任意正整数 $s$，唯一地写成

\[
s=a_0^2c_0,
\]

其中 $c_0$ 平方自由；也就是说，若

\[
s=\prod_\ell \ell^{e_\ell},
\]

则

\[
a_0=\prod_\ell\ell^{\lfloor e_\ell/2\rfloor},\qquad
c_0=\prod_{e_\ell\text{ odd}}\ell. \tag{1}
\]

任取另一种表示 $s=A^2C$。逐素数比较指数得到

\[
A\mid a_0,\qquad
4a_0c_0=\frac{4s}{a_0}\mid\frac{4s}{A}=4AC. \tag{2}
\]

因此 $(a_0,c_0)$ 是同一移位下模数最小的 $AC$ 射线；它不是任意选择的
归一化。

## 支配定理

设 $p\equiv1\pmod4$ 为素数、$p\ge4s$，并设原始表示 $s=A^2C$ 有一个
射线因子

\[
h\mid p+4s,\qquad h\equiv-1\pmod {4AC}. \tag{3}
\]

由 (2)，(3) 蕴含

\[
h\equiv-1\pmod {4a_0c_0}.
\]

故

\[
K_0=\frac{h+1}{4a_0c_0}
\]

为正整数，且 $h=4a_0c_0K_0-1$。又 $h\mid p+4a_0^2c_0$，所以
`type-II-ac-ray-audit` 的因子等价式给出

\[
h\mid K_0p+a_0.
\]

最后，因 $p\ge4a_0^2c_0$，
`type-II-raw-ray-certificate` 的序条件公式给出恢复商 $B\ge a_0$。因此
$(a_0,c_0,K_0)$ 直接恢复一张合法 Type II 证书。

这说明：在 $p\ge4s$ 的范围，任一同移位原始射线的成功都被唯一的平方自由规范
射线吸收。反向包含显然，因为规范表示本身也是一个表示。

## 对半径 14 审计的压缩

令

\[
\mathcal S_{14}=\{A^2C:1\le A,C\le14\}.
\]

原始盒有 $196$ 个坐标对，但其规范表示只有 $169$ 个。最大移位为
$14^3=2744$，所以 $p\ge10976$ 时上面的支配定理适用于盒内每个原始见证。

已存的 `type-ii-ac-ray-500m-bound14-results.json` 逐素数证明原始盒覆盖全部
$p\le5\cdot10^8$ 的核心素数。对于有限边界 $p<10976$，运行

```bash
python3 reproductions/type_ii_canonical_ray.py --limit 11000 --ac-bound 14 \
  --base-shift-bound 14 \
  --output reproductions/type-ii-canonical-rays-low-results.json
```

得到 $153$ 个核心素数均被规范盒覆盖。故由支配定理，169 条规范射线也覆盖既有
$5\cdot10^8$ 审计中的所有 $3{,}292{,}848$ 个核心素数；这只是原有限结论的
结构压缩，绝不外推为全称覆盖。

## 一维骨架及其有限残余

在 $p\le10^6$ 的有限剖面中，取最初的十四个规范移位

\[
s=1,\ldots,14
\]

已覆盖 $9708/9732$ 个核心素数，只余 $24$ 个。将候选空间仍限制为
$\mathcal S_{14}$，确定性贪心补集依次选择

\[
(a_0,c_0)=(6,1),(3,2),(5,2),(3,3),(9,3),(2,6),(4,2),(5,5), \tag{4}
\]

便覆盖该有限残余。这条八项表没有全称意义；它的用途是把下一步的多移位问题压缩为
“为什么规范移位 $1,\ldots,14$ 的共同失败只需要少数平方部较大的补充移位”这一可
检验问题，而不是将 $14\times14$ 参数盒当作黑箱。

运行

```bash
python3 reproductions/type_ii_canonical_ray.py --limit 1000000 --ac-bound 14 \
  --base-shift-bound 14 \
  --output reproductions/type-ii-canonical-rays-1m-results.json
```

会重建这份有限剖面，并对每个命中都恢复完整 Type II 证书。

## 边界

固定 $A,C\le14$ 的盒条件并不在规范化后原样保留：若原来的 $C$ 含平方因子，
$a_0$ 可以超过 14。因此本定理不声称“半径 14”自身可缩小为另一半径 14 盒；它只
压缩给定有限移位集合为每移位一条规范射线。

更重要的是，169 条射线的有限覆盖仍不能证明存在任何全局有限移位集。规范化排除了
同移位参数冗余，留下的困难仍是跨**不同**移位数
$p+4s$ 的因子残数选择。
