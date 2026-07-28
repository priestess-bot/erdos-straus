---
kind: claim
claim_id: type-I-linear-labeled-block-gcd-rigidity
title: 线性源带模数标签块的完整碰撞刚性
statement: 固定核心素数p的有限完整线性源谱。把每个源/仿射因子块去重为B(t,R)=tR+1的坐标对(t,R)。不同标签的块公因子整除标签差；同标签而模数不同的块公因子精确等于gcd(tR+1,abs(R-R'))。故逐块剥离与所有适用标签差或模数差最小公倍数的公因子后，任何两个不同坐标块的私有层两两互素。七个完整压力谱逐项复核该分解。此结论不保证目标平方除子命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- source-square
- factorization
- collision
- private-factors
- gcd-rigidity
- general-b
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性源带模数标签块的完整碰撞刚性

## 定理

固定核心素数 \(p\)，并取它的有限完整线性源谱

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4. \tag{1}
\]

把源与仿射块按坐标对去重，记为

\[
\mathscr B_p=
\{(t,R):t\in\{a,s\}\text{ for some state (1)}\},
\qquad B(t,R)=tR+1. \tag{2}
\]

每个块满足 \(B(t,R)\mid p-t\)。对两个不同的坐标块
\((t,R),(u,U)\in\mathscr B_p\)，有

\[
\gcd(B(t,R),B(u,U))\mid |t-u| \quad(t\ne u), \tag{3}
\]

而在同标签纤维内有精确公式

\[
\boxed{
\gcd(B(t,R),B(t,U))
=\gcd(tR+1,|R-U|)
}\qquad(R\ne U). \tag{4}
\]

对 \(x=(t,R)\in\mathscr B_p\)，定义适用差分的最小公倍数

\[
J_x=operatorname{lcm}\!\left(
\{|t-u|:(u,U)\in\mathscr B_p,\ u\ne t\}
\cup
\{|R-U|:(t,U)\in\mathscr B_p,\ U\ne R\}
\right), \tag{5}
\]

其中空集的最小公倍数为 \(1\)，并置

\[
S_x=\gcd(B(t,R),J_x),
\qquad P_x=\frac{B(t,R)}{S_x}. \tag{6}
\]

则任意不同 \(x,y\in\mathscr B_p\) 满足

\[
\boxed{\gcd(P_x,P_y)=1.} \tag{7}
\]

## 证明

块 \(B(t,R)\) 来自 (1) 时，若 \(t=s\)，则
\(p-s=a(sR+1)\)；若 \(t=a\)，则 \(p-a=s(aR+1)\)。所以
\(B(t,R)\mid p-t\)。两个标签不同的块的公因子同时整除
\(p-t\) 与 \(p-u\)，这给出 (3)。

若标签相同，则

\[
\begin{aligned}
\gcd(tR+1,tU+1)
&=\gcd(tR+1,t(R-U))\\
&=\gcd(tR+1,R-U),
\end{aligned}
\]

最后一步使用 \(\gcd(t,tR+1)=1\)。这证明 (4)。

现在取不同块 \(x,y\)，并令 \(D=\gcd(B_x,B_y)\)。由 (3) 或 (4)，
\(D\mid J_x\) 且 \(D\mid J_y\)。若素数 \(q\) 同时整除 \(P_x,P_y\)，
在 \(B_x,B_y\) 的 \(q\)-进赋值较小的一边记为 \(e\)。则 \(q^e\mid D\mid J_x\)
（或 \(J_y\)，取较小的一边），故这一边的 \(q^e\) 全已被 \(S\) 剥离，不能在相应
\(P\) 中留下 \(q\)。矛盾，故得 (7)。

注意 \(S_x\) 与 \(P_x\) 不必互素；结论只断言**不同坐标块之间**不存在共同的私有剩余。
同一个 \((t,R)\) 在多条有向记录中重复时是同一整数块，必须先按 (2) 合并，不能作为
反例或碰撞对处理。

## 有限审计与范围

对七个既有完整线性压力谱

\[
p\in\{214729,878089,2210569,13782409,64214329,105295129,536944489\}
\]

程序完整枚举其线性源、去重 \((t,R)\) 块，并逐对检验 (3)、(4)、(7)。原始 JSON 保存
每一块的 \(J_x,S_x,P_x\)，可用于进一步研究同标签纤维与反足点积集。

该定理只给出共享素因子的位置约束。它不能推出 \(-1\in\mathcal C_R(K)\)，也不能把不同
模数 \(R\) 的单位群直接比较；因此不能单独证明一般 \(B\) 或混合终端选择器。它严格扩展
[坐标标签碰撞分解](type-I-linear-block-label-collision.md)的跨标签部分，并与
[跨模数 \(K\) 公因子刚性](type-I-linear-cross-modulus-gcd-rigidity.md)处在不同层级：本页控制
组成 \(4K\) 的单个坐标块，后者控制整个 \(K\)。

## 复现

~~~bash
python3 reproductions/type_i_linear_labeled_block_gcd_rigidity.py
python3 -m unittest tests.test_type_i_linear_labeled_block_gcd_rigidity -v
~~~
