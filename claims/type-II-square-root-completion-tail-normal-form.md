---
kind: claim
claim_id: type-II-square-root-completion-tail-normal-form
title: 普通 Type II 双尾递降的平方根补全标准形
statement: 设 p=1 (mod24) 为素数，m=4q-1，m+1|p-1，x=(p+m)/4，并且 d 是一张普通 Type II 双尾证书的除子，即 d<=x、d|x^2 且 d=x^2/d=-x (mod m)。令 t=(p-1)/(m+1)，a 为满足 d|q^2a^2 的最小正整数。则 (d,m)=1，且 t=-4d-1 (mod m)、t=-1 (mod a)、6|qt、d<=q(t+1)；反之这些条件正好重建该双尾证书。因此普通 Type II 双尾递降等价于平方根补全除子的参数标准形。
claim_status: established
topics:
- type-II
- descent
- normal-form
- square-root-completion
- congruence-certificate
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# 普通 Type II 双尾递降的平方根补全标准形

此前的[平方根补全族](type-II-square-root-completion-tail-family.md)给出了充分条件。这里给出
其反向：只要一个普通 Type II 证书真的能沿两条 (p)-尾去 (p)，它必然已经属于同一
个 ((q,d,t)) 参数族。因此这不是又一个局部构造，而是普通双尾 Type II 证书的无损
规范化。

设核心素数 (p\equiv1\pmod{24})，并设

\[
m=4q-1,\qquad m+1\mid p-1,\qquad
t=\frac{p-1}{m+1}. \tag{1}
\]

于是 (p=4qt+1)，并且

\[
x=\frac{p+m}{4}=q(t+1). \tag{2}
\]

对一张普通 Type II 双尾证书，选择较小除子 (d\le x)。两个尾分母整除条件等价于

\[
d\mid x^2,\qquad d\equiv\frac{x^2}{d}\equiv-x\pmod m. \tag{3}
\]

令 (a) 为满足 (d\mid q^2a^2) 的最小正整数。

## 反向证明

先证 ((d,m)=1)。若素数 (r\mid(x,m))，因 ((q,m)=1) 及 (2)，有

\[
r\mid t+1.
\]

又 (4q\equiv1\pmod m)，故

\[
p=4qt+1\equiv t+1\equiv0\pmod r. \tag{4}
\]

但 (r\mid m=4q-1<p=4qt+1)（(t\ge1)），这与 (p) 为素数矛盾。于是
((x,m)=1)。由 (3) 便得到 ((d,m)=1)。

将 (3) 的第一条同余乘以 (4)，再用 (4q\equiv1\pmod m)，即得

\[
t\equiv-4d-1\pmod m. \tag{5}
\]

第二条的平方整除性与 (2) 给出

\[
d\mid q^2(t+1)^2,
\]

按 (a) 的极小定义，故 (a\mid t+1)，即

\[
t\equiv-1\pmod a. \tag{6}
\]

最后，(p\equiv1\pmod{24}) 等价于 (6\mid qt)，而 (d\le q(t+1)) 正是
(d\le x)。这正是平方根补全族的全部条件；反向方向由该族的证书构造立即成立。

所以未来若要把有限闭合提升为一般定理，唯一实质性的新步骤是证明：对给定的核心素数，
存在某个 (4q\mid p-1) 及除子 (d\mid q^2(t+1)^2)，同时满足 (5)--(6) 和大小界。
尾部代数本身不再是独立障碍。

## H19-k23 审计

对 524,288 层 H19-k23 共享选择器闭合的全部 (1\,155\,128) 条普通双尾证书，逐条
恢复 (1) 并检查 (3)--(6)，结果为

\[
1\,155\,128_{\text{normal form}}+0_{\text{failures}}. \tag{7}
\]

其中原共享缺口 (27) 的替代尾中，尾缺口分布为

\[
1\,987_{31}+389_{35}+164_{39}+116_{47}+45_{59}+3_{63}+4_{71}+2_{79}. \tag{8}
\]

这说明 (m=27\to31) 是当前最大替代分支，但 (7)--(8) 只是对有限存档证书的精确
分类，不能选择任意新素数的 (q,d)。

重建命令：

~~~bash
python3 reproductions/type_ii_square_root_completion_normal_form_audit.py \\
  --input reproductions/h19-k23-shared-selector-tail-descent-524288.json \\
  --output reproductions/type-ii-square-root-completion-normal-form-524288.json
python3 -m unittest tests/test_type_ii_square_root_completion_family.py \\
  tests/test_type_ii_square_root_completion_normal_form_audit.py -q
~~~
