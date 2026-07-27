---
kind: claim
claim_id: h19-k23-m27-support-two-tail-ladder
title: H19-k23 m=27 替代尾的支持度二递降梯
statement: 在524288层 H19-k23 的2710条原共享缺口m=27替代尾记录中，沿最先成功尾缺口31,35,39,47,59,63,71,79，全部可由阶段相应的平滑或固定基底乘至多两个不同非基底素因子构成普通 Type II 双尾证书。精确分解为1260条零新增、1430条一新增、20条二新增，零条需三种或更多新增素因子。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- divisor-selection
- factor-support
- h19
- computational-closure
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 \(m=27\) 替代尾的支持度二递降梯

这条结果只处理共享最小缺口为 \(m=27\) 且原证书不能直接双尾递降的有限记录。每一步
都使用闭包审计中的最先成功尾缺口；不是从“某处存在一个证书”倒推固定支持度。

阶段基底依次为：

| 尾缺口 | 参数 \(q\) | 基底 |
|---:|---:|---|
| 31 | 8 | 固定 \(2^6 7^2 19^2\) |
| 35 | 9 | 固定 \(3^4 13^2\) |
| 39 | 10 | \(100u^2\) 的完整 \(2,5\)-平滑部分 |
| 47 | 12 | \(144u^2\) 的完整 \(2,3\)-平滑部分 |
| 59 | 15 | \(225u^2\) 的完整 \(3,5,7\)-平滑部分 |
| 63, 71, 79 | 16, 18, 20 | 各自 \(q^2u^2\) 的相应 \(q\)-平滑部分 |

“新增素因子支持度”只计基底以外的不同素因子；所有指数仍允许在 \(x^2=q^2u^2\) 的
合法范围内变化。每个选出的除子均重新检查平方根补全标准形和严格双尾源。

## 分层结果

\[
\begin{array}{c|r|r|r|r}
\text{tail gap}&\text{base}&\text{one new}&\text{two new}&\text{next residual}\\
\hline
31&1192&795&0&723\\
35&0&387&2&334\\
39&0&155&9&170\\
47&42&68&6&54\\
59&23&21&1&9\\
63&0&2&1&6\\
71&2&2&0&2\\
79&1&0&1&0
\end{array} \tag{1}
\]

因而

\[
2\,710=1\,260_{\text{base}}+1\,430_{\text{one new}}+20_{\text{two new}}. \tag{2}
\]

这条有限主链没有任何三新增素因子见证，也没有未闭合点。它把原来的“替代 \(p-1\)
因子扫描”压缩为有限、逐层的支持度二选择结构。

但 (2) 不是全称选择器：阶段、基底和支持度均依赖于 H19-k23 的 14 条进程及有限
审计层。下一步研究目标是解释为什么这类低支持度梯不能无限维持，或将其提升为可迭代的
势能递降。

重建命令：

~~~bash
python3 reproductions/h19_k23_m27_m31_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-524288.json \
  --output reproductions/h19-k23-m27-m31-selector-profile-524288.json
python3 reproductions/h19_k23_m31_m35_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-524288.json \
  --output reproductions/h19-k23-m31-m35-selector-profile-524288.json
python3 reproductions/h19_k23_m35_m39_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-524288.json \
  --output reproductions/h19-k23-m35-m39-selector-profile-524288.json
python3 reproductions/h19_k23_m39_m47_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-524288.json \
  --output reproductions/h19-k23-m39-m47-selector-profile-524288.json
python3 reproductions/h19_k23_m47_m59_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-524288.json \
  --output reproductions/h19-k23-m47-m59-selector-profile-524288.json
~~~
