---
kind: claim
claim_id: type-II-moving-window-adaptive-one-private-prime-conditional-escape
title: 直接 Type II 移动窗口的一私有素因子状态可条件性延展至 51
statement: 从 p=153633769 的前 37 窗口一私有素因子可采纳状态出发，逐次对新增缺口 m=151,155,...,203 选择 p 的残数并剥离局部覆盖素数，得到 52 条原始且可采纳的线性式 p(k),L_1(k),...,L_51(k)。若它们同时为素数，则每个 x_j=(p(k)+4j-1)/4 都等于固定因子 E_j 乘 L_j(k)，且全部 j<=51 的 Type II 目标均不在 x_j^2 的除子残数集内。因此 Dickson/Schinzel 假设条件下存在无穷多个核心素数逃过直接 Type II 的前 51 个窗口位置。
claim_status: computationally_reproduced
topics:
- type-II
- moving-window
- adaptive-search
- conditional-boundary
- prime-tuples
- divisor-residues
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
- paper: grynkiewicz_marchan_ordaz2009
  locator: subsequence-product framework
  role: divisor-product-set-language
visibility: public
last_checked: '2026-07-25'
---

# 直接 Type II 移动窗口的一私有素因子状态可条件性延展至 51

## 状态扩展

`type-II-moving-window-one-private-prime-conditional-escape` 给出一个前 37 位置的
可采纳状态。对一个状态

\[
p(k)=Ak+B,\qquad
x_j(k)=E_jL_j(k), \tag{1}
\]

若要加入新位置 \(j\)，其缺口为 \(m=4j-1\)。把参数限制为

\[
k=mu+c,\qquad0\le c<m. \tag{2}
\]

于是新的素数形式是

\[
p(u)=(Am)u+(Ac+B), \tag{3}
\]

且每个旧位置与新位置的固定因子、私有线性余因子都可以重新精确计算。若这些线性式
在某个小素数上根集覆盖整个有限域，再对该素数作一次 (2) 型分裂；如果没有覆盖素数，
则该状态是 Dickson/Schinzel 可采纳的。

对 \(j=38,\ldots,51\) 按升序选择第一个可行残数，得到 14 次扩展。其中只有首次
\(m=151\) 需要额外的模 2 分裂：

\[
\begin{array}{c|c|c|c}
j&m&c&\text{额外分裂}\\
\hline
38&151&1&(2,0)\\
39&155&0&\varnothing\\
40&159&1&\varnothing\\
41\le j\le51&4j-1&0&\varnothing
\end{array} \tag{4}
\]

最终输出的 \(p,L_1,\ldots,L_{51}\) 共 52 条线性式均原始、两两不同，并在所有
\(\ell\le52\) 上没有根覆盖；故这是完整的局部可采纳性检查。

## 条件性推论

对最终状态，脚本逐项验证

\[
-x_j\notin\Pi_{4j-1}(E_j^2L_j^2)
\qquad(1\le j\le51). \tag{5}
\]

假定 Dickson 素数元组猜想，或这 52 条线性式的 Schinzel 假设 H，则有无穷多个
参数值使 \(p,L_1,\ldots,L_{51}\) 同时为素数。对充分大的参数，\(L_j\) 不与
\(E_j\) 共享素因子，故 (5) 是完整的 Type II 失败条件。于是得到无穷多个核心素数
同时逃过前 51 个直接移动窗口位置。

运行

    python3 reproductions/type_ii_moving_window_adaptive_escape.py \
      --seed-prime 153633769 --target-window 51 --max-depth 8 \
      --output reproductions/type-ii-moving-window-adaptive-escape-p153633769-j51-results.json

可复现全部状态、因子残数和线性式。

## 当前搜索边界

沿 (4) 的确定性首选状态，加入 \(j=52\)、\(m=207\) 后，全部 207 个参数残数
都在第 52 位置命中一私有素因子模型的 Type II 目标。更强地，这个闭合不依赖模型：
`type-II-gap-207-progression-certificate` 证明整个初始进程都由
\(d=47x/9682\) 在缺口 207 直接捕获。运行

    python3 reproductions/type_ii_moving_window_adaptive_escape.py \
      --target-window 52 --max-depth 20 \
      --output reproductions/type-ii-moving-window-adaptive-escape-p153633769-j52-depth20-results.json

这里的显式证书覆盖从前 37 起始进程导出的全部细分状态；它不证明其它初始窗口
状态都在 \(j=52\) 闭合，也不证明任意实际核心素数必在第 52 个位置有 Type II
证书。

## 对主问题的含义

前 37 的固定窗口已存在条件性逃逸；允许新增缺口后的同一模型还能延展至前 51。
所以“多加几个固定移位必然封闭”的直觉没有目前证据支持。可行的正向命题必须显式处理
整个残数状态树：证明每个分支在有限步内给出证书，或从未封闭的分支构造一个独立的、
严格更小的带标记递降状态。

这不是 Erdős--Straus 猜想的条件性反例。逃逸素数仍可能在第 52 个或更大缺口、其它
Type II 正规形、Type I 分支或其它分解中获得解。
