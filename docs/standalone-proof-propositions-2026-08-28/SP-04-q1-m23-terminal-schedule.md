# SP-04：q=1 根的 \(M_{23}\) 全除子 terminal schedule

**状态：** OPEN_PROPOSITION
**目标：** 证明一个有限、可重放、终端优先的 registered-prefix schedule；不声称自然缺口全域穷尽。
**独立性：** 本文件自包含定义所有 Bradford 对象、量词和验收证据；不使用未在本文写出的前提。

## 0. 术语

* source 是一个有限对象 \(S\)，其中规范字段 \(p(S)\) 是本命题量词中的素数；
* source domain \(\mathscr D\) 是一组这样的对象以及一个可判定合法性谓词；
* terminal certificate 是正整数三元组 \((x,y,z)\)，直接满足
  \(4/p=1/x+1/y+1/z\)；
* schedule 是有限有序判定列表；按顺序执行，首个 terminal HIT 立即返回，只有全部
  MISS 才产生 scope-bound MISS；
* registered-prefix 表示 schedule 只量化明列的有限 gaps，不量化其他 gaps；
* digest 是规范有限编码的内容标识；任何数学结论都必须由重新计算原对象得到，
  不能仅相信 digest 相等；
* producer 是只允许在 schedule 全部 MISS 后执行的后继构造函数。

## 1. 完整背景

设 \(p\) 是满足 \(p\equiv1\pmod4\) 的素数。固定
\(B\equiv3\pmod4\)，\(3\le B\le p-2\)，并令

\[
\mathcal M_B=\{3,7,11,\ldots,B\}.
\]

对每个 \(m\in\mathcal M_B\)，定义首分母

\[
x_m=\frac{p+m}{4}.
\]

Bradford 型短证书有两类。对正整数 \(d\)：

\[
\mathcal I_m(p)=
\{d:d\mid x_m^2,\ m\mid px_m+d\},
\]

\[
\mathcal{II}_m(p)=
\{d:d\mid x_m^2,\ d\le x_m,\ m\mid x_m+d\}.
\]

若 \(d\in\mathcal I_m(p)\)，三项分母定义为

\[
\left(
x_m,\frac{px_m+d}{m},
\frac{p(x_m+px_m^2/d)}{m}
\right).
\]

若 \(d\in\mathcal{II}_m(p)\)，三项分母定义为

\[
\left(
x_m,\frac{p(x_m+d)}{m},
\frac{p(x_m+x_m^2/d)}{m}
\right).
\]

因为 \(m<p\)、\(p\) 为素数且 \(4x_m=p+m\)，有
\(\gcd(p,m)=\gcd(x_m,m)=1\)。因此上述分母在相应同余条件下为整数，
并直接满足 \(4/p=1/x_m+1/y+1/z\)。本命题允许证明者从头展开这一整数性证明，
不能把“程序返回整数”作为公理。

将每个 \(x_m\) 完全分解为

\[
x_m=\prod_i\ell_i^{a_i}.
\]

则 \(x_m^2\) 的所有正除子恰为
\(\prod_i\ell_i^{e_i}\)，其中 \(0\le e_i\le2a_i\)。

## 2. 待证明命题

定义有限命中集合

\[
\mathcal H_B(p)=
\{(m,d,\tau):m\in\mathcal M_B,\
d\in\mathcal B_m^\tau(p),\
\tau\in\{\mathrm I,\mathrm{II}\}\},
\]

其中 \(\mathcal B_m^{\mathrm I}=\mathcal I_m\)，
\(\mathcal B_m^{\mathrm{II}}=\mathcal{II}_m\)。
按 \((m,d,\tau)\) 的字典序排序，并规定 \(\mathrm I<\mathrm{II}\)。

要证明：

\[
\boxed{
\mathcal H_B(p)\ne\varnothing
\Longrightarrow
\text{存在唯一 earliest terminal }h_B(p);
}
\]

\[
\boxed{
\mathcal H_B(p)=\varnothing
\Longrightarrow
\forall m\in\mathcal M_B,\
\mathcal I_m(p)=\mathcal{II}_m(p)=\varnothing.
}
\]

对任意给定 source domain \(\mathscr D\)，其中每个状态 \(S\) 的规范字段绑定一个满足上述条件的
根素数 \(p(S)\)，要进一步证明互斥穷尽分割：

\[
\mathscr D=
\left(\coprod_{h}\{S:h_B(p(S))=h\}\right)
\coprod
\{S:\mathcal H_B(p(S))=\varnothing\}.
\]

在 \(B=23\) 时，\(\mathcal M_{23}=\{3,7,11,15,19,23\}\)。
该六层结果的语义只能是

~~~text
MISS_REGISTERED_PRIORITY_COMPLETE
coverage = REGISTERED_PRIORITY_ONLY
next_unchecked_gap = 27
global_exhaustion = false
~~~

## 3. 必须补出的独立证明

1. 完全因子分解确实生成全部且仅有一次的 \(x_m^2\) 除子；
2. 两类分母公式的整数性和方程恒等式；
3. 每个固定 gap 的所有 Type-I/Type-II 命中都被集合定义捕获；
4. earliest 顺序是确定的，重复证书不会造成两个 terminal 输出；
5. source-domain 分割不删除命中状态，也不通过标签暗中缩小量词；
6. schedule 的固定定义编码、逐 gap 重放编码和 source 绑定编码分离；
7. 构造器和独立 verifier 不共享会改变命中集合的内部结论；
8. terminal 命中先于任何 producer 分支。

## 4. 必须保留的控制

下列控制应在正文中逐项精确复算：

| 素数 | 六层最早结果 |
|---:|---|
| \(p=73\) | gap 7, Type II, \(d=1\) |
| \(p=241441\) | gap 11, Type II, \(x=60363,d=27\) |
| \(p=2689\) | gap 15, Type I, \(x=676,d=26\) |
| \(p=12721\) | gap 19, Type II, \(x=3185,d=7\) |
| \(p=1201\) | gap 23, Type I, \(x=306,d=34\) |
| \(p=2521\) | gap 23, Type II, \(x=636,d=8\) |
| \(p=21169\) | 六层两类全 MISS |

对 \(p=21169\)，还要验证 gap 31 的 Type-II 证书

\[
\frac4{21169}
=\frac1{5300}
+\frac1{3619899}
+\frac1{19185464700},
\]

因此六层 MISS 不能变成 terminal-universe MISS。

## 5. 不允许的推理

~~~text
只扫描 d=1 或少数素因子幂；
把 gaps [3,7,11,23] 称为连续 through-23 prefix；
把 next_unchecked_gap=27 写成所有更大 gap 都 MISS；
把 p=21169 的 arithmetic MISS 当作已验证 source 谱系；
把一个 local miss 重命名为 MISS_COMPLETE；
把 source terminal certificate 改名为另一个对象的 terminal certificate。
~~~

## 6. 完成证据

需要一份从本文件定义出发的数学证明、一份独立实现的逐 gap/divisor transcript、
全部控制的精确整数核验、schedule precedence 变异负控，以及明确的
global_exhaustion=false 证明边界。完成后只能宣称“六层 registered-prefix schedule
成立”，不能宣称所有自然缺口已穷尽，也不能宣称 Erdős–Straus 猜想已证明。
