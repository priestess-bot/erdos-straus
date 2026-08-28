# SP-22：ordinary q=1,G 的 scope-bound phase-root 实际 pilot

**状态：** OPEN_PROPOSITION
**优先级：** P1，首个真实 producer pilot。
**研究任务：** 在已冻结的 policy-relative terminal clearance 下，将一个 actual、
admitted ordinary \(q=1,G\) source 连接到 canonical full-carrier Type-I phase root，
并给出 current T5 contract 所需的 E1--E5 和 recursive re-entry。
**独立性：** 本文件重新定义 source、policy clearance、target、证书和验收量词；既有
receipt、实现或历史 q=1 控制只能作为待独立重放的候选，不能作为逻辑前提。

## 1. source 与 scope

设 \(p=24t+1\) 为素数，

\[
X=6t+1=\frac{p+3}{4},
\]

且 \(X\) 的每个素因子均为 \(1\pmod3\)。source \(S\) 是一个 actual、admitted、
parentless ordinary \(q=1,G\) root，必须带有：

1. 完整规范 source wire 与 state ID；
2. root initializer 或已验证 parent chain；
3. 明确 occurrence path，其值为 \(q=1\)；
4. owner/domain 绑定；
5. 一个冻结有限 policy \(\mathcal P\)；
6. 对所有早于 selected phase-root producer 的 policy actions 的 replay receipt。

最后一项只能产生 scope-bound clearance：

\[
\mathsf{MISS\_HIGHER\_PRIORITY\_POLICY\_COMPLETE},
\qquad
\mathsf{global\_exhaustion}=\mathrm{false}.
\]

它不是 \(\mathsf{MISS\_COMPLETE}\)。

## 2. canonical target

冻结投影不接收调用者给出的 \(R,K\) 或 tie-break：

\[
R=16t+3,\qquad K=X(16t+1).
\]

因此

\[
4K=pR+1.
\]

target 必须以 Type-I/CHARGED full-carrier normal form 重新编码，至少满足：

\[
A=1,\qquad
\mathsf{major\_phase}=\mathsf{TYPEI},\qquad
\mathsf{protocol}=\mathsf{CHARGED}.
\]

它还必须携带重新计算的 common owner、target terminal scope、state ID 和 admission
sidecar。raw projection、target preclassification、T5 draft 或 source-independent arithmetic
object 都不是 persistent target。

## 3. target policy 与 terminal preemption

target 在自己的 subject binding 下独立重放所有 policy-prior p-only terminal actions，
随后重放 phase-root anchor-sink：

\[
R-1\mid K.
\]

对 canonical target，

\[
\gcd(R-1,K)=1,
\]

所以 anchor-sink 为 MISS。但这一互素性不替代 target policy replay，也不允许复制 source
transcript。任一 target terminal HIT 都必须经

\[
\Lambda=\operatorname{id}:\mathsf{Sol}(T)\to\mathsf{Sol}(S)
\]

作为 source terminal 返回，而非接受 successor。

## 4. 待证明命题

对每个满足第 1 节的 source \(S\)，证明 selector 在这个 policy position 恰有一个合法结果：

1. 若 earlier policy terminal action 命中，则输出 \(\mathsf{Terminal}(S)\)；
2. 若 \(\operatorname{PriorClear}_{\mathcal P}(S)\) 成立且 phase-root guard 为真，
   则存在唯一 target \(T\) 及 \(\mathsf{Edge}(S,T)\)。

第二项中的 edge 必须逐项满足：

1. **E1：** source ID、actual lineage、\(q=1\) occurrence path、policy digest、
   complete prior-action trace 和 selected branch 绑定在同一个 source；
2. **E2：** 从 source 的 \(p,t,X\) 唯一重算 \(R,K\) 和 target；
3. **E3：** target 以无环顺序完成 schema、normal form、common owner、admission 和
   target policy receipt；
4. **E4：** 对所有 \(u\in\mathsf{Sol}(T)\)，\(\Lambda(u)=u\in\mathsf{Sol}(S)\)；
5. **E5：** 从当前冻结 T5 evaluator 重算

\[
\Pi(S)=(p,3,0,0,0,0,0),
\qquad
\Pi(T)=\left(p,2,4,\frac{(p-1)^2}{4},K,0,0\right),
\]

   并签发 PHASE_DROP；
6. **R：** final admitted target 经同一 selector 的 owner route 重新进入
   full-carrier Type-I body，而不是形成 \(T\to T\) 自环。

## 5. 无环对象顺序

为避免 target state ID、owner digest、E1--E5 bundle 与 admission sidecar 的循环，构造
必须按如下单向依赖完成：

\[
\text{actual source}
\to\text{policy clearance}
\to P
\to\{C,L,D\}
\to A
\to Q
\to O
\to B
\to U.
\]

其中 \(P\) 是纯 projection，\(C\) 是 predicate preclassification，\(L\) 是 target
policy replay，\(D\) 是 T5 coordinates，\(A\) 是 edge anchor，\(Q\) 是无 owner 的
semantic prestate，\(O\) 是 final owner receipt，\(B\) 是独立 E1--E5 bundle，\(U\)
是 admission/re-entry sidecar。任何倒向引用、把 bundle hash 写入 \(Q\)、或把 producer
self-report 写入 owner 均必须拒绝。

## 6. 必须保留的控制

1. \(p=12721,1201,2521\) 等 M23 prefix HIT 必须在 selected producer 前 terminal；
2. \(p=21169\) 的 M23 MISS 加 gap-31 HIT 必须保持
   global_exhaustion=false，不得制造 MISS_COMPLETE；
3. source/target transcript subject swap 必须失败；
4. q-path swap、projection tie-break swap、policy order swap、owner swap、
   target state-ID/bundle cycle 和 T5 drift 必须失败；
5. 一个 self-sealed source fixture 或 caller-provided authority boolean 不得成为 E1；
6. target re-entry 只能进入注册 owner route，不能借 queue append 或 self-edge 伪造。

## 7. 完成证据

本命题从 OPEN_PROPOSITION 改为 ESTABLISHED 前，必须交付：

* 由外部信任根绑定的 actual source receipt；
* 固定 policy registry 与 independent prior-action replayer；
* source/target 分离的 scope-bound terminal decision；
* source-ID-bound E1、E2、common E3、universal E4、frozen E5 和 R receipts；
* 无环 state/owner/bundle/admission serialization；
* independent end-to-end replayer 与上述负控；
* 一个真实 admitted source 的 terminal 或 verified-edge execution trace。

本命题不要求 global terminal-universe MISS；它也不证明 post-G Type-I body totality、
F1 global constructor coverage、F2/F3 residual closure、T6 或 Erdős--Straus 猜想。
