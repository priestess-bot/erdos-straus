---
kind: claim
claim_id: h19-k23-adaptive-multiscale-audit
title: H19-k23 十四条残存进程的有限自适应尺度递降审计
statement: 对 H19-k23 的14条残存进程 p=Pt+C，在 0<=t<1024 的全部2687个实际素数值上，按37个静态外部尺度的固定顺序完整检查 M_k^2 的平方尾除子残数条件，均获得严格外部源递降。首成功尺度的最大值为15；频数依次为 k=1:1330, 2:671, 3:298, 4:229, 5:87, 6:33, 8:14, 9:13, 10:5, 12:6, 15:1。
claim_status: computationally_reproduced
topics:
- descent
- external-source
- adaptive-scale
- square-divisor
- computation
- conditional-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: external-source-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19-k23 十四条残存进程的有限自适应尺度递降审计

## 审计对象

统一仿射叶子排除后，14 条残存进程均形如

\[
p(t)=Pt+C,\qquad P=1\,552\,726\,375\,200.
\]

对每个静态尺度 \(k\mid1800\) 或 \(k=23\)，令

\[
q_k=4k-1,\qquad
n_k=\frac{q_kp+1}{4k},\qquad M_k=kn_k.
\]

完整平方尾外部源递降在该尺度成立，当且仅当存在

\[
e\mid M_k^2,\qquad e\equiv-M_k\pmod {q_k}. \tag{1}
\]

若初始 \(e>M_k\)，其互补因子仍满足同一残数，故总可取 \(e\le M_k\)。此时

\[
u=\frac{M_k+e}{q_k},\qquad v=\frac{M_ku}{e}
\]

给出

\[
\frac4{n_k}=\frac1{M_k}+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p=\frac1{M_kp}+\frac1u+\frac1v. \tag{2}
\]

因此每个命中都是经过整数恒等式核验的严格递降，而不只是一个残数统计。

## 有限结果

对全部 14 条进程和 \(0\le t<1024\)，先用确定性 64 位素性检验筛出实际素数，再按
37 个静态尺度的既定顺序检查 (1)。每个所用 \(M_k\) 均完成分解，分解乘积和每个素因子的
确定性 64 位素性均独立核验。结果为：

| 项目 | 数目 |
|---|---:|
| 参数层 | 1,024 |
| 实际素数值 | 2,687 |
| 未被 37 尺度捕获的值 | 0 |
| 最大首成功尺度 | 15 |

首成功尺度分布为：

| \(k\) | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 9 | 10 | 12 | 15 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 点数 | 1330 | 671 | 298 | 229 | 87 | 33 | 14 | 13 | 5 | 6 | 1 |

这把此前 \(k=15\) 的单点尺度续生见证放入更大的精确样本：该样本内并不需要
\(k>15\)，但不能据此推出它们在所有参数上永远不需要。

## 对桥接目标的意义

这份结果支持“参数依赖的尺度选择”而不是固定尺度：每个已测点都能从较小集合

\[
\{1,2,3,4,5,6,8,9,10,12,15\}
\]

中选择一个完整平方尾递降。它并没有证明此集合全称覆盖，也没有把选择仅压缩为有限碰撞
标签的函数。下一步的有效目标是把首成功条件 (1) 的共同失败转化为一个新的可证出口，
或证明选择只依赖于可控的有限状态；不能把这份有限零逃逸直接提升为有界尺度猜想。

重建命令为 python3 reproductions/h19_k23_adaptive_multiscale_audit.py 和
python3 -m unittest tests/test_h19_k23_adaptive_multiscale_audit.py -q。
它会重建逐素数首成功尺度、因子分解、平方尾除子和严格提升的完整 JSON 记录。
