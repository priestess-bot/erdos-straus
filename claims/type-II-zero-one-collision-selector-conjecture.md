---
kind: claim
claim_id: type-II-zero-one-collision-selector-conjecture
title: H19 后零/一碰撞素数 Type II 选择器
statement: 设 p=1 mod24 未被 H19 直接证书或碰撞专用证书捕获。令 O_p 为 p+4r (1<=r<=19) 的素因子集。猜想存在 s=a^2c>19、epsilon 属于 {1,3,5,7,13,17} 和素数 q 不属于 O_p，使 epsilon*q 整除 p+4s 且 epsilon*q=-1 mod4ac；当 epsilon>1 时，epsilon 是 H19 碰撞素数并强制 s 与其来源移位同余。该命题若成立则给出直接 Type II 证书。
claim_status: open
topics:
- type-II
- multishift
- collision-factor
- congruence
- selector
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-27'
---

# H19 后零/一碰撞素数 Type II 选择器

## 精确目标

令 \(p\equiv1\pmod{24}\)，并令

\[
\mathcal O_p=\bigcup_{1\le r\le19}\operatorname{Supp}(p+4r).
\]

先剥离 H19 的直接证书及只由旧碰撞因子构成的直接证书。对余下状态，提出比
[单新因子选择器](type-II-one-new-factor-selector-conjecture.md) 更窄的充分命题：存在

\[
s=a^2c>19,\qquad
\epsilon\in\{1,3,5,7,13,17\},\qquad q\notin\mathcal O_p
\]

满足

\[
\epsilon q\mid p+4a^2c,\qquad
\epsilon q\equiv-1\pmod{4ac}. \tag{1}
\]

于是令 \(k=(\epsilon q+1)/(4ac)\)，便有
\(\epsilon q=4ack-1\)，故规范 Type II 射线直接重建 \(4/p\) 的证书。

## 来源约束

当 \(\epsilon>1\) 时，它须是某个基础值 \(p+4t\) 的碰撞素因子，\(1\le t\le19\)。
若它又整除目标值 \(p+4s\)，则因 \(\epsilon\) 为奇素数，

\[
\epsilon\mid4(s-t),\qquad s\equiv t\pmod\epsilon. \tag{2}
\]

另一方面，(1) 蕴含 \(\gcd(\epsilon,4ac)=1\)，并把新素因子限定为唯一残数类

\[
q\equiv-\epsilon^{-1}\pmod{4ac}. \tag{3}
\]

所以这不是泛泛地要求“有一个有用的新因子”：对每个候选碰撞素数，未来移位先被 (2)
限制到一个来源同余类，随后 \(q\) 必须在 (3) 的类中整除对应的 \(p+4s\)。

## 当前证据与边界

在 \(p\le3\cdot10^8,\ s\le200\) 的精确剖面中，260 个新因子状态全都满足 (1)：
253 个取 \(\epsilon=1\)，余下 7 个取一个一次碰撞素数。后七个的
\(\epsilon\) 依次为

\[
3,5,13,3,17,7,3,
\]

且每个均满足其来源同余和逆元残数，见
[一碰撞来源同余审计](type-II-one-collision-source-profile.md)。

将单碰撞来源条件独立复核至 \(p\le10^9\) 后，541 个新因子状态中530个可取
\(\epsilon=1\)，10个可取恰一个碰撞素数，且它们逐一满足 (2)--(3)；单碰撞素数
的频数为 \(3:4,5:2,7:1,13:2,17:1\)。第11个非纯状态正是下述两碰撞边界，
所以这不是“碰撞标签验证不足”留下的遗漏，而是碰撞积复杂度确实增长。

对同一 541 个状态完整延长到 \(s\le500\) 后，最小碰撞重数分布收缩为
\(0:539,1:2\)，没有任何最小重数为二的状态；仍需一次碰撞的仅为
\(p=178{,}400{,}041\) 的 \(17\cdot127\) 与 \(p=751{,}064{,}161\) 的
\(5\cdot67\)。此前的两碰撞状态 \(p=372{,}271{,}201\) 在 \(s=484\) 取得纯新
因子 \(3343\)。这是零/一碰撞命题在该十亿样本和这个更深窗口内的完整有限验证，见
[H19 十亿新因子状态在五百移位内零/一碰撞闭合](type-II-h19-zero-one-collision-500-1b.md)。

进一步延至 \(s\le1008\)，这 541 个状态全都取得纯新见证；最迟者是
\(p=178{,}400{,}041\)，在 \(s=1008\) 取 \(q=9743\)。这强化了有限证据，但不能删去
状态依赖的释放深度问题，见
[H19 十亿新因子状态在移位一千零八内纯新闭合](type-II-h19-pure-new-1008-1b.md)。

五亿审计给出这条强化版的首个固定窗口边界：新因子状态增至 341 个后，
\(p=372{,}271{,}201\) 在完整 \(s\le200\) 枚举中最少需要
\(\epsilon=3\cdot7\)，其单新因子为 \(h=3\cdot7\cdot1051\) 且 \(s=89\)。
所以“\(s\le200\) 内零或一个碰撞素数”已经不是有效的有限选择规则。它并非未限定移位
猜想的反例：同一状态在 \(s=401\) 释放为 \(\epsilon=5\)，在 \(s=484\) 释放为
\(\epsilon=1\)，见
[首个两碰撞状态的延迟释放边界](type-II-h19-two-collision-release-boundary.md)。

这仍然不是全称选择定理。已有固定移位、固定尺度和固定有限扇的条件性逃逸，因而证明
不能把 \(\epsilon\)、\(s\) 或 \(k\) 固定。真正需证明的是：有限个由 (2) 限定的来源类中，
至少一类出现 (3) 的新因子，或全部失败可转化为严格更小且可提升的实例；五亿边界进一步
要求此论证容纳状态依赖的碰撞积和释放深度。

## 重建

    python3 reproductions/type_ii_one_collision_source_profile.py
    python3 -m unittest tests/test_type_ii_one_collision_source_profile.py -q
