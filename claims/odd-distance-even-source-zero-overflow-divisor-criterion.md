---
kind: claim
claim_id: odd-distance-even-source-zero-overflow-divisor-criterion
title: 奇距离偶源零溢出尾的普通除子判据
statement: 设奇距离偶源尾满足 M=(rp+1)/4、(r,M)=1、e|M^2、e<=M、e=-M mod r，并令 x=(M+e)/r。则尾诱导的 Type I 溢出 B=e/(e,x) 等于1，当且仅当存在普通除子 a|M 使 a=-1 mod r；对应关系为 a=M/e、e=M/a。故零溢出偶源选择器等价于在 M 的普通除子集中命中 -1 mod r，而非在 M^2 的平方除子集中搜索。
claim_status: established
topics:
- type-I
- even-source
- normal-form
- overflow
- divisor-residues
- selector
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-26'
---

# 奇距离偶源零溢出尾的普通除子判据

设

\[
M=\frac{rp+1}{4},\qquad (r,M)=1,
\]

且 \(e\mid M^2\)、\(e\le M\)、\(e\equiv-M\pmod r\)。令

\[
x=\frac{M+e}{r},\qquad B=\frac{e}{(e,x)}.
\]

则

\[
B=1
\quad\Longleftrightarrow\quad
\exists a\mid M:\ a\equiv-1\pmod r. \tag{1}
\]

对应为 \(a=M/e\)、\(e=M/a\)。

## 证明

若 \(B=1\)，则 \(e\mid x\)，从 \(rx=M+e\) 得 \(e\mid M\)。令 \(a=M/e\)。
由于 \(e\mid M^2\) 且 \((M,r)=1\)，有 \((e,r)=1\)。模 \(r\) 化简

\[
M+e=e(a+1)\equiv0
\]

即得 \(a\equiv-1\pmod r\)。

反之，若 \(a\mid M\)、\(a\equiv-1\pmod r\)，令 \(e=M/a\)。则 \(e\mid M\mid M^2\)，
且

\[
M+e=e(a+1)equiv0pmod r.
\]

故 \(e\equiv-M\pmod r\)，并且

\[
x=\frac{e(a+1)}r
\]

是 \(e\) 的倍数，所以 \(B=1\)。

这条判据将“零溢出偶源尾”从平方因子积集问题降为普通除子残数问题。它保留了全部源--目标
提升条件，因而可直接作为二次外部源或零溢出偶源选择器的偶源分支。对 649 个存储的首个
\(r\) 命中状态，普通除子枚举逐项恢复全部 1,990 张、且仅恢复这些 \(B=1\) 尾。

它不保证这样的普通除子存在；高溢出状态正是该普通除子残数条件失败的实例。后续应研究
\(\operatorname{Div}(M)\) 在模 \(r\) 的 \(-1\) 命中如何与二次外部源失败发生关联。
