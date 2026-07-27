---
kind: claim
claim_id: type-II-pure-new-factor-boundary
title: H19 新因子状态的纯新因子选择边界
statement: 在 p<=3*10^8、s<=200 的260个 H19 新因子状态中，253个存在不含碰撞因子的单新素因子 Type II 证书，最迟s=200；但 p=345601,9744001,55722241,92421169,178400041,192369241,283163161 在该完整窗口中均没有此类证书。故不能把单新因子选择器在该范围内强化为纯新因子选择器。
claim_status: computationally_reproduced
topics:
- type-II
- multishift
- factorization
- new-factor
- collision-factor
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# H19 新因子状态的纯新因子选择边界

## 强化尝试

在 [H19 后单新因子 Type II 选择器猜想](type-II-one-new-factor-selector-conjecture.md)
中，令碰撞平滑因子 \(e=1\) 会得到一个更强的纯新因子版本：要求某个新素数 \(q\) 自己
满足

\[
q\mid p+4a^2c,\qquad q\equiv-1\pmod{4ac}. \tag{1}
\]

这张卡审计该强化版本，而不把有限失败误写为永久反例。

## 三亿结果

对三亿深度谱的全部 260 个新因子状态，完整扫描每个 \(20\le s\le200\) 的所有 Type II
除子。253 个点最终有 (1) 的证书，最大首次移位为

\[
p=258{,}662{,}881,\qquad s=200. \tag{2}
\]

但下列六点在窗口内全部失败：

\[
345{,}601, 9{,}744{,}001, 55{,}722{,}241, 92{,}421{,}169,
178{,}400{,}041, 192{,}369{,}241, 283{,}163{,}161. \tag{3}
\]

它们仍有含碰撞因子的单新因子 Type II 证书；失败的只是要求 \(e=1\) 的强化。

## 含义

有限数据支持“一个新素因子加碰撞平滑因子”的选择器，却反对把碰撞部分消去。因而下一
条正向引理必须处理 \(e\) 的乘法残数，至少不能预设 \(e=1\)。这与一般共享因子积集的
边界一致，但把它定位到 H19 后的单新因子状态。

该窗口失败不证明 (1) 对六点永远失败，也不否定更大的状态依赖深度；它仅排除在当前
审计范围内用纯新素因子替换完整 \(eq\) 选择器的做法。

## 重建

    python3 reproductions/type_ii_pure_new_factor_release.py
    python3 -m unittest tests/test_type_ii_pure_new_factor_release.py -q
