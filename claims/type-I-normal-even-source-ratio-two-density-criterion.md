---
kind: claim
claim_id: type-I-normal-even-source-ratio-two-density-criterion
title: Type I 偶源桥比二除子残数的半密度入口引理
statement: 设L、R互素且R为奇数，令D_R(L)={d mod R:d|L}、H_R(L)为L的素因子残数生成子群。若2属于H_R(L)且2|D_R(L)|>|H_R(L)|，则存在u,v|L满足u=2v modR；约去gcd(u,v)后得到互素a,b|L，a=2b modR，故E=La/b满足E|L^2、E=2L modR。对Type I情形L=2K、4K=1 modR时，E=1 modR；但还必须独立检查E为偶数和E<=2L-2R，半密度条件本身不是完整终端选择器。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- terminal-bridge
- ratio-two
- divisor-residues
- finite-product
- density
- pigeonhole
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-bridge-context
visibility: public
last_checked: '2026-07-29'
---

# Type I 偶源桥比二除子残数的半密度入口引理

## 代数设置

设 \(L,R\) 为正整数，\(R\) 为奇数且 \((L,R)=1\)。定义

\[
\mathcal D_R(L)=\{d\bmod R:d\mid L\},
\qquad
\mathcal H_R(L)=\langle q\bmod R:q\mid L\rangle.
\]

假设

\[
2\in\mathcal H_R(L),
\qquad
2|\mathcal D_R(L)|>|\mathcal H_R(L)|. \tag{1}
\]

## 比二碰撞结论

乘法平移 \(2\mathcal D_R(L)\) 与 \(\mathcal D_R(L)\) 都是
\(\mathcal H_R(L)\) 中的等势子集。由 (1) 的鸽巢原理，

\[
\mathcal D_R(L)\cap2\mathcal D_R(L)\ne\varnothing. \tag{2}
\]

所以存在除子 \(u,v\mid L\) 使

\[
u\equiv2v\pmod R. \tag{3}
\]

令 \(g=(u,v)\)，并置

\[
a=u/g,\qquad b=v/g.
\]

因为 \((g,R)=1\)，约去 \(g\) 保持同余，且

\[
(a,b)=1,\qquad a,b\mid L,\qquad a\equiv2\pmod R. \tag{4}
\]

于是定义

\[
E=L\frac ab 
\]

得到整数，并且

\[
E\mid L^2,\qquad E\equiv2L\pmod R. \tag{5}
\]

第二个整除关系来自 \(a,b\mid L\) 和互素性：
\(L^2/E=Lb/a\) 为整数。

## 对 Type I 终端桥的翻译

在 Type I 正规形中令 \(L=2K\)，并有

\[
4K=pR+1,\qquad 4K\equiv1\pmod R.
\]

此时 (5) 变成

\[
E\mid4K^2,\qquad E\equiv1\pmod R. \tag{6}
\]

因此半密度条件确实解决了终端选择器中的**残数命中层**。但它没有自动解决另外两层：

1. 偶性：\(E=La/b\) 为偶数当且仅当 \(2\mid a\) 或 \(b\mid L/2\)；
2. 大小：需要 \(E\le2L-2R\)。若碰撞可选为 \(a<b\)，则大小条件自动成立；否则必须单独检查大侧预算。

故 (1) 是一个真正的充分入口，但不是原混合终端选择引理的充分条件。最小抽象例
\(L=2,R=3\) 满足半密度条件并产生 \(E=4\)，但没有满足相应的大小预算，说明这两个
边界不能从群论密度中省略。

## 研究意义

该引理把当前的多素因子平方剩余问题分成两个可分离的阶段：

\[
\text{多素因子残数积集达到半密度}
\Longrightarrow
\text{比二候选 }E,
\]

再研究二进制支撑和数值侧序以得到偶源。它与已有的
[一般 (B) 反足点半密度判据](type-I-general-b-antipodal-divisor-spectrum.md)互补：后者的目标是
\(-1\)，这里的目标是偶桥所需的 \(2\)。后续最具体的全称子目标是：对普通 Type II 遗漏的
某个完整 Type I 状态，证明 \(\mathcal D_R(2K)\) 在 \(\mathcal H_R(2K)\) 中达到该半密度，
并同时保留一个小侧且偶的碰撞。

该结论本身不比较不同 \(R\) 的单位群，也不证明每个核心素数存在满足 (1) 的 Type I 状态。

## 复现

这是有限阿贝尔群上的直接鸽巢证明，无需新的大规模扫描。现有
[比二普通除子对等价](type-I-normal-even-source-ratio-two-pair.md)给出终端参数的完整反向对应。
