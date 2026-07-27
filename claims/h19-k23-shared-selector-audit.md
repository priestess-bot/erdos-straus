---
kind: claim
claim_id: h19-k23-shared-selector-audit
title: H19-k23 残存进程的有限共享因子 Type II 选择器审计
statement: 对 H19-k23 的14条残存进程 p=Pt+C，在 0<=t<1048576 的全部2270418个实际素数值上，均存在 m<=99、m=3 mod4，使 x=(p+m)/4 同时具有非平凡共享除子 D|4x、D=1 modm，和 Type II 除子 d|x^2、d=-x modm。紧凑流式审计逐点保留普通双尾闭包所需字段；1,048,576层最大最小缺口仍为99，故有限样本不支持固定小缺口界。
claim_status: computationally_reproduced
topics:
- type-II
- shared-divisor
- short-certificate
- marked-descent
- adaptive-factor
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: certificate-and-marked-descent-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 残存进程的有限共享因子 Type II 选择器审计

## 联合条件

对核心素数 \(p\) 与合法缺口 \(m\equiv3\pmod4\)，写

\[
x=\frac{p+m}{4}.
\]

审计在同一个缺口上同时要求

\[
D\mid4x,\quad D>1,\quad D\equiv1\pmod m, \tag{1}
\]

以及

\[
d\mid x^2,\quad d\le x,\quad d\equiv-x\pmod m. \tag{2}
\]

(2) 是直接的 Type II 除子证书。由 (1) 写 \(k=(D-1)/m\)，则
\(D=km+1\mid p+m\)。从 (2) 的 Type II 证书 \((x,y,z)\) 恢复严格较小的带标记源

\[
\left(kx,\frac yp,\frac zp\right)
\longmapsto(x,y,z).
\]

所以每一项命中同时是直接短证书和严格带标记源表示；后者本身不应误作无标记递降证明。

## 当前残存样本

对当前 14 条 H19-k23 进程的 \(0\le t<1024\)，以确定性 64 位素性筛选实际素数；
对每个素数按缺口递增穷尽 \(m\le239\)，完整分解 \(x\)，枚举 \(4x\) 的全部共享除子和
\(x^2\) 的全部 Type II 除子。每个记录都用精确分数核验证书、源与目标两个单位分数
恒等式。

| 项目 | 数目 |
|---|---:|
| 残存进程 | 14 |
| 实际素数值 | 2,687 |
| 共享 Type II 命中 | 2,687 |
| 漏洞 | 0 |
| 最大最小缺口 | 59 |

最小缺口频数为：

| \(m\) | 3 | 7 | 11 | 15 | 19 | 23 | 27 | 31 | 35 | 39 | 47 | 55 | 59 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 点数 | 1337 | 695 | 302 | 182 | 86 | 46 | 9 | 17 | 5 | 3 | 1 | 1 | 3 |

## 16384 层扩展

用完全相同的确定性 64 位素性、分解、共享因子和 Type II 除子检查扩展到
\(0\le t<16384\)。14 条进程中出现的实际素数值增至 39,658 个，仍全部命中，
但最小缺口谱增加了 \(m=43\) 和 \(m=71\)，最大值由 59 升至

\[
p=5\,771\,131\,031\,426\,401,\qquad m=71,\qquad D=72. \tag{3}
\]

因此这个更深范围的精确结论是

\[
39\,658=39\,658_{\text{shared Type II hits}}+0_{\text{misses}},
\qquad \max m_{\min}=71. \tag{4}
\]

这强化的是“因子状态允许自适应联合命中”的实验依据，而不是 \(m\le59\) 或
\(m\le71\) 的全称结论。最大记录的增长恰说明下一步理论必须控制允许缺口的增长，
或把持续增长转化为另一种递降。

## 32768 层扩展

进一步将同一确定性审计扩展到 \(0\le t<32768\)。最大候选值为
\(50\,879\,706\,211\,094\,401<2^{64}\)，所以素性、完整分解和除子枚举仍在脚本的
确定性 64 位范围内。14 条进程中出现 77,823 个实际素数，仍无遗漏；最小缺口谱新增
\(m=51,63,87\)，最大值升至

\[
\max m_{\min}=87. \tag{5}
\]

两个 \(m=87\) 记录为

\[
\begin{aligned}
p&=30\,052\,505\,459\,937\,601,\\
p&=31\,109\,912\,121\,448\,801.
\end{aligned} \tag{6}
\]

故最新有限结论为

\[
77\,823=77\,823_{\text{shared Type II hits}}+0_{\text{misses}}. \tag{7}
\]

这再次否定了从有限样本推断固定小缺口界的做法；特别地，\(m\le71\) 不能覆盖该扩展样本。
关于这批记录的普通双尾递降闭合，见
[H19-k23 共享选择器 32768 层的普通双尾递降闭合](h19-k23-shared-selector-tail-descent-32768-closure.md)。

## 65536 层扩展

将参数范围再加倍到 \(0\le t<65536\) 时，最大候选值为
\(101\,759\,444\,073\,648\,001<2^{64}\)。审计可按 14 条独立进程并行运行，仍使用同一
确定性 64 位素性、完整 \(x\) 分解、共享因子与 Type II 除子核验。该范围有 152,893 个
实际素数，全部命中；谱中新出现 \(m=83\)，但最大最小缺口仍为 \(87\)：

\[
152\,893=152\,893_{\text{shared Type II hits}}+0_{\text{misses}},
\qquad \max m_{\min}=87. \tag{8}
\]

唯一的 \(m=83\) 记录为

\[
p=72\,262\,729\,462\,284\,001. \tag{9}
\]

它在普通双尾递降中改用替代缺口 \(159\)，见
[H19-k23 共享选择器 65536 层的普通双尾递降闭合](h19-k23-shared-selector-tail-descent-65536-closure.md)。

## 131072 层扩展

按 14 条独立进程并行将范围扩展到 \(0\le t<131072\)。最大候选为
\(203\,518\,919\,798\,755\,201<2^{64}\)。在 299,782 个实际素数上，全部仍有共享
Type II 命中，且最小缺口谱最大值稳定在 \(87\)：

\[
299\,782=299\,782_{\text{shared Type II hits}}+0_{\text{misses}},
\qquad \max m_{\min}=87. \tag{10}
\]

这不是固定界定理：它只表明上一轮新增的 \(87\) 尚未被更大样本超过。普通双尾闭合中的
原缺口失配类新增 \(m=63\)，见
[H19-k23 共享选择器 131072 层的普通双尾递降闭合](h19-k23-shared-selector-tail-descent-131072-closure.md)。

## 262144 层扩展

继续按 14 条进程并行扩展到 \(0\le t<262144\)，最大候选为
\(407\,037\,871\,248\,969\,601<2^{64}\)。588,526 个实际素数仍全部命中；最小缺口谱
首次出现 \(m=95\) 和 \(m=99\)，后者刷新最大值：

\[
\max m_{\min}=99. \tag{11}
\]

唯一的 \(m=99\) 记录为

\[
p=208\,954\,693\,584\,597\,601. \tag{12}
\]

它的共享因子为 \(100\)，且 \(100\mid p-1\)，故直接形成普通双尾递降。全部样本的
普通双尾闭合见
[H19-k23 共享选择器 262144 层的普通双尾递降闭合](h19-k23-shared-selector-tail-descent-262144-closure.md)。

## 524288 层扩展

将并行审计扩展至 \(0\le t<524288\)，最大候选为
\(814\,075\,774\,149\,398\,401<2^{64}\)。1,155,128 个实际素数仍全部命中；没有新的
最小缺口保持者，最大值维持

\[
\max m_{\min}=99. \tag{13}
\]

这次扩展确认 \(m=99\) 在额外一倍样本中仍未被超过，但不把该稳定性解释为固定界定理。
普通双尾闭合及失配类分布见
[H19-k23 共享选择器 524288 层的普通双尾递降闭合](h19-k23-shared-selector-tail-descent-524288-closure.md)。

## 1048576 层紧凑流式扩展

再将同一审计加倍到 \(0\le t<1048576\)。最大候选仍低于 \(2^{64}\)，
故 64 位确定性素性判定、完整 \(x\) 分解和约数检查的适用范围不变。该层共有
\(2\,270\,418\) 个实际素数，全部命中，且

\[
2\,270\,418=2\,270\,418_{\text{shared Type II hits}}+0_{\text{misses}},
\qquad \max m_{\min}=99. \tag{14}
\]

完整记录还含有 \(x\) 的分解、所有单位分数及带标记源，聚合百万层记录会使父进程
承担不必要的内存和序列化压力。因此本层在工作进程内先完成完整证书和带标记恒等式
核验，随后只流式写出普通双尾闭合所需的 \(p,m,x,d\)（并保留进程与参数索引）。
这改变的是证据的存储表示，不是筛选条件或证书检查。

最小缺口谱新增 \(67,75\)，但没有超过已有的 \(99\)。普通双尾递降在这份紧凑产物上
独立重新构造，得到

\[
2\,270\,418=2\,265\,174_{\text{原共享缺口}}
+5\,244_{\text{替代 }p-1\text{ 缺口}}+0_{\text{遗漏}}. \tag{15}
\]

详见
[H19-k23 共享选择器 1048576 层的普通双尾递降闭合](h19-k23-shared-selector-tail-descent-1048576-closure.md)。
其中原共享缺口 \(m=27\) 的 5,081 条替代尾继续可由至多两种非基底素因子完成，
但尾端已从 79 延长至 91、95；见
[H19-k23 m=27 替代尾 1048576 层的支持度二递降梯](h19-k23-m27-support-two-tail-ladder-1048576.md)。

## 研究含义

这条审计与静态来源的条件性共同逃逸形成互补：后者表明固定 H19 加 37 个来源不能闭合，
而这里允许共享除子 \(D\) 和首尺度 \(k=(D-1)/m\) 随实际因子结构变化，因而在同一有限
残余样本上全部给出直接 Type II 证书。

所以当前最有希望的正向目标不是固定尺度递降，而是证明某种增长缺口的共享残数选择器：

\[
\forall p\equiv1\pmod{24},\quad
\exists m,D,d\text{ 满足 (1)--(2)}.
\]

本结果没有证明 \(m\le71\) 或 \(m\le239\) 对所有 \(p\) 都足够。已知更广泛的有限边界
也表明固定小缺口会出现逃逸；真正的理论问题仍是如何从跨缺口因子积集强制至少一个
联合命中。

重建默认 1024 层命令为 `python3 reproductions/h19_k23_shared_selector_audit.py`；扩展结果为

~~~bash
python3 reproductions/h19_k23_shared_selector_audit.py \\
  --parameter-limit 16384 --gap-cap 239 \\
  --output reproductions/h19-k23-shared-selector-audit-16384.json
python3 reproductions/h19_k23_shared_selector_audit.py \\
  --parameter-limit 65536 --gap-cap 239 \\
  --output reproductions/h19-k23-shared-selector-audit-65536.json
python3 reproductions/h19_k23_shared_selector_audit.py \\
  --parameter-limit 131072 --gap-cap 239 --workers 14 \\
  --output reproductions/h19-k23-shared-selector-audit-131072.json
python3 reproductions/h19_k23_shared_selector_audit.py \\
  --parameter-limit 262144 --gap-cap 239 --workers 14 \\
  --output reproductions/h19-k23-shared-selector-audit-262144.json
python3 reproductions/h19_k23_shared_selector_audit.py \\
  --parameter-limit 524288 --gap-cap 239 --workers 14 \\
  --output reproductions/h19-k23-shared-selector-audit-524288.json
python3 reproductions/h19_k23_shared_selector_audit.py \\
  --parameter-limit 1048576 --gap-cap 239 --workers 14 --compact \\
  --output reproductions/h19-k23-shared-selector-audit-1048576.json
python3 -m unittest tests/test_h19_k23_shared_selector_audit.py -q
~~~
