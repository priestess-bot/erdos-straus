---
kind: claim
claim_id: type-I-h19-small-b-tail-hybrid-20m
title: H19 Type II 与受限 Type I 严格递降的两千万混合闭合
statement: 在 p<=2*10^7 的158595个核心素数中，H19 规范 Type II 直接捕获158530个，余65个。对该65点完整搜索 Type I 规范尾递降：m<=239、B<=4 恢复61个；将缺口仅扩至m<=999仍取B<=4，恢复全部65个，最大首次缺口743。因此该有限范围每点均有 H19 直接证书或受限 Type I 严格递降。Type I 分支是已有完整平方因子外部 source 递降的受限切片，不是新机制。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- normal-form
- external-source
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 Type II 与受限 Type I 严格递降的两千万混合闭合

## 混合规则

先使用前 19 条规范 Type II 射线。它在两千万范围直接捕获 158,530 个核心素数，留下
65 个残余。仅对残余逐项搜索 Type I 正规形，要求其 \(p\)-倍尾能严格去缩放为源，并限制

\[
B\le4,\qquad m\le239.
\]

若仍未命中，再把缺口上界增加到 999，保持 \(B\le4\)。

## 结果

| 分支 | 数量 |
|---|---:|
| 核心素数 | 158,595 |
| H19 Type II 直接证书 | 158,530 |
| H19 残余 | 65 |
| 残余中 \(m\le239,B\le4\) Type I 严格递降 | 61 |
| 扩至 \(m\le999,B\le4\) 后恢复 | 65 |
| 最终残余 | 0 |

只有四点需要越过短缺口盒：

| \(p\) | \(B\) | 首个 \(m\) | 源分母 \(n\) |
|---:|---:|---:|---:|
| 7,378,849 | 1 | 359 | 5,534,137 |
| 8,955,769 | 1 | 743 | 8,209,455 |
| 11,910,361 | 1 | 519 | 11,314,843 |
| 12,180,169 | 1 | 311 | 11,945,935 |

故在这个有限混合闭合中，实际最大 \(B\) 仍不超过 4，最大首次 Type I 缺口为 743。

不过，表中的四点都在较后的规范 Type II 移位直接命中，依次为
\(26,25,36,24\)，且所选证书不含 H19 的旧私有因子，见
[自适应新因子过渡谱](type-II-adaptive-factor-transition.md)。所以远 Type I 缺口在此
只是另一条受限出口，并不构成必须以递降处理的新障碍。

## 范围和下一目标

这条闭合不优于已知“H19 加完整平方因子外部源递降”的机制类别；它的新增信息是该
有限样本只使用了一个很小的证书参数盒。固定 H19、固定 \(B\) 或固定缺口不能由此提升为
全称结论，且已有条件性逃逸排除了把有限分支当作证明。

其可证伪的下一目标是：在 H19 共同残余的因子状态上，证明若当前扇失败，则扩张移位时
必出现一个不复用旧私有因子的 Type II 证书，或转入可控的 \(B\)、缺口或真正不同的源
状态。四个表中点只是前一分支的扩张扇样本；更有信息量的边界是首个后续 Type II 命中
仍必须使用旧私有因子的四点。

## 重建

    python3 reproductions/type_i_h19_small_b_tail_hybrid.py
    python3 -m unittest tests/test_type_i_h19_small_b_tail_hybrid.py -q
