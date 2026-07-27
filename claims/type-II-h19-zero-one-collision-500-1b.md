---
kind: claim
claim_id: type-II-h19-zero-one-collision-500-1b
title: H19 十亿新因子状态在五百移位内零/一碰撞闭合
statement: 对p<=10^9的541个H19新因子状态，从各自首次无旧私有因子移位起完整枚举至s<=500的单新因子规范 Type II 证书，541个全部命中；最小碰撞重数分布为0:539、1:2、2:0。最大最小碰撞移位为484，唯一达到该值的是p=372271201，届时取纯新因子h=3343。仍需一碰撞的仅p=178400041与p=751064161，分别取17*127与5*67。因此该有限状态集满足零/一碰撞选择器的s<=500版本，不推出统一移位界或全称选择器。
claim_status: computationally_reproduced
topics:
- type-II
- multishift
- factorization
- new-factor
- collision-factor
- release-depth
- finite-audit
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

# H19 十亿新因子状态在五百移位内零/一碰撞闭合

令 H19 表示前十九条规范 Type II 射线，先剥离直接 H19 证书、只使用旧碰撞因子的
证书和含旧私有因子的证书。存储的 \(p\le10^9\) 剖面留下 \(541\) 个首次无旧私有因子
且仍含新因子的状态。对每个状态，从其首次无旧私有因子移位起，逐个枚举至

\[
s\le500
\]

的所有规范 Type II 因子，并只保留恰含一个相对于 H19 新的素因子的证书。对每张候选
记其 H19 碰撞素因子按重数的总数为 \(\nu_{\mathrm{coll}}\)。

## 精确结果

全部 \(541\) 个状态都存在候选，且逐点最小化 \(\nu_{\mathrm{coll}}\) 后得到

\[
\#\{\nu_{\mathrm{coll}}=0\}=539,\qquad
\#\{\nu_{\mathrm{coll}}=1\}=2,\qquad
\#\{\nu_{\mathrm{coll}}\ge2\}=0. \tag{1}
\]

仍需一次碰撞的仅有两点：

| \(p\) | \(s\) | \(h\) | 碰撞素因子 | 新素因子 |
| ---: | ---: | ---: | ---: | ---: |
| \(178{,}400{,}041\) | \(72\) | \(17\cdot127\) | \(17\) | \(127\) |
| \(751{,}064{,}161\) | \(36\) | \(5\cdot67\) | \(5\) | \(67\) |

每个 \(h\) 都满足 \(h\mid p+4s\) 及 \(h\equiv-1\pmod{4ac}\)，其中
\(s=a^2c\)，所以它直接恢复一张 Type II 证书。碰撞因子还满足其 H19 来源移位的
必要同余 \(s\equiv t\pmod\ell\)。

最大最小碰撞移位为

\[
p=372{,}271{,}201,\qquad s=484,\qquad h=3343. \tag{2}
\]

该见证是纯新的；它正是此前在 \(s\le200\) 最少需要两种碰撞素因子的状态。故已知的
两碰撞边界在本次更深窗口中释放，不再是整个十亿状态集的最小碰撞障碍。

## 与较浅窗口的比较

同一 \(541\) 个状态在 \(s\le200\) 时的分布为

\[
0:530,\qquad1:10,\qquad2:1. \tag{3}
\]

所以从 200 扩展到 500 不只是把一张见证替换为更深见证：九个浅窗口的正碰撞状态
转为纯新，唯一两碰撞状态也转为纯新，只留下两条一次碰撞证书。这个现象为
`type-II-zero-one-collision-selector-conjecture` 提供更强的有限支持，同时把真正待证的
问题收紧为解释状态依赖的释放深度。

## 边界

式 (1) 只对这个有限的 H19、十亿、\(s\le500\) 样本成立。它不说明未来样本不会出现
更高碰撞重数，也不说明 \(500\) 是统一上界；固定有限移位扇仍有条件性逃逸边界。它也
不自动给出严格递降，所给的是直接 Type II 短证书。

可复现命令：

~~~bash
python3 reproductions/type_ii_minimal_collision_support.py \
  --input reproductions/type-ii-source-free-transition-h19-1b-results.json \
  --shift-cap 500 \
  --output reproductions/type-ii-minimal-collision-support-h19-1b-s500-results.json
python3 -m unittest tests/test_type_ii_minimal_collision_support.py -q
~~~
