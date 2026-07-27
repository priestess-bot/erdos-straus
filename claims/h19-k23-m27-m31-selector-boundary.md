---
kind: claim
claim_id: h19-k23-m27-m31-selector-boundary
title: H19-k23 的 m=27 残余到 m=31 除子选择边界
statement: H19-k23 的14条残存仿射进程均满足32|p-1和133|(p+31)/32，因此均可尝试m=31普通 Type II 双尾。524288层中，原共享缺口m=27且需要替代尾的2710条记录里，1192条由固定因子2^6*7^2*19^2闭合，795条由该固定因子乘一个新增素数幂闭合，余723条在完整m=31除子扫描中失败而首次转到m=35,39,47,59,63,71,79，频数为389,164,116,45,3,4,2。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- divisor-selection
- p-minus-one
- h19
- computational-boundary
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 的 \(m=27\) 残余到 \(m=31\) 除子选择边界

14 条 H19-k23 残存进程均为

\[
p=As+C,\qquad A=1\,552\,726\,375\,200,\qquad C\equiv1\pmod {32}. \tag{1}
\]

因 \(32\mid A\)，每个实际素数点都满足 \(32\mid p-1\)。故尾缺口

\[
m=31=4\cdot8-1 \tag{2}
\]

不受原进程分支限制。更强地，\(4256=32\cdot133\mid A\)，且全部常数满足

\[
C\equiv-31\pmod {4256}.
\]

所以对每个进程点都有

\[
133\mid u=\frac{p+31}{32}. \tag{3}
\]

## 精确的选择问题

令

\[
t=\frac{p-1}{32},\qquad u=t+1,\qquad x=8u. \tag{4}
\]

则 \(m=31\) 的普通 Type II 双尾证书等价于寻找一个除子 \(d\)，满足

\[
1\le d\le8u,\qquad d\mid64u^2,\qquad d\equiv-8u\pmod{31}. \tag{5}
\]

确实，(5) 的前两项是 \(d\le x,d\mid x^2\)。又 \(31\nmid u\)：否则由

\[
p=32u-31\equiv u\pmod{31}
\]

会有 \(31\mid p\)，而这里 \(p>31\)。所以 \(x\) 在模 \(31\) 下可逆，(5) 的最后一项
自动使补除子 \(x^2/d\equiv-x\pmod{31}\)。这正是两个尾分母的整除条件；反向也成立。

因此这一分支不再是笼统的 Type II 搜索，而是一个明确的“有界平方除子命中指定非零
模 \(31\) 剩余类”问题。

## 固定部分与单新增素数部分

由 (3)，有固定平方因子

\[
H=2^6\cdot7^2\cdot19^2=1\,132\,096\mid64u^2. \tag{6}
\]

所有 \(d\mid H\) 的模 \(31\) 剩余恰为

\[
R=\{1,2,4,5,7,8,9,10,14,16,18,19,20,25,28\}. \tag{7}
\]

在全部 14 条进程上，\(d\le H<8u\)。所以只要

\[
-8u\pmod{31}\in R, \tag{8}
\]

就能选取固定 \(d\mid H\) 满足 (5)，无条件给出 \(m=31\) 双尾递降。等价的 \(u\)
剩余类为

\[
\{3,6,11,12,13,15,17,21,22,23,24,26,27,29,30\}\pmod {31}. \tag{9}
\]

对不满足 (8) 的其余类，令 \(u=133w\)。更窄的变量选择器只允许

\[
d=h\ell^e,\qquad h\mid H,\quad \ell\notin\{2,7,19\},\quad
\ell^e\mid w^2, \tag{10}
\]

并仍检查 (5)。这正是“固定基底加一个新增素数幂”的可证伪版本；并不假定任意 \(w\)
都有这类因子。

## 524,288 层边界

在共享最小缺口为 \(27\)、且原缺口不能直接双尾递降的记录中，完整按 \(p-1\) 递增
缺口扫描给出

\[
2\,710=1\,192_{\text{fixed }H}+795_{\text{one new prime}}+723_{\text{no }m=31}. \tag{11}
\]

795 个变量 \(m=31\) 命中逐条由 (10) 重建；723 个 \(m=31\) 未命中逐条穷尽 (10) 后
仍为空。因此在这个有限层内，固定加单新增素数选择器恰好刻画全部 \(m=31\) 命中。

后 723 条的第一次成功尾缺口为

\[
389_{35}+164_{39}+116_{47}+45_{59}+3_{63}+4_{71}+2_{79}. \tag{12}
\]

14 条进程都同时出现固定、单新增素数和未命中状态，故这一障碍不是某一条仿射分支缺少
\(32\mid p-1\)，而是 (10) 中新增素数幂的参数依赖选择。该结论是有限审计边界；不能
推出对所有 \(u\) 的命中率或全称选择器。

重建命令：

~~~bash
python3 reproductions/h19_k23_m27_m31_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-524288.json \
  --output reproductions/h19-k23-m27-m31-selector-profile-524288.json
python3 -m unittest tests/test_h19_k23_m27_m31_selector_profile.py -q
~~~
