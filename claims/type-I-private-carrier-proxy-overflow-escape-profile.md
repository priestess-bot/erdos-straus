---
kind: claim
claim_id: type-I-private-carrier-proxy-overflow-escape-profile
title: 私有载体代理过载的较小 R 或 Type II 有限分流
statement: 在253个冻结平方终端F状态的确定性首个盒外见证中，筛出37个不同(p,R,q)状态：q坐标满足完整线性源私有唯一性判据，其代理overflow excess严格超过唯一块的全部q进高度，且全部合法载体分配均不能承载该见证。完整线性目标谱中35个状态已有严格更小R的一般B Type I命中及显式偶终端；168434809的R=27与310002289的R=19是仅剩两个更小R反例。31个不同素数又全部有h<=51的直接Type II证书，故有限优先选择器精确分流为37=35+2。这证明代理私有过载不强制较小R，但不证明全称逃逸，也不建立overflow到真实载体的注入。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-all-assignment-height-upper-bound
  - type-I-f-square-terminal-relation-certificate
  - type-I-linear-b-gt-one-full-spectrum-profile-600m
  - type-I-linear-private-carrier-support-exit-marked-equivalence
  - type-II-coprime-factor-normal-form
topics:
  - type-I
  - type-II
  - private-carrier
  - proxy-overflow
  - support-exit
  - smaller-R
  - finite-selector
  - counterexample-boundary
  - proof-program
sources:
  - claim: type-I-f-overflow-all-assignment-height-upper-bound
    role: deterministic-overflow-excess-and-optimistic-height-input
  - claim: type-I-f-square-terminal-relation-certificate
    role: source-state-and-F-certificate-input
  - claim: type-I-linear-b-gt-one-full-spectrum-profile-600m
    role: complete-linear-source-target-spectrum
  - claim: type-I-linear-private-carrier-support-exit-marked-equivalence
    role: private-support-exit-and-even-terminal-interface
  - claim: type-II-coprime-factor-normal-form
    role: exact-independent-Type-II-verification
visibility: public
last_checked: '2026-07-30'
---

# 私有载体代理过载的较小 \(R\) 或 Type II 有限分流

## 筛选对象

冻结平方终端数据包含 253 个有限指数 F 状态。对每个状态，既有高度审计保存一个
半径不超过 6 的确定性首个盒外见证，并在全部合法线性源和方向分配上给出乐观载体高度
上界。这里只取类别

```text
no_assignment_can_carry_all_excess
```

中的记录。对见证的每个溢出素数 \(q\)，再要求当前源的两个有序块中恰有一个

\[
B=tR+1
\]

被 \(q\) 整除，并置

\[
d_0=\frac Bq,
\qquad
n_0=\frac{p-t}{q}=u d_0.
\]

保留条件为

\[
0<t,R<q,
\qquad
d_0+R>n_0-1,
\tag{1}
\]

且 \(d_0\) 是 \(n_0\) 中唯一满足

\[
D\ge d_0,
\qquad
D\equiv d_0\pmod t
\tag{2}
\]

的正因子。式 (1)--(2) 正是完整有序源谱私有唯一性判据。最后还要求该确定性见证在
\(q\) 坐标的盒外层数严格超过唯一块的全部高度：

\[
e_q>v_q(tR+1).
\tag{3}

完整筛选得到

\[
37\text{ 个不同 }(p,R,q)\text{ 状态},
\qquad31\text{ 个不同核心素数}.
\tag{4}

按

```text
p, R, q, overflow_excess, block_height, t, u, d0, n0
```

编码的 37 行 TSV 的 SHA-256 为

```text
94595e1e49e0faf5046dd03ab94fd15cfe3703adec4718f0f47a978f4bfc05d0
```

这里的“代理过载”有严格限定：它对当前确定性首见证和全部合法载体分配成立，但没有对
完整目标纤维取最小 \(q\)-缺陷，也没有证明盒外指数必须逐层收费到真实块。因此 (3) 不是
已经完成的 overflow-to-carrier 注入。

## 完整线性谱中的向下退出

对 31 个素数调用已经冻结的完整线性源谱。每个谱已经穷尽全部源可达
\(R\equiv3\pmod4\)，并把目标中心化平方除子分类为 hit、有限指数障碍或子群角色障碍。
脚本对每个选中状态检查全部 \(R'<R\)：

\[
\boxed{
37=35_{\text{存在更小 }R'\text{ Type I 命中}}
+2_{\text{全部更小 }R'\text{ 失败}}.}
\tag{5}

对 35 个命中状态，脚本不只读取分类标签，还重新分解所选

\[
K_{R'}=\frac{pR'+1}{4},
\]

完整枚举 \(D\mid K_{R'}^2\)，恢复一般 \(B\) 正规形、一个实际线性源以及目标和偶源
的两条精确单位分数恒等式。又逐项验证

\[
q\nmid K_{R'}.
\]

这与[私有载体的支撑退出定理](type-I-linear-private-carrier-support-exit-marked-equivalence.md)
一致：这些不是循环复用原私有 \(q\) 的形式命中，而是真正换掉该支撑的 Type I 偶终端。

此前容量一代理余核的两个重状态都在这 35 个对象中：

| \(p\) | 原 \((R,q)\) | 代理超额/块高 | 所选更小 \(R'\) | \(D\) | Type I 缺口 |
|---:|:---:|:---:|---:|---:|---:|
| 99151369 | \((82011,115561)\) | \(4/1\) | 11 | 261 | 95 |
| 487572409 | \((318051,6965317)\) | \(3/1\) | 23 | 684 | 119 |

所以这两个有限余核已经有比候选差菜单更直接的解释：完整谱中存在较小 \(R\) 的
\(q\)-free Type I 命中及显式严格偶终端。

## 两个更小 R 反例

式 (5) 的两个遗漏说明“私有载体代理过载必然向下换模命中”是错误命题。

### \(p=168434809\)

当前状态为

\[
(t,u,R,q,d_0,n_0)
=(2054083,3,27,27730121,2,6),
\tag{6}

且

\[
tR+1=55460242=2q,
\qquad
K_R=41\cdot27730121.
\]

确定性首见证的两个坐标超额为 \((3,4)\)，两个块的最大高度均为 1。完整源谱中小于
27 的源可达模数及目标分类为：

| \(R'\) | \(K_{R'}\) | 一般 \(B\) 目标 |
|---:|---:|:---:|
| 3 | 126326107 | miss |
| 7 | 294760916 | miss |
| 11 | 463195725 | miss |
| 19 | 800065343 | miss |
| 23 | 968500152 | miss |

当前 \(R=27\) 也为 miss；其后 \(R=51,55,59\) 继续失败，首次目标命中反而位于

\[
R'=75>27,
\quad D=803531,
\quad(A,B,C,H;m)=(3512,67,179,263333;42855).
\tag{7}

### \(p=310002289\)

此时

\[
(t,u,R,q,d_0,n_0)
=(5344867,3,19,50776237,2,6),
\tag{8}

\[
tR+1=101552474=2q,
\qquad
K_R=29\cdot50776237,
\]

且首见证同样有超额 \((3,4)\)、最大块高度 \((1,1)\)。全部更小源可达模数

\[
R'=3,7,11,15
\]

均为目标 miss。首次线性目标命中是

\[
R'=23>19,
\quad D=2524,
\quad(A,B,C,H;m)=(61411,2,631,1412451;439).
\tag{9}

两例都没有合法的 lower-modulus 严格下降可替代这个失败；但它们不是 Erdős--Straus
反例，也不是逃逸三分支的反例，因为下一节的独立 Type II 分支立即闭合。

## 独立 Type II 分支

脚本对 31 个不同素数依次完整检查

\[
h=3,7,11,\ldots,51,
\qquad x_h=\frac{p+h}{4},
\]

并枚举全部

\[
d\mid x_h^2,
\qquad d\le x_h,
\qquad h\mid x_h+d.
\tag{10}

每个命中都规范化为

\[
x_h=ABC,
\qquad d=A^2C,
\qquad(A,B)=1,
\qquad A\le B,
\qquad h\mid A+B,
\]

并以精确有理数重放三个目标分母。结果是 31 个素数全部命中；最小 Type II 缺口分布为

\[
\begin{array}{c|rrrrrrr}
h&15&19&27&31&39&47&51\\ \hline
\#p&3&12&4&9&1&1&1.
\end{array}
\tag{11}

两个更小 \(R\) 反例的直接证书为：

| \(p\) | \(h\) | \(x\) | \(d\) | \((A,B,C)\) |
|---:|---:|---:|---:|:---|
| 168434809 | 31 | 42108710 | 47 | \((1,895930,47)\) |
| 310002289 | 19 | 77500577 | 43 | \((1,1802339,43)\) |

因此按“先找更小 \(R\) Type I，失败后取直接 Type II”的有限优先规则，37 个状态精确
闭合为

\[
\boxed{37=35_{\text{更小 }R\text{ Type I 偶终端}}+2_{\text{直接 Type II}}.}
\tag{12}

注意 31 个素数其实全部已有 \(h\le51\) Type II；式 (12) 是为了测量两个分支的逻辑
必要性，而不是声称前 35 个必须使用 Type I。

## 复现与证明边界

复现命令：

~~~bash
python3 reproductions/type_i_private_carrier_escape_profile.py
~~~

结果文件：

~~~text
reproductions/type-i-private-carrier-escape-profile-results.json
~~~

~~~text
script sha256:
6f642df2350bbbf9bf26acdb9a72adbcaa3d09d6ad0b40db162f4d89cdaf0ca6

result sha256:
7466040e4f693ff39ab5d8f53e2222c18e10f3e48d1316ff8dbf767f458448df
~~~

该脚本哈希锁定三个既有输入，并独立重建所选 Type I/偶源和全部 Type II 恒等式；它不
回跑历史大范围素数扫描。

本剖面的理论含义是负面但明确的：即使把“私有”加强到完整源谱唯一性，并把当前首见证
的超额加强到超过全部块高度，仍不能删除 Type II 分支而只证明向下换模。另一方面，冻结
样本没有三分支反例。要升级为全称定理，仍必须：

1. 用完整目标纤维或完整 Pareto 集定义选择不变的 \(q\)-缺陷；
2. 证明该缺陷确实注入真实载体高度，而不是只比较两个数值；
3. 从真实缺陷构造较小 \(R\) 命中、精确 Type II 正规形或不同标记且可递归闭合的下降。

因此 (12) 是一个有限压力剖面和反例边界，不是私有载体逃逸引理的证明。
