# SP-22：ordinary \(q=1,G\) 的 scope-bound phase-root actual edge

**状态：** ESTABLISHED。  
**量词保持：** 对每个满足本文谓词并由签名 root initializer 实际准入的 \(q=1,G\) source。  
**基准提交：** `e6e9e4a8c41b90a330b9ef333e542c18c2cb7be4`。

本命题不把一个有限 witness 集冒充原命题。\(p=21169\) 是完整正向 trace；全称结论由统一公式证明。

## 1. source domain 与 selector

令

\[
p=24t+1\text{ 为素数},\qquad X=6t+1,
\]

并假设 \(X\) 的每个素因子均为 \(1\pmod3\)。source 是外部 coordinator 准入的 parentless ordinary \(q=1,G\) root，方程接口为 \(4/p\)，势为

\[
\Pi(S)=(p,3,0,0,0,0,0).
\]

冻结 source policy 依次为 gaps \(3,7,11,15,19,23\) 的完整 Bradford terminal actions，index 6 phase-root producer，以及明确 later 的 gap 31 terminal。全部 registered terminal overlap 均被签名 manifest 穷尽分类；policy 无 reject。

每个 source terminal 完整枚举有限的 \(x^2\) divisors，返回可靠 HIT 或 MISS。若 prior M23 中存在 HIT，最早 HIT terminal 抢占。本文只需处理六项全 MISS 的分支。

## 2. actual E1 与 scope clearance

root initializer 从 \(p\) 重算域谓词、\(t,X\)、factorization、owner/domain、lineage 和 `arithmetic/q=1` occurrence，构造规范 source wire 和 content-addressed state ID。actual-source receipt 绑定外部签名 statement、policy digest、root admission contract 和 source wire。

六项全 MISS 时，independent prefix replayer 产生唯一 receipt：

\[
\mathsf{semantic}=\mathsf{MISS\_HIGHER\_PRIORITY\_POLICY\_COMPLETE},
\]

\[
\mathsf{coverage}=\mathsf{REGISTERED\_HIGHER\_PRIORITY\_ONLY},\qquad
\mathsf{global\_exhaustion}=\mathrm{false}.
\]

records 恰覆盖 0--5，逐项绑定同一 source、policy 和 action contract。producer guard 在该分支核验 actual/admitted/domain source、ordinary \(q=1,G\)、owner/domain 和完整 clearance，故对每个到达 index 6 的合法 source 都为 TRUE。

## 3. E2：统一且唯一的 projection

producer 不接受 caller 提供的 \(R,K,A\) 或 tie-break，仅计算

\[
R=16t+3,\qquad K=X(16t+1),\qquad A=1.
\]

展开得

\[
4K=4(6t+1)(16t+1)=(24t+1)(16t+3)+1=pR+1.
\]

由于域内 \(t\ge1\)，有 \(3\le R\le p-2\)，并且 \(K>0\)。因此 projection 在每个 source 上存在且唯一。

## 4. target-local terminal policy

source prior actions 仅依赖 \(p\)。target 在不同 subject ID 下重放相同 M23 actions，所以六项仍 MISS；source records 不被复制成 target records。

随后检查 anchor-sink \(R-1\mid K\)。令 \(M=R-1=16t+2\)。

\[
\gcd(M,16t+1)=1,
\]

且

\[
\gcd(M,X)\mid 3M-8X=-2.
\]

\(X\) 为奇数，所以 \(\gcd(M,X)=1\)，进而 \(\gcd(M,K)=1\)。因 \(M>1\)，\(M\nmid K\)。故 target terminal policy 对所有到达 producer 的域内 source 都注册前缀 MISS；该 receipt 同样不声称 global exhaustion。

## 5. E3：无环 common admission

构造顺序为

\[
S\to C_S\to P\to\{C,L,D\}\to A_e\to Q\to O\to B\to U\to R_e.
\]

其中 \(P\) 是 pure projection；\(C\) 是非授权 preclassification；\(L\) 是 target-bound terminal receipt；\(D\) 是 potential draft；\(A_e\) 是只绑定上游对象的 edge anchor；\(Q\) 是 semantic prestate；\(O\) 是 state ID 之后由 common classifier 重算的 owner；\(B\) 是 E1--E5/R bundle；\(U\) 是 admission sidecar 与 queue ingress；\(R_e\) 是 consume/re-entry receipt。

\(Q\) 的 state-ID preimage 不含 owner、bundle 或 admission，故不存在 bundle hash 回写 target 或 sidecar 自引用。common classifier 唯一选择 `type_i_full_carrier_post_g` owner 和注册 route。common admission 在 producer 外重算 target ID、owner、terminal receipt、edge bundle 和 authority 后才允许唯一 pilot queue writer。

## 6. E4：全称 lift

source 与 target 的规范 equation object 都是

\[
\{\mathsf{numerator}:4,\mathsf{denominator}:p\}.
\]

令 \(\Lambda\) 为正整数三元组上的恒等映射。则直接由相同解谓词得到

\[
\forall u\in\mathsf{Sol}(T),\qquad
\Lambda(u)=u\in\mathsf{Sol}(S).
\]

该证明与 source 是否还存在其他 terminal 解无关。

## 7. E5：固定势严格下降

semantic target 势为

\[
\Pi(T)=\left(p,2,4,\frac{(p-1)^2}{4},K,0,0\right).
\]

与

\[
\Pi(S)=(p,3,0,0,0,0,0)
\]

按固定字典序比较：第一坐标相同，第二坐标 \(2<3\)。因此

\[
\Pi(T)<_{\mathrm{lex}}\Pi(S),
\]

并统一签发 `PHASE_DROP`。后续大坐标不影响该结论。

## 8. R：实际 re-entry

owner registry 固定 `route_type_i_full_carrier_post_g_v1` 与
`body_type_i_full_carrier_post_g_v1`。common admission 将通过的 final envelope 写入本 pilot 的唯一 persistent ingress。同一 runtime 随后消费该 envelope，重新核验 route 与 state binding，并产生

`ENTERED_TYPE_I_FULL_CARRIER_POST_G_BODY`。

receipt 明确 `self_edge_emitted=false`、`queue_write_during_reentry=false` 和 queue 已消费。因此 target 实际回到同一 selector system 的注册 body，而非停在 analysis-only JSON。

## 9. 全称 selector 结果

对任意域内 actual source：若 M23 有 HIT，最早 terminal action 决定；否则 index 6 guard 必为 TRUE，而第 3--8 节统一建立 E1--E5/R。故

\[
\boxed{
\forall S\in D_{q=1,G}^{\mathrm{actual}},\quad
\mathsf{Selector}(S)=\mathsf{Terminal}
\ \lor\ 
\mathsf{VerifiedSuccessor}(S,T).}
\]

无 reject 或 fallthrough。这闭合 SP-22 原量词中的 actual scoped edge/local totality，而不依赖 complete global terminal MISS。

## 10. 正向 trace 与 later-terminal 负控

对

\[
p=21169,\quad t=882,\quad X=5293=67\cdot79,
\]

M23 六项均 MISS，index 6 得

\[
R=14115,\qquad K=74700109,
\]

并实际完成 E1--E5/R、common admission、唯一 queue ingress 与 re-entry。

index 7 gap 31 的独立 analysis replay 同时给出

\[
\frac4{21169}=
\frac1{5300}+\frac1{3619899}+\frac1{19185464700}.
\]

所以 M23 receipt 只能是 scope clearance。later certificate 存在不否定 identity lift，也不改变冻结 priority。

作为额外回归，两个独立实现对 \(p<100000\) 的 606 个域内 source 得到完全相同的决定分布；successor roots 为
\(21169,61681,67369,87481,94441,99961\)。这不是全称证明的逻辑前提。

## 11. 独立验证和状态边界

independent replayer 只使用标准库，采用不同的除数生成算法；它可对任意域内 source 独立重建 prefix decision，并对 \(p=21169\) 重建完整 edge、admission、queue trace、re-entry 和所有 seals。测试拒绝 policy/order/overlap/authority/artifact/source/path/branch/owner/T5/global-MISS/queue mutations。

因此 SP-22 为 `ESTABLISHED`。未证明：post-G body totality、所有 producer 的 production common admission/no-bypass、F1 global source coverage、F2/F3 residual totality、T6 和 Erdős--Straus 猜想。
