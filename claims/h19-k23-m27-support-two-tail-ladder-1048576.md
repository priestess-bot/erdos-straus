---
kind: claim
claim_id: h19-k23-m27-support-two-tail-ladder-1048576
title: H19-k23 m=27 替代尾 1048576 层的支持度二递降梯
statement: 在1048576层 H19-k23 的5081条原共享缺口m=27替代尾记录中，沿最先成功尾缺口31,35,39,47,59,63,71,79,91,95，全部由阶段相应平滑或固定基底乘至多两个不同非基底素因子构成普通 Type II 双尾证书。精确分解为2419条零新增、2628条一新增、34条二新增，零条需三种或更多新增素因子。
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

# H19-k23 \(m=27\) 替代尾 1,048,576 层的支持度二递降梯

这是 [524,288 层支持度二梯](h19-k23-m27-support-two-tail-ladder.md) 的独立加倍复验。
与旧层相比，\(m=27\) 替代记录由 2,710 增至 5,081，末端新增 \(m=91,95\)；
它们分别只需一个和两个非基底素因子。因此旧的“终端不超过 79”不是稳定规律，
但支持度二界在该样本上保持。

\[
\begin{array}{c|r|r|r|r}
\text{tail gap}&\text{base}&\text{one new}&\text{two new}&\text{next residual}\\
\hline
31&2287&1443&0&1351\\
35&0&733&3&615\\
39&0&278&15&322\\
47&83&131&9&99\\
59&42&33&1&23\\
63&0&4&2&17\\
71&5&5&1&6\\
79&2&0&2&2\\
91&0&1&0&1\\
95&0&0&1&0
\end{array} \tag{1}
\]

故

\[
5\,081=2\,419_{\text{base}}+2\,628_{\text{one new}}
+34_{\text{two new}}. \tag{2}
\]

每一项均由阶段相应 \(q^2u^2\) 的平滑或固定部分，加上至多两个不同非基底素因子幂，
重新检查平方根补全标准形和严格双尾源。这个结论仍是有限审计：它排除不了更深层出现
三新增素因子，也不提供对尾缺口长度的统一界。

重建命令：

~~~bash
python3 reproductions/h19_k23_m27_m31_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-1048576.json \
  --output reproductions/h19-k23-m27-m31-selector-profile-1048576.json
python3 reproductions/h19_k23_m31_m35_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-1048576.json \
  --output reproductions/h19-k23-m31-m35-selector-profile-1048576.json
python3 reproductions/h19_k23_m35_m39_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-1048576.json \
  --output reproductions/h19-k23-m35-m39-selector-profile-1048576.json
python3 reproductions/h19_k23_m39_m47_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-1048576.json \
  --output reproductions/h19-k23-m39-m47-selector-profile-1048576.json
python3 reproductions/h19_k23_m47_m59_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-1048576.json \
  --output reproductions/h19-k23-m47-m59-selector-profile-1048576.json
~~~
