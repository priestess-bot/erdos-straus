# 本证明包明确没有闭合的边界

## 1. 非平凡 marked terminal membership

当前 ordinary theorem 使用

\[
W=\operatorname{Sol}(p).
\]

如果输入状态携带更窄的

\[
W_{p,\theta}\subsetneq\operatorname{Sol}(p),
\]

不能默认现有 `v1` root-entry 仍合法。只有当 mark 可以在 fresh tree 中逐字重新序列化时，identity-lift 论证才可迁移。

这与旗舰 T3 Marked-Terminal 仍然不同。

## 2. T5 Global-Well-Foundedness

本文 E5 使用一个单向 phase prefix：

\[
2\to1.
\]

它证明 handoff 本身不会回到 Type II nonterminal phase，但没有构造覆盖仓库**全部** recursive edge 的统一序数/词典序势。

所以 T5 仍开放。

## 3. T6 Global-Selector

进入 Type I 后，不能由“已经有 fresh source”推出“必有 terminal 或 strict successor”。

本包只关闭 q=1 专属的一段 tree；其后的普通 Type I state 仍需要全局 selector。

## 4. `c=8, q_*=103`

`47fedc2` 的后续 q=1 image 研究已经把某些 reachable residual 压到特殊 capacity 层，包括

\[
c=8,
\qquad q_*=103.
\]

但已有实际控制表明：

> 存在 non-`p` actual raw prime，并不自动意味着 capacity 下降。

因此不能用

\[
q\ne p\Longrightarrow c'<c
\]

作为下一定理。

真正值得研究的是：

\[
\boxed{
\forall H\in\mathcal I_{8,103},
\quad
\exists\text{ actual endpoint }:
\text{terminal}
\lor c_a<8
\lor c_\Sigma<8.
}
\]

它应当登记为 T6 的 `Q1-Image-Totality` 子命题。

## 5. 不应声称 ESC 已证明

本证明只证明一个 phase handoff 和它后的有限专属模块。逻辑上：

\[
\text{T4 closed}
\not\Rightarrow
\text{T6 closed}
\not\Rightarrow
\text{ESC proved}.
\]
