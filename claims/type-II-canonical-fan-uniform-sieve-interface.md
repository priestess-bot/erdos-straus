---
kind: claim
claim_id: type-II-canonical-fan-uniform-sieve-interface
title: 规范移位扇具有显式模数与横截面熵界
statement: 对前 H 条平方自由规范 Type II 移位 s=1,...,H，写 s=a_s^2c_s、M_s=4a_sc_s。则 M_s|4s，故 Q_H=lcm(24,{M_s}) 整除 lcm(1,...,4H)，特别 log Q_H<=4H log(4H)。每条失败射线的半大小横截面选择至多有 2^(phi(M_s)/2) 种，整扇的选择数至多 2^(H(H+1))。这些显式界把固定扇筛法的模数与组合成本控制为 H 的函数，是研究增长规范移位选择器的统一筛法接口；它们本身不推出逐点覆盖。
claim_status: established
topics:
- type-II
- canonicalization
- sieve
- modulus
- combinatorics
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: Appendix A, shifted-prime sieve methodology
  role: uniform-sieve-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 规范移位扇具有显式模数与横截面熵界

## 规范扇

对每个 $1\le s\le H$，唯一写成

\[
s=a_s^2c_s,
\]

其中 $c_s$ 平方自由，并定义该移位的规范 Type II 模数

\[
M_s=4a_sc_s. \tag{1}
\]

因为

\[
4s=4a_s^2c_s=a_sM_s, \tag{2}
\]

有 $M_s\mid4s$。令

\[
Q_H=\operatorname{lcm}\left(24,\{M_s:1\le s\le H\}\right). \tag{3}
\]

当 $H\ge2$，24 整除 $\operatorname{lcm}(1,\ldots,4H)$，再由 (2) 得

\[
Q_H\mid\operatorname{lcm}(1,\ldots,4H). \tag{4}
\]

使用 $\operatorname{lcm}(1,\ldots,n)\le n!$，得到完全初等的显式界

\[
\log Q_H\le4H\log(4H). \tag{5}
\]

这与一般任取有限 $(A,C)$ 集合不同：这里总模数的增长不需要从参数盒逐项估计，
而是直接由移位上界控制。

## 横截面选择的组合界

对单条模数 $M_s$，Type II 射线失败时，其素因子残数可放进
$U(M_s)$ 的一个半大小横截面。对合配对给出横截面数量至多

\[
2^{\varphi(M_s)/2}. \tag{6}
\]

故前 $H$ 条射线的全部横截面系统数量至多

\[
2^{\frac12\sum_{s\le H}\varphi(M_s)}
\le2^{\frac12\sum_{s\le H}M_s}
\le2^{2\sum_{s\le H}s}
=2^{H(H+1)}. \tag{7}
\]

这不是关于失败模式的精确计数，而是可直接用于并集上界筛的统一组合成本。

## 精确样本

脚本计算的几个扇如下；总模数以十进制字符串保存，避免超过 JavaScript 安全整数后
丢失精度。

| $H$ | $Q_H$ | $\sum_{s\le H}\varphi(M_s)$ | 横截面 $\log_2$ 上界 |
|---:|---:|---:|---:|
| 14 | 240240 | 146 | 73 |
| 50 | 29514709564247587680 | 1518 | 759 |
| 100 | 110667262269384884388148903071924291360 | 6054 | 3027 |

```bash
python3 reproductions/type_ii_canonical_fan_geometry.py \
  --bounds 14 50 100 \
  --output reproductions/type-ii-canonical-fan-geometry-results.json
```

会逐项验证 (2)、(4) 并重建此表。

## 对增长选择器的意义

`type-II-ac-rays-superlog-residual` 对每个固定扇给出任意对数幂稀薄的失败集，但其
隐含常数未对扇大小统一。式 (5)--(7) 明确了针对前 $H$ 个**规范移位**统一化时必须
支付的两项成本：模数约为 $\exp(O(H\log H))$，横截面枚举至多
$\exp(O(H^2))$。

因此一个可检验的正向子目标是：在这些成本下建立对缓慢增长 $H=H(X)$ 仍有效的
上界筛，例如先处理 $H$ 为某个小的 $\log\log X$ 幂。这样的定理会给出
$\sigma(p)>H(X)$ 的定量密度界；它仍不自动排除所有例外点，也不替代真正的逐点
因子选择器。
