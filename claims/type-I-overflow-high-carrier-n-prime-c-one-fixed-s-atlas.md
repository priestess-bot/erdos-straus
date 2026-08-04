---
kind: claim
claim_id: type-I-overflow-high-carrier-n-prime-c-one-fixed-s-atlas
title: 高载体 n=p 中 C=1 mod 3 的 fixed-s 除子图谱
statement: 对 exact n=p G-anchor 的真高载体行，令 B_p=(p-1)^2/4、Q=(p-3)/2、A=B_p/C、2<=C<Q 且 C=1 (mod 3)。相位闭式给出固定行列式 p*s=4*r*d+1，其中 r=(AQ mod p)、d=(2C+p)/3。所有满足 A<L<=B_p、4L>s、B_p/L<C 且 L|r*d 的 L 都给出 canonical chart (4L-s, L(p-r*d/L))，并严格降低外层势 floor(B_p/L)<C；它们仍是依赖来源标记集和可达性的条件边。六个代表性合成样本中，三个 fixed-s 有候选，三个 fixed-s hard core 均被 gap<=255 的 A=1 Type II 直接探针覆盖；该有限图谱不是全称定理。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-high-carrier-n-prime-normal-form
  - type-I-overflow-high-carrier-n-prime-g-anchor-phase
  - type-I-overflow-fixed-s-bounded-divisor-saturation
  - type-II-a-one-gap-three-factor-terminal
topics:
- type-I
- overflow
- high-carrier
- n-equals-p
- G-state
- fixed-s
- divisor-atlas
- conditional-edge
- hard-core
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: exact C=1 fixed-s divisor enumeration and verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: six-row synthetic atlas with bounded Type II post-router
visibility: public
last_checked: '2026-08-04'
---

# 高载体 \(n=p\) 中 \(C\equiv1\pmod3\) 的 fixed-\(s\) 除子图谱

## 1. 输入与固定行列式

在 exact \(n=p\) G-anchor 的真高载体区域，令

\[
B=B_p=\frac{(p-1)^2}{4},\qquad Q=\frac{p-3}{2},\qquad A=\frac{B}{C},
\]

其中 \(2\le C<Q\)、\(C\mid B\)、\(C\equiv1\pmod3\)。前一张相位卡给出

\[
u=A-t_A=c+\frac A3,\qquad c=\frac{p-1}{6},
\]

以及

\[
d=\frac{2C+p}{3},\qquad M=AQ,
\qquad p n_C=4Md+1.
\]

令

\[
r=M\bmod p,\qquad s=\frac{4rd+1}{p},\qquad T=rd.
\]

因为 \(p\mid4Md+1\)，有 \(r\ne0\)、\(p\mid4rd+1\)，从而

\[
p s=4T+1.
\tag{1}
\]

这把 bundle overflow 转成了一个固定-\(s\) 的整数除子图谱；这里的 \(s\) 是由 \(M\) 的
模 \(p\) 残数决定的，不是额外猜测的参数。

## 2. 可接受除子与势下降

枚举 \(L\mid T\)，只保留

\[
A<L\le B,\qquad 4L>s,\qquad \left\lfloor\frac{B}{L}\right\rfloor<C.
\tag{2}
\]

对每个保留的 \(L\)，令 \(T/L\) 为余因子，则规范图表直接是

\[
(R_L,K_L)=\left(4L-s,\;L\left(p-\frac{T}{L}\right)\right).
\tag{3}
\]

式 (1) 保证其 Type I 行列式恒等式，(2) 给出支撑范围、正余数和严格的外层势下降。
若 \(R_L\le p\)，目标是 G 图表；若 \(R_L>p\)，目标仍在 overflow 菜单中。两种情形
都需要来源回执提供完整标记集、可达性和提升合同，才能把算术候选升级为 E1--E5 边。

## 3. 有限图谱结果

统一选择器重算六个合成行：

| \(p\) | \(C\) | \(A\) | \(T=rd\) | 可接受 \(L\) 数 | 路由 |
| ---: | ---: | ---: | ---: | ---: | --- |
| 193 | 64 | 144 | 18190 | 7 | fixed-\(s\) 条件边候选 |
| 241 | 64 | 225 | 2952 | 8 | fixed-\(s\) 条件边候选 |
| 241 | 100 | 144 | 3675 | 7 | fixed-\(s\) 条件边候选 |
| 5281 | 1408 | 1872 | 1950 | 0 | gap-7 Type II 终端 |
| 15601 | 4000 | 15210 | 65980529 | 0 | gap-3 Type II 终端 |
| 16633 | 4312 | 16008 | 20790 | 0 | gap-7 Type II 终端 |

前三行的所有候选均满足严格势下降。后三行没有满足 (2) 的 fixed-\(s\) 除子，但均在
gap<=255 的 A=1 Type II factor-ray 探针中得到直接终端；这只是有限探针结果，不能替代
对所有 p,C 的短证书或递降证明。

## 4. 证明边界与下一步

该卡是有限合成图谱，不是对所有 \((p,C)\) 的全称定理。选择器将每行保持为
`analysis_evidence`，并令递归资格为假；conditional edge contract 中 E1--E5 的算术
字段虽全部可写出，但 `source_marked_solution_set_required` 和 `source_reach_status`
仍未满足。

下一步应把 gap 探针失败的 fixed-\(s\) hard core 接入 alternate/对偶容量分支，优先分析
T=rd 的素因子结构、目标余数 R_L 的跨状态映射，以及能否建立与 C=0 (mod 3) 重置
或 C=2 (mod 3) 空窗口之间的统一良基势。

复现：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
