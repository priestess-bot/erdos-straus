# 自包含性核对记录

**核对日期：** 2026-08-28（第二次逐文件复查）
**核对对象：** 本目录的 SP-*.md 命题文件和 manifest.json

## 判定规则

一个命题文件只有同时满足下列条件，才被标为“结构上可独立交付”：

1. 文件明确写出独立性声明；
2. 文件内给出研究对象、变量、域、方程和特殊术语的定义；
3. 文件内有明确的待证明命题和量词；
4. 文件内列出已知局部事实时，说明它们必须在独立证明中重建，或把它们作为显式假设；
5. 文件内列出 E1--E5/R 时，说明每一项的含义；
6. 文件内列出反例控制和完成证据；
7. 文件不把外部路径、版本记录、测试、状态标签或其他 SP-*.md 作为逻辑前提。
8. 所有 specialized 内部名称要么删除，要么在同一文件定义为数学对象、有限关系或
   待构造映射。

## 结果

| 检查项 | 结果 |
|---|---|
| 命题文件数 | 22 |
| manifest 条目数 | 22 |
| 独立性声明 | 22/22 |
| 命题定义/证明义务段落 | 22/22 |
| 完成证据段落 | 22/22 |
| 外部路径作为前提 | 0 |
| proposition-to-proposition 隐式引用 | 0 |
| F1/F2/F3/T6/R1--R6/QC1/TR1 等项目标签作为命题前提 | 0 |
| 未定义的 constructor/runtime 依赖 | 0 |
| 未定义的 specialized 路线名称 | 0；构造型 dossier 均把映射纳入存在量词 |
| 外部状态修改 | 0 |
| SP-02 状态 | ESTABLISHED（条件有限模型） |
| SP-04 状态 | ESTABLISHED（六层 registered-prefix） |
| SP-05 状态 | OPEN_PROPOSITION（complete-terminal boundary 已复验） |
| SP-21 / SP-22 状态 | SP-21 abstract theorem ESTABLISHED、concrete instance OPEN；SP-22 OPEN |
| OPEN_PROPOSITION 总数 | 20 |

SP-02 的状态已更新为 ESTABLISHED，因为其 dossier 现包含完整的条件证明、
形式化 tie-break/StateChangeRegistry 修订、独立标准库 verifier
(reproductions/sp02_constructor_source_completeness.py) 和聚焦测试
(tests/test_sp02_constructor_source_completeness.py)。该状态仅适用于显式有限且良构的
抽象模型；它不证明当前仓库 concrete constructor census 的闭世界、selector totality 或
source fidelity，因此不改变 U-A0-01/U-A0-02/U-A0-03/U-A0-08、F1 或 T6 的状态。
实际命令输出与控制码见 SP-02-VERIFICATION.md。
SP-04 的完整包复验、transcript 对比和 precedence 变异结果见
reproductions/sp04_q1_m23/verification_report.txt。
SP-05 的完整 terminal 决策、完整 MISS 与反例的等价边界，以及对 actual edge 仍未闭合的
原因，见 reproductions/sp05_complete_terminal_decision/SP-05-complete-proof.md。
SP-21 的 canonical abstract safety proof 与原始提交归档分别见
SP-21-ABSTRACT-SAFETY-PROOF-2026-08-29.md 和
docs/archive/proof-submissions/2026-08-29/。

## 重要解释

“独立”表示证明者可以把单个文件复制到一个没有任何项目历史的干净环境中，并根据文件内
的定义、假设和交付条件开始证明；它不表示命题已经成立，也不表示文件内列出的
specialized arithmetic facts 已经被本目录证明。凡写成“同一证明的子命题”或“待构造
映射”的段落，都属于该 dossier 自己的证明任务，不是外部前提。若要将命题状态从
OPEN_PROPOSITION 改成 ESTABLISHED，必须在同一 dossier 中补上证明，或把该事实明确
升级为待证子命题。

## 本次形式修正

第二次逐文件复查还修正了三类会妨碍独立证明的缺陷：

* SP-02 将 `UNKNOWN` 改为诊断算法的真实输出，而非从分类值域预先排除的符号；
* SP-07 把 \(q_\star=103\) 的素数最小性条件与额外的 \(25\nmid6s-1\) 5-adic gate
  明确分离；
* SP-17 将 \(v_5(T)\ge2\) 改写为对任意允许的 \(p\) 都正确的
  \(\varrho\equiv(p+1)(2p^2)^{-1}\pmod{25}\)，并把数值类 11 限定到
  \(p\equiv11,22\pmod{25}\) 的子域；
* SP-08 将无条件的 \(\gcd(P,N)=1\) 改为 \(\gcd(P,N)\mid11\)，并把互素性
  明确限定为 \(P\)-hard-core 条件的推论；
* 高根与 \(q=5\) 文件将“完整最大化正规化”改为本地逐素数公式：当
  \(\zeta_\ell\le v_\ell(K)\) 时取 \((v_\ell(D),v_\ell(E))=(\zeta_\ell,0)\)，
  否则取 \((v_\ell(A),\zeta_\ell-v_\ell(A))\)，并补出先前未绑定的整数变量。

这些是命题陈述的形式修正，不构成任何 OPEN_PROPOSITION 的证明。

## 不可替代的内容

本记录不能替代：

* F1 unknown 清零；
* F2/F3 residual 清零；
* actual E1、deterministic E2、common E3、universal E4、fixed E5 和 re-entry；
* complete terminal schedule；
* 独立 verifier；
* 任何外部工作流的状态升级。

它只证明本次整理的文件结构和依赖边界符合用户要求。
