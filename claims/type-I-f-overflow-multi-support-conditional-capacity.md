---
kind: claim
claim_id: type-I-f-overflow-multi-support-conditional-capacity
title: 分色 F 状态的多支持盒溢出条件性容量边界
statement: 对冻结的 291 个分色 F 状态，半径六以内找到 253 个目标仿射格见证，并按两个载体方向的确定性规则形成 506 个联合支持组。基准多支持需求没有超载且 410 组饱和；若把每个溢出坐标的超额层数都计入其选定载体的联合高度需求，则 504 组超载，最大需求/容量比为 8400。该映射假设尚未证明，因此这是条件性压力边界，不是选择器定理。
claim_status: conditional
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-active-support-boundary
  - type-I-f-full-cross-color-pair-capacity-boundary
  - type-I-f-bounded-fourier-certificate
topics:
- type-I
- F-state
- relation-lattice
- overflow-radius
- multi-support
- q-adic
- colored-capacity
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# 分色 F 状态的多支持盒溢出条件性容量边界

## 输入与范围

本审计读取校正后的完整 Fourier 谱、双颜色共享模数容量和活跃/非活跃溢出边界，
分别固定以下输入哈希：

```text
Fourier: b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d
cross:   c99ee379e61aef20b1dbbcdffb1a2b2f532fa8b8697308cdf32ac45b31608cb5
support: 93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1
```

输入包含 291 个无法由同色双方向容量直接闭合的分色 F 状态。溢出见证只在扩张指数盒
半径不超过 6 的范围内搜索；未找到见证的状态不被解释为不存在见证。

## 多支持模型

对每个找到的见证，令 \(e_q\) 为其坐标超出原始指数预算的层数。规范 Fourier 活跃
素数 \(q_a,q_s\) 保留在指定的 \(a/s\) 颜色；其余有 \(e_q>0\) 的素数按

\[
v_q(aR+1)\mathrel{\ge}v_q(sR+1)
\]

的确定性规则分配给 \(a\) 颜色，严格较小的一侧分配给 \(s\) 颜色，平局分配给 \(a\)。
这只定义一个可复现的应力模型，并没有证明该分配与真实提升或递降保持一致。

对支持集合 \(A,S\)，基准需求取活跃方向的已知需求与非活跃支持的单位基线之积：

\[
D_0=\prod_{q\in A}d_q\prod_{q\in S}d_q.
\]

条件性溢出需求把每个超额层数加到对应支持因子：

\[
D_{\mathrm{ov}}
=\prod_{q\in A}(d_q+e_q)\prod_{q\in S}(d_q+e_q).
\]

容量是在同一核心素数的完整线性源状态和对应 \(R\) 窗口中计算的精确联合载体和：

\[
C(A,S)=\sum_{(a,R,s)}
\prod_{q\in A}v_q(aR+1)
\prod_{q\in S}v_q(sR+1).
\]

## 结果

```text
unresolved_record_count: 291
support_record_count: 253
assignment_count: 506
group_count: 506

base capacity:     overloads 0, maximum ratio 1, saturation 410
overflow capacity: overloads 504, maximum ratio 8400, saturation 2
```

因此，在这个条件模型中，非活跃溢出支持并非只增加载体种类；它会把已经恰好饱和的
联合账本推入超载区。结果支持下一条理论桥应同时保留活跃方向、非活跃溢出坐标和坐标
间迁移成本，而不是把所有几何缺陷压缩到规范双活跃对。

## 逻辑边界

上述超载不能直接推出跨状态矛盾，原因有四：

1. 尚未证明指数盒外的超额层数必须消耗同一载体块的 \(q\)-进高度；
2. 非活跃素数的确定性颜色分配不一定是所有合法提升/递降的唯一分配；
3. 38 个状态没有在半径六以内找到见证，不能作为反例或无穷远缺陷证明；
4. 需求模型只使用超额层数，没有证明其与 Fourier 相位质量、目标表示纤维或提升代价
   的精确对应。

所以本卡的严格结论仅是：在明确列出的溢出收费假设下，多支持容量足以造成 504/506
组超载；真正的未解问题是证明一个不依赖任意颜色选择的溢出—高度或溢出—下降映射。

## 复现

```bash
python3 reproductions/type_i_f_overflow_multi_support_capacity.py
```

结果文件：

```text
reproductions/type-i-f-overflow-multi-support-capacity-results.json
```

结果文件 SHA-256：

```text
789ac393d328225044c07ad6a5eb99188eaaafe4184edee0b4f0660c7199b580
```
