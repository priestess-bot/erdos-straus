---
kind: claim
claim_id: type-I-linear-gaussian-quartic-source-pullback-57399241
title: 57,399,241 高阶线性状态的高斯四次源标签拉回
statement: 对p=57399241的高阶G型状态R=444955=35*12713，取12713=N(pi)、pi=13+112i。任取q|K=13*51341*9566533及唯一标签t属于{3,43}使q|tR+1，取q的规范高斯因子rho。高斯四次符号满足(q/pi)_4=(pi/rho)_4^2*(-35t/rho)_4。该式逐项恢复q=13、51341、9566533的四次相位，并与该状态的分离角色核条件(q/pi)_4=(q/7)一致。它是保留四次相位的精确固定源拉回，不比较另一个变模数状态，故不强制目标命中。
claim_status: established
proof_provenance: mixed
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- subgroup-character
- order-four-character
- gaussian-integers
- quartic-reciprocity
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 57,399,241 高阶线性状态的高斯四次源标签拉回

## 高斯记号

令

\[
r=12{,}713=N(\pi),\qquad
\pi=13+112i,\qquad
R=35r. \tag{1}
\]

\(\pi\) 是 \(r\) 的规范 primary 高斯因子。对任意 \(q\equiv1\pmod4\)，令
\(\rho\) 是满足

\[
q=N(\rho)=\rho\bar\rho \tag{2}
\]

的规范 primary 高斯因子。以 \((\alpha/\beta)_4\in\{1,i,-1,-i\}\) 表示
\(\mathbb Z[i]\) 中的四次剩余符号。

## 定理

令 \(q\) 是奇素数，且存在标签 \(t\) 满足

\[
q\mid tR+1=t\cdot35N(\pi)+1. \tag{3}
\]

若 \(q\equiv1\pmod4\)，则

\[
\boxed{
\left(\frac{q}{\pi}\right)_4
=
\left(\frac{\pi}{\rho}\right)_4^2
\left(\frac{-35t}{\rho}\right)_4.
} \tag{4}
\]

右侧只使用标签 \(t\)、\(q\) 的规范高斯分解和固定的 \(\pi\)。所以 (4) 是把
\(12{,}713\) 分量的四次角色值拉回到实际 \(K\) 素因子上的精确公式。

## 证明

记

\[
A=\left(\frac{\pi}{\rho}\right)_4,\qquad
B=\left(\frac{\bar\pi}{\rho}\right)_4,\qquad
S=\left(\frac{-35t}{\rho}\right)_4. \tag{5}
\]

由 (3)，在 \(\mathbb Z[i]/(\rho)\) 中有

\[
-35t\equiv(\pi\bar\pi)^{-1},
\]

从而

\[
S=(AB)^{-1}. \tag{6}
\]

对 primary 高斯整数应用经典四次互反律，并使用共轭恒等式

\[
\left(\frac{\pi}{\bar\rho}\right)_4=B^{-1},
\]

得到

\[
\left(\frac{q}{\pi}\right)_4
=\left(\frac{\pi}{\rho}\right)_4
 \left(\frac{\pi}{\bar\rho}\right)_4
=AB^{-1}. \tag{7}
\]

将 (6) 代入右端：

\[
A^2S=A^2(AB)^{-1}=AB^{-1},
\]

即为 (4)。

## 高阶 G 状态的逐项重放

在

\[
p=57{,}399{,}241,\qquad
K=13\cdot51{,}341\cdot9{,}566{,}533 \tag{8}
\]

中，唯一源标签及 (4) 的指数结果如下。指数 \(0,1,2,3\) 分别代表
\(1,i,-1,-i\)。

| \(q\) | \(t\) | \(\rho\) | \((q/\pi)_4\) | \((\pi/\rho)_4\) | \((-35t/\rho)_4\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 3 | \(3+2i\) | \(-1\) | \(1\) | \(-1\) |
| 51,341 | 3 | \(-221+50i\) | \(-1\) | \(-i\) | \(1\) |
| 9,566,533 | 43 | \(1647+2618i\) | \(1\) | \(-1\) | \(1\) |

该状态的四阶分离角色是模 \(7\) 二次角色与 \((\cdot/\pi)_4\) 的乘积。
因此其在所有 \(q\mid K\) 上平凡，等价于

\[
\left(\frac{q}{\pi}\right)_4=\left(\frac q7\right), \tag{9}
\]

表中三行都直接满足 (9)。

## 含义与边界

[二次影子相容律](type-I-linear-order-four-shadow-compatibility-57399241.md)只看 (4) 的平方，
无法看见第二行出现的 \(-i\) 相位。公式 (4) 因此给出了真正可继续比较的四次数据。

不过，这仍是固定 \(R=444{,}955\) 的恒等式。要强制同一核心素数的另一个线性源逃逸，还需要把
另一状态的分离角色或反足点积集与同一个 \(\rho\) 联系起来；目前没有这样的全称桥。

## 复现

~~~bash
python3 reproductions/type_i_linear_gaussian_quartic_source_pullback_57399241.py
python3 -m unittest tests.test_type_i_linear_gaussian_quartic_source_pullback_57399241 -v
~~~
