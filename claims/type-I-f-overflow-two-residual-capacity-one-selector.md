---
kind: claim
claim_id: type-I-f-overflow-two-residual-capacity-one-selector
title: 两个局部余核的容量一代理最小面与短证书选择器
statement: 对先前遗留的 (p,t)=(99151369,27337)、(487572409,106017)，重坐标 q=115561、6965317 在完整线性源谱中都只有一个高度 1 的真实块，故与真实块高度相容的有限代理约束是重坐标盒外量不超过 1，而不是等于 0。在该容量一代理模型中两例的精确最低成本都为 12，完整最小面共有 8 个向量、4 个反演对和 4 个 overflow pattern；40 个 shared-gap 检查及 13884 个三类直接分因子对均无 Type II 命中，但过载坐标的 q 可除标签差/模数差有限菜单给出 11 个不同的 state-scoped、经独立验证的 Type II 命中缺口并覆盖全部 4 个 pattern。两例还分别在 h=19、31 有逐项验证的同缺口 Type I/II 正规形。因此两个对象在该有限选择器下已经闭合；它们只是局部状态余核，不是素数层未解实例。候选差仍不构造真实 q 迁移边，本卡不推出从 overflow 到载体的全称容量桥、全称选择器或一般双正规形定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-four-hard-core-collision-selector
  - type-I-linear-private-carrier-isolation-criterion
  - type-I-f-overflow-lower-modulus-omega-carrier-boundary
  - type-II-coprime-factor-normal-form
  - type-I-linear-source-general-b-completion-profile-600m
topics:
  - type-I
  - type-II
  - F-state
  - lower-modulus
  - capacity-one
  - minimum-face
  - q-divisible-difference
  - adaptive-selector
  - state-prime-ledger
  - finite-audit
  - proof-program
sources:
  - claim: type-I-f-overflow-four-hard-core-collision-selector
    role: two-state-residual-input-and-zero-capacity-boundary
  - claim: type-I-linear-private-carrier-isolation-criterion
    role: complete-spectrum-heavy-carrier-uniqueness
  - claim: type-II-coprime-factor-normal-form
    role: complete-Type-II-certificate-test
  - claim: type-I-linear-source-general-b-completion-profile-600m
    role: existing-cross-support-Type-I-context
visibility: public
last_checked: '2026-07-30'
---

# 两个局部余核的容量一代理最小面与短证书选择器

## 状态余核不等于素数余核

此前的四硬核差值菜单闭合两例后，台账留下

\[
(p,t)=(99151369,27337),
\qquad
(487572409,106017).
\tag{1}
\]

这里的“余核”只表示指定低模数目标纤维、指定当前 \(K\)-支撑和指定局部容量接口尚未
闭合。它不表示相应素数没有 Erdős--Straus 分解。事实上，仓库既有
`type-ii-tail-deflation-500m-full-results.json` 已分别保存缺口 \(19\) 和 \(31\) 的
最短 Type II 证书；一般 \(B\) 全谱也已有其它 \(K\)-支撑上的 Type I 证书。

本卡的新内容不是发现两个素数可解，而是回答更细的问题：从 (1) 的局部容量状态出发，
能否由一个有限、精确且不混淆真实迁移的二级选择器重新得到短终端？答案对这两个冻结
状态都是肯定的。

## 与真实块高度相容的容量模型

写当前目标纤维的指数盒为 \(|z_i|\le\nu_i\)，盒外需求为

\[
e_i(z)=(|z_i|-\nu_i)_+,
\qquad
\Omega_1(z)=\sum_i e_i(z).
\tag{2}
\]

两个状态的完整线性源谱分别只有以下一个重 \(q\)-块：

| \(p\) | 重 \(q\) | 唯一 \((c,R)\) | \(cR+1\) | \(v_q(cR+1)\) |
|---:|---:|:---:|---:|---:|
| 99151369 | 115561 | \((31,82011)\) | \(2542342=22\cdot115561\) | 1 |
| 487572409 | 6965317 | \((219,318051)\) | \(69653170=10\cdot6965317\) | 1 |

其完整谱唯一性另由
[线性源私有 q 载体的唯一性判据](type-I-linear-private-carrier-isolation-criterion.md)
作解析证明。因此该有限载体模型中可用的重坐标高度为 1。旧卡中的“禁止重坐标溢出”
是容量 \(H=0\) 的边界实验，不是与真实块高度相容的版本。对

\[
\Theta_q(H)=
\min\{\Omega_1(z):z\text{ 命中目标纤维且 }e_q(z)\le H\}
\tag{3}
\]

脚本从 \(H=0\) 精确算到首次恢复无约束最低价，得到：

| \(p\) | \(\Theta_q(0)\) | \(\Theta_q(1)\) | 后续容量曲线 |
|---:|---:|---:|:---|
| 99151369 | 12 | **12** | \(H=2,3,4:12;\ H=5:12;\ H=6:10;\ H=7:9\) |
| 487572409 | 15 | **12** | \(H=2:10;\ H=3:9;\ H=4:8\) |

特别地，两例的块高度相容容量一代理最低价都是 12。旧的 \(12,15\) 应保留为容量零
历史边界，不能再称为两个状态的“实际下一最小面”。这里仍未证明任意 overflow 层都能
注入一个真实块层；该缺口正是后文保留的全称容量桥。

## 容量一代理完整最小面

两个状态的当前 \(K\) 都是五个不同素数之积。按下表给定的素数顺序，容量一代理模型的
成本 12 最小面为：

| \(p\) | 素数顺序 | 向量代表（连同相反向量） | overflow pattern |
|---:|:---|:---|:---|
| 99151369 | \((5,11,227,1409,115561)\) | \((1,6,1,8,1)\) | \((0,5,0,7,0)\) |
|  |  | \((1,-2,-11,-1,-2)\) | \((0,1,10,0,1)\) |
|  |  | \((0,1,12,2,1)\) | \((0,0,11,1,0)\) |
| 487572409 | \((5,31,149,241,6965317)\) | \((-1,7,2,5,2)\) | \((0,6,1,4,1)\) |

所以共有 8 个向量、4 个反演对和 4 个 pattern。升序成本壳层的直接枚举逐层与截断
生成函数

\[
\prod_i\left((2\nu_i+1)+\frac{2x}{1-x}\right)
\tag{4}
\]

的相应系数一致；容量零与容量一代理模型的目标层又由独立 meet-in-the-middle 重建得到
同一向量集合。因此这里枚举的是完整代理最小面，不是从一次最短路中抽出的代表元。

## shared-gap 与直接分因子边界

对每个反演对写

\[
\prod_iq_i^{z_i}=\frac ab,
\qquad (a,b)=1,
\qquad t\mid a+b.
\]

完整分解 \(a+b\) 后，两例分别得到 9 和 31 个不同合法 shared gap，共 40 个
状态内检查，Type II 命中为 0。随后完整生成三类互素因子对：

| \(p\) | 定向分因子 | 任意坐标重分配 | 纯二坐标 | 直接 Type II 命中 |
|---:|---:|---:|---:|---:|
| 99151369 | 963 | 5594 | 172 | 0 |
| 487572409 | 864 | 6188 | 103 | 0 |
| **合计** | **1827** | **11782** | **275** | **0** |

所以容量一代理最小面不能由共享和式或面内直接重分配闭合。这里的 13884 是三类菜单大小
之和；各菜单分别去重，不声称三类之间互不重叠。

## 过载坐标的差值候选选择器

把既有三通道高度作为乐观局部容量，两例的容量向量分别为

\[
(7,4,2,1,1),
\qquad
(7,3,3,3,1).
\tag{5}
\]

只对每个 pattern 中严格超过 (5) 的坐标生成 \(q\)-可除标签差或模数差菜单。完整结果
如下；表中的命中均由随后独立执行的 Type II 除子枚举与单位分数恒等式确认。

| \(p\) | overflow pattern | 严格过载坐标 | 可选命中缺口 |
|---:|:---|:---|:---|
| 99151369 | \((0,5,0,7,0)\) | \(11,1409\) | \(19,55,87,95,311,435,803\) |
| 99151369 | \((0,1,10,0,1)\) | \(227\) | \(71\) |
| 99151369 | \((0,0,11,1,0)\) | \(227\) | \(71\) |
| 487572409 | \((0,6,1,4,1)\) | \(31,241\) | \(31,43,7967\) |

五个 \(q\)-菜单共有 49 条候选边；按素数内合并后是 97 个不同缺口检查和 11 个不同的
state-scoped 命中缺口。每个命中都经 Type II 正规形与单位分数恒等式独立验证；四个
pattern 都至少有一张证书。因此有限选择器可以取

\[
\begin{aligned}
(0,5,0,7,0)&\longmapsto(q,h)=(11,19),\\
(0,1,10,0,1),(0,0,11,1,0)&\longmapsto(q,h)=(227,71),\\
(0,6,1,4,1)&\longmapsto(q,h)=(31,31).
\end{aligned}
\tag{6}
\]

注意第二个 \(99151369\) pattern 虽在 \(11\) 坐标有需求 1，但该需求没有超过容量 4；
它必须按过载坐标 \(227\) 选择，而不能把“出现在支撑中”误写成“发生容量过载”。

式 (6) 是**候选生成规则加独立证书验证**。\(q\mid(t-t')\) 或
\(q\mid(R-R')\) 本身不说明两端的实际块都含 \(q\)，更不产生一条可收费的真实载体
迁移边。重素数 \(115561,6965317\) 的真实碰撞图由上一节的唯一性结论明确为无边。

## 同缺口 Type I/II 终端

每个状态的差值菜单还包含一组同 \(p\)、同缺口、同第一分母的 Type I/II 正规形：

| \(p\) | \(h\) | \(x=(p+h)/4\) | Type I \((A,B,C)\) | Type II \((A,B,C)\) |
|---:|---:|---:|:---|:---|
| 99151369 | 19 | 24787847 | \((60019,1,413)\) | \((59,60019,7)\) |
| 487572409 | 31 | 121893110 | \((2,11855,5141)\) | \((53,970,2371)\) |

脚本逐项验证 \(ABC=x\)、相应互素与定向条件、\(A^2C\mid x^2\)、两个尾分母的
整性和精确单位分数恒等式。这里的“双正规形”只是两个有限巧合，不是一般存在定理。
同时，旧 Type II 台账在相同首达缺口已经保存更小除子 \(47\) 与 \(1060\) 的证书；
所以本节是状态选择器与素数证书台账的对齐，不是新的素数层存在性发现。

## 复现与边界

~~~bash
python3 reproductions/type_i_f_overflow_two_residual_constrained_minimum_face.py
~~~

~~~text
script sha256:
57632da428518446886201ccecc1899fbfaa063dd668249116572f0f5f9319e7

result sha256:
c35756a1b06f35eac38f9e965f3737755a98aa00f63476040fcaea5064feea55
~~~

本卡只闭合两个冻结的低模数容量状态及明确定义的有限菜单。它不证明任意核心素数都在
相同缺口界内闭合，也不把候选差升级为实际迁移。结合私有载体唯一性判据后，下一项真正
的全称任务已变为：对容量不足的私有强制坐标，证明必有较小 \(R\) 的目标命中、独立
Type II 证书或严格可提升递降，即建立私有载体逃逸引理。
