---
kind: claim
claim_id: type-II-collision-factor-relay-boundary
title: 带来源标签的碰撞与私有因子 relay 的有限完备审计
statement: 对一个共同失败的有限规范 Type II 扇，把碰撞素因子幂及扇内私有素因子幂按来源移位标记。自然范围 u<=p/4 内，证书因子 h 若由碰撞闭包与至多 b 种不同的基础私有素因子组成，则 h<=2p 且可由 h 的有限枚举及 ac|(h+1)/4 完整穷尽。对 H=19、p<=10^7 的 45 个共同失败点，b=0,1,2 分别覆盖 25,39,40 个，仍留下 20,6,5 个；在最后五个残余上，b=3 仍为零命中。特别地 p=225289 在 b=3 下的 8185 个候选都无 relay，故在该模型中任何 relay 必须含至少四种基础私有素因子或扇外新因子。
claim_status: computationally_reproduced
topics:
- type-II
- multishift
- collision-state
- factorization
- certificate
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# 带来源标签的碰撞与私有因子 relay 的有限完备审计

## 带标签闭包

固定规范移位扇 \(\mathcal S\)，对每个 \(s=a_s^2c_s\in\mathcal S\) 写

\[
N_s=p+4s.
\]

碰撞素数是某个 \(s-t\) 的素因子。若 \(q^e\Vert N_s\) 且 \(q\) 是碰撞素数，
将 \(q^e\) 连同来源 \(s\) 记录。令

\[
L_{\mathcal S}(p)=\operatorname{lcm}\left(24,\,
q^e:q^e\Vert N_s,\ q\text{ 是碰撞素数},\ s\in\mathcal S\right). \tag{1}
\]

这里不能只保留 \(L_{\mathcal S}(p)\) 而丢弃来源标签。若奇素数幂
\(q^e\mid p+4s\) 又整除 \(p+4u\)，则

\[
u\equiv s\pmod {q^e}. \tag{2}
\]

因此一个由多个碰撞素数幂组成的因子，要求所有来源移位与目标移位同时相容。这正是
单射线积集状态所没有、但不同 \(p+4s\) 的固定差值强制提供的信息。

## 有界私有源的有限完备性

设候选目标移位为 \(u=a^2c\)，其中 \(c\) 平方自由。碰撞闭包以外，允许证书因子
再含至多 \(b\) 个不同的素数 \(q_i\)，每个 \(q_i^{e_i}\) 都来自某个基础移位
\(s_i\) 的私有部分。若

\[
h=g\prod_{i=1}^{r}q_i^{e_i},\quad g\mid L_{\mathcal S}(p),\quad r\le b,\qquad
h\mid p+4u,\qquad
h\equiv-1\pmod {4ac},\qquad
u\le p/4, \tag{3}
\]

则 \(h\le p+4u\le2p\)。再令

\[
d=ac,\qquad B=\frac{h+1}{4}.
\]

由 (3) 有 \(d\mid B\)，而 \(a\mid d\)、\(c=d/a\) 平方自由，且

\[
u=a^2c=ad. \tag{4}
\]

对每个私有来源的指数，\(q_i^{e_i}\mid p+4s_i\) 且 \(q_i^{e_i}\mid p+4u\)
仍强制

\[
u\equiv s_i\pmod {q_i^{e_i}}. \tag{5}
\]

反之，枚举每个 \(g\mid L_{\mathcal S}(p)\)、至多 \(b\) 个彼此不同的来源私有素因子
幂，再保留 \(h\le2p\)，随后枚举
\(d\mid(h+1)/4\) 和满足 \(a\mid d,\ d/a\) 平方自由的 \(a\)，便穷尽了 (3) 的
全部规范目标。最后直接验证 \(h\mid p+4u\) 并重建 Type II 证书。

这不是对未来移位设置一个任意上界：给定 \(b\) 的自然范围内每个这类 relay 都包含在
有限枚举中。但它不能排除含 \(b+1\) 种基础私有素因子、扇外新素因子，或任何递降。

## 精确审计

    python3 reproductions/type_ii_collision_factor_relay.py \
      --limit 1000000 --base-shift-bound 14 \
      --output reproductions/type-ii-collision-factor-relay-h14-1m-results.json

    python3 reproductions/type_ii_collision_factor_relay.py \
      --limit 10000000 --base-shift-bound 19 \
      --output reproductions/type-ii-collision-factor-relay-h19-10m-results.json

得到：

| 基础扇 | 范围 | 共同失败 | 有 relay | 无 relay |
|---:|---:|---:|---:|---:|
| \(H=14\) | \(p\le10^6\) | 24 | 12 | 12 |
| \(H=19,\ b=0\) | \(p\le10^7\) | 45 | 25 | 20 |
| \(H=19,\ b=1\) | \(p\le10^7\) | 45 | 39 | 6 |
| \(H=19,\ b=2\) | \(p\le10^7\) | 45 | 40 | 5 |
| \(H=19,\ b=3\) | 上行 5 个残余 | 5 | 0 | 5 |

其中 \(b=0\) 是纯碰撞闭包。通过

    python3 reproductions/type_ii_collision_factor_relay.py \
      --limit 10000000 --base-shift-bound 19 \
      --private-source-prime-budget 1 \
      --output reproductions/type-ii-collision-plus-one-private-relay-h19-10m-results.json

和把最后的参数改为 `2`，可重建后两行。

对两私有层的五点残余，运行：

    python3 reproductions/type_ii_collision_factor_relay.py \
      --primes 225289,2031121,3569329,3660721,7378849 \
      --base-shift-bound 19 --private-source-prime-budget 3 \
      --output reproductions/type-ii-collision-plus-three-private-relay-h19-10m-residual-results.json

得到五点全部无 relay；候选数依次为
\(8185,36726,26638,53731,53400\)。

这里并非表示这些素数没有后续证书。例如 \(p=225289\) 的首次后续规范证书在

\[
u=32,\qquad h=2591,\qquad h\equiv-1\pmod {4\cdot4\cdot2}.
\]

这个 \(2591\) 是素数，且不整除前十九个 \(p+4s\) 中的任何一个；它正是三私有层
无法表达的扇外新因子。

例如 \(p=3361\) 在前十四条规范射线都失败。其闭包中

\[
h=99=3^2\cdot11
\]

分别来自移位 \(8\) 与 \(4\)，并在 \(u=125=5^2\cdot5\) 会合：

\[
99\mid3361+4\cdot125,\qquad
99\equiv-1\pmod {4\cdot5\cdot5}.
\]

所以 \(k=1\) 重建一张缺口 \(39\) 的 Type II 证书。脚本同时保存每个 \(q^e\)
对应的所有满足 (2) 的来源移位。

纯碰撞 \(H=14\) 下，前十四条扇的无 relay 点包括

\[
92569,176089,176401,197521,225289,319321,
345601,465721,600961,806521,813121,868849.
\]

对首个共同真实递降逃逸点

\[
p=2451289
\]

也作了同一自然范围的完整枚举：\(L_{14}(p)=23423400\) 在 \(h\le2p\) 内有
428 个除子，但没有任何闭包 relay。故该机制确实产生新的直接证书，却不能替代
对剩余状态的可提升递降。

    python3 reproductions/type_ii_collision_factor_relay.py \
      --prime 2451289 --base-shift-bound 14 \
      --output /tmp/type-ii-collision-factor-relay-p2451289-h14-results.json

## 对下一步的约束

这项结果支持把来源标记保留为状态的一部分：它已为大多数有限共同失败点合成了跨移位的
新证书。但这个支撑数不能固定在很小常数：\(p=225289\) 在 \(b=3\) 下有 8,185 个
自然范围候选仍全部失败；而 \(b=3\) 后的五个残余为

\[
225289,\ 2031121,\ 3569329,\ 3660721,\ 7378849.
\]

下一步应研究这五点的加强二分：要么私有源支撑必须继续增长到四种以上，要么如
\(p=225289\) 一样必须出现扇外新因子。后者只能在加入新移位后才获得来源标签，
所以新的核心问题是自适应扇扩张后旧、新因子状态如何共同更新，或如何由该新因子
构造严格更小且有显式提升的实例。把 (1) 简化为无标签的积集大小，或把有限 relay
覆盖误读为全称闭包定理，都会丢失这个边界。
