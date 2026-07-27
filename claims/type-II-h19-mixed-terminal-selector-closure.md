---
kind: claim
claim_id: type-II-h19-mixed-terminal-selector-closure
title: H19 十亿残余的混合终端选择器有限闭合
statement: 对存储的 p<=10^9 的664个 H19 残余，662个具有普通 Type II 双尾证书；余下225289与2707609分别具有正规形 (687,1,82) 与 (7871,1,86)，其偶桥因子分别为 E=197128、2594792，满足 E|4K^2、E=1 mod R、E<=4K-2R。因此该有限剖面逐点满足普通 Type II 双尾证书或偶 Type I 正规形终端桥的混合析取。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-II
- type-I
- terminal-bridge
- even-source
- descent
- mixed-selector
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-and-Type-II-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-28'
---

# H19 十亿残余的混合终端选择器有限闭合

## 审计目标

对前十九条规范 Type II 射线未命中的存储残余，检验以下与全称混合终端选择引理相同的析取：

\[
\text{普通 Type II 双尾证书}
\quad\lor\quad
\text{Type I 正规形的偶桥 }E. \tag{1}
\]

第二支要求正规形参数满足

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad
E\le4K-2R,\qquad 2\mid E. \tag{2}
\]

## 结果

H19 剖面含 \(664\) 个不超过十亿的核心素数。现有完整 \(p-1\) 控制双尾枚举给出
\(662\) 个普通 Type II 双尾证书。其仅有的两条遗漏由完整平方因子外源见证重新正规化为
(2) 的偶桥：

| \(p\) | \((A,B,C)\) | \(R\) | \(K\) | \(E\) |
| ---: | --- | ---: | ---: | ---: |
| \(225{,}289\) | \((687,1,82)\) | \(7\) | \(394{,}256\) | \(197{,}128\) |
| \(2{,}707{,}609\) | \((7871,1,86)\) | \(23\) | \(15{,}568{,}752\) | \(2{,}594{,}792\) |

两行均由
[偶二次外源到正规形终端桥](type-I-even-external-source-normal-bridge.md) 的精确恒等式
逐项重建。故该剖面有不交分流

\[
664=662_{\mathrm{Type\,II\ tail}}+2_{\mathrm{Type\,I\ even\ terminal}},
\qquad\text{未闭合}=0. \tag{3}
\]

## 重建

~~~bash
python3 reproductions/type_ii_h19_mixed_terminal_selector_closure.py
python3 -m unittest tests/test_type_ii_h19_mixed_terminal_selector_closure.py -q
~~~

脚本读取普通双尾审计，但对两条遗漏从原始完整平方因子外源记录重新计算正规形、\(R\)、\(K\)
与 \(E\)，而不是把“严格递降”标签当作终端条件。

## 范围

(3) 是一个十亿 H19 残余集的有限实例，不是对所有核心素数的选择定理。它只说明：在这份
压力剖面中，普通 Type II 双尾分支的两个精确遗漏恰好都落入目标所要求的 Type I 偶桥分支；
全称证明仍缺少产生这两个分支之一的逐点机制。
