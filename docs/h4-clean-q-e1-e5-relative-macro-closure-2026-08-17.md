# H4 clean \(q\)-bridge 的 corrected E1–E5 相对闭包：完整证明与实现说明

**日期：2026-08-17**
**结论状态：relative closure established / repository derivation + computational verification / internal review**

本文把 H4 clean \(q\)-bridge 的现有算术结果、修正后的 support 公式、E1–E5 状态合同以及通用 verifier 合并成一个可独立审阅的局部闭包证明。

> **证明边界。** 本文证明的是一个 **relative macro closure**：输入必须已经是由仓库既有 19-phase H4 source/provenance 机制认可的 actual H4 receipt，并且进入 H4 clean \(q\)-macro 前的版本化 priority prefix 已经产生 `miss` receipt。本文不重新证明所有核心素数都会到达 H4，也不重新证明上游 19-phase provenance，更不证明 \(q=1\) G fresh-source handoff、global selector 或 Erdős–Straus 猜想本身。

> **集成注记。** 当前主仓库另有更强的 parent-anchored、fully typed atomic macro；本
> 文保留 release 的相对闭包与独立整数 verifier，不能替代该强宏。release 产生的原始
> single-side / atomic 二分在当前 actual high-H4 域已被 single-side exclusion 收缩为
> atomic-only，因而这里的 single-side 推导是兼容的冗余分支，而非新的 live endpoint。

---

## 1. 目标定理

设 \(P\) 为 H4 分支的 persistent parent，并满足

\[
\Lambda_p^\sharp(P)=(0,p-1).
\]

设 actual H4 checkpoint 的整数数据为

\[
(p,R_4,K_4,M_4,c_4),
\qquad
pR_4+1=4K_4,
\qquad
K_4=M_4c_4,
\]

其中 \(p\equiv1\pmod{24}\) 为素数，且已经满足仓库定义的 proper-overlap、top-capacity、\(a_{\rm alt}=1\) 与 actual source/provenance 条件。

令

\[
h=(R_4-1,K_4),\qquad z=R_4-h,
\]

\[
w=\frac{p+1}{2},\qquad d=(w,M_4),\qquad q=\frac wd>1.
\]

沿 canonical clean \(q\)-word 得到 endpoint

\[
y_q=\frac zq,\qquad x_q=R_4-y_q.
\]

相对 \(K_4\) 取唯一 maximal complete-excess decomposition

\[
x_q=Q_x\beta_x,
\qquad
y_q=Q_y\beta_y.
\]

统一定义修正后的 support

\[
\boxed{M_q=\operatorname{lcm}(M_4,Q_x,Q_y)}.
\]

令

\[
c_q=\left\langle(4M_q)^{-1}\right\rangle_p,
\qquad
K_q=M_qc_q,
\qquad
R_q=\frac{4K_q-1}{p}.
\]

我们要证明：在 upstream actual-H4 receipt 与 priority-prefix miss 的前提下，H4 clean \(q\)-macro 满足 E1–E5，并且

\[
\boxed{
\Lambda_p^\sharp(R_q,K_q;M_q)=(0,c_q)<(0,p-1)=\Lambda_p^\sharp(P).
}
\]

因此该 H4 clean \(q\)-bridge 是一个 phase-local decreasing macro。

---

# 2. 基础定义

## 2.1 complete-excess block

对正整数 \(v,K\)，定义 \(Q_K(v)\) 为 \(v\) 中所有满足

\[
v_\ell(v)>v_\ell(K)
\]

的素数 \(\ell\) 的**完整** \(\ell\)-幂乘积；也就是说，若 \(\ell\) 被选中，则保留 \(v\) 中的完整指数 \(v_\ell(v)\)。

于是唯一写成

\[
v=Q_K(v)\,\beta,
\]

其中 \(\beta\mid K\) 在所有没有 complete excess 的坐标上承担 residual block。

verifier 中使用与该定义等价的 canonical 公式

\[
Q_K(v)
=
\gcd\!\left(v,
\left(\frac{v}{(v,K)}\right)^N\right),
\]

其中 \(N\ge\operatorname{bitlength}(v)\)。

## 2.2 E1–E5

本文遵守仓库 `denominator-escape-state-contract` 的边合同：

- **E1 premises**：source、真实 path、scope、最大 complete-excess 分解等全部可从整数 receipt 重算；
- **E2 construction**：target 是确定性的合法整数状态；
- **E3 normal form**：target 的 state/edge/owner serialization 唯一，不继承旧图表标签；
- **E4 solution lift**：存在对全部 marked solutions 有效的显式 lift；
- **E5 strict rank**：预先定义的良基势严格下降。

---

# 3. 算术层：A1–A12

## A1. \((q,K_4)=1\)

**命题。** 对 actual H4 clean \(q\)-carrier，

\[
\boxed{(q,K_4)=1}.
\]

**证明。** 取任意素数 \(\ell\mid q\)。因为

\[
q\mid \frac{p+1}{2},
\]

故

\[
p\equiv-1\pmod\ell.
\]

假设 \(\ell\mid K_4\)。由

\[
pR_4+1=4K_4
\]

模 \(\ell\) 得

\[
-R_4+1\equiv0\pmod\ell,
\]

即

\[
R_4\equiv1\pmod\ell.
\]

于是

\[
\ell\mid(R_4-1,K_4)=h.
\]

另一方面 actual H4 q-carrier 有 \(q\mid z=R_4-h\)，故 \(\ell\mid z\)。但

\[
z=R_4-h\equiv1-0\equiv1\pmod\ell,
\]

矛盾。因此没有素数 \(\ell\mid q\) 能整除 \(K_4\)，故

\[
(q,K_4)=1.
\]

证毕。

---

## A2. canonical clean \(q\)-word 全程合法并保持 primitive

写

\[
q=\prod_\ell \ell^{a_\ell}.
\]

canonical raw word 按固定顺序逐个除去这些素因子。

若当前已经除去 \(e\mid q\)，当前 y-coordinate 为

\[
y_e=\frac ze.
\]

若下一步还需除 \(\ell\mid q/e\)，则

\[
v_\ell(y_e)\ge1,
\qquad
v_\ell(K_4)=0
\]

由 A1 成立，所以这一步是合法 complete-excess raw edge。

再证 primitive。由于

\[
h=(R_4-1,K_4)\mid R_4-1,
\]

有

\[
R_4\equiv1\pmod h,
\]

从而

\[
z=R_4-h\equiv1\pmod h,
\]

故 \((z,h)=1\)。又 \(R_4=z+h\)，于是

\[
(z,R_4)=1.
\]

任意 \(y_e=z/e\) 仍与 \(R_4\) 互素，因此

\[
(x_e,y_e)=(R_4-y_e,y_e)=1.
\]

所以完整 q-word 到达唯一 endpoint

\[
\boxed{
(x_q,y_q)=\left(R_4-\frac zq,\frac zq\right)
}
\]

并保持 primitive。

---

## A3. 所有 proper prefixes 都不是 full-excess sink

取真前缀 \(e\mid q\)、\(e<q\)。选择任意素数

\[
\ell\mid q/e.
\]

则

\[
\ell\mid y_e=\frac ze,
\]

而 A1 给

\[
\ell\nmid K_4.
\]

因此

\[
y_e\nmid K_4.
\]

若该 prefix 是 full-excess Type I sink，则必须有

\[
x_ey_e\mid K_4,
\]

特别推出 \(y_e\mid K_4\)，矛盾。

所以

\[
\boxed{
 e<q\Longrightarrow\text{该 proper prefix 不是 full-excess sink}.
}
\]

注意：本命题只排除这一类 full-excess sink，不自动排除未来 registry 中其它独立 terminal policy；这类 policy 由 priority prefix 单独管理。

---

## A4. actual carry 恒等式 \(h=2d\) 与 \(hq=p+1\)

现有 H4 carry 给

\[
h=2e,
\qquad
e=(w,c_3-s_4),
\]

并有

\[
M_4=M_3L,
\qquad
(w,M_3)=1.
\]

因此

\[
d=(w,M_4)=(w,L).
\]

由

\[
Lc_4=c_3+ps_4
\]

和 \(p\equiv-1\pmod w\)，得

\[
Lc_4\equiv c_3-s_4\pmod w.
\]

所以

\[
d=(w,L)\mid(w,c_3-s_4)=e.
\]

另一方面

\[
e\mid h\mid K_4.
\]

A1 给 \((q,K_4)=1\)，故 \((e,q)=1\)。而 \(e\mid w=qd\)，所以 \(e\mid d\)。结合 \(d\mid e\) 得

\[
e=d.
\]

故

\[
\boxed{h=2d}.
\]

又

\[
q=\frac{w}{d}=\frac{p+1}{2d},
\]

于是

\[
\boxed{hq=p+1}.
\]

---

## A5. endpoint 不含 \(p\)-primary block

首先 \(p\nmid z\) 且 \(q<p\)，所以

\[
p\nmid y_q.
\]

现在排除 \(p\mid x_q\)。由

\[
R_4\equiv1\pmod p
\]

和

\[
y_q=\frac{R_4-h}{q},
\]

有

\[
p\mid x_q
\iff
h\equiv1-q\pmod p.
\]

由于 \(2\le h<p+1\)，只能有

\[
h=p+1-q.
\]

而 \(h\mid p+1\)，结合 \(p+1=h+q\) 可得 \(h\mid q\)。又

\[
h\ge\frac{p+1}{2}=w,
\qquad
q\le w,
\]

所以只能

\[
h=q=w.
\]

但 \(h=2d\) 为偶数，而核心素数 \(p\equiv1\pmod{24}\) 给 \(w=(p+1)/2\) 为奇数，矛盾。

因此

\[
\boxed{p\nmid x_qy_q}.
\]

于是 maximal complete-excess blocks 也满足

\[
\boxed{p\nmid Q_xQ_y}.
\]

---

## A6. y-side complete-excess block 必非平凡：\(Q_y>1\)

现有 H4 high-R premise 给

\[
R_4>\frac{p^3}{2}-\frac1p.
\]

proper overlap 又有

\[
h,q\le\frac{p+1}{2}.
\]

因此对实际核心范围 \(p\ge73\)，有

\[
y_q=\frac{R_4-h}{q}>p^2-p-1.
\]

同时

\[
p^2-p-1>\frac{p^2+p+2}{2}\ge ph+1.
\]

故

\[
\boxed{y_q>ph+1}.
\]

假设 \(Q_y=1\)。按 maximal complete-excess 定义，说明

\[
y_q\mid K_4.
\]

而

\[
4K_4=pR_4+1
=p(qy_q+h)+1
=pqy_q+ph+1.
\]

于是 \(y_q\mid ph+1\)，但 \(0<ph+1<y_q\)，矛盾。

所以

\[
\boxed{Q_y>1}.
\]

这同时排除了 endpoint full-excess sink 以及 \(Q_y=1<Q_x\) 的反向单侧分支。

---

## A7. 旧 single-side support 公式为假

旧卡曾按分支写

\[
M_q=
\begin{cases}
\operatorname{lcm}(M_4,Q_x),&\text{恰一块非平凡},\\
\operatorname{lcm}(M_4,Q_x,Q_y),&\text{双侧非平凡}.
\end{cases}
\]

但 A6 与后续 endpoint 分类说明 actual single-side 只能是

\[
Q_x=1<Q_y.
\]

于是旧第一行给

\[
M_q=\operatorname{lcm}(M_4,1)=M_4,
\]

完全没有吸收唯一非平凡的 \(Q_y\) block。这与 complete-excess support enlargement 的定义直接冲突。

因此

\[
\boxed{\text{旧 single-side 公式被证伪。}}
\]

这是局部接口错误；后续 stutter-reduction 卡已经使用统一的正确公式，所以后续 stutter proof 不因此失效。

---

## A8. 正确 support 公式

无论 endpoint 属于 single-side 还是 atomic-split，统一定义

\[
\boxed{M_q=\operatorname{lcm}(M_4,Q_x,Q_y)}.
\]

令

\[
Q=Q_{K_4}(z),
\qquad
z=Q\delta,
\qquad
\delta\mid K_4.
\]

A1 说明 q 的全部素因子在 \(K_4\) 中指数为 0，且 q-word 正好移除 q，因此

\[
y_q=\frac Qq\delta.
\]

所以

\[
\boxed{Q_y=Q/q},
\qquad
\boxed{\beta_y=\delta}.
\]

定义

\[
L_0=\frac{\operatorname{lcm}(M_4,Q)}{M_4}.
\]

因为 \((q,M_4)=1\)，有

\[
(M_4,Q)=(M_4,Q/q),
\]

从而 y-side 新增倍率为

\[
E_y
=
\frac{Q_y}{(M_4,Q_y)}
=
\frac{L_0}{q}.
\]

再令

\[
E_x=\frac{Q_x}{(M_4,Q_x)}.
\]

endpoint primitive 给 \((Q_x,Q_y)=1\)，因此 lcm 增量乘法分解为

\[
\boxed{
L_q:=\frac{M_q}{M_4}
=E_xE_y
=\frac{L_0}{q}E_x.
}
\]

---

## A9. target capacity 同余公式

定义

\[
c_q=\left\langle(4M_q)^{-1}\right\rangle_p.
\]

H4 top-capacity alternate support 给

\[
c_4L_0^{-1}\equiv-1\pmod p.
\]

由 A8 的

\[
L_q=\frac{L_0}{q}E_x,
\]

得到

\[
\begin{aligned}
c_q
&\equiv c_4L_q^{-1}\pmod p\\
&\equiv
c_4\left(\frac{L_0}{q}E_x\right)^{-1}\pmod p\\
&\equiv
-qE_x^{-1}\pmod p.
\end{aligned}
\]

所以

\[
\boxed{c_q\equiv-qE_x^{-1}\pmod p}.
\]

---

## A10. 唯一 first-stutter gate

由 A9，

\[
c_q=p-1
\]

当且仅当

\[
-qE_x^{-1}\equiv-1\pmod p,
\]

即

\[
\boxed{E_x\equiv q\pmod p}.
\]

因此这就是唯一 capacity stutter。

特别地，single-side 有 \(Q_x=1\)，所以

\[
E_x=1.
\]

于是

\[
c_q\equiv-q\pmod p.
\]

因 \(1<q<p\)，规范剩余正好为

\[
\boxed{c_q=p-q\le p-2}.
\]

所以 single-side 不可能 stutter。

---

## A11. actual atomic first-stutter 全部排除

atomic-split 若 stutter，则由 A10

\[
E_x\equiv q\pmod p.
\]

写

\[
x_q=E_xD,
\qquad
D=(M_4,Q_x)\beta_x\mid K_4.
\]

从

\[
qx_q=(q-1)R_4+h
\]

以及 \(R_4\equiv1\pmod p\)、\(h=2d\)，得 stutter 时

\[
q^2D\equiv q+2d-1\pmod p.
\]

又由

\[
2dq=p+1
\]

得到

\[
q^{-1}\equiv2d\pmod p.
\]

因此

\[
\boxed{
D\equiv2d(4d^2-2d+1)=:\delta_d\pmod p.
}
\]

另一方面，把原方程与 \(D\mid K_4\) 联立，得到

\[
\boxed{D\mid ph-q+1},
\]

并有

\[
0<D<2dp.
\]

所以任意 actual stutter 必须通过一个完全 source-only 的 \((d,q,D)\) 门。

现有 universal source-D gate closure 将其分成三个互斥区域：

### 区域 I：\(p\le\delta_d\)

此时

\[
2\le q\le4d^2-2d+1.
\]

仓库的穷尽整数筛枚举 31 个 phase classes、109 个 odd \((u,d)\)、2204 个 q，以及 4,475,827 个 D 候选，survivor 为 0。该筛是有限证明对象，不是随机/统计采样。

### 区域 II：\(p>\delta_d\)、\(D>\delta_d\)

写

\[
D=\delta_d+kp,
\qquad
ph-q+1=\ell D.
\]

由大小条件得到

\[
k\ell\le2d-1,
\]

并可消元得到

\[
\boxed{
p=
\frac{2d\ell\delta_d-(2d-1)}
{4d^2-1-2dk\ell}.
}
\]

完整有限菜单共有 233,378 个 \((d,k,\ell)\) 候选；137 个产生整数 p，89 个满足 \(p>\delta_d\)，其中 7 个为素数，但没有一个属于实际 19-phase progression。因此该区域为空。

### 区域 III：\(p>\delta_d\)、\(D=\delta_d\)

109 个 odd phase/divisor pairs 中：54 个被模 3 排除，38 个 CRT 不相容，只剩 17 条无限 arithmetic rays。

这 17 条进一步分解：

- 7 条在 H3 已由 \(\ell\equiv3\pmod4\) 的 Type II terminal 提前关闭；
- 3 条 \(d=17\) ray 可证明 \(17\nmid M_4\)，与 \(d=((p+1)/2,M_4)=17\) 矛盾；
- 最后 7 条通过 complete-excess valuation receipt 证明某 \(\ell\mid d\) 实际满足 \(v_\ell(M_4)=0\)，再次与 \(\ell\mid d=((p+1)/2,M_4)\) 矛盾。

因此 actual atomic stutter 也不存在。

综上

\[
\boxed{1\le c_q\le p-2}
\]

对所有 actual H4 clean q endpoints 成立。

> **证据类型说明。** A11 的中间 finite closures 是“数学约化 + 完整有限枚举/valuation receipt”的计算辅助证明。它不是仅凭 p=73、241 两个 control 得出的结论。通用 verifier 消费的是这条已经建立的 universal stutter-closure claim；control fixtures 只用于回归实现。

---

## A12. endpoint 完整二分

A6 给

\[
Q_y>1.
\]

A5 给

\[
p\nmid Q_xQ_y.
\]

所以 maximal complete-excess endpoint 只剩：

1. \(Q_x=1<Q_y\)：single-side；
2. \(Q_x>1,Q_y>1\)：atomic-split。

即

\[
\boxed{
\text{endpoint}=\text{single-side}\ \lor\ \text{atomic-split}.
}
\]

同时 A11 给两类都满足

\[
\boxed{c_q\le p-2}.
\]

这完成纯算术 endpoint 分类。

---

# 4. E1–E5 层：B1–B6

## B1. single-side E1 payload 合法

single-side 中

\[
Q_x=1<Q_y.
\]

所以 \(x_q\) 没有超过 \(K_4\) 的 complete-excess prime power，即

\[
x_q\mid K_4.
\]

同时 A8 给

\[
\beta_y=\delta\mid K_4.
\]

由 endpoint primitive，

\[
(x_q,\beta_y)=1.
\]

故

\[
\boxed{x_q\beta_y\mid K_4}.
\]

因此 single-side 的 residual payload 可以从原整数唯一重算，不依赖候选搜索。

---

## B2. atomic-split 局部 E1 payload 与 maximality 合法

atomic-split 中

\[
Q_x,Q_y>1.
\]

唯一 maximal decomposition 给

\[
x_q=Q_x\beta_x,
\qquad
y_q=Q_y\beta_y,
\]

且 residual factors 满足

\[
\beta_x\beta_y\mid K_4.
\]

endpoint primitive 给

\[
(Q_x,Q_y)=1.
\]

A5 给

\[
p\nmid Q_xQ_y.
\]

由于 \(Q_K(v)\) 有 canonical 最大定义，\(Q_x,Q_y\) 不是选择性 factorization，而是从 \((v,K_4)\) 唯一确定的整数函数。因此 atomic E1 的 source/path/maximality/blocks 都能确定性重算。

---

## B3. E2 canonical target 总存在

统一取

\[
M=M_q=\operatorname{lcm}(M_4,Q_x,Q_y).
\]

A5 给 \(p\nmid Q_xQ_y\)，而 H4 source 本身有 \(p\nmid M_4\)，所以

\[
p\nmid M.
\]

因此 \((4M)^{-1}\pmod p\) 存在。定义其规范正剩余

\[
c=\langle(4M)^{-1}\rangle_p,
\qquad 1\le c\le p-1.
\]

令

\[
K'=Mc,
\qquad
R'=\frac{4K'-1}{p}.
\]

因为

\[
4Mc\equiv1\pmod p,
\]

故 \(R'\in\mathbb Z\)，并有

\[
pR'+1=4K'.
\]

又因为 \(p\equiv1\pmod4\)，从该等式模 4 得

\[
R'\equiv-1\equiv3\pmod4.
\]

且 \(R'>0\)。因此

\[
\boxed{T=(p,R',K';M)}
\]

是确定存在的 canonical linear chart target。

---

## B4. E3：canonical serialization + `pending_dispatch`

这一步要区分“数学状态身份”和“以后 selector 使用的派生标签”。

本 macro 的 E1/E2/E4/E5 只依赖 canonical integers、support、source/path receipt 和 rank；它不需要先知道 target 是 F、G 还是 hit。source 与 target 的 marked set 又都取完整

\[
W=\operatorname{Sol}(p).
\]

因此可以安全地把 target 序列化为

```text
dispatch_status = pending_dispatch
selector_consumable = false
inherited_type_label = false
mandatory_next_step = normalize_target_state
```

规则是：

1. target `state_id` 只由 state kind/version、\((p,R',M)\) 与 scope 决定；\(K'\)、
   capacity、rank、`pending_dispatch` 与所有 classifier cache 都是派生或队列字段，
   不得进入数学身份；
2. 绝不继承 H4/source 的 F/G/hit 标签；
3. 任何下一条需要 F/G/hit、target fiber、signed defect 或 certificate context 的 selector，在消费 target 前必须从 target integers 重新运行完整 classifier；
4. `pending_dispatch` 或其它惰性字段不得参与 E5 排名；
5. atomic endpoint 的 owner ID 由 adapter version、source state ID、canonical q-path、endpoint 与 maximal blocks 的 digest 唯一生成；single-side 同理生成 canonical bundle ID；
6. priority prefix 的 policy version、source state ID、receipt ID 与 `miss` 状态写入 edge receipt。

所以 E3 的确定性没有被削弱；这里只是把 type-specific classifier 推迟到真正需要它的下一条边。

---

## B5. E4 是 \(\operatorname{Sol}(p)\) 上恒等 lift

persistent parent 和 target 都对应同一个目标方程

\[
\frac4p=\frac1x+\frac1y+\frac1z,
\]

且 marked set 均为完整

\[
W_P=W_T=\operatorname{Sol}(p).
\]

定义

\[
\Phi:W_T\to W_P,
\qquad
\Phi(u)=u.
\]

显然任何 \(u\in W_T\) 仍是正整数三分母解，并满足同一个 \(4/p\) 恒等式。因此

\[
\boxed{\Phi=\mathrm{id}_{\operatorname{Sol}(p)}}
\]

是全域 solution lift。E4 完成。

---

## B6. E5 phase-local 严格下降

关键是比较 **原 persistent parent** 与 **最终 target**，而不是比较中间 H4 checkpoint。

现有 persistent macro 给

\[
\Lambda_p^\sharp(P)=(0,p-1).
\]

H4 已在 high-support 区域：

\[
M_4>B_p=\frac{(p-1)^2}{4}.
\]

而

\[
M_q\ge M_4,
\]

所以 target 第一 rank 坐标仍为 0。

第二坐标正是 canonical capacity \(c_q\)。A11 给

\[
c_q\le p-2.
\]

因此

\[
\boxed{
\Lambda_p^\sharp(T)=(0,c_q)<(0,p-1)=\Lambda_p^\sharp(P).
}
\]

E5 完成。

---

# 5. 两个“不需要再证明”的伪义务

## C1. 不需要证明所有更早 priority 都 miss

错误的要求是：为了闭合 H4，必须证明所有 earlier terminal/alternate action 都 miss。

实际 dispatcher 只需要满足：

- 若更早 action 命中 verified terminal 或 verified strict edge，则该 branch 已经更早闭合；
- 只有当版本化 priority prefix 产生 `miss` receipt 时，才进入 H4 macro。

所以要证明的是

\[
\boxed{\text{priority hit}\Rightarrow\text{合法出口}}
\]

而不是

\[
\boxed{\text{所有 priority 必须 miss}}.
\]

因此后者不是 H4 closure 的必要命题。

## C2. 不需要跨所有未选择 action 的 global one-use ledger

在单个 deterministic H4 macro 内，canonical q-path、endpoint、maximal blocks 和 owner digest 都唯一。只有当一个更大的证明同时对多个互斥候选 action 的资源做全局聚合收费时，才需要跨 action one-use ledger。

H4 relative closure 本身选择一个确定的 outgoing macro，不对未选择 action 同时收费。因此跨所有候选 action 的 global one-use 不是本定理的必要前提。

---

# 6. corrected H4-Closure 定理

**定理（H4 clean \(q\)-bridge corrected E1–E5 relative macro closure）。**
设：

1. \(P\) 是已经通过既有 19-phase H4 source/provenance 验证的 persistent parent；
2. \(\Lambda_p^\sharp(P)=(0,p-1)\)；
3. versioned earlier priority prefix 已产生对同一 source state 的 `miss` receipt；
4. actual proper-overlap top-capacity \(a_{\rm alt}=1\) H4 receipt 成立。

则 canonical clean \(q\)-word：

- 可完整重放并保持 primitive；
- 所有真前缀都不是 full-excess sink；
- endpoint 为 p-free；
- \(Q_y>1\)；
- endpoint 只有 \(Q_x=1<Q_y\) single-side 或 \(Q_x,Q_y>1\) atomic-split；
- 使用修正 support
  \[
  M_q=\operatorname{lcm}(M_4,Q_x,Q_y)
  \]
  时 universal first-stutter closure 给
  \[
  1\le c_q\le p-2;
  \]
- canonical target
  \[
  K_q=M_qc_q,
  \qquad
  R_q=(4K_q-1)/p
  \]
  是合法确定整数状态；
- target 以 `pending_dispatch` 序列化，不继承 F/G/hit；
- E4 为 \(\operatorname{Sol}(p)\) 上恒等 lift；
- E5 满足
  \[
  (0,c_q)<(0,p-1).
  \]

因此，若较早 priority action 未先闭合该 branch，则 H4 clean \(q\)-bridge 本身输出一条 phase-local decreasing E1–E5 macro。

**证明。** E1 由 A1–A8、A12、B1–B2 和 upstream receipt 的 canonical replay 给出；E2 由 B3；E3 由 B4；E4 由 B5；E5 由 A11 与 B6。证毕。

---

# 7. 证明依赖与不能外推的部分

本定理仍依赖以下上游已登记结论/机制：

- `type-II-q-one-c-two-19-phase-three-anchor-persistent-macro`；
- `type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge`；
- `type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-interior-terminal-localization`；
- `type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-y-block-nonempty`；
- `type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion`；
- `type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction`；
- `type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure`；
- `type-I-path-anchored-atomic-split-complete-excess-admission`；
- `denominator-escape-state-contract`。

因此本结果的准确状态是

\[
\boxed{\text{H4 clean q-bridge relative closure: CLOSED}}
\]

而不是

\[
\boxed{\text{H4 upstream provenance: independently reproved}}
\]

也不是

\[
\boxed{\text{global ESC proof: closed}}.
\]

---

# 8. 通用 verifier 与数学命题的对应关系

文件：

`reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py`

verifier 依次执行：

1. 验证 relative premises：input schema、persistent parent rank、charged-history scope、priority-prefix miss、upstream H4 receipt reference；
2. 重算 H4 chart：\(pR_4+1=4K_4\)、\(K_4=M_4c_4\)、high-support、high-R；
3. 重算 \(h,z,w,d,q\)，验证 \(h=2d\)、\(hq=p+1\)；
4. 计算 \(Q_{K_4}(z)\)，检查 \((q,K_4)=1\)；
5. 重放 canonical prime-factor q-word；
6. 审计所有 proper prefixes 不成为 full-excess sink；
7. 重算 endpoint \((x_q,y_q)\) 与 maximal blocks \(Q_x,Q_y\)；
8. 使用 corrected support
   \[
   M_q=\operatorname{lcm}(M_4,Q_x,Q_y);
   \]
9. 重算 multiplier identity 与 \(c_q\)；
10. 检查 stutter miss；
11. 构造 canonical target \((p,R_q,K_q;M_q)\)；
12. 生成 deterministic state/edge/owner IDs；
13. 输出 `pending_dispatch`，显式禁止 inherited type label；
14. 验证 identity lift；
15. 验证 persistent-parent-to-target strict rank。

当输入 receipt 明确声明已经通过 external actual-H4 provenance 与 priority-prefix miss
验证时，只有全部成立才输出 phase-local macro：

```text
E1 = true
E2 = true
E3 = true
E4 = true
E5 = true
selector_status = candidate_transition
phase_local_macro_eligible = true
recursive_edge_eligible = false
```

局部 control receipt 只检查同一相对推导的整数、序列化与 rank 逻辑；它们保留
`E1--E5` 的**相对**真值，但必须输出 `selector_status = control_only` 与
`recursive_edge_eligible = false`，不得被当作真实 proof-graph edge。全局 selector 与跨
phase 良基势完成后，才可由另一个 admission 层决定是否升级其状态。

---

# 9. 一个容易混淆但已修正的实现细节

H4 的 \(a_{\rm alt}=1\) premise 属于 **top-capacity alternate source chart**，其整数为

\[
n_{\rm alt}=\frac{4M_{\rm alt}+1}{p}.
\]

因此

\[
a_{\rm alt}
=
\frac{(p+1)/2}
{\gcd((p+1)/2,(n_{\rm alt}+1)/2)}.
\]

它不能误用最终 E2 canonical target 的

\[
R_q=\frac{4M_qc_q-1}{p}.
\]

两个对象的正负号和数学角色不同：前者验证 upstream H4 \(a_{\rm alt}=1\) gate，后者是 closure macro 的最终 linear-chart target。通用 verifier 已把两者分开。

---

# 10. 回归验证结果

2026-08-17 本地重新运行：

```text
Ran 6 tests
OK
```

测试包括：

- 两个已有 arithmetic controls 全部通过 E1–E5；
- 旧 single-side support 公式 regression；
- priority miss 是真实 premise；
- target 不继承 source type label；
- canonical receipt/state/edge ID 可重复生成；
- multiplier 与已有 control 数值一致。

Control 1：

\[
p=73,\qquad q=37,\qquad c_q=24,
\]

且

\[
M_q=3559956824877628.
\]

Control 2：

\[
p=241,\qquad q=121,\qquad c_q=80,
\]

且

\[
M_q=92255470189779250300.
\]

两者输出

```text
E1 = E2 = E3 = E4 = E5 = true
```

这些 controls 只验证 arithmetic/serialization regression；它们输出 `control_only`，
**不替代** universal upstream H4 provenance 或 A11 的 universal stutter finite closure，
也不具备递归入队资格。

---

# 11. 仓库修改清单

本 release 包含：

- `H4_CLEAN_Q_E1_E5_COMPLETE_PROOF.md`：本文，完整数学证明与 proof boundary；
- `claims/type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure.md`：新的 theorem card；
- `reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py`：通用 relative macro verifier；
- `tests/test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py`：6 个 focused tests；
- `concepts/denominator-escape-state-contract.pending-dispatch.patch.md`：E3 `pending_dispatch` 合同补充；
- `OLD_FORMULA_FIX.md`：旧 support 公式修正说明；
- `reproductions/README.addition.md`：reproduction README 增补；
- `index/CURRENT_FRONTIER_2026-08-17_ADDITION.md`：frontier closure 增补；
- `control_receipts.json`：两个 control receipt；
- `apply_h4_closure.py`：将上述修改应用到仓库 checkout 的 installer；
- `VERIFICATION_RESULTS.md`：本次实际测试记录；
- `MANIFEST.sha256`：文件完整性校验。

---

# 12. 应用到仓库后的完整验证过程

从 release 包外运行：

```bash
python h4_closure_release_2026-08-17/apply_h4_closure.py /path/to/erdos-straus
```

进入仓库：

```bash
python scripts/kb.py validate

python -m unittest \
  tests.test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier -v

python \
  reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py \
  --verify-controls

python scripts/kb.py build

git diff --check
```

若环境有 Ruff：

```bash
ruff check \
  reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py \
  tests/test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py
```

> 规范集成已在主仓库完成：focused suite 扩展为 9 项，并区分 local controls 与带 verified
> premises 的 phase-local macro。完整集成记录见
> [H4 Closure Release Audit](h4-closure-release-audit-2026-08-17.md)。

---

# 13. 方向 1 的最终研究状态

在本文使用的明确 proof boundary 下：

\[
\boxed{
\textbf{方向 1 的该相对输入域：H4 clean q-bridge 的 E1–E5 相对闭包——完成。}
}
\]

后续研究不应继续把该输入域的 H4 first-stutter 或 corrected q-support 当成 active
arithmetic gap。它仍不把 phase-local `candidate_transition` 升格为全局递归边；其它 H4
selector branch、global well-foundedness 与 q=1 G handoff 仍须各自闭合。除非独立审阅
推翻某个上游 dependency，主攻方向应转向：

\[
\boxed{
q=1\;G\longrightarrow\text{fresh Type I/F/G handoff}
}
\]

以及它与 global well-founded selector 的连接。
