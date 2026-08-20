# 独立验证说明

## 1. 验证原则

本包刻意不 import `erdos-straus` 仓库的 reproduction module。

原因是：如果 claim 的生成实现和 verifier 使用完全相同的 helper/dispatch 代码，一个共同 bug 可能同时通过“生成”和“验证”。本包把核心算术重新写成最小 Python 实现，用作第二实现。

## 2. `verify_symbolic.py`

使用 `sympy` 重算：

- full-carrier root 的 `4K=pR+1`；
- uniqueness 所需 `3R_X=8X+1`；
- odd first child；
- even transient overflow 与 fixed-`n` child；
- odd second-anchor 闭式；
- 一般 fixed-`n` quotient-fold 恒等式；
- odd/even p-free gate 的 `j,n` 闭式；
- even regeneration 的 multiplier 恒等式。

这些是恒等式验证，不是数值抽样。

## 3. `verify_controls.py`

对仓库使用的控制素数：

```text
73, 241, 2521, 76129, 118801
```

独立重算：

- `q=1 G` 判别；
- root；
- low full-carrier 唯一性（直接穷尽整个 low `R` 区间）；
- fresh universal source；
- first strict child。

此外对 `p <= 200000` 的全部 core primes 做 sanity scan。运行结果：

- core primes：2212；
- q=1 G primes：1106；
- 所有 q=1 G control 均通过 root/source/first-child invariants。

该扫描仅用于发现实现错误；全称证明来自 `PROOF.md` 的代数论证。

## 4. `verify_counterexamples.py`

独立验证：

- `p=241` 为 double-G，否定 `q=1 G => R=3 non-G`；
- `p=2521` 仍为 double-G；
- 数个控制上旧 canonical root 的 `(X,K_old)=1`。

## 5. `verify_state_contract.py`

对多个 q=1 G controls 物化 source/target state，检查：

- E1 actual source；
- E2 deterministic root；
- E3 normal form；
- E4 `Sol(p)` identity；
- E5 phase lexicographic strictness。

## 6. `verify_downstream_formulas.py`

重新实现 complete-excess、canonical chart 与 fixed-`n` fold，检查：

- second anchor 强制 high overflow；
- odd/even carrier 选择；
- quotient fold；
- `delta != 1`；
- persistent `d=1` receiver；
- `p=193` 的 `q_*=23` regeneration control。

## 7. 如何运行

```bash
python3 verification/run_all.py
python3 -m unittest discover -s tests -v
```

成功后报告写入：

```text
outputs/verification_report.json
```
