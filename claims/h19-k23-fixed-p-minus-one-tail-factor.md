---
kind: claim
claim_id: h19-k23-fixed-p-minus-one-tail-factor
title: H19-k23 共同 p-1 因子自动给出大多数双尾递降
statement: H19-k23 的14条残存进程均满足165600|p-1。故任何已有 Type II 证书的缺口m只要m+1|165600，就自动给出普通双尾严格递降。在262144层的588526条共享选择器记录中，586992条由此固定因子直接闭合；其余1534条仅有m=27,43,51,55,63,83,87，其中3条偶然满足m+1|p-1，其余1531条由替代p-1缺口闭合。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- p-minus-one
- affine-progressions
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 共同 \(p-1\) 因子自动给出大多数双尾递降

14 条残存进程都形如

\[
p=At+C,\qquad A=1\,552\,726\,375\,200.
\]

对每条进程计算 \(\gcd(A,C-1)\)，再在 14 条间取公因子，得到

\[
G=165\,600=2^5\cdot3^2\cdot5^2\cdot23. \tag{1}
\]

因为 \(G\mid A\) 且 \(G\mid C-1\)，所以对每个参数值都有 \(G\mid p-1\)。因此若一张
直接 Type II 证书的缺口为 \(m\)，并且

\[
m+1\mid G, \tag{2}
\]

则 \(m+1\mid p-1\)。Type II 双尾去 \(p\) 引理立即把该证书变成严格源
\(n=(p+m)/(m+1)<p\) 的普通双尾递降。

在 262,144 层的共享选择器记录中，满足 (2) 的最小缺口为

\[
3,7,11,15,19,23,31,35,39,47,59,71,95,99. \tag{3}
\]

它们贡献 586,992 条直接递降。固定因子没有覆盖的残余恰为

\[
1\,534=1\,490_{m=27}+22_{m=43}+8_{m=51}+7_{m=55}
+4_{m=63}+1_{m=83}+2_{m=87}. \tag{4}
\]

其中 3 条 \(m=63\) 记录因额外参数依赖因子仍直接满足 \(m+1\mid p-1\)；其余 1,531 条
由完整 \(p-1\) 候选缺口扫描获得替代 Type II 双尾递降。这把当前有限闭合精确分成

\[
588\,526=586\,992_{\text{fixed-factor}}
+3_{\text{accidental direct}}
+1\,531_{\text{alternative}}. \tag{5}
\]

替代部分中还有一块由 \(q^2\) 同余族直接解释：取 \((q,m)=(8,31)\)，则
\(d\mid64\) 且 \(6\mid8t\) 的一般构造覆盖 247 条原 \(m=27\) 记录的 \(m=31\)
替代证书，除子频数为

\[
53_{d=1}+55_{d=2}+36_{d=4}+55_{d=8}+48_{d=16}=247. \tag{6}
\]

这 247 条只是最小的 \(d\mid64\) 子族，并非当前最强分类。进一步利用所有 14 条进程
共有的 \(133\mid(p+31)/32\)，固定因子 \(2^6\cdot7^2\cdot19^2\) 在同一 262,144
层给出完整的 \(m=31\) 固定选择器，共覆盖 667 条原 \(m=27\) 替代记录；其余 421 条
\(m=31\) 命中均可由固定因子乘一个新增素数幂重建，402 条才在 \(m=31\) 失败并改走更大
尾缺口。该更细的边界见
[H19-k23 的 \(m=27\) 残余到 \(m=31\) 除子选择边界](h19-k23-m27-m31-selector-boundary.md)。

固定因子引理是无条件代数结论；(3)--(5) 是对有限共享选择器产物的精确分类，不能推出
该固定因子覆盖全部 Type II 证书或所有核心素数。

重建命令：

~~~bash
python3 reproductions/h19_k23_fixed_tail_factor_profile.py
python3 -m unittest tests/test_h19_k23_fixed_tail_factor_profile.py -q
~~~
