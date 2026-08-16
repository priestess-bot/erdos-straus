---
kind: claim
claim_id: root-context-terminal-disjunctive-invariant
title: 根证书与标记纤维的析取终端不变量
statement: >-
  固定一个不可变根素数 p0。若每个合法状态 S 都携带 W_S 和根上下文 p0，则将归纳
  结果类型定义为 C(p0) disjoint-union W_S，其中 C(p0) 是已核验的直接根方程
  4/p0 证书。任何既有的合法边 lift W_T to W_S 都唯一扩张为该析取类型上的映射：
  根证书恒等、标记解按原 lift 提升。因此一张直接核验 4/p0 的 Type I/II terminal
  可关闭全局根目标而无需伪称属于当前 W_S；所有非终端边、改变方程的终端和较小分母
  解仍须满足原有 E1--E5 与 marked-lift 合同。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - denominator-escape-state-contract
  - type-II-relation-reach-gcd-shadow-endpoint-descent
  - type-I-unified-terminal-first-selector-contract
topics:
  - root-context
  - terminal
  - marked-solutions
  - solution-lift
  - well-founded-induction
  - type-I
  - type-II
  - proof-boundary
sources:
  - concept: denominator-escape-state-contract
    role: legal-state-E1-to-E5-and-marked-fiber-contract
  - claim: type-II-relation-reach-gcd-shadow-endpoint-descent
    role: same-root-Type-II-endpoint-terminal-and-edge-context
  - claim: type-I-unified-terminal-first-selector-contract
    role: direct-terminal-versus-even-predecessor-boundary
  - reproduction: reproductions/root_context_terminal_disjunctive_invariant.py
    role: focused-same-root-terminal-and-mark-refusal-control
visibility: public
last_checked: '2026-08-17'
---

# 根证书与标记纤维的析取终端不变量

## 1. 问题：两个不同的结论类型被错误合并

固定根素数 \(p_0\)。当前递归状态 \(S\) 可以带有严格标记解集

\[
W_S\subseteq \operatorname{Sol}(c_S,n_S),
\]

而全局目标却只是构造根方程

\[
\frac4{p_0}=\frac1x+\frac1y+\frac1z
\tag{1}
\]

的一组正整数分母。两种结论并不相同：

1. 一个三元组属于当前 \(W_S\)，因而可以作为状态归纳值或被一条后继边提升；
2. 一个三元组已经直接验证 (1)，因而可以结束整个根证明。

若把第 2 类也强制要求为第 1 类，就会错误地要求一张同根 Type I/II certificate 满足
一个与根方程无关的 mark。这个额外要求不是 E4，也不能由递降势支付。

## 2. 根证书与结果类型

令 \(\mathcal C(p_0)\) 是所有带有已注册 direct receipt 的对象

\[
C=(\sigma;x,y,z)
\]

的集合，其中 \(\sigma\) 通过相应 Type I/II normal-form verifier、短界和正性检查，且

\[
4xyz=p_0(xy+xz+yz).
\tag{2}
\]

每个进入同一 proof run 的状态保留不可变根上下文

\[
\operatorname{root}(S)=p_0.
\tag{3}
\]

定义该状态的归纳结果类型

\[
\boxed{\quad
\operatorname{RootOutcome}_{p_0}(S)
 =\mathcal C(p_0)\sqcup W_S .
\quad}
\tag{4}
\]

左分支不是 \(W_S\) 的元素；右分支也不需要预先包含一个根 certificate。这个析取只改变
归纳命题的余域，不改变状态的 equation target、mark、source provenance 或 potential。

## 3. 两种 terminal leaf

### 3.1 marked terminal

若回执要声明当前状态已得到归纳值，它必须恢复 \(w\in W_S\)，并输出

\[
\operatorname{inr}(w)\in\operatorname{RootOutcome}_{p_0}(S).
\tag{5}
\]

这保留原合同的全部成员资格要求。

### 3.2 root terminal

若回执直接重算 (2)，并明确包含根素数 \(p_0\)、三分母和其 Type I/II receipt，则它输出

\[
\operatorname{inl}(C)\in\operatorname{RootOutcome}_{p_0}(S).
\tag{6}
\]

这里**不**断言 \((x,y,z)\in W_S\)。接纳条件只有：

1. 当前状态的根上下文是 \(p_0\)；
2. 该 receipt 已通过原有 direct-terminal verifier；
3. (2) 按整数等式重算；
4. 它是 \(4/p_0\) 的证书，而非只解 \(c_S/n_S\) 或 \(4/n\)（\(n<p_0\)）的证书；
5. 输出没有后继状态。

所以这不是对 marked terminal 的放宽，而是一个不同的终端结果类型。

## 4. 边 lift 的唯一扩张

考虑一条已经通过 E1--E5 的边

\[
S\longrightarrow T,
\qquad
\Phi_{T\to S}:W_T\longrightarrow W_S,
\tag{7}
\]

并要求它保持 (3)。定义

\[
\widehat\Phi_{T\to S}:
\mathcal C(p_0)\sqcup W_T
\longrightarrow
\mathcal C(p_0)\sqcup W_S
\tag{8}
\]

为

\[
\widehat\Phi_{T\to S}(\operatorname{inl}C)=\operatorname{inl}C,
\qquad
\widehat\Phi_{T\to S}(\operatorname{inr}w)
=\operatorname{inr}\bigl(\Phi_{T\to S}(w)\bigr).
\tag{9}
\]

式 (9) 良定义：左分支只使用相同根方程，右分支正是原有 E4。它不修改
\(\Phi\)、不为一个新方程伪造 lift，也不改变 E5 的势比较。

## 5. 良基归纳定理

设 \(\Pi\) 是任意已经建立的、在所有 nonterminal verified edge 上严格下降的全局良基势。
假定每个 legal state \(S\) 的 total selector 只会输出下列三者之一：

1. 一个 root terminal \(C\in\mathcal C(p_0)\)；
2. 一个 marked terminal \(w\in W_S\)；
3. 一条保持根上下文的 verified edge \(S\to T\) 且
   \(\Pi(T)<\Pi(S)\)。

则对每个状态 \(S\)，有

\[
\operatorname{RootOutcome}_{p_0}(S)\ne\varnothing.
\tag{10}
\]

**证明。** 对 \(\Pi(S)\) 作良基归纳。前两种输出分别给出 (4) 的左、右分支。第三种输出
可用归纳假设取得 \(o\in\operatorname{RootOutcome}_{p_0}(T)\)，再由 (9) 得到
\(\widehat\Phi_{T\to S}(o)\)。证毕。

在根状态 \(S_0\) 取

\[
W_{S_0}=\operatorname{Sol}(4,p_0).
\tag{11}
\]

若 (10) 的元素在左分支，(2) 已直接给出根解；若在右分支，(11) 给出根解。因此此不变量
足以把一个覆盖全部 legal state 的 selector 转为全局根结论。

## 6. 对 Type II gcd-shadow 的直接影响

gcd-shadow endpoint 的重算仍分为 direct Type I/II terminal 与严格 \(q'<q\) 边。此前，
一张 ordinary terminal 若不满足非平凡 mark，无法作为 \(W_S\) 的成员返回。现在只要该
terminal 的三分母直接满足 \(4/p\)，它应输出 (6)，并结束根结论；只有没有直接根证书、
或必须作为 \(W_S\) 值继续使用的分支，才继续面对 mark membership 问题。

这消除了 T3 中“同根直接终端必须先证明 mark membership”的伪阻塞，但没有消除：

- 只解 \(4/n\) 的 even predecessor 或 generalized dyadic candidate；
- 改变 equation target 后而尚未恢复根方程的 terminal；
- 任一 nonterminal support switch、q-adic lift 或 G/Type I handoff 的 E4；
- 全局势、全局 selector 和所有核心素数的覆盖性。

## 7. 定向控制

复现脚本使用 \(p=73\)：

- 直接 Type I receipt \((m,d)=(7,10)\) 生成
  \((20,210,30660)\)，并被“后两分母都被 \(p\) 整除”的 Type II mark 拒绝；
- 该 Type I 三元组仍通过根方程检查，故产生 root terminal；
- 直接 Type II receipt \((7,1)\) 生成 \((20,219,4380)\)，可作为 marked terminal；
- 对同一根上下文的不同 equation target，根 certificate 仍可结束根目标；若根素数改为
  \(241\)，则该 certificate 被拒绝。

运行：

~~~bash
python3 reproductions/root_context_terminal_disjunctive_invariant.py --verify
~~~

该脚本只核对类型边界和精确整数式；它不声称该示例 mark 是某条实际递归路径，也不扫描
素数范围。
