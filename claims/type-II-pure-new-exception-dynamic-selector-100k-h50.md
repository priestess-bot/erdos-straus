---
kind: claim
claim_id: type-II-pure-new-exception-dynamic-selector-100k-h50
title: 真实 pure-new 例外在 10 万、H=50 范围的动态选择器闭合
statement: 对全部不超过 100000 且同余于 1 模 24 的素数，按 H19 旧支持和 20<=s<=50 的 canonical fan 纯新因子定义精确重算，得到 477 个真实 E_new(100000,50) 例外。在全部 q,k|(p-1)/4 构成的有限域上作完备存在性搜索并在命中后确定性短路，动态低缺陷尾与完整平方尾外源出口的可用性分类为 both=469、tail-only=7、external-only=1、neither=0；因此两分支并集在这个有限范围覆盖 477/477。唯一 external-only 素数 67369 由 k=6、M=387372、e=684 给出外源见证。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: independent_review
topics:
- type-II
- pure-new-factor
- support-defect
- external-source
- selector
- computation
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 真实 pure-new 例外在 10 万、\(H=50\) 范围的动态选择器闭合

## 精确作用域

令 \(E_{\mathrm{new}}(100000,50)\) 为所有素数
\(p\le 100000\)、\(p\equiv1\pmod{24}\)，使得对每个
\(20\le s\le50\) 都不存在素数 \(r\) 同时满足

\[
r\mid p+4s,\qquad r\equiv-1\pmod{4a_sc_s},\qquad
r\notin\bigcup_{1\le t\le19}\operatorname{Supp}(p+4t),
\]

其中 \(s=a_s^2c_s\)，且 \(c_s\) 平方自由。程序从这个定义重新生成集合，
而不是把先前的 marked bridge 遗漏或 H19 残余当作真实例外。

在 1,181 个核心素数中，704 个被上述纯新因子捕获，余下

\[
\lvert E_{\mathrm{new}}(100000,50)\rvert=477.
\]

## 两个动态分支的完备存在性搜索

对每个 \(p\in E_{\mathrm{new}}(100000,50)\)，置 \(B=(p-1)/4\)。计算对
全部 \(q\mid B\) 构成的有限域搜索普通 \(p-1\) Type II 尾，并对
\(d\mid x_q^2\)、\(d\le x_q\) 作完备的支持缺陷至多 2 存在性搜索；同时在全部
\(k\mid B\) 构成的有限域搜索外部源尺度，并使用完整条件

\[
e\mid M_k^2,\qquad e\le M_k,
\qquad e\equiv-M_k\pmod{4k-1}.
\]

这里外源分支的候选域是 \(M_k^2\) 的全部除子，不是较窄的 \(e\mid n_k\) 或
\(e\mid M_k\) 子域。实现按固定顺序扫描，并在找到见证后短路；若某分支返回失败，
则已遍历该点上相应的全部有限候选域。两分支的包含性交并分类为：

| 可用分支 | 素数个数 |
|---|---:|
| 两者都有 | 469 |
| 仅动态低缺陷尾 | 7 |
| 仅动态外源出口 | 1 |
| 两者都没有 | 0 |

动态尾存在的 476 个素数中，全局最小支持缺陷的直方图为

\[
456_{\delta=0}+20_{\delta=1}+0_{\delta=2}=476.
\]

若选择规则优先采用动态尾，则 476 个走尾分支，余下 1 个走外源分支；故有限闭合为

\[
477=476_{\mathrm{tail}}+1_{\mathrm{external}}+0_{\mathrm{unresolved}}.
\]

## \(p=67369\) 的完整平方尾见证

唯一的 `external-only` 记录是 \(p=67369\)。所有 \(q\mid16842\) 的
支持缺陷至多 2 尾均未命中；外源分支取

\[
B=16842,\quad k=6,\quad r=23,\quad n=64562,
\quad M=kn=387372,
\]

并取 \(e=684\)。精确检查给出

\[
e\mid M^2,\qquad e\nmid M,\qquad e\nmid n,\qquad
e\equiv-M\pmod{23}.
\]

由此 \(y=(M+e)/23=16872\)、\(z=My/e=9555176\)，并可直接回放

\[
\frac4{64562}
=\frac1{387372}+\frac1{16872}+\frac1{9555176},
\]

以及严格提升

\[
\frac4{67369}
=\frac1{26096864268}+\frac1{16872}+\frac1{9555176}.
\]

这个已存见证不属于较窄的 \(e\mid n\) 或 \(e\mid M\) 子族，因而可以核对实现确实
枚举了完整平方尾，而不是在代码中悄悄退化为窄搜索。不过，同一点另有

\[
e'=3398\mid n,\qquad e'\mid M,
\qquad e'\equiv-M\pmod{23},
\]

它给出 \(y'=16990\)、\(z'=1936860\)。所以这个有限样本没有证明完整平方尾比窄子族
在“是否覆盖”意义下必不可少；它只证明当前存储和回放的首个见证来自更广的搜索空间。

## 可复现锚点

- 实现：
  [`reproductions/type_ii_pure_new_exception_dynamic_selector.py`](../reproductions/type_ii_pure_new_exception_dynamic_selector.py)
- 完整结果：
  [`reproductions/type-ii-pure-new-exception-dynamic-selector-100k-h50-results.json`](../reproductions/type-ii-pure-new-exception-dynamic-selector-100k-h50-results.json)
- 独立定义、证书回放和产物一致性测试：
  [`tests/test_type_ii_pure_new_exception_dynamic_selector.py`](../tests/test_type_ii_pure_new_exception_dynamic_selector.py)
- 选择器的统一候选表述：
  [动态低缺陷尾或外源出口选择器](dynamic-low-defect-tail-or-external-exit-selector.md)

~~~bash
python3 reproductions/type_ii_pure_new_exception_dynamic_selector.py
python3 -m unittest tests.test_type_ii_pure_new_exception_dynamic_selector -v
~~~

## 边界条件

这是精确整数算术下的有限计算复现，不是统一选择器定理。它只证明
\(X=100000,H=50\) 的真实例外集合在所述两个分支下零遗漏；不能外推到更大的
\(X\)、随 \(X\) 增长的 \(H\)、全部核心素数或 H19-k23 压力进程，也不能由
477/477 的命中率推出两个分支之一必然对任意 \(p\) 成立。
