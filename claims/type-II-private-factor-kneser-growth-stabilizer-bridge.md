---
kind: claim
claim_id: type-II-private-factor-kneser-growth-stabilizer-bridge
title: Type II 私有因子的 Kneser 增长—稳定子吸收二分
statement: 设 H 为有限阿贝尔群，A 非空，g 属于 H，B_e={1,g,...,g^e}，P=A B_e，T=Stab_H(P)。若 g 不属于 T，则 |P| >= |AT|+|T|；若产品没有增长到该下界，则 g 被当前稳定子吸收，进入商群 H/T。对 Type II 碰撞/私有分解，q 进容量保证私有素因子是独立来源，因此每个新增私有残数要么支付目标纤维增长，要么进入稳定子商并交给 Fourier/G 型分支。该桥接是状态级容量—对偶二分，不是全称选择器或递降定理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
- type-II-shared-selector-kneser-target-fiber-terminal
- type-II-shared-factor-q-adic-difference-bound
- type-I-fixed-layer-stabilizer-defect-reduction
topics:
- type-II
- private-factor
- Kneser
- stabilizer
- target-fiber
- q-adic-capacity
- Fourier
- proof-program
sources:
- claim: type-II-shared-selector-kneser-target-fiber-terminal
  role: Type-II-target-product-capacity
- claim: type-II-shared-factor-q-adic-difference-bound
  role: private-source q-adic separation
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: Kneser-growth-input
visibility: public
last_checked: '2026-08-04'
---

# Type II 私有因子的 Kneser 增长—稳定子吸收二分

## 引理

令 \(H\) 为有限阿贝尔群，\(A\subseteq H\) 非空，\(g\in H\)，并令
\[
B_e=\{1,g,g^2,\ldots,g^e\},\qquad P=A B_e,\qquad
T=\operatorname{Stab}_H(P).
\]
Kneser 定理给出
\[
|P|\ge |AT|+|B_eT|-|T|. \tag{1}
\]
若 \(g\notin T\)，则 \(B_eT/T\) 至少含两个元素，故
\[
|P|\ge |AT|+|T|. \tag{2}
\]
因此每个新增私有残数有严格二分：

1. \(g\notin T\)：它使目标积集相对 \(AT\) 至少增长一个稳定子块；
2. \(g\in T\)：它被当前稳定子吸收，投影到 \(H/T\) 后成为平凡方向。

对一串私有残数逐个应用 (2)，在目标积集达到 Kneser 全群阈值前，非吸收因子的数量
受到剩余商群容量约束；所有吸收因子则集中到稳定子商，可由固定层 Fourier/G 型角色
继续处理。

## 与 q 进私有来源的连接

在 Type II 窗口中，剥离碰撞素因子后，私有素因子不同时出现在两条移位中；更强的
q 进容量引理还记录其来源残类的层级预算。因此把私有素因子按 \(g\) 加入 \(A\) 时，
“独立来源”不是重复计数：每个未被稳定子吸收的来源都必须支付一次积集增长，吸收则
显式进入稳定子商。这提供了从跨状态 q 进容量到目标纤维/Kneser 的状态级接口。

## 具体吸收实例

在 \(p=33\,011\,449,m=63,j=16\) 的联合失败行中，
\[
x=8\,252\,878,\qquad E=2\cdot19\cdot29,\qquad R=7489,
\]
私有残数集为
\[
A=\Pi_{63}(R)=\{1,55\},\qquad g=7489\equiv55\pmod{63}.
\]
这里 \(A=\langle55\rangle\)，所以 \(g\in\operatorname{Stab}(A)\)：私有方向被稳定子吸收，
而不是产生新的 \(A\) 规模。其稳定子商至少把这一阶二方向压掉；对应的 Type II
目标积集 \(C A^2\) 的稳定子阶为 \(6\)，Kneser 下界为 \(30\)，而 \(|H|=36\)，
留下容量缺口 \(6\)。这是一条可复核的“稳定子吸收”而非增长分支。

## 限制

式 (2) 只说明非吸收私有因子会增加目标积集，不能保证有限数量的因子一定达到全群；
稳定子吸收也只产生更小的商群，不自动给出解提升或严格递降。要完成全局选择器，还
需证明商群中的 Fourier/字符缺口或 q 进容量缺口必然继续下降，或在增长达到阈值时
构造实际 Type II/共享除子。
