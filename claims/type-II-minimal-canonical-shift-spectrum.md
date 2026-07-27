---
kind: claim
claim_id: type-II-minimal-canonical-shift-spectrum
title: 规范 Type II 首次成功移位在一亿内不超过五十二
statement: 对每个 p<=10^8、p=1 mod24 的素数，按 s=1,2,... 扫描平方自由规范 Type II 射线 s=a^2c，精确审计得到 719781 个核心素数均在 s<=52 命中。首次成功移位的记录保持者依次为 (p,s)=(73,1),(97,2),(193,8),(1009,9),(3361,29),(56401,31),(66529,50),(81846241,52)。这是有限最小移位谱，不能推出全局固定 52 覆盖；固定小扇已另有条件性逃逸边界。
claim_status: computationally_reproduced
topics:
- type-II
- canonicalization
- minimal-shift
- computation
- short-certificate
- proof-program
sources:
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# 规范 Type II 首次成功移位在一亿内不超过五十二

## 定义

对每个正整数 $s$，唯一写成

\[
s=a_s^2c_s,
\]

其中 $c_s$ 平方自由。对核心素数 $p$，定义首次成功规范移位

\[
\sigma(p)=\min\left\{s\ge1:
\exists h\mid p+4s,\quad h\equiv-1\pmod {4a_sc_s},
\quad\text{且该射线恢复合法 Type II 证书}\right\}. \tag{1}
\]

扫描会直接重建证书，因此 (1) 不是仅检查一个必要同余条件。

## 有限谱

在

\[
p\le10^8,\qquad p\equiv1\pmod {24},
\]

的 $719{,}781$ 个核心素数上，所有点均满足

\[
\sigma(p)\le52. \tag{2}
\]

当 $\sigma(p)$ 创下新记录时，得到：

| $p$ | $\sigma(p)$ | $(a_s,c_s)$ | $h$ | 缺口 $m$ |
|---:|---:|---:|---:|---:|
| 73 | 1 | (1,1) | 7 | 11 |
| 97 | 2 | (1,2) | 7 | 15 |
| 193 | 8 | (2,2) | 15 | 15 |
| 1009 | 9 | (3,1) | 11 | 95 |
| 3361 | 29 | (1,29) | 1159 | 3 |
| 56401 | 31 | (1,31) | 2975 | 19 |
| 66529 | 50 | (5,2) | 39 | 1711 |
| 81846241 | 52 | (2,13) | 60943 | 1343 |

特别地，前十四移位的共同失败点 $p=3361$ 并非 Type II 机制本身的困难点；
允许可变量移位后，$s=29$ 已给出缺口 3 的直接证书。

```bash
python3 reproductions/type_ii_minimal_canonical_shift.py \
  --limit 100000000 --shift-cap 100 \
  --output reproductions/type-ii-minimal-canonical-shift-100m-results.json
```

会生成完整的首次移位直方图、空遗漏表和每次记录更新的证书。

## 边界与方向

(2) 是有限计算，不是“$s\le52$ 对所有核心素数成立”的猜想或定理。事实上，
此前一千万范围的 \(50\) 在一亿内已被 \(p=81846241\) 的 \(52\) 推翻；
保持者可增长是必须解释的现象，而不是计算噪声。
`type-II-mod-three-recursive-escape-boundary` 已表明固定十四移位扇在标准素数元组假设下
会有无穷共同遗漏；其它固定有限扇是否有类似边界仍须分别证明，不能由此直接推断。

因此该谱的正确用途是研究**增长的**选择器，例如证明

\[
\sigma(p)\le (\log p)^C
\quad\text{或}\quad
\sigma(p)\le p^\varepsilon, \tag{3}
\]

而不是将有限记录外推为固定常数。若 (3) 的任一逐点界被证明，便会直接给出
可验证的 Type II 证书分支；当前仍缺少这种因子选择定理。
