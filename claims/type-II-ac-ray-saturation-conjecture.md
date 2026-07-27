---
kind: claim
claim_id: type-II-ac-ray-saturation-conjecture
title: 有界 A,C 的 Type II 因子射线饱和猜想
statement: 猜想存在绝对常数 B，使每个素数 p=1 mod24 都存在 1<=A,C<=B 和 K>=1，令 h=4ACK-1 后有 h|Kp+A 且 A<=(Kp+A)/h。该条件给出 p 的 Type II 除子证书，因而该猜想蕴含 Erdős--Straus 猜想。
claim_status: open
topics:
- type-II
- conjecture
- factorization
- short-certificate
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 2 and 4 (statements; the paper leaves their proofs to the reader)"
  role: Type-II-certificate-statement-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-27'
---

# 有界 \(A,C\) 的 Type II 因子射线饱和猜想

## 精确命题

猜想存在绝对常数 \(B\)，使每个素数 \(p\equiv1\pmod{24}\) 都有

\[
1\le A,C\le B,\qquad K\ge1,
\]

令

\[
h=4ACK-1,\qquad B'=\frac{Kp+A}{h},
\]

则

\[
h\mid Kp+A,\qquad A\le B'. \tag{1}
\]

由 Type II 正规形，(1) 给出

\[
m=\frac{A+B'}K,\qquad x=AB'C,\qquad d=A^2C,
\]

以及 \(4/p\) 的一张合法 Type II 除子证书。

由 `type-II-raw-ray-certificate` 的缺口恒等式，若 \(A\le B\)，这张证书还满足

\[
m\le\frac p3+\frac{4B}{3}.
\]

故本猜想是原计划中一个真正的“有界短证书”分支，而不只是换一种方式陈述存在性。

等价地，可消去 \(K\) 的无界搜索：

\[
h\mid p+4A^2C,\qquad
h\equiv-1\pmod{4AC},\qquad
K=\frac{h+1}{4AC}, \tag{2}
\]

再检查 (1) 的序条件。互素性不是证书构造所需的条件，只是正规形的归一化；
式 (2) 是一个有限组移位整数
\(p+4A^2C\) 的因子残数命题，而不是固定有限的同余模板命题。

这里的序条件在充分大处其实自动成立。由

\[
B'-A=\frac{K(p-4A^2C)+2A}{h},
\]

只要 \(p\ge4A^2C\) 便有 \(A\le B'\)。故若固定了候选界 \(B\)，则对
\(p\ge4B^3\)，猜想等价于：某个 \(1\le A,C\le B\) 的移位数
\(p+4A^2C\) 有因子 \(h>1\) 满足 (2)。小于该阈值的素数只有有限多个，
可独立核验。这样，全称难点不在恢复证书的序条件，而在强制所需的因子残数。

## 为什么它足以完成证书分支

若猜想成立，对每个核心素数直接恢复 Type II 证书；非核心素数和合数已由经典恒等式及
缩放约化处理。因此该猜想本身蕴含 Erdős--Straus 猜想，无需另行递降。

它比“固定 \((A,C,K)\) 参数盒”更强，因为 \(K\) 随 \(p\) 变化。已有的
type-II-finite-template-obstruction 只排除后者，不能排除本猜想。

## 当前证据与缺口

type-II-ac-ray-audit 已精确验证：在 \(p\le5\cdot10^8\) 中，\(B=14\) 覆盖全部
\(3{,}292{,}848\) 个核心素数；在先前 \(p\le10^8\) 的审计中，\(B=11\) 只遗漏
\(p=84{,}525{,}841\)。这是候选常数的有限证据，不是全称证明。

bounded-ac-ray-k-growth-obstruction 进一步表明：即使这类全局常数 \(B\) 存在，
对某些无穷核心素数，任何限定在该有限 \(A,C\) 盒中的见证也必须允许
\(K\gg_B\log p/\log\log p\)。所以固定小 \(A,C\) 不能被误解为有限模板或
常数时间的 \(K\) 扫描；全称证明必须真正控制移位数的因子。

即使不假定 \(A,C\) 有统一界，type-II-ac-rays-superlog-residual 已证明：逃过全部
\(AC\) 射线的核心素数集合对任意固定对数幂都稀薄。这是对该方向的解析支持，但仍与
“残余为空”相差一个逐点选择器。

要证明该猜想，必须对每个 \(p\) 强制以下有限组之一出现合适因子：

\[
p+4A^2C\quad(1\le A,C\le B)
\]

含有 \(h\equiv-1\pmod{4AC}\)，并满足恢复证书所需的
\(A\le B'\)。单纯的 Dirichlet 同余覆盖不能给出这种关于未知因子的结论；反之，
固定有限三元组的避免定理也不足以否定允许 \(K\) 变化的射线。

这使它成为“短证书或递降”计划当前最具体的正向子目标：证明它即可完成短证书分支；
若能构造无限反例，则会明确迫使研究转向真正的递降机制。
