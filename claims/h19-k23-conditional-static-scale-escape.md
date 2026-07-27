---
kind: claim
claim_id: h19-k23-conditional-static-scale-escape
title: H19-k23 十四条残存进程的条件性静态尺度共同逃逸
statement: 对 H19-k23 经统一仿射叶子削减后保留的每一条14个进程，H19 的20条私有余因子型与37个静态外部来源 k|1800 或 k=23 的私有余因子型合计57条，均为正本原仿射型且无覆盖素数；H19 射线和每个来源的完整平方尾目标均为空。故在 Dickson 素数元组猜想或 Schinzel 假设下，每条进程都条件性地含有无穷多个实际素数，同时逃过 H19 与全部37个静态来源的完整平方尾严格递降。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- external-source
- adaptive-scale
- admissibility
- conditional-boundary
- obstruction
- proof-program
sources:
- paper: chamberland2026
  locator: Theorem 1
  role: affine-prime-cofactor-context
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19-k23 十四条残存进程的条件性静态尺度共同逃逸

## 有限前提

令 \(\mathcal K=\{k:k\mid1800\}\cup\{23\}\)，故 \(|\mathcal K|=37\)。当前 14 条
H19-k23 残存进程均为本原素数型 \(p(t)=Pt+C\)。对每条进程：

1. H19 贡献 \(p(t)\) 及 19 条射线私有余因子型，共 20 条；
2. 每个 \(k\in\mathcal K\) 的来源
   \[
   n_k(t)=F_kN_k(t)
   \]
   贡献一条私有余因子型 \(N_k(t)\)，共 37 条；
3. 57 条正本原仿射型的有限域覆盖集为空；
4. H19 的完整射线因子检查为空，且每个来源的完整平方尾目标
   \[
   -M_k\notin\Pi_{4k-1}(M_k^2),\qquad M_k=kn_k,
   \]
   在“私有余因子 \(N_k\) 为素数”的完整因子模型中均失败。

第 4 点不是只检查了固定除子。若 \(N_k\) 为充分大的新素数，则 \(M_k=kF_kN_k\) 的
全部平方除子恰由固定部分的除子与 \(N_k^0,N_k^1,N_k^2\) 组成；程序枚举的残数支撑
因此就是全部 \(\Pi_{4k-1}(M_k^2)\)。

## 条件性推论

由第 3 点，57 条型构成可采纳的仿射素数元组。假定 Dickson 素数元组猜想，或相应的
Schinzel 假设，则对每一条残存进程存在无穷多个充分大的参数 \(t\)，使这 57 条型同时为
素数。对这些 \(t\)：

\[
\text{H19 的 19 条射线全部失败，}
\qquad
\text{所有 }k\in\mathcal K\text{ 的完整平方尾外部源递降全部失败}. \tag{1}
\]

这不是 Erdős--Straus 猜想的条件性反例。它只否定一个方法性希望：不能把当前 37 个
静态来源与 H19 固定扇的有限样本成功外推成全称闭合。

## 与有限审计的关系

[有限自适应尺度审计](h19-k23-adaptive-multiscale-audit.md) 在前 1,024 个参数层的
2,687 个实际素数上均找到首成功尺度，且最大为 15；本条说明这一现象在逻辑上不能推出
固定尺度定理。两者合起来给出正确的研究约束：

\[
\text{必须让尺度、来源状态或证书族随参数的非固定信息更新。}
\]

下一步不应继续证明某个固定 \(\mathcal K\) 的覆盖，而应寻找把共同失败转化为新尺度、
新证书或可提升标记状态的桥接机制。

重建命令为 python3 reproductions/h19_k23_conditional_static_scale_escape.py 和
python3 -m unittest tests/test_h19_k23_conditional_static_scale_escape.py -q。
