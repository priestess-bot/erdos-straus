---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
title: q=1 高 C=2 19 相位的最大超额第四 anchor 完成
statement: >-
  在 q=1 high C=2 19 相位的 31 个 H3 residual 类中，令
  g=gcd((p+1)/2,c3)，并对 v=R3-1 相对于 K3 取真正的最大 complete-excess 块
  Q*=Q_K3(v)，而非只在 g=1 时使用 (R3-1)/2。若 beta=v/Q*、d=gcd(M3,Q*)、
  lambda=beta*d/2，则 lambda|g|1536-a(p)，且新增 carrier 倍率严格为
  L=lcm(M3,Q*)/M3=(R3-1)/(2lambda)>1。第四 canonical capacity c4 的唯一非严格
  情形 c4=p-1 等价于 p 整除固定常数
  Theta_a(lambda)=3072*lambda*197955072+2261*57*(2261a-11943424)。遍历 31 个
  phase 类和 lambda|abs(1536-a) 的全部 213 个有限组合后，没有任何相位素数整除相应
  Theta。因此所有实际 residual phase prime 都有 1<=c4<=p-2；terminal-first 后，
  原来的全 1 (mod 4) q=1 mask 也可追加为从 persistent P 到 H4 的严格最大超额宏。
  这消除了 H3 的 mask 阻塞，但没有给出 H4 的 terminal/下一选择器，故不是全局出口定理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - complete-excess
  - capacity-map
  - finite-selector
  - persistent-macro
  - solution-lift
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
    role: H3-residues-source-gates-and-residue-polynomials
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: persistent-P-to-H3-parent-and-endpoint-rank
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: maximal-complete-excess-anchor-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_maximal_fourth_anchor_completion.py
    role: exact-lambda-top-gate-and-hard-control-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的最大超额第四 anchor 完成

## 1. H3 overlap 的精确有限界

保留 H3 的记号

\[
p=912u+769,
\qquad
c_3=\frac{1536+a p}{2261},
\qquad
w=\frac{p+1}{2},
\qquad
g=(w,c_3),
\tag{1}
\]

其中 \(a=a(p)\) 只由 \(u\pmod {119}\) 决定。先前的 H3 门已给出

\[
(R_3-1,K_3)=2g,
\qquad p\nmid R_3(R_3-1).
\tag{2}
\]

这里有一个比素因子根界更强的整除式。由于 \(g\mid w\)，有
\(p\equiv-1\pmod g\)；又 \(g\mid c_3\)，所以

\[
0\equiv2261c_3=ap+1536\equiv1536-a\pmod g.
\]

故

\[
\boxed{g\mid1536-a.}
\tag{3}
\]

特别地，H3 的重叠不仅有有限素数支撑；其每个可能素数幂也被当前 phase 的固定小整数
完整控制。

## 2. 最大 complete-excess 的真实第四倍率

令

\[
v=R_3-1,
\qquad
Q^*=Q_{K_3}(v)
=\prod_{\nu_\ell(v)>\nu_\ell(K_3)}\ell^{\nu_\ell(v)},
\qquad
\beta=\frac v{Q^*}.
\tag{4}
\]

这必须是完整素数幂定义，不能以 \(v/(2g)\) 取代。令

\[
d=(M_3,Q^*),
\qquad
\lambda=\frac{\beta d}{2}.
\tag{5}
\]

H3 有 \(p\equiv1\pmod8\)，故从 \(pR_3+1=4K_3\) 立即得到
\(v_2(v)=1\)。由 (2)，\(K_3\) 为偶数，故 \(Q^*\) 与 \(d\) 都是奇数，
而 \(\beta\) 恰有一个因子 \(2\)。最大超额的逐素数定义给出

\[
\beta\mid(v,K_3)=2g,
\qquad d\mid(v,K_3)=2g,
\qquad (\beta,d)=1.
\tag{6}
\]

因此 \(\beta/2\) 与 \(d\) 是互素的 \(g\) 因子，进而

\[
\boxed{\lambda\mid g\mid1536-a.}
\tag{7}
\]

设

\[
M_4=\operatorname{lcm}(M_3,Q^*),
\qquad L=\frac{M_4}{M_3}.
\tag{8}
\]

由 \(Q^*\beta=v\) 和 (5)，有精确式

\[
\boxed{L=\frac{Q^*}{(M_3,Q^*)}
=\frac{R_3-1}{2\lambda}.}
\tag{9}
\]

这个倍率总是大于一。事实上 \(M_3>B_p=(p-1)^2/4\)、\(c_3\ge g\) 给出

\[
p(R_3-1)=4M_3c_3-p-1
>g(p-1)^2-p-1>2pg,
\tag{10}

\]

所以 \(R_3-1>2g=(R_3-1,K_3)\)，从而真正的 complete-excess 块非平凡。
又由 (2)，\(p\nmid Q^*\)，因此 H3 的 universal \(p\)-source、anchor 和
maximal bundle 都满足已有 path-anchored 完整超额合同。

当 \(g=1\) 时，\(\lambda=1\)、\(Q^*=(R_3-1)/2\)，正好回收原来的 clean
第四 p-anchor。对于旧的 \(q=1\) mask，(9) 自动除去已被 \(K_3\) 承担的重叠，
而不把它误当成完整超额。

## 3. 容量顶端化为有限常数门

定义第四 canonical capacity

\[
c_4\equiv c_3L^{-1}\pmod p,
\qquad1\le c_4\le p-1.
\tag{11}
\]

它等于顶端 \(p-1\) 当且仅当 \(L+c_3\equiv0\pmod p\)。由 (9)，这等价于

\[
R_3-1+2\lambda c_3\equiv0\pmod p.
\tag{12}
\]

令

\[
\Delta=197955072.
\]

H3 的精确残数为

\[
\Delta(R_3-1)
\equiv57(2261a-11943424)\pmod p,
\qquad2261c_3\equiv1536\pmod p.
\tag{13}
\]

又

\[
2261\Delta=2^9\cdot3^2\cdot7^2\cdot17^2\cdot19^3.
\]

其素因子均不为 \(1\pmod {24}\)，故任何本 phase 的素数 \(p\equiv1\pmod {24}\)
都与 \(2261\Delta\) 互素。将 (12) 乘以这个可逆常数后，得到等价整数门

\[
\boxed{
p\mid\Theta_a(\lambda):=
3072\lambda\Delta+
2261\cdot57(2261a-11943424).}
\tag{14}
\]

这一步是关键：由 (7)，对固定 \(u\) 只需检查
\(\lambda\mid|1536-a|\)，而不是分解任何随 \(p\) 增长的 \(R_3-1\)。

31 个 residual \(u\) 类中的这些因子盒总计只有 213 个 \((u,\lambda)\)。对每一个
固定常数 \(\Theta_a(\lambda)\)，精确分解其素因子并检查对应 progression

\[
p=912u+769+108528t,\qquad t\ge0
\tag{15}
\]

没有得到任何 phase prime。因此 (14) 从不成立，且

\[
\boxed{1\le c_4\le p-2}
\tag{16}
\]

对每个实际 H3 residual phase prime 都成立。

## 4. 从 persistent P 的第四宏

在 terminal-first 已检查 H3 后，按下表分派：

| H3 情形 | 输出 |
|---|---|
| \(g\) 有 \(3\pmod4\) 素因子 | 原有的直接 Type II terminal |
| 否则 | 取 (4) 的最大 \(Q^*\)，追加 H3 \(\Rightarrow\) H4 |

第二行由 (2)、(4)、(8)、(11)、(16) 提供 actual source、primitive path、唯一 maximal
complete-excess bundle、p-free carrier、canonical target 与重新分类入口。把它附到已有
\(P\Rightarrow H_3\) persistent macro 后，两端的高支撑势为

\[
\Lambda_p^\sharp(P)=(0,p-1)
>(0,c_4)=\Lambda_p^\sharp(H_4).
\tag{17}

\]

因此普通图表无关 \(\operatorname{Sol}(p)\) 标记下，E4 仍为恒等映射，(17) 支付
E5；E1--E3 由前宏的 persistent parent 和 maximal-bundle receipt 重放。原来
\(g>1\) 且所有因子 \(1\pmod4\) 的 q=1 mask 不再阻塞 H3 的后继构造。

固定 hard control

\[
p=14449,\quad a=431,\quad g=5
\]

给出

\[
\beta=10,\qquad d=1,\qquad\lambda=5,
\qquad c_4=13391<14448.
\tag{18}
\]

这是真实 mask 分支上的 strict macro 控制；它与此前该点的 \(p+1\) 商上半区桥失败
并不矛盾，因为两者是不同的标记状态转换。

## 5. 边界

该结果关闭的是 H3 的“无后继”缺口，不是整个 G/Type I 全局出口。H4 必须重新执行
terminal-first 和 typed reclassification；本卡没有证明 H4 必有短证书、不会回到更大状态，
或可继续得到严格分母递降。它只把下一条真正缺口推进到 H4 的 selector/termination。

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_maximal_fourth_anchor_completion.py --verify
```
