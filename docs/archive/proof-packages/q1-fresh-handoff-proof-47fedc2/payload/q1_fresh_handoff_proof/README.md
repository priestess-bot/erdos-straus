# q=1 Type II G → Type I Fresh-Source Handoff 证明包

基线仓库：`priestess-bot/erdos-straus`

冻结提交：`47fedc2` — **Archive H4 clean q relative closure**（2026-08-17）

本包针对旗舰方向 T4：

> 每个 ordinary `q=1 Type II G` endpoint 是否存在一个不复用 Type II 旧 source support、且不读取未知目标解的有限 fresh-source lineage，进入 Type I 或 terminal？

## 结论

本包证明以下两个层次。

### 定理 A：ordinary Fresh-G-Handoff 闭合

对每个 ordinary `q=1 Type II G` endpoint

\[
S=(p,q=1,G;W_S=\operatorname{Sol}(p)),\qquad p\equiv1\pmod{24},
\]

存在由 `p` 唯一决定的 low full-carrier Type I root

\[
X=\frac{p+3}{4}=6t+1,
\qquad
R_X=16t+3=\frac{8X+1}{3},
\qquad
K_X=X(16t+1),
\]

以及一个完全 fresh、target-independent 的实际 `p`-raw source

\[
(p,\ R_X(p-1)-p,\ p-1)\to(1,R_X-1,1).
\]

在声明的不可回返 phase policy 下，该 reindexing 逐项满足 E1--E5；E4 是
\(\operatorname{Sol}(p)\) 上的恒等映射，E5 是 phase `2 → 1` 的严格下降。

因此 **T4 的 ordinary 字面量词已经成立**。

### 定理 B：加强的“进入后立即严格推进”

上述 root 不会只是一个无支付的标签切换。它无条件具有第一条严格 Type I segment：

- `t` 奇：直接进入 low marked-absorb；
- `t` 偶：先出现闭式 overflow，再通过 fixed-`n` identity-lift 进入 low Type I chart。

因此每个 ordinary `q=1 G` endpoint 在至多两条 phase/persistent edge 后进入一个具有真正局部势下降的 Type I state。

## 本包没有证明什么

本包**不**声称：

1. Erdős--Straus 猜想已证明；
2. 一般 Type I selector 已全称闭合；
3. T5 Global-Well-Foundedness 已完成；
4. T6 Global-Selector 已完成；
5. 任意非平凡 marked solution set 都可直接用现有 `v1` root-entry；
6. handoff 后的 `c=8, q_*=103` Type I image 已全称终止。

这些边界详见 `docs/OPEN_BOUNDARIES.md`。

## 文件结构

```text
q1_fresh_handoff_proof/
├── README.md
├── PROOF.md
├── docs/
│   ├── PROPOSITION_LEDGER.md
│   ├── STATE_CONTRACT_E1_E5.md
│   ├── DOWNSTREAM_Q1_MODULE.md
│   ├── OPEN_BOUNDARIES.md
│   ├── UPSTREAM_MANIFEST.md
│   └── REPOSITORY_INTEGRATION_PROPOSAL.md
├── verification/
│   ├── common.py
│   ├── verify_symbolic.py
│   ├── verify_controls.py
│   ├── verify_counterexamples.py
│   ├── verify_state_contract.py
│   ├── verify_downstream_formulas.py
│   └── run_all.py
├── outputs/
│   └── verification_report.json
└── upstream/
    ├── claims/                 # 成功取得的 47fedc2 原始 claim 快照
    └── concepts/               # flagship 与 state-contract 原始快照
```

## 独立验证

从包根目录运行：

```bash
python3 verification/run_all.py
```

验证器只使用 Python 标准库与 `sympy`，不依赖原仓库内部 module。

验证分两类：

- `verify_symbolic.py`：用符号代数重算全部核心闭式恒等式；
- `verify_controls.py` / `verify_counterexamples.py`：对控制素数和有限扫描做独立 sanity check。

有限扫描**不是证明**；证明在 `PROOF.md` 中。程序的作用是发现代数笔误、符号分支错误和边界条件错误。

## 推荐仓库状态调整

基于本证明，建议将 T4 从“开放”改为：

> **ordinary relative closure established**：full-carrier fresh root-entry 与首个严格 Type I segment 已闭合；非平凡 marked handoff 和 global T5 admission 单独保留。

详见 `docs/REPOSITORY_INTEGRATION_PROPOSAL.md`。
