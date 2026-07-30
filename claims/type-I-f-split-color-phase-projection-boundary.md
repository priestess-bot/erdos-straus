---
kind: claim
claim_id: type-I-f-split-color-phase-projection-boundary
title: 分色 F 状态的二维 Fourier 目标投影边界
statement: 在冻结完整线性谱中，291 个无法同色承载两个方向的 F 状态全部具有二维规范 Fourier 活跃支撑；二维目标相位投影计数为 0、2、4 的状态数分别为 40、2、249。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-bounded-fourier-certificate
  - type-I-f-full-cross-color-pair-capacity-boundary
topics:
- type-I
- F-state
- finite-fourier
- phase-projection
- relation-lattice
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 分色 F 状态的二维 Fourier 目标投影边界

## 主张

在冻结完整线性谱中，无法用一个颜色块承载两个活跃方向的 291 个达标 F 状态，其规范
Fourier 活跃支撑全部为二维。直接在这两个坐标的有限指数盒中检查目标相位方程，得到：

\[
\begin{array}{c|ccc}
\text{二维相位兼容点数}&0&2&4\\ \hline
\text{状态数}&40&2&249
\end{array}
\]

其中 40 个状态的二维目标投影为空，因此对所选规范角色已经构成状态内的精确 F 型
空缺证书；其余 251 个状态虽然有少量相位兼容点，但这只是必要条件，不能推出目标
指数纤维命中。

## 口径

这是有限状态内的 Fourier 投影边界，不是跨状态容量矛盾。它说明分色容量的 291 个
记录中至少 40 个可以转入“相位空缺”分支；对剩余记录，需要组合第二个角色、完整
关系格或相位半径，才能把投影点进一步排除或转化为算术需求。

## 复现

```text
python3 reproductions/type_i_f_split_color_phase_projection.py
```

结果文件：

```text
reproductions/type-i-f-split-color-phase-projection-results.json
```
