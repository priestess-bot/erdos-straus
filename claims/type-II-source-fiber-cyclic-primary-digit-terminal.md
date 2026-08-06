---
kind: claim
claim_id: type-II-source-fiber-cyclic-primary-digit-terminal
title: Type II 源纤维循环 ell-primary 进位层终端
statement: 设目标差分群为循环群 C_{ell^a}，并有一组合法且可独立选择的二点关系块 {0,v_j}。若对每个精确 ell-进赋值层 k=0,...,a-1，至少有 ell-1 个块满足 nu_ell(v_j)=k，则这些块的和集覆盖整个 C_{ell^a}。若目标锚点落在差分群内，这给出 Type II 命中；目标缺失则强制锚点在群外或至少有一个进位层只有 ell-2 个及以下块。该终端是固定参数纤维的构造性容量引理，不自动保证关系块的跨纤维合法性。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-low-rank-lock-cyclic-terminal
  - type-II-source-fiber-elementary-rank-qheight-injection
  - type-II-source-lattice-fibered-kneser-selector
topics:
- type-II
- source-fiber
- cyclic
- primary
- ell-adic
- digit-capacity
- cauchy-davenport
- target-fiber
- constructive-certificate
- proof-program
sources:
  - claim: type-II-source-fiber-low-rank-lock-cyclic-terminal
    role: cyclic-low-rank-target
  - claim: type-II-source-fiber-elementary-rank-qheight-injection
    role: relation-source-columns
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: integer-Type-II-lift
visibility: public
last_checked: '2026-08-05'
---

# Type II 源纤维循环 \(\ell\)-primary 进位层终端

## 循环关系块

令 \(H=C_{\ell^a}\) 为阶 \(\ell^a\) 的循环群，使用加法记号。设一组
保持当前参数纤维且可以独立选择的二点关系块

\[
B_j=\{0,v_j\}\subseteq H,
\qquad v_j\ne0.
\tag{1}
\]

“可以独立选择”表示任意 \((\varepsilon_j)\in\{0,1\}^r\) 都对应盒内合法的
源关系组合，并且这些组合的整数因子来源仍满足同一个 Type II 参数纤维的
source-switch 合同。这个条件是构造性证书的一部分，不能由抽象群元素自动假定。

对非零 \(v\in C_{\ell^a}\)，定义精确 \(\ell\)-进赋值

\[
\nu_\ell(v)=\max\{0\le k<a:v\in\ell^k C_{\ell^a}\}.
\tag{2}
\]

记第 \(k\) 层的块数为

\[
c_k=\#\{j:\nu_\ell(v_j)=k\},
\qquad 0\le k<a.
\tag{3}
\]

## 进位层覆盖定理

若

\[
\boxed{c_k\ge\ell-1\quad(0\le k<a),}
\tag{4}
\]

则

\[
\boxed{B_1+\cdots+B_r=C_{\ell^a}.}
\tag{5}
\]

### 证明

对 \(a\) 作归纳。

当 \(a=1\) 时，所有 \(v_j\) 都是 \(C_\ell\) 中的非零元素。逐次使用
Cauchy–Davenport，

\[
|A+\{0,v_j\}|\ge\min(\ell,|A|+1),
\]

所以 \(c_0\ge\ell-1\) 时和集大小达到 \(\ell\)，得到 (5)。

设 \(a>1\)。取精确层 \(k=0\) 的 \(c_0\ge\ell-1\) 个块，令其和集为 \(S_0\)。
模 \(\ell\) 投影后，所有 \(v_j\) 都是非零元；同样的 Cauchy–Davenport 迭代给出

\[
\operatorname{pr}_\ell(S_0)=C_\ell.
\tag{6}
\]

其余层 \(k\ge1\) 的块都落在 \(\ell C_{\ell^a}\)。把它们除以 \(\ell\)，得到
\(C_{\ell^{a-1}}\) 中的二点块；原来的第 \(k\) 层变成新的第 \(k-1\) 层。由归纳假设
和 \(c_k\ge\ell-1\)，这些剩余块的和集覆盖
\(\ell C_{\ell^a}\)：

\[
S_{\ge1}=\ell C_{\ell^a}.
\tag{7}
\]

任取 \(x\in C_{\ell^a}\)。由 (6) 选 \(s_0\in S_0\) 使
\(s_0\equiv x\pmod\ell\)，于是 \(x-s_0\in\ell C_{\ell^a}=S_{\ge1}\)。
故 \(x\in S_0+S_{\ge1}\)，得到 (5)。证毕。

## Type II 命中与缺口三分

沿用低秩循环终端的锚点 \(\alpha\)。若

\[
\alpha^{-1}\in H
\tag{8}
\]

且 (4) 成立，则 (5) 覆盖目标相对指数，得到 \(-1\) 的源关系命中；由
Type II 源纤维选择器的整数回译，构造出 Type II 短证书。

反之，若目标仍缺失，则至少一个条件成立：

\[
\boxed{
\alpha^{-1}\notin H
\quad\text{或}\quad
\exists k\in\{0,\ldots,a-1\}:c_k\le\ell-2.
}
\tag{9}
\]

第一项是 ANCHOR_OUTSIDE_DIFFERENCE；第二项是一个精确的
CYCLIC_PRIMARY_DIGIT_DEFICIT，指出缺失发生在哪个 \(\ell\)-进位层。

## 例子

### \(C_4\) 的二进位终端

取 \(\ell=2,a=2\)。只需一个精确层 \(0\) 的块和一个精确层 \(1\) 的块：

\[
\{0,1\}+\{0,2\}=C_4.
\]

这是 \(p=5113\)、\(D_*=1\) 纤维中残数 \(7\equiv-1\pmod4\) 的最小型终端；
17 的残数 \(1\) 是吸收列，不计入非零层。

### \(C_9\) 的三进位终端

取 \(\ell=3,a=2\)。每层需要至少两个块。例如

\[
\{0,1\}+\{0,1\}+\{0,3\}+\{0,6\}=C_9.
\]

第一层给出全部模 3 余数，第二层给出全部 \(3C_9\)，两者相加覆盖 \(C_9\)。
若只有一个精确层 1 的块，式 (9) 给出严格的高阶循环容量缺口。

## 研究边界

本引理把高阶循环的“孔”压缩为具体的 \(\ell\)-进位层缺口，并提供了可构造的
Type II 终端。它仍不证明任意源纤维都能产生这些独立关系块；当关系块来自不同
参数纤维、重复 q 账本或稳定子折叠时，必须先通过 source-switch 合同和目标关系格
检查。最高不足层的饱和尾吸收和严格商接口见
[Type II 循环 primary 最高缺口的饱和尾压缩与严格递降](type-II-source-fiber-highest-deficit-tail-compression.md)；
它把 CYCLIC_PRIMARY_DIGIT_DEFICIT 进一步规范为低模数商、顶层广义 \(2^j\) 缺口或
另一条 Type I/II 射线。
