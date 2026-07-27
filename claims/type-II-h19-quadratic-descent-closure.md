---
kind: claim
claim_id: type-II-h19-quadratic-descent-closure
title: H19 规范 Type II 扇与平方因子外部源严格递降的十亿边界
statement: 在存储的 p<=10^9 H19 残余剖面中有664个素数。自适应外部源严格递降命中562个，混合因子递降命中656个，完整平方因子递降命中660个；35840809、132285169、141326089、640775689 四点逃过完整平方因子族，分别有移位45、27、63、45的纯新因子 Type II 证书。二次递降首成功尺度最大达到 k=178，故该家族不是固定尺度或全称递降选择器；它与自适应 Type II 选择器互补。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- external-source
- factorization
- computation
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 规范 Type II 扇与平方因子外部源严格递降的十亿边界

## 审计对象

对每个

\[
p\le2\cdot10^7,\qquad p\equiv1\pmod {24},
\]

先枚举前 19 条规范 Type II 射线。第 \(s\) 条使用唯一表示
\(s=a_s^2c_s\)，其中 \(c_s\) 平方自由，并搜索

\[
h\mid p+4s,\qquad h\equiv-1\pmod {4a_sc_s}.
\]

若未命中，再对每个允许的 \(k\mid(p-1)/4\) 令

\[
q=4k-1,\qquad n=\frac{qp+1}{q+1},\qquad M=kn.
\]

完整平方因子外部源分支搜索

\[
e\mid M^2,\qquad e\le M,\qquad e\equiv-M\pmod q.
\]

每个命中的 \(e\) 都显式构造

\[
\frac4n=\frac1M+\frac1u+\frac1v,\qquad
\frac4p=\frac1{Mp}+\frac1u+\frac1v,
\]

所以它不是目标证书的重新参数化：源分母 \(n<p\)，源解、目标解和 Type I 除子证书均以
精确有理数逐项验证。

## 两千万基线

| 分类 | 数量 |
|---|---:|
| 核心素数 | 158,595 |
| H19 规范 Type II 直接捕获 | 158,530 |
| H19 共同残余 | 65 |
| 自适应外部源严格递降 | 55 |
| 混合因子外部源严格递降 | 65 |
| 完整平方因子外部源严格递降 | 65 |

普通自适应分支的 10 个遗漏包括此前的 7 个点及
\(13422481,17883889,18337201\)。它们全都由混合因子分支恢复。
千万级范围内的 7 个遗漏为

\[
3361,\ 345601,\ 1398769,\ 3660721,\ 6868801,\ 6899281,\ 9744001.
\]

它们都由混合因子分支恢复；例如 \(p=3361\) 取

\[
k=2,\quad q=7,\quad n=2941,\quad g=34
\]

给出缺口 \(39\) 的 Type I 证书和严格提升。完整平方因子扇在相同点可取
\(e=68\)，恢复同一个证书。

两千万范围的 65 个混合因子见证所用 \(k\) 的频数为：

| \(k\) | 1 | 2 | 3 | 4 | 5 | 6 | 9 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 数量 | 25 | 25 | 4 | 2 | 3 | 3 | 1 | 2 |

其中 \(p=12180169\) 的混合见证首次使用 \(k=9\)。这否定了把千万级中观察到的
\(\{1,2,3,4,5,6,12\}\) 当作固定选择器的外推；目前只能记录“本范围的命中 \(k\)
不超过 12”这一较弱事实。

## 十亿目标集审计

为避免给十亿个整数建立全局最小素因子表，目标集审计直接读取 H19 残余剖面中的 664 个
素数，只对每个允许的 \(k\) 及其 \(n_k\) 作精确试除分解；三个构造器仍逐项验证源恒等式、
目标恒等式、严格 \(n<p\) 和 Type I 证书。结果为：

| 分类 | 数量 |
|---|---:|
| H19 残余 | 664 |
| 自适应外部源严格递降 | 562 |
| 混合因子外部源严格递降 | 656 |
| 完整平方因子外部源严格递降 | 660 |
| 完整平方因子遗漏 | 4 |

遗漏恰为

\[
35{,}840{,}809,\qquad132{,}285{,}169,\qquad141{,}326{,}089. \tag{3}
\]

十亿新增第四点

\[
640{,}775{,}689. \tag{4}
\]

它们不是当前 Type II 选择器的遗漏：分别在 \(s=45,27,63,45\) 有纯新因子证书
\(h=31139,107,83,359\)。因此完整平方因子递降与新因子选择器是互补出口，而不是一个
包含另一个。二次递降中最大的首成功尺度为

\[
p=726{,}075{,}529,\qquad k=178. \tag{5}
\]

这否定任何从两千万闭合推断“平方因子递降必然成功”或“小固定 \(k\) 表足够”的做法。

## 可复现性

```bash
python3 reproductions/type_ii_h19_quadratic_descent_closure.py
python3 reproductions/type_ii_h19_quadratic_descent_closure.py \
  --limit 20000000 \
  --output reproductions/type-ii-h19-quadratic-descent-closure-20m-results.json
python3 reproductions/type_ii_h19_targeted_quadratic_descent.py
python3 -m unittest tests/test_type_ii_h19_quadratic_descent_closure.py -q
python3 -m unittest tests/test_type_ii_h19_targeted_quadratic_descent.py -q
```

机器可读结果分别在
`reproductions/type-ii-h19-quadratic-descent-closure-10m-results.json` 和
`reproductions/type-ii-h19-quadratic-descent-closure-20m-results.json`，逐点记录了
三个嵌套递降族的源分母、因子、源解、目标解和证书。

## 研究含义

这给出当前“短证书或递降”纲领最有信息量的有限边界：固定 H19 扇的 65 个残余不是随机地
靠更远 Type II 移位才被覆盖；它们均已有真实的严格递降出口。普通外部源选择器的 10 个
失败说明仅搜索 \(g\mid n\) 不够，而混合条件 \(g\mid kn\) 在此范围恰好补齐。

因此下一项可证伪的理论目标应是：在 H19 或缓增 Type II 扇的共同残余上，证明存在
受控增长 \(k\) 的平方因子外部源见证，或证明其失败会强制一个新的规范 Type II 因子。
这个命题必须允许模数扩张时强制因子吸收旧障碍，不能把 H22 型的固定模数闭合当作归纳步骤。

十亿边界进一步要求这种命题是真正的析取：平方因子递降的四个遗漏仍由后续纯新因子
Type II 证书恢复。合理的下一条引理应从同一 H19 状态同时导出“受限新因子命中”或
“某个 \(n_k<p\) 的严格提升”，而不能把任一分支孤立地提升为全称断言。

## 范围

该结果没有证明 H19 是全称 Type II 界，也没有证明任何固定 \(k\) 集合对所有核心素数
足够。平方因子外部源分支虽然为每个命中点
给出完备且严格的提升，但尚无对其参数选择的逐点定理。
