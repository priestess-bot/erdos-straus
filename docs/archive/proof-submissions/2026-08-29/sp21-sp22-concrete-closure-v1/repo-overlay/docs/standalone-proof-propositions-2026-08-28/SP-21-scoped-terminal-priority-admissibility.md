# SP-21：scope-bound terminal-first 准入的健全性

**状态：** ESTABLISHED。  
**精确作用域：** 本文的冻结、外部签名 ordinary \(q=1,G\) policy domain。  
**基准提交：** `e6e9e4a8c41b90a330b9ef333e542c18c2cb7be4`。  
**非结论：** 本命题不建立 production-wide SP-03、F1、F2、F3、T6 或 Erdős--Straus 猜想。

本文同时给出抽象定理和一个真实执行的具体实例。外部文件只作为可复现证据；数学结论在本文内定义并证明。

## 1. 抽象策略定理

令 \(\mathscr S\) 为有限编码状态集合。每个状态 \(S\) 有方程接口 \(\mathsf{Eq}(S)\) 和解集
\(\mathsf{Sol}(S)\)。冻结有限策略

\[
\mathcal P=(A_0,\ldots,A_N)
\]

的动作仅有三类：terminal 返回 `HIT(c)` 或 `MISS`；producer 返回 `TRUE(T)` 或 `FALSE`；reject
返回稳定拒绝。动作顺序、predicate、版本、实现/证明标识、owner/domain 和 subject binding 都属于策略规范编码，动作本身无权改写策略。

对固定 \(S\)，\(r_i(S)=\operatorname{Replay}(A_i,S)\) 是终止且确定的。定义

\[
\operatorname{Pass}_i(S)\iff
\begin{cases}
r_i(S)=\mathsf{MISS},&A_i\text{ terminal},\\
r_i(S)=\mathsf{FALSE},&A_i\text{ producer},\\
\bot,&A_i\text{ reject}.
\end{cases}
\]

以及

\[
\operatorname{Reach}_{\mathcal P,j}(S)
\iff \forall i<j\;\operatorname{Pass}_i(S).
\]

合法 prefix receipt 必须恰好覆盖每个 prior terminal/producer index 一次，并把每条 record 绑定到同一个
source ID、完整 policy digest、index、action ID 和 action-contract digest。其唯一语义是

\[
\mathsf{MISS\_HIGHER\_PRIORITY\_POLICY\_COMPLETE},
\]

且强制

\[
\mathsf{coverage}=\mathsf{REGISTERED\_HIGHER\_PRIORITY\_ONLY},\qquad
\mathsf{global\_exhaustion}=\mathrm{false}.
\]

### 定理 1（有限前缀唯一分割）

顺序执行任意有限前缀时，恰有一个最小决定位置：最早 terminal HIT、最早 TRUE producer、最早 reject；若三者都不存在，则整个前缀 Pass。

**证明。** 对前缀长度归纳。长度 0 真空成立。若前 \(k\) 项已有最小决定位置，加入第 \(k\) 项不会改变它；若前 \(k\) 项全 Pass，确定的 \(r_k(S)\) 唯一落入 Pass 或三种决定输出之一。动作输出类型互斥，策略有限且 replay 终止，故结果存在且唯一。\(\square\)

### 定理 2（scope-bound terminal-first safety）

设 \(A_j\) 为 producer。若所有 prior action 可终止、确定地 replay，terminal HIT certificate 可靠，且 selected edge 独立满足 E1--E5/R 与

\[
\forall u\in\mathsf{Sol}(T),\quad \Lambda(u)\in\mathsf{Sol}(S),
\]

则：

\[
\operatorname{Reach}_{\mathcal P,i}(S)\land r_i(S)=\mathsf{HIT}(c)
\Longrightarrow c\in\mathsf{Sol}(S),
\]

以及

\[
\operatorname{Reach}_{\mathcal P,j}(S)\land r_j(S)=\mathsf{TRUE}(T)
\land\mathsf{EdgeOK}(S,T)
\Longrightarrow\mathsf{VerifiedSuccessor}(S,T).
\]

两种结果互斥。

**证明。** 定理 1 给出最小决定位置。terminal 情形由 certificate verifier 得
\(c\in\mathsf{Sol}(S)\)。producer 情形中，前缀到达性给出 selector 确实选择 \(j\)，E1--E5/R 和全称 lift 独立给出 successor soundness。若 earlier terminal 同时 HIT，则 clearance 要求同一个绑定 replay 为 MISS，违反确定性。\(\square\)

注意：含 earlier reject 的策略不能仅靠原始 terminal/producer clearance 到达 \(j\)。具体实例通过静态禁止 reject 消除这一缺口。

### 推论 3（不需要 global exhaustion）

上述证明只量化已注册 prior actions。它既不假设也不推出 \(\mathsf{Sol}(S)=\varnothing\)，不量化未注册 terminal families。未注册或明确 later 的 terminal 解可以存在；只要 edge lift 独立成立，它们不破坏 successor safety。

## 2. 具体可执行 source domain

签名域是所有满足下列可判定谓词的整数 \(p\)：

\[
p=24t+1\text{ 为素数},\qquad q=1,\qquad X=6t+1=\frac{p+3}{4},
\]

且 \(X\) 的每个素因子均为 \(1\pmod3\)。因 \(p=1\) 非素，域内必有 \(t\ge1\)。

外部 coordinator 授权 parentless root initializer。initializer 从 \(p\) 唯一重建 source wire：方程 \(4/p\)、\(q\) 的实际 occurrence path、owner/domain、root lineage、域谓词核验和势

\[
\Pi(S)=(p,3,0,0,0,0,0).
\]

state ID 是规范 source wire 的 SHA-256；actual-source receipt 同时绑定 source ID、policy digest、authority statement、initializer、root admission、owner/domain 和 occurrence。域不是有限 fixture，也不由 producer 列举 source IDs。

## 3. 冻结具体 policy

source policy 恰为：

| index | action | kind | coordinator relation |
|---:|---|---|---|
| 0 | Bradford gap 3 | terminal | PRIOR |
| 1 | Bradford gap 7 | terminal | PRIOR |
| 2 | Bradford gap 11 | terminal | PRIOR |
| 3 | Bradford gap 15 | terminal | PRIOR |
| 4 | Bradford gap 19 | terminal | PRIOR |
| 5 | Bradford gap 23 | terminal | PRIOR |
| 6 | canonical \(q=1\) phase-root | producer | SELECTED |
| 7 | Bradford gap 31 | terminal | LATER |

无 reject，且 index 6 之前无 producer。全部七个 terminal predicate 都是同一 source \(p\) 上的固定-gap、p-only predicate，故都与 producer domain 重叠。签名 overlap manifest 穷尽 registered terminal action IDs：indices 0--5 明确 PRIOR 且小于 6；index 7 明确 LATER 且大于 6；未分类数为 0。因此所有 coordinator-declared prior overlap 都确实位于 producer 前，所有不在前面的 registered overlap 都有明确 later 位置。

对本 policy：

\[
\operatorname{PriorClear}_{\mathcal P,6}(S)
\iff \operatorname{Reach}_{\mathcal P,6}(S).
\]

## 4. terminal replay 的完整性和可靠性

固定 \(g\equiv3\pmod4\)，令 \(x=(p+g)/4\)。action 完整枚举 \(x^2\) 的全部正因子 \(d\)，按 \(d\) 递增，并固定 Type I 先于 Type II。

Type I：

\[
g\mid px+d,\quad y=\frac{px+d}{g},\quad z=\frac{pxy}{d}.
\]

Type II：

\[
d\le x,\quad g\mid x+d,\quad y=\frac{p(x+d)}g,\quad z=\frac{xy}{d}.
\]

只有正整数候选且满足

\[
4xyz=p(xy+xz+yz)
\]

才返回 HIT。两类定义均直接推出

\[
\frac4p=\frac1x+\frac1y+\frac1z.
\]

除数集有限，故 replay 终止；排序和 tie-break 固定，故确定；最终整数恒等式验证保证 HIT soundness。constructor 用素因子指数笛卡尔积生成除数；independent replayer 用平方根扫描与互补除数生成同一集合，不导入 constructor 或 producer。

## 5. 外部 authority 与 artifact lock

离线 coordinator 使用 RSA-3072 PKCS#1 v1.5/SHA-256 签名规范 statement。签名覆盖：authority ID、基准 commit、policy payload digest、artifact-lock digest、`producer_may_mutate_policy=false` 和 `caller_authority_boolean_accepted=false`。

runtime 只固定受信公钥指纹，不含私钥或签名函数。artifact lock 固定 policy、selector、独立 replayer、测试、dossiers、账本和 reproduction 文档。任何动作重排、predicate/owner/branch/implementation 变更、replayer 变更或代码变更都会改变 lock 或 policy digest，使旧签名失效。producer API 不接受布尔 authority，也不能签发或修改 policy。

这是本研究 slice 的一次性外部 authority，不是 production T6 role grant。

## 6. actual source、receipt 与 independent prefix replayer

每个 replay record 绑定

\[
(\mathsf{sourceID},\mathsf{policyDigest},\mathsf{policyID},i,
 \mathsf{actionID},\mathsf{actionContractDigest}).
\]

clearance verifier 要求 records 恰为 indices 0--5、无缺失或重复、全部 MISS、subject/policy/action binding 一致。source swap、policy swap、branch swap 或 record splice 均改变 seal 并被拒绝。

独立 replayer 提供对任意域内 \(p\) 的 `independent_source_prefix_decision`：它从签名 policy 和 \(p\) 重建 actual source，独立执行 M23；最早 HIT 时返回 terminal，否则构造完整 scope receipt 并独立得到 index 6 `GUARD_TRUE`。该函数不导入、不调用 selected producer 或其 E1--E5/R verifier。端到端 replayer另行重建正向 edge evidence。

## 7. 全称局部 totality

对每个域内 actual source：

1. indices 0--5 各自是有限、确定、二值 `HIT/MISS` action；
2. 若存在 HIT，有限有序表存在唯一最早 HIT，selector terminal；
3. 若六项全 MISS，则 clearance 完整；
4. producer guard 只检查已经签名并由 receipt 建立的 actual/admitted/domain source、\(q=1,G\)、owner/domain 和完整 prior clearance，因此在该分支必为 TRUE；
5. policy 无 reject，producer 后无需 fallthrough；
6. 第 8--9 节给出对任意域内 \(p\) 的统一 E1--E5/R construction。

故

\[
\boxed{
\forall S\in D_{q=1,G}^{\mathrm{actual}},\quad
\mathsf{Selector}(S)\in
\{\mathsf{Terminal},\mathsf{VerifiedSuccessor}\}.}
\]

这是真正的 predicate-domain 局部 totality，不是有限样本归纳。

## 8. uniform producer edge

六项 prior MISS 后，producer 从 source 唯一计算

\[
R=16t+3,\qquad K=X(16t+1),\qquad A=1.
\]

展开得

\[
4K=(24t+1)(16t+3)+1=pR+1.
\]

且 \(t\ge1\) 给出 \(3\le R\le p-2\)。target 在新的 projection subject 下重放 M23。由于这些 action 仅依赖同一 \(p\)，其输出与 source prior replay 相同，故仍全 MISS。

随后 target-local anchor-sink 检查 \(R-1\mid K\)。令 \(M=R-1=16t+2\)。有

\[
\gcd(M,16t+1)=1,
\]

以及

\[
\gcd(M,X)\mid 3M-8X=-2.
\]

\(X=6t+1\) 为奇数，所以 \(\gcd(M,X)=1\)，从而 \(\gcd(M,K)=1\)。又 \(M>1\)，故 \(M\nmid K\)，anchor-sink 对所有域内 \(p\) 都 MISS。

## 9. E1--E5/R、common admission 与 re-entry

对任意到达 producer 的域内 source：

- **E1：** bundle 绑定外部 authority、actual source receipt、root lineage、实际 `arithmetic/q=1` occurrence、policy digest、完整 prior trace、clearance、index 6 与 guard record。
- **E2：** projector 只接收 source wire，按上述公式唯一产生 \(R,K,A\)，无 caller tie-break。
- **E3：** target semantic prestate 在 state-ID preimage 中不含 owner、bundle 或 admission；owner 在 state ID 后由签名 registry 的 common classifier 重算；target-bound terminal receipt、schema 和 route 均复核。
- **E4：** source 与 target 的 equation interface 都是同一规范对象 \(4/p\)，所以 \(\Lambda=\mathrm{id}\) 满足
  \[
  \forall u\in\mathsf{Sol}(T),\quad u\in\mathsf{Sol}(S).
  \]
- **E5：** target 势为
  \[
  \Pi(T)=\left(p,2,4,\frac{(p-1)^2}{4},K,0,0\right),
  \]
  与 \(\Pi(S)=(p,3,0,0,0,0,0)\) 比较时第二坐标严格下降，签发 `PHASE_DROP`。
- **R：** common classifier 唯一选择注册的 `type_i_full_carrier_post_g` route。common admission 复核全部对象后生成 token，经唯一 pilot queue ingress 写入；同一 runtime 消费 envelope 并返回 `ENTERED_TYPE_I_FULL_CARRIER_POST_G_BODY`，无 self-edge 或 re-entry write。

因此第 7 节所用 successor 是实际 admitted、实际 re-entered 的 verified successor。

pilot runtime 的 producer 无 queue 参数；静态 AST audit 将 ingress mutation 限定为一个 writer，动态 trace 证明正向执行只经过该 writer。此结论只覆盖本签名 producer；所有 producer 的 production-wide no-bypass 仍属于 SP-03。

## 10. 可复现证据和负控

回归 witnesses 包含 terminal 与 successor 两类执行：\(73,193,1201,2521,12721\) 被 prior terminals 抢占，\(21169\) 选择 producer。另有两个独立实现对 \(2\le p<100000\) 的全部 606 个域内根进行 bounded census，动作计数为：

\[
(0,475,83,11,16,15,6)
\]

对应 indices 0--6；六个 successor 为

\[
21169,61681,67369,87481,94441,99961.
\]

该 census 只是回归证据；全称结论来自第 7--9 节的结构证明。

对 \(p=21169\)，M23 全 MISS，producer 得

\[
t=882,\ X=5293=67\cdot79,\ R=14115,\ K=74700109.
\]

later gap 31 仍有 Type II、\(d=1\) certificate：

\[
\frac4{21169}=
\frac1{5300}+\frac1{3619899}+\frac1{19185464700}.
\]

因此 scope MISS 绝不能序列化为 `MISS_COMPLETE`，而 later certificate 的存在不破坏 E4。

测试必须拒绝：policy mutation、action reorder、overlap omission、authority-ID 或公钥替换、artifact mutation、source/q/branch/owner swap、mixed-policy records、later-terminal 伪 global MISS、target/bundle cycle、T5 drift、duplicate token、queue bypass 和 independent-replayer local import。

## 11. 结论和严格边界

六个原 concrete 缺口均在本签名 policy domain 内闭合：具体 policy、完整 priority/overlap partition、producer 外部 authority、actual source/lineage/policy receipt binding、独立 prefix/E2E replayer，以及每个域内 actual source 的局部 totality。

因此 SP-21 在该精确作用域为 `ESTABLISHED`。它不证明全局 terminal universe exhaustion，不把现有 production zero-authority runtime 变为有权 runtime，也不关闭 SP-03、F1/F2/F3/T6 或猜想。
