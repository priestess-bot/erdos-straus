---
kind: claim
claim_id: gap-seven-congruence-certificates
title: 三个模 7 核心剩余类的固定缺口 m=7 证书
statement: 对核心素数 p=1 mod24，若 p=3 mod7，则 m=7、d=1 是 Type II 证书；若 p=5 mod7，则 m=7、d=2x（x=(p+7)/4）是 Type I 证书；若 p=6 mod7，则 m=7、d=2 是 Type II 证书。故该固定缺口无条件覆盖三个非零模7类；剩余 p=1,2,4 mod7 不由此三种固定除子构造覆盖。
claim_status: established
topics:
- certificate
- congruences
- type-I
- type-II
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: certificate-reconstruction
visibility: public
last_checked: '2026-07-23'
---

# 三个模 \(7\) 核心剩余类的固定缺口 \(m=7\) 证书

令 \(p\equiv1\pmod{24}\)，并写

\[
x=\frac{p+7}{4}.
\]

此时 \(x\) 是偶数，且模 \(7\) 有 \(x\equiv2p\pmod7\)。下表给出三条无条件证书：

\[
\begin{array}{c|c|c|c}
p\pmod7 & \text{类型} & d & \text{所需整除}\\
\hline
3 & \mathrm{II} & 1 & 7\mid x+1\\
5 & \mathrm{I} & 2x & 7\mid px+2x=x(p+2)\\
6 & \mathrm{II} & 2 & 7\mid x+2
\end{array}
\]

## 证明

当 \(p\equiv3\pmod7\) 时，\(x\equiv6\pmod7\)，故 \(7\mid x+1\)；
\(d=1\) 满足 \(d\mid x^2\) 及 \(d\le x\)，所以是 Type II 证书。

当 \(p\equiv5\pmod7\) 时，\(7\mid p+2\)。因 \(x\) 为偶数，

\[
d=2x\mid x^2,
\]

且 \(7\mid x(p+2)=px+d\)，故是 Type I 证书。

当 \(p\equiv6\pmod7\) 时，\(x\equiv5\pmod7\)，所以 \(7\mid x+2\)。
又 \(2\mid x^2\)、\(2\le x\)，故 \(d=2\) 给出 Type II 证书。

三个情形均有 \(m=7\equiv3\pmod4\)，且核心素数 \(p\ge73\)，所以
\(3\le7\le p-2\)。Bradford 的恢复公式于是给出 \(4/p\) 的三项单位分数解。

## 边界

这只是 \(m=7\) 的三个固定除子切片；它不声称其余 \(p\equiv1,2,4\pmod7\) 没有
缺口 7 的其他除子证书。例如 \(p=5569\equiv4\pmod7\) 的最短证书仍是 Type I、
\(m=7\)、\(d=17\)。因此该结论只增加直接覆盖，不替代对其余类的除子搜索或递降。
