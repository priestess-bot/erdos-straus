---
kind: claim
claim_id: odd-distance-even-source-prime-overflow-criterion
title: 奇距离偶源尾的素数溢出判据
statement: 设 (M,r)=1。存在一个偶源平方尾，其正规形溢出 B 恰为素数 q，当且仅当令 q^nu||M 后存在 a|M/q^nu，使 q<=a 且 a=-q mod r。此时 g=M/a、e=qg 给出该尾，且 e/gcd(e,(M+e)/r)=q。十亿 H19 首 r 剖面的91个高溢出状态中，60个满足该素数溢出分支，余31个的所有首 r 尾均为复合溢出。
claim_status: established
topics:
- type-I
- even-source
- overflow
- normal-form
- divisor-residues
- factorization
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-tail-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-26'
---

# 奇距离偶源尾的素数溢出判据

设 \((M,r)=1\)。一个偶源平方尾的正规形为

\[
M=ag,\qquad e=Bg,\qquad (a,B)=1,\qquad B\mid g,\qquad B\le a,
\qquad a+B\equiv0\pmod r. \tag{1}
\]

令 \(q\) 为素数，\(q^\nu\mathbin{\Vert}M\)。则存在满足 (1) 且 \(B=q\) 的尾，当且仅当

\[
\exists a\mid\frac{M}{q^\nu}:\qquad q\le a,\qquad a\equiv-q\pmod r. \tag{2}
\]

在 (2) 下，令

\[
g=\frac Ma,\qquad e=qg. \tag{3}
\]

则 \(e\mid M^2\)、\(e\le M\)、\(e\equiv-M\pmod r\)，并且

\[
\frac{e}{\gcd\left(e,(M+e)/r\right)}=q. \tag{4}
\]

## 证明

若 (1) 中 \(B=q\)，则 \((a,q)=1\) 且 \(q\mid g=M/a\)。因此 \(a\) 不含 \(M\) 的
任何 \(q\)-幂，即 \(a\mid M/q^\nu\)。其余两项正是 (1) 的 \(B\le a\) 和
\(a+B\equiv0\pmod r\)，得到 (2)。

反之，(2) 使 \(q^\nu\mid g\)，故 \(q\mid g\)，且 \((a,q)=1\)。将 \(B=q\) 代入
(1) 的各项即可得到尾 (3)。最后由尾正规形的最大公因子恒等式
\(\gcd(e,(M+e)/r)=g\)，得到 (4)。

这个判据把“溢出恰为一个素数”从平方因子搜索化为一个普通除子问题，但它不是零溢出：
目标残数是 \(-q\)，而非 \(-1\)。也不能把它与指数缺陷 \(\delta\) 混同，后者要求乘法
残数 \(a w\equiv-1\pmod r\)，而 (1) 给出的是加法关系 \(a+q\equiv0\pmod r\)。例如
\(p=6{,}868{,}801,r=959\) 的首尾有素数溢出 \(q=3\)，但其零溢出指数缺陷为 \(2\)。

## H19 有限剖面

对十亿 H19 首 \(r\) 状态的 91 个高溢出点，独立枚举 (2) 并与全部 \(M^2\) 尾因子枚举
逐项比较，二者给出的素数溢出集合完全相同：

| 类别 | 状态数 |
| --- | ---: |
| 至少有一个素数溢出尾 | 60 |
| 最小溢出本身为素数 | 49 |
| 所有首 \(r\) 尾均为复合溢出 | 31 |

所以，若研究目标是把高溢出尾化为更短的局部因子条件，真正需要处理的有限边界已从 91 点
缩至 31 个“纯复合溢出”状态。这个缩小仍是有限审计；一般证明还须说明为何 (2) 或另一条
可提升递降分支必然出现。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_prime_overflow_profile.py \
  --input reproductions/type-ii-h19-bounded-r-overflow-profile-1b-results.json \
  --output reproductions/type-ii-h19-prime-overflow-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_prime_overflow_profile.py -q
~~~
