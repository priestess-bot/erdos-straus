---
kind: claim
claim_id: h19-k23-global-tail-pressure-external-source-bridge-2097152
title: H19-k23 全局尾压力进程的固定因子外部源递降桥
statement: H19-k23 二百万层全局尾规范基底压力集的22条可提升素数进程中，20条在全部参数上都有一个固定的平稳外部源尺度 k 和一个固定平方尾除子 e，使完整平方因子外部源给出从 p 到 n=( (4k-1)p+1 )/(4k)<p 的严格递降。该结论由穷尽每条进程的全部平稳尺度 k|gcd((p0-1)/4,P/4) 和每个固定源因子的平方除子残数得到。两个未命中进程的种子为 2220549727681245601 与 748375048866405601；未命中只排除固定因子桥，不排除变量因子或其它递降。
claim_status: computationally_reproduced
topics:
- type-I
- external-source
- strict-descent
- stationary-scale
- pressure-family
- h19
- global-tail-menu
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: external-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局尾压力进程的固定因子外部源递降桥

全局尾的规范基底压力进程有形式

\[
p(n)=p_0+Pn,\qquad n\ge0, \tag{1}
\]

并保持此前的全局尾基底失配。对任意平稳尺度

\[
k\mid\gcd\left(\frac{p_0-1}{4},\frac P4\right),\qquad q=4k-1, \tag{2}
\]

外部源与其乘积为

\[
N_k(n)=\frac{qp(n)+1}{4k}<p(n),\qquad
M_k(n)=kN_k(n)=\frac{qp(n)+1}{4}. \tag{3}
\]

因 (qP/4equiv0pmod q)，(M_k(n)\bmod q) 与 (n) 无关。再令

\[
F_k=\gcd\left(\frac{qP}{4k},\frac{qp_0+1}{4k}\right). \tag{4}
\]

则 (kF_kmid M_k(n)) 对所有 (n) 成立。若其平方的一个固定除子满足

\[
e\mid(kF_k)^2,\qquad e\equiv-M_k(0)pmod q,\qquad e\le M_k(0), \tag{5}
\]

则它对整条进程恒有 (emid M_k(n)^2)、(ele M_k(n)) 及所需残数。因此

\[
u=\frac{M_k+e}{q},\qquad v=\frac{M_ku}{e} \tag{6}
\]

给出完整平方尾恒等式和严格提升

\[
\frac4{p(n)}=\frac1{M_k(n)p(n)}+\frac1u+\frac1v. \tag{7}
\]

## 完整压力审计

对 22 条压力进程，程序穷尽 (2) 的全部尺度，并对每个 (kF_k) 的**全部**平方除子
残数表执行 (5)。每个报告的见证又在 (n=0,1) 上用有理数恒等式独立核验。结果为：

| 项目 | 数目 |
|---|---:|
| 压力进程 | 22 |
| 有固定因子严格递降桥 | 20 |
| 未有此类桥 | 2 |

两个未桥接种子为

\[
2,220,549,727,681,245,601,\qquad
748,375,048,866,405,601. \tag{8}
\]

尤其，先前用于 72 尾完整 Type II 条件性逃逸的种子

\[
p_0=955,643,834,512,728,001
\]

在 (k=18)、(q=71) 有

\[
F_{18}=7453,\qquad e=67077, \tag{9}
\]

从而整条进程都具有外部源严格递降。这解释了为何固定菜单的 Type II 条件性逃逸不能接近
Erdős--Straus 反例：它已有不依赖 Dickson 假设的 Type I 出口。

两个未命中只说明在所有平稳尺度上，固定源因子不能单独完成 (5)。它不排除变量余因子、
平移外部源、菜单外 Type II 尾，或另一种带标记递降状态。事实上两个**种子点**都已由
变量因子外部源直接下降；见
[两条固定因子桥缺口的外部源种子递降](h19-k23-pressure-external-source-seed-profile-2097152.md)。
未解决的仅是把这种变量因子选择提升为整条进程上的统一规则。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_tail_pressure_external_source_bridge.py \
  --input reproductions/h19-k23-global-base-only-prime-obstruction-2097152.json \
  --output reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json
python3 -m unittest tests/test_h19_k23_global_tail_pressure_external_source_bridge.py -q
~~~
