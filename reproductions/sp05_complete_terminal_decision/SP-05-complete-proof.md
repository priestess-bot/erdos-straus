# SP-05：完整 terminal 分支定理、phase-root 后继证明与首条活动边不可闭合定理

## 结论与状态

本文件给出三个彼此分离的结论。

1. **完整 terminal 判定定理已经闭合。** 对每个固定正整数 `p`，存在一个有限、确定、可独立重放的 schedule，命中当且仅当
   \[
   \operatorname{Sol}(4,p)=\left\{(x,y,z)\in\mathbb N_{>0}^3:
   \frac4p=\frac1x+\frac1y+\frac1z\right\}
   \]
   非空；其 MISS 因而是真正的 `MISS_COMPLETE`。
2. **条件性 phase-root 分支定理已经闭合。** 给定一个由仓库外部信任根验证的 exact-HEAD、已准入且 actual 的 ordinary `q=1,G` source，以及 independently replayed `MISS_COMPLETE`，冻结 projection 唯一产生一个满足 E1--E5 和 re-entry 语义的 phase-root target。这里闭合的是条件定理；本独立包不签发 source actualness、registry grant、admission 或 queue authority。
3. **“首条现实非终止活动边”仍不能标为 ESTABLISHED。** 在上述完整 terminal 语义下，现实非终止边存在，当且仅当 ordinary `q=1,G` 域中存在一个 Erdős--Straus 反例，并且该 source 已取得 actual/admission authority。当前没有这样的 witness。本证明因此不能诚实地把仓库中的 SP-05 从 `OPEN_PROPOSITION` 改为“已有首条活动边”。

本包固定审阅基线为公开仓库 commit

```text
7dff8a9e7338814e83ab839c33b8b58c28f4ea0d
```

但该 commit 仅作为 repository-compatibility 审计基线；以下数学证明不把代码执行结果作为前提。

---

## 0. 规范编码、类型和拒绝语义

所有可重放 wire 都是有限 JSON 值。允许的叶类型只有 `null`、布尔值、字符串和有符号整数；需要整数的字段必须满足 `type(v) is int`，因此布尔值不能冒充整数。数组保序；对象键必须是字符串且不得重复。

规范字节编码固定为

```text
json.dumps(
    value,
    sort_keys=True,
    separators=(",", ":"),
    ensure_ascii=True,
    allow_nan=False,
).encode("ascii")
```

seal 为

\[
\operatorname{Seal}(w)
= w\cup\{\texttt{digest}=\operatorname{SHA256}(\operatorname{Canon}(w))\}.
\]

state ID 和 projection ID 均是带类型前缀的 canonical SHA-256；不同 artifact type 不共享 ID namespace。任何字段集变化、source/target subject swap、数组重排或非规范数值都会改变 seal。

本包使用以下代数数据类型：

```text
TerminalCertificate =
  {certificate_kind, denominators:[x,y,z], equation_interface:{4,p}, ...}

PrefixResult =
  HIT(TerminalCertificate)
  | MISS_REGISTERED_PRIORITY_COMPLETE(transcript_summary)

GlobalResult =
  HIT(TerminalCertificate, x, reduced_residual, factor_pair)
  | MISS_COMPLETE(x_bounds, exhaustive_counts, coverage_identity)

CompleteTerminalDecision =
  {subject_binding, schedule_id, prefix_result, global_result,
   anchor_result, outcome, certificate, coverage_theorem_id, digest}

SelectorResult =
  TERMINAL(source_or_target_bound_certificate)
  | CONDITIONAL_SUCCESSOR_MODEL(projection, E1--E5, reentry)
  | REJECT(code)
```

`CompleteTerminalDecision` 的 source 与 target 版本使用不同 `schedule_id`、`subject_kind`、subject ID 和 digest；target 版本另含 projection binding。完整字段合同见 `TYPE-CONTRACTS.md`，执行实现见 `sp05_constructor.py`，不导入 constructor 的重放实现见 `sp05_independent_replayer.py`。

所有算法在其声明的合法有限整数域上都是总的：它们返回 `HIT`、`MISS_COMPLETE` 或稳定拒绝码。非法输入、无法验证的 authority、字段不一致和 seal 不一致一律返回 `REJECT`；不得降级为 MISS，也不得构造 target。

尤其，本独立包没有外部 Git trust-anchor resolver，也不拥有 V5/V6 issuer 权限。它可以验证 source wire 的静态绑定形状，但必须拒绝任何试图由本包自身授予 actualness 的 receipt，包括字段完整、seal 正确且 digest 非零的伪造 receipt。actualness 在条件定理中是外部已验证前提，不是本包可制造的布尔值。

---

## 1. 数学对象

令

\[
p=24t+1
\]

为素数，且

\[
X=6t+1=\frac{p+3}{4}.
\]

称其为 ordinary `q=1,G`，若 distinguished integer 为 `q=1`，并且 `X` 的每个素因子都同余 `1 mod 3`。

source 和 phase-root target 的 equation interface 都定义为

\[
\mathsf{Eq}_p:\qquad \frac4p,
\]

解集为

\[
\mathsf{Sol}_p=
\left\{(x,y,z)\in\mathbb N_{>0}^3:
4xyz=p(xy+xz+yz)\right\}.
\]

对任意三元组可以排序而不改变方程，故 terminal 完备性只需覆盖

\[
x\le y\le z.
\]

---

## 2. 六层 registered-prefix

固定

\[
\mathcal M_{23}=\{3,7,11,15,19,23\}.
\]

对每个 `m` 令

\[
x_m=\frac{p+m}{4}.
\]

按 `m` 的上述顺序、`d|x_m^2` 的数值递增顺序、Type-I-before-Type-II 检查

\[
\operatorname{TypeI}(p,m,d)
\iff m\mid px_m+d,
\]

\[
\operatorname{TypeII}(p,m,d)
\iff d\le x_m\ \land\ m\mid x_m+d.
\]

### 2.1 Type-I soundness

Type-I 命中时定义

\[
y=\frac{px+d}{m},
\qquad
z=\frac{px(px+d)}{md},
\qquad x=x_m.
\]

因 `p>m` 且 `4x-m=p` 为素数，

\[
\gcd(m,x)=1.
\]

由 `d|x^2` 得 `gcd(m,d)=1`。又因 `my=px+d`，

\[
mxy=px^2+dx
\]

被 `d` 整除，故 `d|xy`，从而 `z=pxy/d` 为正整数。并且

\[
\frac1y+\frac1z
=
\frac{m}{px+d}+
\frac{md}{px(px+d)}
=
\frac m{px}.
\]

又

\[
\frac4p-\frac1x
=
\frac{4x-p}{px}
=
\frac m{px},
\]

所以 Type-I 证书满足 terminal 方程。

### 2.2 Type-II soundness

Type-II 命中时定义

\[
y=\frac{p(x+d)}m,
\qquad
z=\frac{px(x+d)}{md}.
\]

令 `h=(x+d)/m`。则 `y=ph`，且

\[
mxh=x^2+dx
\]

被 `d` 整除。由 `gcd(m,d)=1` 得 `d|xh`，所以 `z=pxh/d` 为正整数。并且

\[
\frac1y+\frac1z
=
\frac m{p(x+d)}+
\frac{md}{px(x+d)}
=
\frac m{px}.
\]

因此 Type-II 证书同样满足 terminal 方程。

这证明了六层 schedule 每个 HIT 的 soundness；它尚未证明六层 MISS 是全 terminal 宇宙 MISS。

---

## 3. 全局有限 terminal schedule

六层 MISS 后运行下述全局 fallback。

### 3.1 最小分母的有限界

任取排序解 `x<=y<=z`。因为后两项为正，

\[
\frac4p>\frac1x,
\]

故

\[
x>\frac p4.
\]

另一方面，`1/y<=1/x` 且 `1/z<=1/x`，所以

\[
\frac4p
=\frac1x+\frac1y+\frac1z
\le\frac3x,
\]

从而

\[
x\le\frac{3p}{4}.
\]

因此只需枚举有限区间

\[
\boxed{
\left\lfloor\frac p4\right\rfloor+1
\le x\le
\left\lfloor\frac{3p}{4}\right\rfloor.}
\]

### 3.2 固定 `x` 的因子对双射

固定该区间中的 `x`，将 residual 约分为

\[
\frac4p-\frac1x
=
\frac{4x-p}{px}
=
\frac ab,
\qquad
\gcd(a,b)=1,
\quad a,b>0.
\]

方程

\[
\frac ab=\frac1y+\frac1z
\]

等价于

\[
ayz=b(y+z).
\]

于是

\[
\begin{aligned}
(ay-b)(az-b)
&=a^2yz-ab(y+z)+b^2\\
&=b^2.
\end{aligned}
\]

对任意正解，`a/b>1/y` 且 `a/b>1/z`，所以

\[
ay-b>0,
\qquad
az-b>0.
\]

令

\[
d=ay-b,
\qquad e=az-b.
\]

则

\[
de=b^2,
\qquad d\le e,
\qquad d\equiv e\equiv-b\pmod a,
\]

并且

\[
y=\frac{b+d}{a},
\qquad
z=\frac{b+e}{a}.
\]

反过来，任取正因子对

\[
de=b^2,
\qquad d\le e,
\]

若

\[
a\mid b+d,
\qquad a\mid b+e,
\]

并且重建出的整数满足

\[
x\le y\le z,
\]

则展开 `(ay-b)(az-b)=b^2` 可逆地得到

\[
\frac ab=\frac1y+\frac1z,
\]

故得到一个排序 terminal 解。

因此固定 `x` 时，排序解与满足上述同余和顺序条件的 `b^2` 正因子对一一对应。

### 3.3 可终止性和完备性

每个固定 `x` 的 `b` 是正整数，`b^2` 的正因子集合有限；`x` 的区间也有限。故下列算法必停：

1. 按递增顺序枚举所有允许的 `x`；
2. 计算约分后的 `(a,b)`；
3. 按递增 `d` 枚举所有 `d|b^2` 且 `d<=b`，令 `e=b^2/d`；
4. 检查两个同余、整数性和 `x<=y<=z`；
5. 首个 HIT 交叉乘法验证 terminal 方程并立即返回；
6. 全部穷尽才返回 `MISS_COMPLETE`。

soundness 已由因子恒等式证明；completeness 由第 3.1 节的 `x` 有限界和第 3.2 节的双射证明。因此

\[
\boxed{
\operatorname{CompleteSchedule}(p)=\operatorname{HIT}
\iff
\mathsf{Sol}_p\ne\varnothing.}
\]

以及

\[
\boxed{
\operatorname{CompleteSchedule}(p)=\mathsf{MISS\_COMPLETE}
\iff
\mathsf{Sol}_p=\varnothing.}
\]

该结论不依赖 Erdős--Straus 猜想为真或为假；它只是对每个固定输入给出有限决定过程。

---

## 4. 完整 terminal-first 顺序

source schedule 固定为：

```text
M23_REGISTERED_PREFIX
then GLOBAL_SORTED_FACTOR_PAIR_EXHAUSTION
```

任一六层 HIT 在全局 fallback 之前返回；六层 MISS 仅允许进入 fallback。全局 HIT 在 projection 之前返回。只有全局穷尽才签发 `MISS_COMPLETE`。

因此 producer permission 必须满足

\[
\operatorname{Edge}(S,T)
\Longrightarrow
\operatorname{CompleteSchedule}(p(S))=\
\mathsf{MISS\_COMPLETE}.
\]

反之，任何 terminal HIT 都排除 edge：

\[
\operatorname{CompleteSchedule}(p(S))=
\operatorname{HIT}(c)
\Longrightarrow
\neg\exists T\,\operatorname{Edge}(S,T).
\]

这比非排他的外层析取

\[
\operatorname{Terminal}(S)\lor\exists T\operatorname{Edge}(S,T)
\]

严格更强，并准确表达 terminal-preemption。

### 4.1 `p=21169` 控制

\[
p=21169=24\cdot882+1,
\qquad
X=5293=67\cdot79,
\]

且 `67,79` 均为 `1 mod 3`。六层 prefix 共出现 `102` 个 divisor positions 和 `204` 个 Type-I/II 有序检查，全部 MISS。

但 `m=31,d=1` 时

\[
x=\frac{21169+31}{4}=5300,
\qquad 31\mid5301,
\]

故 Type-II 给出

\[
(x,y,z)=
(5300,3619899,19185464700)
\]

以及

\[
\frac4{21169}
=
\frac1{5300}
+
\frac1{3619899}
+
\frac1{19185464700}.
\]

全局因子对 fallback 在 `x=5300` 重建同一证书。因此该 input 必须 terminal-preempt；它绝不能成为 phase-root edge witness。

---

## 5. E1：actual source 的精确义务

E1 不能由 `p` 重建。完整 source authority 输入必须至少绑定：

```text
head_sha
source_state_id
source_wire_digest
V5 admission receipt id/digest
V6 actual-source/rebind receipt id/digest
producer_id
branch_id
occurrence_path = ["facts", "relation_q"]
occurrence_value = 1
complete source terminal decision id/digest
source_terminal_result = MISS_COMPLETE
```

验证顺序是：

1. 解析完整 source wire；
2. 重算 canonical state ID 和 wire digest；
3. 重放 admission/lineage receipts；
4. 从 source wire 的实际路径读取整数 `1`；
5. 重放完整 terminal schedule；
6. 将相同 source ID/digest 绑定到 branch、producer、occurrence 和 terminal decision。

actualness 是 selector 的输入门；它先于 terminal issuance，但 terminal HIT 仍先于任何 projection 或 target construction。

本包中的 `make_reference_root_state` 只生成字段形状控制，并显式标记为

```text
REFERENCE_FIXTURE_NOT_REPOSITORY_AUTHORITY
```

独立重放器必须拒绝用该 fixture 签发 E1 或 edge。

---

## 6. E2：唯一 phase-root projection

在 `MISS_COMPLETE` 分支定义

\[
R=16t+3,
\qquad
K=X(16t+1).
\]

直接计算

\[
\begin{aligned}
4K
&=4(6t+1)(16t+1)\\
&=384t^2+88t+4,
\end{aligned}
\]

而

\[
\begin{aligned}
pR+1
&=(24t+1)(16t+3)+1\\
&=384t^2+88t+4.
\end{aligned}
\]

所以

\[
\boxed{4K=pR+1.}
\]

`t=(p-1)/24` 和 `X=6t+1` 均由 `p` 唯一确定；projector 不接收 `R,K` 或 tie-break 参数，所以 target payload 唯一。

若同时使用当前 low full-carrier constraints `X|K`、`R≡3 mod 4`、`3<=R<=p-2`，唯一性也可内生推出。由 `p=4X-3` 和 `4K=pR+1`，模 `X` 得

\[
3R\equiv1\pmod X.
\]

冻结 `R=16t+3` 满足 `3R-1=8X`。任何另一解 `R'` 同时满足 `R'≡R mod X` 和 `R'≡R mod4`；因 `X` 为奇数，

\[
R'\equiv R\pmod{4X}.
\]

允许区间宽度小于 `4X`，故 `R'=R`，再由 chart equation 得 `K'=K`。

---

## 7. target terminal replay

target 必须在 target subject 下重新执行完整 p-only schedule；它不能复制 source transcript。固定顺序为：

```text
independent p-only complete schedule
then phase-root anchor-sink
```

若 p-only replay HIT，anchor 为 `NOT_REACHED`。只有 p-only `MISS_COMPLETE` 后才检查 anchor。

令

\[
M=R-1=16t+2.
\]

有

\[
\gcd(M,16t+1)=1.
\]

又

\[
\gcd(M,X)\mid3M-8X=-2.
\]

`X` 为奇数，所以该 gcd 也是奇数，只能等于 `1`。故

\[
\gcd(M,K)
=
\gcd(M,X(16t+1))
=1.
\]

且 `M>1`，所以

\[
R-1\nmid K.
\]

anchor 恒 MISS。

若在一般 target 中 anchor 命中，令 `a=K/(R-1)`，则

\[
\frac1a+\frac1K+\frac1{pK}
=
\frac{R-1}{K}+\frac1K+\frac1{pK}
=
\frac{pR+1}{pK}
=
\frac4p.
\]

因此任何未来 anchor HIT 都必须作为 target-bound certificate 经 identity lift 返回 source terminal；不能接受后继。

---

## 8. E3：canonical target typing 与对象边界

canonical target facts 为：

```text
major_phase=TYPEI
type_i_protocol=CHARGED
t5_eta_p=0
endpoint_fiber=NONE
relation_q=null
provenance_kind=FULL_CARRIER_POST_G
full_carrier_scope=true
is_overflow=false
support_A=1
chart_R=16t+3
chart_K=X(16t+1)
```

其余 V1 facts 取冻结的 `null/0/NONE/false` 值。冻结 family predicates 的唯一 match 是

```text
type_i_full_carrier_post_g
```

且 precedence index 为 `14`。因此目标语义的 schema、normal form 和 common owner 唯一。

但当前 V1 wire 存在对象依赖环：raw successor ID 已哈希一个声称 E1--E5 为真的 source receipt，而 independently replayable bundle 又需要 target ID 和 final owner digest。因此 current-HEAD 中只能诚实地产生 non-authorizing prestate，不能把它直接称为 admitted V1 successor。

完整 admission 必须使用无环顺序：

```text
P  canonical projection
C  predicate preclassification
L  complete target terminal decision
D  target T5 coordinates
A  edge anchor
Q  target prestate semantic ID
O  final owner receipt
B  independently replayed E1--E5 bundle
U  admission/re-entry sidecar
```

所有引用只从左向右。`Q` 不携带 owner、bundle、ticket 或 queue authority；`U` 只有在 `O` 和 `B` 全部重放成功后才授予 persistent admission。最终 selector state 是不可变 semantic prestate `Q` 与 verified sidecar `U` 的规范组合。该结构消除了 content-ID cycle，并使 common predicate/owner verifier仍从原始 integers 重算。

这一步是 current repository 所需的合同扩展。没有该 extension 或等价的 verified wrapper，E3 authority 不能从数学事实自动产生。

---

## 9. E4：全称 identity lift

source 和 target 的 equation interface 都是同一 `ROOT_SOL(4,p)`。定义

\[
\Lambda_{S,T}:\mathsf{Sol}(T)\to\mathsf{Sol}(S),
\qquad
\Lambda_{S,T}(x,y,z)=(x,y,z).
\]

任取 `u=(x,y,z) in Sol(T)`，则

\[
4xyz=p(xy+xz+yz).
\]

source 使用同一个 `p` 和同一个 equation interface，所以同一等式表明 `u in Sol(S)`。因此

\[
\forall u\in\mathsf{Sol}(T),
\qquad
\Lambda_{S,T}(u)\in\mathsf{Sol}(S).
\]

该证明不选取某个未知解；即使解集为空，映射仍是唯一的空域恒等限制。

---

## 10. E5：冻结 T5 `PHASE_DROP`

使用当前冻结七元势，而不是自定义控制 rank：

\[
\Pi_{T5}(S)
=(p,3,0,0,0,0,0),
\]

\[
\Pi_{T5}(T)
=
\left(
 p,
 2,
 4,
 \frac{(p-1)^2}{4},
 K,
 0,
 0
\right).
\]

第一坐标相同，第二坐标满足

\[
2<3.
\]

所以

\[
\boxed{
\Pi_{T5}(T)<_{\mathrm{lex}}\Pi_{T5}(S).}
\]

首个下降坐标是 major phase，ticket 固定为

```text
PHASE_DROP
```

比较对象是 actual parent 与完成 terminal replay、owner classification、bundle verification 和 admission 的 final target；不得与 provisional `P/C/L/D/A/Q` 中间对象比较。

---

## 11. R：同一 selector 的 re-entry

re-entry registration 固定消费 owner

```text
type_i_full_carrier_post_g
```

并使用同一 `t6_selector`。re-entry verifier执行：

1. 验证 target semantic state 与 admission sidecar；
2. 重算 common owner；
3. 重放 target-bound complete terminal decision；
4. 验证 anchor MISS；
5. 进入 Type-I full-carrier body。

其输出是

```text
PHASE_BODY_ENTERED
```

而不是一条 `T->T` self-edge。故不会伪造另一张 T5 ticket，也不会产生递降循环。只要上述 admission extension 已注册，target 属于同一 selector 的持久域并可被再次消费。

---

## 12. 唯一性

给定同一个 actual source `S` 和同一个 complete-miss receipt：

1. `p,t,X` 由 source 唯一；
2. `R,K` 由冻结公式唯一；
3. target facts 是固定函数；
4. canonical encoding/content IDs 是确定函数；
5. family match singleton 和 owner digest 唯一；
6. source/target complete decisions 是固定有序算法的唯一输出；
7. T5 coordinates 和 `PHASE_DROP` 唯一；
8. admission/re-entry sidecars由固定输入的 canonical seal 唯一。

因此若 edge branch 可达，则 final target 唯一。

---

## 13. 负控

独立 replayer 必须拒绝：

| 控制 | 拒绝理由 |
|---|---|
| 把 source terminal decision 当作 target decision | subject kind、subject ID 和 projection digest 不同 |
| source swap | parent/source state ID、wire digest、actualness receipts 不一致 |
| q-path swap | occurrence path 不是 `["facts","relation_q"]` |
| projection tie-break swap | 重算值不等于 `R=16t+3,K=X(16t+1)` |
| 把六层 MISS 改名为 `MISS_COMPLETE` | 全局 factor-pair replay 重建遗漏 terminal 或证明未穷尽 |
| T5 taxonomy drift | 坐标不等于冻结向量或 ticket 不是 `PHASE_DROP` |
| owner/re-entry swap | target owner 不在注册的 source owner 集合 |
| reference fixture 冒充 actual source | authority class 和 V5/V6 receipt digests 不成立 |

本包的两套实现不互相调用后继构造结论：constructor 以完整因子分解生成 divisor lattice；independent replayer 使用不同的素数筛分/因子生成路径并从 raw wires 重建 expected decisions。

---

## 14. 分支总定理

设 `S` 是 exact-HEAD admitted actual ordinary `q=1,G` source，并且 source wire 中实际存在 `q=1` occurrence。则完整 selector 有且只有以下互斥输出之一：

### Terminal 分支

若

\[
\operatorname{CompleteSchedule}(p(S))=
\operatorname{HIT}(c),
\]

则 `c` 是有效 terminal certificate，且

\[
\neg\exists T\,\operatorname{Edge}(S,T).
\]

### Successor 分支

若

\[
\operatorname{CompleteSchedule}(p(S))=
\mathsf{MISS\_COMPLETE},
\]

并且 exact-HEAD complete-schedule、E1--E5、admission 和 re-entry authority 已注册，则存在唯一 final target `T`，满足 E1--E5 与 R。

证明：E1 由 actual source binding 和 complete-miss binding；E2 由第 6 节；target terminal clearance 由第 7 节；E3 由第 8 节的 canonical facts、singleton owner 和无环 admission；E4 由第 9 节；E5 由第 10 节；R 由第 11 节；唯一性由第 12 节。证毕。

---

## 15. 首条非终止边与 Erdős--Straus 反例的等价性

由第 3 节完整性，

\[
\operatorname{CompleteSchedule}(p)=\mathsf{MISS\_COMPLETE}
\iff
\mathsf{Sol}_p=\varnothing.
\]

terminal-first 又要求 edge 只能在 `MISS_COMPLETE` 后产生。因此：

\[
\exists\text{ actual nonterminal SP-05 edge at }p
\Longrightarrow
\mathsf{Sol}_p=\varnothing.
\]

右侧正是 `p` 为 Erdős--Straus 反例。反过来，若 ordinary `q=1,G` 域存在这样的反例，并且 source actualness、complete schedule、admission、T5 和 re-entry authority 均已注册，则第 14 节构造产生唯一非终止 phase-root edge。

故有精确等价：

\[
\boxed{
\begin{aligned}
&\text{存在一条现实 complete-terminal-first 的}\
&\text{ordinary }q=1,G\text{ 非终止 phase-root edge}
\end{aligned}
}
\]

\[
\boxed{
\iff
\begin{aligned}
&\text{ordinary }q=1,G\text{ 域存在 Erdős--Straus 反例，}\
&\text{且对应 actual/admission authority 已签发。}
\end{aligned}}
\]

这不是实现缺口，而是目标语义的逻辑后果。

因此，若 SP-05 的完成标准是“证明 branch 在 hypothetical complete miss 上正确”，本文件已经给出完整证明。若完成标准保持标题所写的“首条现实非终止活动边”，则在没有反例 witness 的情况下必须继续保持

```text
OPEN_PROPOSITION
```

不能通过把 registered-prefix MISS 重命名、跳过 gap-31 terminal、伪造 `MISS_COMPLETE`、或把 non-authorizing prestate 称为 persistent target 来改变这一结论。

---

## 16. 可执行核验

运行：

```bash
./run_all.sh
```

核验包括：

- constructor 与独立 direct-`y` scan 在所有素数 `p<=1000` 上逐例一致；
- `p=21169` 的 `204` 次六层检查全 MISS，随后重建 gap-31 terminal；
- 六个 M23 earliest-hit 控制；
- source 与 target subject 的独立 replay；
- projection、anchor gcd 和冻结 T5；
- fake `MISS_COMPLETE`、source swap、q-path swap、tie-break swap、T5 drift 和 re-entry owner 负控；
- reference source fixture 不能取得 actualness。

测试通过只验证实现与本文定义一致；第 2--15 节的数学论证才是证明。
