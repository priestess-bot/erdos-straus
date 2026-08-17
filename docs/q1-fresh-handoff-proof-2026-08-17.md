# ordinary `q=1 Type II G → Type I` Fresh-Source Handoff 的完整证明

## 0. 范围与逻辑目标

本文只证明下面的方向性定理，不证明 Erdős--Straus 猜想本身。

设

\[
\frac4p=\frac1x+\frac1y+\frac1z,
\qquad p\equiv1\pmod{24}
\]

的 proof program 已经从普通 Type II relation phase 到达 `q=1 G` endpoint。ordinary 状态的 marked set 是

\[
W_S=\operatorname{Sol}(p).
\]

需要构造一个**不复用旧 Type II physical source support**、**不读取未知目标解**的 deterministic fresh-source handoff 到合法 Type I state，并逐项满足 E1--E5。

下面证明的不仅是“存在一个 Type I 标签”，还证明该 root 后无条件发生第一条严格 Type I edge。

---

# 1. 主定理

## 定理 1（ordinary Fresh-G-Handoff）

令

\[
S=(p,q=1,G;W_S=\operatorname{Sol}(p))
\]

为 ordinary `q=1 Type II G` endpoint，其中

\[
p=24t+1
\]

为素数。定义

\[
X=\frac{p+3}{4}=6t+1,
\]

\[
R_X=16t+3=\frac{8X+1}{3},
\qquad
K_X=X(16t+1)=X(R_X-2).
\]

则存在唯一的 low Type I full-carrier chart

\[
T_X=(p,R_X,K_X;A=1),
\]

满足

\[
4K_X=pR_X+1,
\qquad
3\le R_X\le p-2,
\qquad
X\mid K_X.
\]

并且存在实际、预声明、仅依赖 `p` 的 fresh raw source

\[
(U_X,V_X,m_X)
=
\bigl(p,R_X(p-1)-p,p-1\bigr)
\]

以唯一 `p`-edge、shift `1`、无 gcd reduction 到达

\[
(1,R_X-1,1).
\]

若 root-entry 采用以下有向 phase policy：

\[
\operatorname{phase}(q=1G)=2,
\qquad
\operatorname{phase}(\text{fresh Type I})=1,
\qquad
\operatorname{phase}(n<p)=0,
\]

并禁止任何非终端 `1 → 2` 返回，则

\[
S\longrightarrow T_X
\]

逐项满足 E1--E5；其 solution lift 是

\[
\Phi_{T_X\to S}=\operatorname{id}_{\operatorname{Sol}(p)}.
\]

因此 ordinary T4 `Fresh-G-Handoff` 成立。

### 证明

分七步。

---

## 2. `q=1 G` 的精确输入语义

因为

\[
p=24t+1,
\qquad
X=\frac{p+3}{4}=6t+1,
\]

Type II 的 `q=1` endpoint 对应 gap

\[
m=3,
\qquad x=X.
\]

其 source group 是 `X` 的素因子在

\[
(\mathbb Z/3\mathbb Z)^\times=\{1,-1\}
\]

中的像所生成的群，目标为 `-1`。

因此：

\[
q=1\text{ endpoint 为 G}
\iff
\forall\ell\mid X,\ \ell\equiv1\pmod3.
\]

这个条件只说明 Type II `q=1` 的目标纤维为空。它**不**假设
\(\operatorname{Sol}(p)\) 已知非空，也不会为 Type I root 提供 physical source provenance。

这是后面必须使用 fresh source，而不能“继承旧 support”的原因。

---

# 3. full-carrier root 的存在

定义

\[
R_X=16t+3,
\qquad
K_X=(6t+1)(16t+1).
\]

直接计算：

\[
\begin{aligned}
pR_X+1
&=(24t+1)(16t+3)+1\\
&=384t^2+88t+4,
\end{aligned}
\]

而

\[
\begin{aligned}
4K_X
&=4(6t+1)(16t+1)\\
&=4(96t^2+22t+1)\\
&=384t^2+88t+4.
\end{aligned}
\]

所以

\[
\boxed{4K_X=pR_X+1.}
\]

又因核心素数要求 `t >= 3`，

\[
R_X=16t+3\ge3,
\]

且

\[
(p-2)-R_X
=(24t-1)-(16t+3)
=8t-4>0.
\]

故

\[
\boxed{3\le R_X\le p-2.}
\]

最后

\[
K_X=X(16t+1),
\]

所以

\[
\boxed{X\mid K_X.}
\]

因此 `(R_X,K_X)` 是合法 low Type I chart，而且完整承载 `X`。

---

# 4. full-carrier low chart 的唯一性

下面证明它不是从目标后向挑出来的任意图表，而是由 `p` 预先唯一决定。

设 `(R,K)` 为任意 low Type I chart：

\[
4K=pR+1,
\qquad
3\le R\le p-2,
\]

并假设

\[
X\mid K.
\]

则

\[
4X\mid4K=pR+1.
\]

注意

\[
p=4X-3.
\]

所以模 `4X` 有

\[
0\equiv pR+1
\equiv(4X-3)R+1
\equiv-3R+1,
\]

即

\[
\boxed{3R\equiv1\pmod{4X}.}
\]

另一方面，

\[
3R_X
=3(16t+3)
=48t+9
=8(6t+1)+1
=8X+1
\equiv1\pmod{4X}.
\]

又因为

\[
X=6t+1\equiv1\pmod3,
\]

所以

\[
(3,4X)=1.
\]

故所有解满足

\[
R\equiv R_X\pmod{4X}.
\]

low 区间为

\[
3\le R\le p-2=4X-5,
\]

其宽度严格小于 `4X`，因此至多包含一个该同余类代表。`R_X` 已经位于此区间，所以

\[
\boxed{
3\le R\le p-2,
\ X\mid K
\iff
(R,K)=(R_X,K_X).
}
\]

这证明了 target-independent uniqueness。

---

# 5. fresh universal `p`-source 的存在

定义

\[
U_X=p,
\qquad
V_X=R_X(p-1)-p,
\qquad
m_X=p-1.
\]

首先

\[
U_X+V_X
=p+R_X(p-1)-p
=R_X(p-1)
=R_Xm_X.
\]

其次 `V_X>0`。因为 `R_X >= 3`，

\[
V_X\ge3(p-1)-p=2p-3>0.
\]

再看互素性：

\[
\begin{aligned}
(U_X,V_X)
&=(p,R_X(p-1)-p)\\
&=(p,-R_X).
\end{aligned}
\]

因为

\[
0<R_X<p
\]

且 `p` 为素数，

\[
\boxed{(U_X,V_X)=1.}
\]

由

\[
4K_X=pR_X+1
\]

模 `p` 得

\[
4K_X\equiv1\pmod p,
\]

所以

\[
\boxed{p\nmid K_X.}
\]

因此 `q=p` 是合法 raw prime。因为

\[
m_X=p-1,
\]

唯一使

\[
p\mid m_X+s,
\qquad1\le s\le p
\]

成立的 shift 是

\[
s=1.
\]

raw edge 为

\[
\left(
\frac{U_X}{p},
\frac{V_X+R_X}{p},
\frac{m_X+1}{p}
\right).
\]

逐项计算：

\[
\frac{U_X}{p}=1,
\]

\[
V_X+R_X
=R_X(p-1)-p+R_X
=p(R_X-1),
\]

所以

\[
\frac{V_X+R_X}{p}=R_X-1,
\]

以及

\[
\frac{m_X+1}{p}=1.
\]

因此

\[
\boxed{
(p,R_X(p-1)-p,p-1)
\longrightarrow
(1,R_X-1,1).
}
\]

目的节点两侧互素，所以没有额外 gcd reduction。

这条 source/path receipt 完全由 `p` 和预声明 root 构造，没有读取 Type II endpoint 的 factorization，也没有复用旧 physical support。

---

# 6. 为什么旧 Type II support 不能作为 E1 的替代

`q=1` Type II 的 physical source primes 来自

\[
X=\frac{p+3}{4}.
\]

仓库此前的另一条 canonical root slice 满足

\[
(X,K_{\rm old})=1.
\]

因此“把旧 Type II source primes 原样重命名为 Type I charged support”在自然 root 上严格失败。

full-carrier root 的解决方式不是绕过这个事实，而是改变 E1 语义：

- Type II endpoint 保留自己的历史；
- 新 Type I tree 使用 `fresh_source_tree_only`；
- root 的实际 source 是刚刚显式构造的 universal `p`-source；
- 两边只通过“同根方程、同 ordinary marked set、单向 phase reindex”连接。

因此 provenance 是 fresh 的，而不是伪继承。

---

# 7. E1--E5 的逐项证明

现在定义 target state

```text
state_origin        = q_one_full_carrier_phase_root_entry_v1
source_tree_scope   = fresh_source_tree_only
normal_form         = type_i_full_carrier_low_root_v1
equation_target     = 4/p
marked_solution_set = Sol(p)
chart               = (p,R_X,K_X)
absorbed_support    = 1
```

并声明相位：

\[
\operatorname{rank}_{\rm phase}(S)=2,
\qquad
\operatorname{rank}_{\rm phase}(T_X)=1.
\]

非终端只允许

\[
2\to1,
\qquad1\to1,
\qquad1\to0,
\]

而 Type I tree 中后来发现的 Type II certificate 只能作为 terminal leaf，禁止非终端

\[
1\to2.
\]

### E1 — Provenance

- 输入 `S` 是实际 ordinary `q=1 G` endpoint；
- target root `(R_X,K_X)` 在读取任何 target factorization 前由 `p` 闭式声明；
- 第 5 节给出实际 `p`-raw source、唯一 shift 与 anchor；
- source scope 显式为 `fresh_source_tree_only`。

故 E1 成立。

### E2 — Deterministic construction

`t,X,R_X,K_X` 都由 `p` 唯一确定；不存在搜索 tie-break 或事后选择。

故 E2 成立。

### E3 — Normal-form validation

已经逐式证明：

\[
4K_X=pR_X+1,
\quad
3\le R_X\le p-2,
\quad
X\mid K_X,
\quad
p\nmid K_X,
\]

以及实际 source 的正性、互素性和 raw edge。

且新 state 不继承 Type II 的 F/G/fiber witness，而是 fresh Type I normal form。

故 E3 成立。

### E4 — 全域 solution lift

两端 equation target 完全相同，且 ordinary marking 为

\[
W_S=W_{T_X}=\operatorname{Sol}(p).
\]

定义

\[
\boxed{
\Phi_{T_X\to S}(u)=u.
}
\]

这是一个对 `W_{T_X}` 每个元素都定义的真实全域函数；不需要预先知道该集合是否非空。

故 E4 成立。

### E5 — phase-relative strictness

取词典序 potential 前缀

\[
\Pi(S)=(2,1,0),
\qquad
\Pi(T_X)=(1,B_p,K_X),
\]

其中

\[
B_p=\frac{(p-1)^2}{4}.
\]

第一坐标已经满足

\[
1<2,
\]

故

\[
\boxed{\Pi(T_X)<\Pi(S).}
\]

再加上 policy 禁止非终端 `1 → 2`，该 root-entry 是 phase-relative well-founded edge。

这并不自动证明 T5 的全局势函数；它只证明该具名 handoff 自身有合法 E5。

E1--E5 全部完成，定理 1 得证。∎

---

# 8. 加强定理：root 后无条件发生第一条严格 Type I segment

## 定理 2（Immediate Strict Progress）

在定理 1 的 `T_X` 上，universal source 到达 anchor

\[
(1,R_X-1,1).
\]

令

\[
M=R_X-1=16t+2=2(8t+1).
\]

则

\[
\boxed{(M,K_X)=1.}
\]

因此 complete-excess bundle 被强制为整个 `M`，charged support 从 `A=1` 严格增长，并按 `t` 奇偶得到一条完整 Type I strict edge。

### 证明

有

\[
K_X=(6t+1)(16t+1).
\]

显然

\[
(M,16t+1)=1.
\]

又

\[
3M-8(6t+1)
=3(16t+2)-8(6t+1)
=-2.
\]

而 `6t+1` 为奇数，所以

\[
(M,6t+1)=1.
\]

故

\[
\boxed{(M,K_X)=1.}
\]

于是 anchor 的 complete-excess 无选择：

\[
Q=M,
\qquad
\beta=1.
\]

下面分奇偶。

---

## 9. 奇 `t` 分支

若 `t` 为奇数，定义

\[
R_o=20t+3,
\qquad
K_o=(8t+1)(15t+1),
\qquad
A_o=M=16t+2.
\]

因为 `t` 为奇数，`15t+1` 为偶数，所以

\[
A_o=2(8t+1)\mid K_o.
\]

并且

\[
\begin{aligned}
pR_o+1
&=(24t+1)(20t+3)+1\\
&=480t^2+92t+4\\
&=4(8t+1)(15t+1)\\
&=4K_o.
\end{aligned}
\]

以及

\[
R_o<p
\iff20t+3<24t+1
\iff t>\frac12,
\]

故核心范围恒成立。

所以 `H_o=(p,R_o,K_o;A_o)` 是合法 low Type I child。

取局部势

\[
\Lambda(R,K;A)=
\left(
\left\lfloor\frac{B_p}{A}\right\rfloor,
\frac KA
\right).
\]

从 `A=1` 到 `A_o>1`，第一坐标严格下降：

\[
\left\lfloor\frac{B_p}{A_o}\right\rfloor
< B_p.
\]

两端仍取

\[
W=\operatorname{Sol}(p),
\]

所以 E4 仍为 identity。

因此奇支给出一条实际 strict marked-absorb edge。

---

# 10. 偶 `t` 分支

若 `t` 为偶数，先由完整 `M` bundle 得到显式 transient overflow：

\[
R_M=52t+7,
\qquad
K_M=(8t+1)(39t+2).
\]

验证

\[
R_M>p
\]

显然成立，因为

\[
R_M-p=28t+6>0.
\]

定义 determinant 参数

\[
n=4M-R_M=12t+1,
\]

\[
d=p-\frac{39t+2}{2}=\frac{9t}{2}.
\]

`t` 偶保证 `d` 为正整数。直接计算

\[
\boxed{pn=4Md+1.}
\]

取 fixed-`n` carrier

\[
L=d=\frac{9t}{2}.
\]

则

\[
R_e=4d-n=6t-1,
\]

\[
K_e=d(p-M)=\frac{9t}{2}(8t-1).
\]

有

\[
pR_e+1=4K_e,
\qquad
L\mid K_e,
\]

且

\[
3\le R_e\le p-2.
\]

所以

\[
H_e=(p,6t-1,\tfrac{9t}{2}(8t-1);A_e=\tfrac{9t}{2})
\]

是合法 low Type I state。

因为

\[
A_e=\frac{9t}{2}>1,
\]

局部 support potential 严格下降。

该 fixed-`n` edge 的两端仍然标记 `Sol(p)`，故 E4 是 identity。

所以偶支同样得到第一条严格 Type I edge。

定理 2 得证。∎

---

# 11. 结论：T4 ordinary 版本已经闭合

定理 1 已经足以证明旗舰 T4 的字面版本：

\[
\boxed{
q=1\ G
\Longrightarrow
\text{target-independent fresh Type I root}.
}
\]

定理 2 进一步证明：该 handoff 不是纯标签切换，而是无条件接上一条 strict Type I local edge：

\[
\boxed{
q=1\ G
\Longrightarrow
T_X
\Longrightarrow
H_{\rm odd/even}.
}
\]

因此对 ordinary marked set `Sol(p)`，方向 3 不应继续被标为一个尚未找到 root 的开放问题。

---

# 12. 旧候选命题的严格证伪

## 12.1 `R=3` 必非 G —— 假

Type I `R=3` chart 有

\[
K=N=\frac{3p+1}{4}=18t+1.
\]

它为 G 当且仅当 `N` 的每个素因子都为 `1 mod 3`。

取

\[
p=241,
\qquad X=61,
\qquad N=181.
\]

`61` 与 `181` 都是 `1 mod 3` 的素数，因此 q=1 Type II 与 R=3 Type I 同时为 G。

所以

\[
\boxed{
q=1\ G\not\Rightarrow R=3\text{ 非 G}.
}
\]

## 12.2 旧 canonical root 直接继承 Type II support —— 假

旧 root slice 满足

\[
(X,K_{\rm old})=1.
\]

所以来自 `X` 的 physical Type II source primes 无法直接变成该 root 的 charged support。

因此必须采用 fresh root-entry，而不能依赖 support rename。

---

# 13. 非平凡 marked set 的状态

现有 `q_one_full_carrier_phase_root_entry_v1` 明确限定

\[
W_S=W_T=\operatorname{Sol}(p).
\]

所以“现有 v1 自动适用于任意 nontrivial mark”是错误命题。

然而，如果某个 mark predicate `theta` 满足：

1. 它只依赖根方程解 `(x,y,z)` 与可逐字保存的标签；
2. 它不要求继承旧 `charged_history_only` physical occurrence；
3. target state 能以 `fresh_source_tree_only` 重新序列化同一个 predicate；

则可以定义

\[
W_S=W_T=W_{p,\theta}
\]

并仍取

\[
\Phi=\operatorname{id}_{W_{p,\theta}}.
\]

E1、E2、E3、E5 不变，因此在这种 **portable mark** 条件下可得到 mark-preserving 版本。

但这需要一个新的 typed normal form / serializer；它不应被混写成当前 `v1` 已经建立的 claim。

---

# 14. 与全局证明的关系

这份证明关闭的是：

\[
\boxed{
\text{ordinary }q=1\text{ Type II G}
\to
\text{fresh Type I phase entry}.
}
\]

它没有关闭：

\[
\boxed{
\text{每一个后续 Type I state 都有 terminal 或 strict edge}.
}
\]

后者属于 T6 Global-Selector。

此外，本文 E5 使用明确的 phase policy，只证明这条 handoff 的 phase-relative strictness。证明所有 Type II、Type I、overflow、marked descent edge 共享同一个全局良基势属于 T5。

所以逻辑关系是：

\[
\text{T4 ordinary closed}
\quad\not\Rightarrow\quad
\text{T5/T6 closed}.
\]

这也是本证明最重要的边界。
