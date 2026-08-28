# SP-04：$q=1$ 根的 $M_{23}$ 全除子 terminal schedule

## 完成结论

下述命题成立。对任意满足题面条件的 $p,B$，由全部 $x_m^2$ 正除子形成的 registered-prefix schedule 是有限、确定、可重放且 terminal-first 的；它返回且只返回按 $(m,d,\tau)$ 字典序（$\mathrm I<\mathrm{II}$）的最早命中。若没有命中，则其结论严格等价于所有**已注册** gap 的两类集合均为空。

在 $B=23$ 时，唯一允许的全 MISS 语义为

```text
MISS_REGISTERED_PRIORITY_COMPLETE
coverage = REGISTERED_PRIORITY_ONLY
next_unchecked_gap = 27
global_exhaustion = false
```

这里没有对 $m\ge 27$ 的其他自然 gap 作任何全称断言。特别地，本证明不推出自然 gap 全域穷尽，也不推出 Erdős–Straus 猜想。

## 1. schedule 的精确定义

令

$$
D_m(p)=\{d\in\mathbb Z_{>0}:d\mid x_m^2\},\qquad x_m=\frac{p+m}{4},
$$

并把 $D_m(p)$ 按数值递增排列。对固定 $p,B$，定义候选顺序为：先按 $m=3,7,\ldots,B$ 递增；固定 $m$ 后按 $d\in D_m(p)$ 递增；固定 $(m,d)$ 后先 $\mathrm I$、后 $\mathrm{II}$。Type-II 谓词本身包含 $d\le x_m$，所以 $d>x_m$ 时该测试必为 MISS。

生产 schedule 为：

```text
for m in [3,7,...,B] in increasing order:
    x := (p+m)/4
    D := every positive divisor of x^2, sorted increasingly
    for d in D:
        test Type-I;  if HIT, return its terminal certificate immediately
        test Type-II; if HIT, return its terminal certificate immediately
return the registered-scope MISS record
```

producer 不属于上述命中扫描；只有最后一行已经发生后，外层 orchestration 才可调用 producer。

## 2. 全除子枚举：全部且仅一次

设完全分解

$$
x_m=\prod_{i=1}^r\ell_i^{a_i},
$$

其中 $\ell_i$ 两两不同且均为素数。于是

$$
x_m^2=\prod_{i=1}^r\ell_i^{2a_i}.
$$

若 $d\mid x_m^2$，由算术基本定理，$d$ 不含任何 $\ell_i$ 之外的素因子，而且每个 $\ell_i$ 的指数唯一满足 $0\le e_i\le 2a_i$；故

$$
d=\prod_i\ell_i^{e_i}.
$$

反之，任意这样的指数向量都给出 $x_m^2$ 的正除子。两个不同指数向量不可能给出同一整数，否则违反素因数分解唯一性。因此指数笛卡尔积生成全部正除子，且每个正除子恰好一次；其数目为

$$
|D_m(p)|=\prod_i(2a_i+1)<\infty.
$$

这同时给出每个 gap 扫描的有限性。

## 3. 基本互素性

因为 $p\equiv1\pmod4$ 且 $m\equiv3\pmod4$，$x_m=(p+m)/4$ 是正整数。又因 $0<m<p$ 且 $p$ 为素数，$\gcd(p,m)=1$。

若正整数 $g$ 同时整除 $x_m,m$，则

$$
g\mid 4x_m-m=p.
$$

由于 $g\mid m<p$，不可能有 $g=p$，故 $g=1$。所以 $\gcd(x_m,m)=1$。进而，只要 $d\mid x_m^2$，就有

$$
\gcd(d,m)=1. \tag{3.1}
$$

## 4. 两类分母的整数性与恒等式

先记

$$
\frac4p-\frac1{x_m}=\frac{4x_m-p}{px_m}=\frac{m}{px_m}. \tag{4.1}
$$

### 4.1 Type-I

设 $d\in\mathcal I_m(p)$。令

$$
y=\frac{px_m+d}{m},\qquad
z=\frac{p(x_m+px_m^2/d)}{m}.
$$

由定义，$m\mid px_m+d$，所以 $y\in\mathbb Z_{>0}$。因 $d\mid x_m^2$，

$$
t=x_m+\frac{px_m^2}{d}\in\mathbb Z_{>0}.
$$

而

$$
dt=dx_m+px_m^2=x_m(d+px_m),
$$

右端被 $m$ 整除。结合 (3.1) 和 Euclid 引理，$m\mid t$，故 $z=pt/m\in\mathbb Z_{>0}$。

此外

$$
z=\frac{px_m(d+px_m)}{md}=\frac{px_my}{d},
$$

从而

$$
\frac1y+\frac1z
=\frac1y+\frac{d}{px_my}
=\frac{px_m+d}{px_my}
=\frac{m}{px_m}.
$$

结合 (4.1)，得到

$$
\frac4p=\frac1{x_m}+\frac1y+\frac1z.
$$

### 4.2 Type-II

设 $d\in\mathcal{II}_m(p)$。令

$$
y=\frac{p(x_m+d)}{m},\qquad
z=\frac{p(x_m+x_m^2/d)}{m}.
$$

由 $m\mid x_m+d$，$y$ 为正整数。再令

$$
t=x_m+\frac{x_m^2}{d}\in\mathbb Z_{>0}.
$$

则

$$
dt=dx_m+x_m^2=x_m(d+x_m),
$$

被 $m$ 整除；由 (3.1)，$m\mid t$，故 $z$ 为正整数。并且

$$
z=\frac{px_m(d+x_m)}{md}=\frac{x_my}{d},
$$

所以

$$
\frac1y+\frac1z
=\frac1y+\frac{d}{x_my}
=\frac{x_m+d}{x_my}
=\frac{m}{px_m}.
$$

再次结合 (4.1)，得到同一三项恒等式。条件 $d\le x_m$ 是 Type-II 命中定义的一部分；整数性证明没有擅自删去或放宽它。

## 5. 固定 gap 的命中完备性

对固定 $m$，第 2 节证明 schedule 枚举的列表恰为 $D_m(p)$，没有遗漏，也没有重复。对每个 $d\in D_m(p)$：

* Type-I 测试恰为 $m\mid px_m+d$，所以其 HIT 集恰为 $\mathcal I_m(p)$；
* Type-II 测试恰为 $d\le x_m$ 且 $m\mid x_m+d$，所以其 HIT 集恰为 $\mathcal{II}_m(p)$。

因此每个固定 gap 的全部 Type-I/Type-II 命中都被集合定义捕获；反向也没有伪命中。这里没有只扫描 $d=1$、少数素因子或少数素因子幂。

## 6. earliest 的唯一性、重复证书和 MISS 等价

$\mathcal M_B$ 有限，每个 $D_m(p)$ 有限，所以 $\mathcal H_B(p)$ 有限。字典序加上 $\mathrm I<\mathrm{II}$ 是全序；非空有限全序集存在唯一最小元。记其为

$$
h_B(p)=\min\mathcal H_B(p).
$$

第 1 节的执行顺序与该字典序完全相同，因此 schedule 在且仅在到达 $h_B(p)$ 时首次 HIT，并立即返回。即使不同标签计算出相同的三元组，最小的**标签**仍唯一，而且控制流只执行一次 `return`；因此不会产生两个 terminal 输出。若同一 $(m,d)$ 两类都 HIT，则 $\mathrm I$ 按定义优先。

又由 $\mathcal H_B(p)$ 的定义，

$$
\mathcal H_B(p)=\varnothing
\iff
\forall m\in\mathcal M_B,
\quad \mathcal I_m(p)=\mathcal{II}_m(p)=\varnothing. \tag{6.1}
$$

题面要求的第二个蕴含是 (6.1) 的一个方向；事实上这里得到等价。

## 7. source-domain 的互斥穷尽分割

令

$$
\Lambda_B=\mathcal M_B\times\mathbb Z_{>0}\times\{\mathrm I,\mathrm{II}\}.
$$

题设已假定每个 $S\in\mathscr D$ 的规范字段 $p(S)$ 都满足合法根素数条件。定义

$$
\mathscr D_h=\{S\in\mathscr D:
\mathcal H_B(p(S))\ne\varnothing\ \text{且}\ h_B(p(S))=h\},
\quad h\in\Lambda_B,
$$

以及

$$
\mathscr D_{\mathrm{miss}}=
\{S\in\mathscr D:\mathcal H_B(p(S))=\varnothing\}.
$$

对任意 $S\in\mathscr D$，由排中律，$\mathcal H_B(p(S))$ 为空或非空。为空时 $S\in\mathscr D_{\mathrm{miss}}$；非空时第 6 节给出唯一 $h_B(p(S))$，故 $S$ 属于唯一的 $\mathscr D_h$。两个不同纤维不可能相交，命中纤维也不可能与 MISS 纤维相交。因此

$$
\mathscr D=
\left(\coprod_{h\in\Lambda_B}\mathscr D_h\right)
\coprod\mathscr D_{\mathrm{miss}}.
$$

该构造没有按标签预筛 source，没有删除命中状态，也没有把不同但具有相同 $p(S)$ 的 source 合并。标签只是在完整执行后给出的纤维值，不参与合法性谓词，因而没有暗中缩小量词。

## 8. 三类编码严格分离，digest 不作为数学公理

证据包采用如下前缀无歧义编码。对任意有限字节串 $b$，令

$$
F(b)=\operatorname{dec}(|b|)\,\texttt{:}\,b,
$$

其中十进制长度无前导零。记录编码为

$$
R(t;(n_i,v_i)_{i=1}^k)
=F(t)F(\operatorname{dec}k)\prod_{i=1}^kF(n_i)F(v_i),
$$

每种记录类型固定字段次序；列表编码为

$$
L(v_1,\ldots,v_k)=F(\texttt{SP04.LIST.v1})F(\operatorname{dec}k)\prod_iF(v_i).
$$

长度前缀使解析唯一。三种顶层 tag 和内容彼此分离：

1. `SP04.DEFINITION.v1`：只编码 $B$、注册 gap、候选顺序、两类谓词与分母公式、MISS 字面量及 producer precedence；
2. `SP04.GAP-REPLAY.v1`：只编码 $(p,m,x)$、$x$ 的分解、每个完整除子行、命中与精确等式；不含 source payload；
3. `SP04.SOURCE-BINDING.v1`：编码完整 source payload、由 domain adapter 提取的 $p$、definition 标识、六个 replay 标识和最终 outcome；不把 source 与某个命中标签预先绑定。

固定 definition 的 SHA-256 内容标识为

```text
5f30a27886ab95f30c8adad094e19d70c6ea021e9251cc33b2468bdb2bcbca93
```

但 verifier 的验收顺序是：从原 source 重新提取并验证 $p$；重新计算 $x$、全部除子、两类命中、分母和恒等式；重建 definition/replay/binding 的完整字节；最后才核对 digest 作为索引。故任何数学结论都不由“digest 相等”单独推出。

## 9. constructor 与独立 verifier 的非共享结论

实现 A（`sp04_constructor.py`）先完全分解 $x$，再用指数范围 $0\le e_i\le2a_i$ 的笛卡尔积生成除子。

实现 B（`sp04_verifier.py`）不导入实现 A，也不使用 A 的分解来决定命中。它令 $N=x^2$，逐个扫描 $1\le k\le x=\sqrt N$；若 $k\mid N$，同时加入 $k$ 与 $N/k$。该方法完备，因为任一 $d\mid N$：若 $d\le x$，它被直接扫描；若 $d>x$，则互补除子 $N/d<x$ 被扫描并把 $d$ 加入。之后 B 独立重算所有同余、整数分母和

$$
4xyz=p(yz+xz+xy). \tag{9.1}
$$

B 只共享公开 specification，不共享会改变命中集合的中间结论。证据中注册六层共有 756 个除子行；另有 gap 31 的 75 行边界 replay，共 831 行。A 写出 `divisor_transcript.tsv`，B 独立写出 `independent_divisor_transcript.tsv`，两者逐字节行内容一致。素性 transcript 对七个控制数逐个列出 $2\le r\le\lfloor\sqrt p\rfloor$ 的精确余数，共 884 行；B 同样另写独立副本并比较。

## 10. producer precedence 与变异负控

正确 orchestration 在 terminal HIT 时立即返回，producer 调用次数为零；只有六个 gap 全部完成且都 MISS 后，才先产生 registered-scope MISS，再调用 producer。

独立 verifier 执行了两种故意错误的变异：

* `producer-first`：扫描前调用 producer；
* `local-miss-as-complete`：仅 gap 3 MISS 就调用 producer。

六个命中控制在正确 schedule 下均返回题定 terminal 且 `producer_calls=0`；两种变异均先返回 `PRODUCER_SENTINEL`，与期望 terminal 不同，故全部被拒绝。对 $p=21169$，正确 event 顺序的末尾严格为

```text
... GAP_COMPLETE_MISS:23
REGISTERED_SCOPE_MISS
PRODUCER_CALLED
```

所以 producer 既不先于 terminal，也不先于六层完整 MISS。

## 11. 控制的精确重算

### 11.1 素性和合法性

下表中的素性由对所有 $2\le r\le\lfloor\sqrt p\rfloor$ 检查 $p\bmod r\ne0$ 得到；每个余数均在 `primality_transcript.tsv` 明列。

| $p$ | $\lfloor\sqrt p\rfloor$ | $p\bmod4$ | $23\le p-2$ |
|---:|---:|---:|:---:|
| 73 | 8 | 1 | 是 |
| 241441 | 491 | 1 | 是 |
| 2689 | 51 | 1 | 是 |
| 12721 | 112 | 1 | 是 |
| 1201 | 34 | 1 | 是 |
| 2521 | 50 | 1 | 是 |
| 21169 | 145 | 1 | 是 |

### 11.2 六层全部 hit sets

下表不是抽样。`#div` 是 $x_m^2$ 的全部正除子数；每个具体 $d$、两个余数、Type-II eligibility、命中分母和 (9.1) 两边都逐行存于 `divisor_transcript.tsv`，并由实现 B 独立逐行比对。

| $p$ | $m$ | $x_m$ | $x_m$ 完全分解 | #div | $\mathcal I_m(p)$ | $\mathcal{II}_m(p)$ |
|---:|---:|---:|:---|---:|:---|:---|
| 73 | 3 | 19 | `19^1` | 3 | $\varnothing$ | $\varnothing$ |
| 73 | 7 | 20 | `2^2*5^1` | 15 | $\{10,80\}$ | $\{1,8\}$ |
| 73 | 11 | 21 | `3^1*7^1` | 9 | $\{7\}$ | $\{1\}$ |
| 73 | 15 | 22 | `2^1*11^1` | 9 | $\{44\}$ | $\varnothing$ |
| 73 | 19 | 23 | `23^1` | 3 | $\varnothing$ | $\varnothing$ |
| 73 | 23 | 24 | `2^3*3^1` | 21 | $\varnothing$ | $\varnothing$ |
| 241441 | 3 | 60361 | `7^1*8623^1` | 9 | $\varnothing$ | $\varnothing$ |
| 241441 | 7 | 60362 | `2^1*30181^1` | 9 | $\varnothing$ | $\varnothing$ |
| 241441 | 11 | 60363 | `3^2*19^1*353^1` | 45 | $\{1539,543267,191773251\}$ | $\{27,1083,9531\}$ |
| 241441 | 15 | 60364 | `2^2*15091^1` | 15 | $\varnothing$ | $\varnothing$ |
| 241441 | 19 | 60365 | `5^1*12073^1` | 9 | $\varnothing$ | $\varnothing$ |
| 241441 | 23 | 60366 | `2^1*3^1*10061^1` | 27 | $\{90549\}$ | $\{9\}$ |
| 2689 | 3 | 673 | `673^1` | 3 | $\varnothing$ | $\varnothing$ |
| 2689 | 7 | 674 | `2^1*337^1` | 9 | $\varnothing$ | $\varnothing$ |
| 2689 | 11 | 675 | `3^3*5^2` | 35 | $\varnothing$ | $\varnothing$ |
| 2689 | 15 | 676 | `2^2*13^2` | 25 | $\{26,17576\}$ | $\{104\}$ |
| 2689 | 19 | 677 | `677^1` | 3 | $\varnothing$ | $\varnothing$ |
| 2689 | 23 | 678 | `2^1*3^1*113^1` | 27 | $\{1356\}$ | $\{12\}$ |
| 12721 | 3 | 3181 | `3181^1` | 3 | $\varnothing$ | $\varnothing$ |
| 12721 | 7 | 3182 | `2^1*37^1*43^1` | 27 | $\varnothing$ | $\varnothing$ |
| 12721 | 11 | 3183 | `3^1*1061^1` | 9 | $\varnothing$ | $\varnothing$ |
| 12721 | 15 | 3184 | `2^4*199^1` | 27 | $\varnothing$ | $\varnothing$ |
| 12721 | 19 | 3185 | `5^1*7^2*13^1` | 45 | $\{13,4459\}$ | $\{7,2401\}$ |
| 12721 | 23 | 3186 | `2^1*3^3*59^1` | 63 | $\varnothing$ | $\varnothing$ |
| 1201 | 3 | 301 | `7^1*43^1` | 9 | $\varnothing$ | $\varnothing$ |
| 1201 | 7 | 302 | `2^1*151^1` | 9 | $\varnothing$ | $\varnothing$ |
| 1201 | 11 | 303 | `3^1*101^1` | 9 | $\varnothing$ | $\varnothing$ |
| 1201 | 15 | 304 | `2^4*19^1` | 27 | $\varnothing$ | $\varnothing$ |
| 1201 | 19 | 305 | `5^1*61^1` | 9 | $\varnothing$ | $\varnothing$ |
| 1201 | 23 | 306 | `2^1*3^2*17^1` | 45 | $\{34,5508\}$ | $\{108\}$ |
| 2521 | 3 | 631 | `631^1` | 3 | $\varnothing$ | $\varnothing$ |
| 2521 | 7 | 632 | `2^3*79^1` | 21 | $\varnothing$ | $\varnothing$ |
| 2521 | 11 | 633 | `3^1*211^1` | 9 | $\varnothing$ | $\varnothing$ |
| 2521 | 15 | 634 | `2^1*317^1` | 9 | $\varnothing$ | $\varnothing$ |
| 2521 | 19 | 635 | `5^1*127^1` | 9 | $\varnothing$ | $\varnothing$ |
| 2521 | 23 | 636 | `2^2*3^1*53^1` | 45 | $\{848\}$ | $\{8\}$ |
| 21169 | 3 | 5293 | `67^1*79^1` | 9 | $\varnothing$ | $\varnothing$ |
| 21169 | 7 | 5294 | `2^1*2647^1` | 9 | $\varnothing$ | $\varnothing$ |
| 21169 | 11 | 5295 | `3^1*5^1*353^1` | 27 | $\varnothing$ | $\varnothing$ |
| 21169 | 15 | 5296 | `2^4*331^1` | 27 | $\varnothing$ | $\varnothing$ |
| 21169 | 19 | 5297 | `5297^1` | 3 | $\varnothing$ | $\varnothing$ |
| 21169 | 23 | 5298 | `2^1*3^1*883^1` | 27 | $\varnothing$ | $\varnothing$ |

因此各控制的最早标签正是题面所列；例如，$p=241441$ 的 gap 3、7 两类均空，而 gap 11 的最小命中 $d=27$ 属于 Type-II，早于该 gap 的 $d=1539$ Type-I 命中。

### 11.3 最早 terminal 的精确三元组

下表最后一列是同一个精确整数

$$
K=4xyz=p(yz+xz+xy),
$$

所以不是浮点近似。

| $p$ | earliest $(m,d,\tau)$ | $(x,y,z)$ | $K$ |
|---:|:---|:---|---:|
| 73 | $(7,1,\mathrm{II})$ | $(20,219,4380)$ | 76737600 |
| 241441 | $(11,27,\mathrm{II})$ | $(60363,1325511090,2963400960210)$ | 948428487105143400350362800 |
| 2689 | $(15,26,\mathrm{I})$ | $(676,121186,8472598004)$ | 2776359747671259776 |
| 12721 | $(19,7,\mathrm{II})$ | $(3185,2137128,972393240)$ | 26475361169535532800 |
| 1201 | $(23,34,\mathrm{I})$ | $(306,15980,172727820)$ | 3378473249846400 |
| 2521 | $(23,8,\mathrm{II})$ | $(636,70588,5611746)$ | 1007734181392512 |

这些三元组分别直接满足 $4/p=1/x+1/y+1/z$。此外，独立 verifier 对表 11.2 中所有非空 hit，而不只是 earliest，均执行了相同的整数性和交叉乘法核验。

### 11.4 $p=21169$ 的六层 MISS 与 gap 31 边界证书

表 11.2 给出

$$
\forall m\in\{3,7,11,15,19,23\},\qquad
\mathcal I_m(21169)=\mathcal{II}_m(21169)=\varnothing.
$$

故六层结果严格为

```text
MISS_REGISTERED_PRIORITY_COMPLETE
coverage = REGISTERED_PRIORITY_ONLY
next_unchecked_gap = 27
global_exhaustion = false
```

另一方面，$31\equiv3\pmod4$、$31<21169$，且

$$
x_{31}=\frac{21169+31}{4}=5300,
\qquad d=1\mid5300^2,
\qquad 1\le5300.
$$

Type-II 同余为

$$
5300+1=5301=31\cdot171.
$$

因此

$$
y=\frac{21169(5300+1)}{31}
=21169\cdot171
=3619899,
$$

并且

$$
5300+5300^2=28095300=31\cdot906300,
$$

所以

$$
z=\frac{21169(5300+5300^2)}{31}
=21169\cdot906300
=19185464700.
$$

精确交叉乘法给出

$$
4\cdot5300\cdot3619899\cdot19185464700
=1472328223019784360000,
$$

以及

$$
21169\bigl(3619899\cdot19185464700
+5300\cdot19185464700
+5300\cdot3619899\bigr)
=1472328223019784360000.
$$

故

$$
\frac4{21169}
=\frac1{5300}
+\frac1{3619899}
+\frac1{19185464700}.
$$

这给出一个具体反例，否定“六层 MISS 蕴含所有自然 gap MISS”。它没有把 gap 31 证书改名为别的 source 对象的证书；它只是同一根素数 $p=21169$ 的独立、未注册边界 witness。

## 12. 证明边界

已证明的命题恰为：

> **六层 registered-prefix schedule 成立。**

没有证明、也没有使用以下任一更强命题：

* $m=27$ 或所有 $m\ge27$ 都 MISS；
* $p=21169$ 具有任何未提供的 source 谱系；
* registered MISS 是 terminal-universe MISS；
* 所有自然 gap 已穷尽；
* Erdős–Straus 猜想成立。

`next_unchecked_gap=27` 仅表示序列 $3,7,11,15,19,23,27,\ldots$ 中紧随最后注册项的下一个 gap；`global_exhaustion=false` 既由量词范围本身要求，也由第 11.4 节的 gap-31 witness 具体见证。

## 13. 重放

在证据目录执行：

```bash
python3 sp04_constructor.py
python3 sp04_verifier.py
```

预期最后一项为：

```text
SP-04 INDEPENDENT VERIFICATION: PASS
```

`sp04_constructor.py` 与 `sp04_verifier.py` 仅使用 Python 标准库。constructor transcript 与独立 verifier transcript、素性 transcript、分离的 definition/replay/source-binding 编码、变异负控结果和最终报告均随证据包提供。
