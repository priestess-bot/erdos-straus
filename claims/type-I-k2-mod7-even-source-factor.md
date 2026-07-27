---
kind: claim
claim_id: type-I-k2-mod7-even-source-factor
title: k=2模七二次剩余因子边界
statement: 令p≡25 mod48为素数，n=(7p+1)/8。固定k=2,q=7的混合因子偶源边存在，当且仅当n有一个素因子不属于{1,2,4} mod7；等价地，存在真除子d|n且d≡3 mod7。命中时取g=2d给出严格偶源Type I提升；若所有n的素因子均在{1,2,4} mod7，则此固定k=2尺度的所有混合因子均不能命中-1 mod7。
claim_status: established
topics:
- type-I
- descent
- even-source
- external-source
- factorization
- congruence
- terminal-factor
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-27'
---

# k=2模七二次剩余因子边界

这是[混合因子外部源严格递降族](mixed-factor-external-source-descent.md)在固定
$k=2$、$q=4k-1=7$ 的一个可直接检索的终止推论。

## 定理

令 $p\equiv25\pmod{48}$ 为素数，定义

$$
n=\frac{7p+1}{8}.
$$

下列三条等价：

1. 存在 $g\mid2n$ 使 $g\le n$ 且 $g\equiv-1\pmod7$；
2. 存在真除子 $d\mid n$ 使 $d\equiv3\pmod7$；
3. $n$ 有素因子 $\ell\not\equiv1,2,4\pmod7$。

在这些条件成立时，取第二条中的 $d$，令

$$
g=2d,\qquad
u=\frac{2(n+2d)}7,\qquad
v=\frac{nu}{2d}.
$$

则这些量均为正整数，$n$ 为偶数且 $2\le n<p$，并且

$$
\frac4n=\frac1{2n}+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p=\frac1{2np}+\frac1u+\frac1v. \tag{1}
$$

相应的 Type I 缺口证书为

$$
m=\frac{16d+1}{7},\qquad D=\frac{u^2}{4d}. \tag{2}
$$

## 证明

由 $p\equiv25\pmod{48}$，有 $p\equiv1\pmod{24}$，并且

$$
7p+1\equiv0\pmod{16}.
$$

故 $n$ 是偶数，且 $n\equiv1\pmod7$。

若第二条成立，令 $g=2d$。由于 $d$ 是真除子，$g\le n$，且

$$
g=2d\mid2n,\qquad g\equiv2\cdot3\equiv-1\pmod7.
$$

这证明第二条蕴含第一条。

若第三条成立，按 $\ell\pmod7$ 分三类构造第二条中的 $d$：

$$
\ell\equiv3:\ d=\ell;\qquad
\ell\equiv5:\ d=\frac n\ell;\qquad
\ell\equiv6:\ d=\frac n{2\ell}. \tag{3}
$$

这些都是 $n$ 的真除子，且由 $n\equiv1\pmod7$ 分别有 $d\equiv3\pmod7$。所以第三条
蕴含第二条。反过来，若 $n$ 的所有素因子均在 $\{1,2,4\}$ 中，则 $2n$ 的任意因子也在
该乘法子群中，绝不可能为 $-1\equiv6\pmod7$；故第一条不成立。这也证明第一条蕴含第三条。

最后，$k=2$ 整除 $(p-1)/4$，并且

$$
n=\frac{(4k-1)p+1}{4k}.
$$

因此混合因子外部源定理的全部条件成立。代入其公式即得 (1) 和 (2)。源 $n$ 是偶数，
所以 (1) 的左式可由 $n=2$ 的解按比例缩放终止。

## 十亿 H19 审计

对十亿 H19 的 $664$ 个源自由残余，其中 $243$ 个满足 $p\equiv25\pmod{48}$。对每个这类
$p$ 精确分解 $n=(7p+1)/8$，并独立枚举真除子及所有 $g\mid2n$。三种等价条件恰共同命中
$124$ 个；其中只有 $72$ 个已由单素因子 $3\pmod7$ 命中，另有 $52$ 个必须使用复合因子。
余下 $119$ 个的全部 $n$ 素因子均在 $\{1,2,4\}\pmod7$，故固定 $k=2$ 尺度的**所有**
混合因子边均被子群障碍排除。命中者包括新的四支撑边界点

$$
p=48{,}605{,}881,\qquad
n=42{,}530{,}146,\qquad
d=353,
$$

给出 $g=706$、$m=807$。这一子群障碍只否定固定 $k=2$；它不排除其他外部尺度或内部偶桥。

可复现命令：

~~~bash
python3 reproductions/type_i_k2_mod7_even_source_audit.py
python3 -m unittest tests/test_type_i_k2_mod7_even_source_audit.py -q
~~~
