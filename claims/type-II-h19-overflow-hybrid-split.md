---
kind: claim
claim_id: type-II-h19-overflow-hybrid-split
title: H19 十亿残余的二次外部源与偶源溢出分流
statement: 在存储的664个 p<=10^9 H19 残余中，91个首个 r 尾命中最小溢出 B>1 的点和15个 r<=9999 未命中的点全部具有二次因子外部源严格递降；二次外部源仅有的4个遗漏均具有最小 B=1 的首个 r 尾命中。因此该有限剖面按“标准二次源”与“零溢出偶源尾”完全闭合，但不证明此分流在更大范围或一般核心素数上成立。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- external-source
- overflow
- hybrid
- strict-descent
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: even-source-and-external-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19 十亿残余的二次外部源与偶源溢出分流

把两个既有、独立重建的剖面按核心素数连接：

1. 二次因子外部源严格递降；
2. \(r\le9999\) 内首个偶源尾命中诱导的最小 Type I 溢出 \(B\)。

664 个 H19 残余分为下列有限状态：

| 状态 | 数量 | 二次外部源递降 |
| --- | ---: | --- |
| 首命中且最小 (B=1) | 558 | 不作为本分流的要求 |
| 首命中且最小 (B>1) | 91 | 全部存在 |
| (rle9999) 内无命中 | 15 | 全部存在 |
| 二次外部源遗漏 | 4 | 全部属于第一行 |

特别地，四个标准遗漏

\[
35840809,\quad132285169,\quad141326089,\quad640775689
\]

均有零溢出首尾；反之，所有高溢出点以及所有 \(r\)-窗口未命中点都不需要依赖该偶源尾，
因为已有二次外部源严格递降。

这是一个比“标准或小 \(r\)”更细的有限分流：当前压力状态集中，难以用低溢出尾闭合的部分
恰被另一条可读标准源闭合。它提示可尝试的正向势量是联合的，而非单独界定 \(r\) 或 \(B\)：
证明高溢出/无尾命中会强制一个标准或混合源证书，或证明标准源失败会强制低溢出偶源尾。

高溢出分支的标准递降在当前剖面中还有一个低尺度特征。91 个 \(B>1\) 状态所存的完整
平方因子外部源见证均可取 \(k\le20\)，其频数为：

| \(k\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 11 | 12 | 15 | 20 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 状态数 | 29 | 15 | 21 | 4 | 6 | 2 | 5 | 2 | 1 | 1 | 1 | 3 | 1 |

这说明十亿范围内高溢出并不对应“只能靠很大外部尺度”的行为；在 \(r\le99999\) 仍未释放的
52 个状态也属于该高溢出集合，因而同样已有此类严格递降。它只是一项有限的低尺度现象，
不能升级为固定 \(k\le20\) 的一般选择器。

该结论只来自存储的 \(10^9\) H19 剖面，不是一般二分法。特别是它没有控制更大 \(r\)、
更大规模或非 H19 核心点。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_overflow_hybrid_split.py \
  --overflow reproductions/type-ii-h19-bounded-r-overflow-profile-1b-results.json \
  --quadratic reproductions/type-ii-h19-targeted-quadratic-descent-1b-results.json \
  --output reproductions/type-ii-h19-overflow-hybrid-split-1b-results.json
python3 -m unittest tests/test_type_ii_h19_overflow_hybrid_split.py -q
~~~
