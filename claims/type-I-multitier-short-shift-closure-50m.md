---
kind: claim
claim_id: type-I-multitier-short-shift-closure-50m
title: 五千万前缀的Type I八移位闭合
statement: 对p不大于50000017的374903个核心素数，完整二幂p减一桥、固定12项非二幂p减一菜单、E不大于10^6的源平方允许p减一因子对、两个固定移位B一状态和八移位动态桥选择器依次闭合359988、14444、424、12、35点，合计全部374903点。最后一层使用移位集合{3,5,7,9,11,17,25,29}、E不大于10^6、B不大于7。此前四移位集{3,7,9,25}在同一最终剩余上遗漏4点，故八移位结果只是有限计算闭合，不构成固定移位菜单的全称定理。合成见证的E最大20808、B最大5564、源距离最大29。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- factorization
- dyadic
- source-state
- selector
- finite-audit
- closure
- shifted-source
- boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 五千万前缀的 Type I 八移位闭合

对所有

\[
p\le50{,}000{,}017,\qquad p\equiv1\pmod{24},
\]

以下五个精确选择层按顺序作用于前一层的遗漏，故计数彼此不重叠。

| 层 | 机制 | 新闭合点数 |
|---|---|---:|
| 1 | 完整允许二幂 \(E=2^t\) 的 \(n=p-1\) 因子对 | 359,988 |
| 2 | 固定 12 项非二幂 \(E\) 菜单、\(B\in\{1,2\}\)、\(n=p-1\) | 14,444 |
| 3 | \(E\le10^6\)、\(E\mid(p-1)^2/4\) 的完整 \(BC\mid K\) 对、\(n=p-1\) | 424 |
| 4 | 固定 \((s,R)=(9,31),(25,19)\) 的 \(B=1\) 移位源除子剩余类 | 12 |
| 5 | 动态桥的八移位 \(s\in\{3,5,7,9,11,17,25,29\}\)，\(E\le10^6\)、\(B\le7\) | 35 |

所以

\[
359988+14444+424+12+35=374903. \tag{1}
\]

第 5 层对每个尚未命中的点，以 \(n=p-s\) 枚举所有满足

\[
E\mid\frac{n^2}{\gcd(E,4)},\qquad E\le10^6,\qquad
R=\frac{E-1}{s},\qquad K=\frac{pR+1}{4}
\]

的偶桥；再穷尽 \(B\le7\) 及 \(BC\mid K\)，用[源状态实现判据](type-I-normal-source-state-realization.md)
重建 Type I 证书。35 个选中的 \(B\) 仅为

\[
\{1,2,3,5,7\}. \tag{2}
\]

本轮也确定了一个可复核的菜单边界：若仍限制到两千万中使用的

\[
\{3,7,9,25\},\qquad E\le10^6,\qquad B\le7,
\]

则第五层的 35 个输入中有四个遗漏：

\[
20{,}878{,}729,\quad32{,}499{,}289,\quad37{,}467{,}049,\quad43{,}827{,}529. \tag{3}
\]

它们分别由新增移位 \(11,17,29,5\) 的同类状态释放。更强地，其中后三个

\[
32{,}499{,}289,\quad37{,}467{,}049,\quad43{,}827{,}529 \tag{4}
\]

在固定四移位下即使将审计盒子扩大至 \(E\le10^8\)、\(B\le64\) 仍无命中。因此它们不是这个方向上
单纯提高桥上界或 \(B\) 上界能够消除的遗漏，而是要求新的移位源。这个结论仍只排除指定的有限盒子；它不排除更大或不同的源状态，更不能推出任何全称反例。反过来，八移位的成功也只是该有限前缀的计算事实，尚未给出一个对所有素数有效的选择律。

五层合成后的实际最坏参数为

\[
E\le20808,\qquad B\le5564,\qquad p-n\le29. \tag{5}
\]

这里最大 \(E\) 出现在第 3 层，最大 \(B\) 出现在第 1 层；最后的动态短移位层并未需要超过 \(B=7\)。因此 (1)--(4) 是严格的五千万前缀计算结论，而不是 Erdős--Straus 猜想的证明。它把下一步理论任务收窄为：从 \(p\) 的算术结构中导出可扩展的移位选择规则，或证明小 \(B\) 证书在某类状态中必然存在。

可复现命令：

~~~bash
python3 reproductions/type_i_short_shift_low_e_profile.py \\
  --residual reproductions/type-i-shifted-source-b1-menu-profile-50m-results.json \\
  --shifts 3,5,7,9,11,17,25,29 \\
  --e-cap 1000000 --b-cap 7 \\
  --output reproductions/type-i-short-shift-low-e-b7-profile-50m-results.json
python3 reproductions/type_i_multitier_short_shift_closure_50m.py
python3 -m unittest \\
  tests/test_type_i_short_shift_low_e_profile_50m.py \\
  tests/test_type_i_multitier_short_shift_closure_50m.py -q
~~~
