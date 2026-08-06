---
kind: claim
claim_id: type-II-shared-factor-q-adic-difference-bound
title: Type II 共享素因子幂的移位差 q 进上界
statement: 设 p 为奇素数，s_i != s_j 为两个 Type II 移位，q 为奇素数。若 q^e 同时整除 p+4s_i 与 p+4s_j，则 q^e 整除 4(s_j-s_i)，从而得到逐对高度界；更一般地，对任意有限移位集 S 和截断 E，有 sum_s min(v_q(p+4s),E) <= sum_{r=1}^E max_a # {s in S: s = a mod q^r}。该有限 q 进容量界不构造 Type I/II 证书，不给出全局容量注入，也不推出递降。
claim_status: established
topics:
- type-II
- q-adic
- multishift
- collision
- capacity-boundary
- proof-program
depends_on:
- type-II-collision-factor-relay-boundary
- type-II-two-power-character-depth-sieve
sources:
- claim: type-II-collision-factor-relay-boundary
  locator: shared-prime-power congruence u = s mod q^e
  role: prior-multishift-collision-boundary
- reproduction: type-ii-canonical-fan-escape-trichotomy
  locator: shared_factor_q_adic_bridge
  role: exact-finite-q-adic-replay
visibility: public
last_checked: '2026-08-04'
---

# Type II 共享素因子幂的移位差 q 进上界

## 引理

令 \(p\) 为奇素数，\(s_i\ne s_j\) 为两个正整数移位，并令 \(q\) 为奇素数。写

\[
N_i=p+4s_i,\qquad N_j=p+4s_j.
\]

若 \(q^e\mid N_i\) 且 \(q^e\mid N_j\)，则相减得到

\[
q^e\mid N_j-N_i=4(s_j-s_i). \tag{1}
\]

令 \(e_i=v_q(N_i)\)、\(e_j=v_q(N_j)\)。取
\(e=\min(e_i,e_j)\) 即得

\[
\min\bigl(v_q(p+4s_i),v_q(p+4s_j)\bigr)
\le v_q\bigl(4(s_j-s_i)\bigr). \tag{2}
\]

这说明共享素因子幂的共同高度由移位差预先支付；若
\(q\nmid4(s_j-s_i)\)，则 \(q\) 不可能同时整除两条移位。

## 有限移位集的 q 进容量

令 \(S\) 为任意有限移位集，\(E\ge1\)，并定义

\[
C_r(S,q)=\max_{a\bmod q^r}
\#\{s\in S:s\equiv a\pmod {q^r}\}.
\]

由于 \(q\) 为奇素数，4 在每个 \(q^r\) 上可逆。对固定的 \(p\)，条件
\(q^r\mid p+4s\) 等价于

\[
s\equiv -p\,4^{-1}\pmod {q^r}, \tag{4}
\]

即所有在第 \(r\) 层有 q 进赋值的移位都落在同一个残类中。因此对任意截断高度
\(E\)，逐层计数给出

\[
\sum_{s\in S}\min\bigl(v_q(p+4s),E\bigr)
=\sum_{r=1}^{E}\#\{s\in S:q^r\mid p+4s\}
\le\sum_{r=1}^{E}C_r(S,q). \tag{5}
\]

式 (5) 是真正的跨状态 q 进容量不等式：右侧只由移位集和 \(q\) 决定，与 \(p\)
无关；左侧是所有状态在各层共享 q 因子的总需求。它比逐对界更强，因为同时控制了
任意多条移位的总赋值，而不是只控制一条边。

定义第 \(r\) 层的容量缺口

\[
\Delta_r(p;S,q)
=C_r(S,q)-\#\{s\in S:q^r\mid p+4s\}\ge0,
\]

以及截断总缺口
\(\Delta_E(p;S,q)=\sum_{r=1}^{E}\Delta_r(p;S,q)\)。则

\[
\Delta_E(p;S,q)=0
\quad\Longleftrightarrow\quad
\text{对每个 }1\le r\le E,\
-p\,4^{-1}\pmod {q^r}
\text{ 是一个最大容量残类}. \tag{6}
\]

因此每个有限状态集都有一个严格的“刚性链/容量缺口”二分：等号状态必须在所有
层同时沿最大残类链运行；只要某一层的目标残类不是最大类，就支付至少一个单位的
q 进容量缺口。这是把局部 q 进数据接入选择器的第一条状态级分派规则。

刚性分支还可显式参数化。令
\[
\mathcal A_r(S,q)=
\left\{a\bmod q^r:
\#\{s\in S:s\equiv a\pmod{q^r}\}=C_r(S,q)\right\},
\]
并定义兼容的素数残类集合
\[
\mathcal P_{S,q,E}=
\left\{p\bmod q^E:
-p\,4^{-1}\bmod q^r\in\mathcal A_r(S,q)
\ \text{for every }r\le E\right\}. \tag{7}
\]
则 \(\Delta_E(p;S,q)=0\) 当且仅当 \(p\bmod q^E\in\mathcal P_{S,q,E}\)。
各层的 \(\mathcal A_r\) 不必自动向下投影为上一层的最大类，因此
\(\mathcal P_{S,q,E}\) 正是对这些层施加兼容性筛选后的有限、可枚举等号进程集合；
若它为空，则该移位集对所有 \(p\) 都有严格 q 进容量缺口。

## 选择器中的回放

在 \(p=433\) 的两条 raw 射线
\((A,C)=(4,1),(5,4)\) 中，移位为 \(s_i=16,s_j=100\)，

\[
N_i=497=7\cdot71,\qquad N_j=833=7^2\cdot17.
\]

这里

\[
\min(v_7(497),v_7(833))=1,\qquad
v_7\bigl(4(100-16)\bigr)=v_7(336)=1, \tag{3}
\]

所以局部共享高度界达到等号。统一选择器的回执同时保存共享因子相位、私有余因子
和该差值界，字段为 difference_bound_status=tight。这是高阶字符分支中第一个与真实
移位差相连的可复核 q 进局部上界。

回执还按高度保存碰撞层：在 \(q^1=7\) 层，两条移位的残基均为
\(16\equiv100\equiv2\pmod7\)；在 \(q^2=49\) 层，只有 \(833\) 仍有足够的
赋值，故活动行从两条收缩为一条。这是 exact_local_collision_tree，而不是已经求和的
跨状态容量树。

对这两条移位，\(C_1(S,7)=2\)、\(C_2(S,7)=1\)。实际赋值需求为
\(v_7(497)+v_7(833)=1+2=3\)，右端容量也是 \(2+1=3\)，所以式 (5) 在
\(p=433,S=\{16,100\},q=7,E=2\) 上达到等号。这是一个已构造的、非空但紧的
跨状态 q 进容量证书；它说明下一步必须寻找严格容量缺口，或把等号情形转为 Type II
目标命中/严格递降。

例如在 \(S=\{16,100,3,10,17\}\)、\(q=7\)、\(p=433\)、\(E=2\) 时，
\(C_1=3\)（残类 \(3\bmod7\)），而目标残类为 \(2\bmod7\)，只含 \(16,100\)；
第 1 层立即产生一个单位缺口，故总容量严格大于实际需求。这个严格缺口实例说明
“最大残类链”不是形式上的重写，而是可计算地排除一部分跨状态 q 进需求。

对 \(S=\{16,100\},q=7,E=2\)，有
\(\mathcal A_1=\{2\bmod7\}\)，而模 \(49\) 的两个出现残类 \(2,16\) 都是最大类；
故兼容链给出
\[
\mathcal P_{S,7,2}=\{41,34\}\pmod{49}.
\]
确实 \(433\equiv41\pmod{49}\)，所以该样本处于等号进程。加入
\(\{3,10,17\}\) 后，第 1 层最大类变为 \(3\bmod7\)，而 \(433\) 的目标类仍为
\(2\bmod7\)，立即落入严格缺口进程。

该结论可直接写成 relay 标签形式。若目标移位 \(u\) 的因子标签要求
\(q^{f_s}\mid p+4s\) 且 \(q^{f_s}\mid p+4u\)（\(s\in S\)），则
\[
\sum_{s\in S}f_s\le\sum_{r=1}^{\max f_s}C_r(S,q). \tag{7}
\]
因此一个 relay 不能把同一 \(q\)-幂的高层标签任意复制到多个来源；复制深度本身消耗
各层容量。在 \(p=433,S=\{16,100\},q=7\) 中，若两条来源都要求 \(f_s=2\)，需求为
\(4\)，而容量只有 \(C_1+C_2=3\)，故这种双 \(7^2\) relay 严格不可能；实际
\((f_{16},f_{100})=(1,2)\) 正好达到容量等号。

等号链也不自动代表障碍。上述同一核心素数 \(p=433\) 在另一条移位 \(s=1\) 上有
\[
433+4=437=19\cdot23,\qquad 19\equiv-1\pmod4.
\]
取 \((A,C,K)=(1,1,5)\)，\(h=4ACK-1=19\) 立即重建一张 Type II 短证书。
因此 q 进容量等号分支必须继续接目标纤维或其他素因子的残数信息；单独强化 q 进核
不能排除直接命中。

## 限制

式 (5) 只控制移位整数中的 q 进总赋值。它没有说明私有因子是否能组成目标残数
\(-1\pmod{4AC}\)，也没有把不同移位的局部预算注入同一棵容量树。要得到全局选择器，
还需证明私有余因子的避靶条件、字符相位或可提升载体能把这些逐对上界求和为严格不足，
或者在失败时产生良基递降。碰撞层的分区本身也不改变这一限制。
