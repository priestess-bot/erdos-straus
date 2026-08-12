---
kind: claim
claim_id: type-I-odd-primary-character-height-antipodal-source-admission
title: 奇主阶记录的最小角色高度与反向对来源准入
statement: >-
  设 H 是核心 Type I Jacobi 图表中 K 的素因子模 R 所生成的单位群，z 是一条
  Jacobi-negative 记录，s_z=-Phi(z)，且奇素数 ell 整除 ord(s_z)。定义
  h= max{j>=0:s_z 属于 H^(ell^j)}。则 h 有限，且 h+1 是使某个角色
  chi:H->C_(ell^(h+1)) 在 s_z 上非平凡的最小目标高度；可取 chi(s_z) 精确
  ell 阶。因而 chi(-1)=1，gamma=chi o Phi 把实际反向记录对的差 2z 送到非零元。
  特别地 h=0 当且仅当 s_z 不属于 H^ell；此时 gamma:Z^r->C_ell 是 whole-ambient
  pullback，2z 是非零的实际 source relation，且 ell 不整除 content(2z)，故该
  记录给出 SOURCE_RANK_DEMAND(ell,1) 与零 q-height source-line depth。若 h>0，
  每个 C_ell 角色都杀掉 s_z；任何由该记录的相位导出的同态 source role 都至少需要
  C_(ell^(h+1))，这是精确的高 primary 分流，而非 E4/E5 出口。规范抽出的 top
  torsion omega_z 的可见高度可以严格大于 s_z 的高度，所以不能用 omega_z 的
  C_ell 可见性拒绝原记录的 elementary source role。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-core-jacobi-punctured-kernel-primary-selector
  - type-I-odd-primary-component-kernel-crt-rechart-descent
  - type-I-odd-primary-component-torsion-rank-collapse
  - type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary
  - type-I-source-lattice-qheight-dual-valuation-shift-carrier
  - denominator-escape-state-contract
topics:
  - type-I
  - odd-primary
  - finite-abelian-groups
  - character-height
  - ambient-pullback
  - source-rank
  - antipodal-records
  - q-height
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-core-jacobi-punctured-kernel-primary-selector
    role: symmetric-Jacobi-negative-records-and-generated-unit-group
  - claim: type-I-odd-primary-component-kernel-crt-rechart-descent
    role: named-s_z-and-top-torsion-extraction
  - claim: type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary
    role: C_ell-visibility-criterion-and-source-carrier-contract
  - claim: type-I-source-lattice-qheight-dual-valuation-shift-carrier
    role: source-line-depth-and-physical-layer-admission
  - reproduction: reproductions/type_i_odd_primary_character_height_antipodal_source.py
    role: focused-visible-record-and-high-primary-top-torsion-controls
visibility: public
last_checked: '2026-08-12'
---

# 奇主阶记录的最小角色高度与反向对来源准入

## 1. 不能把 record phase 与 top torsion 混为同一个角色对象

固定核心图表

\[
p\equiv1\pmod {24},\qquad R\equiv3\pmod4,\qquad 4K=pR+1,
\tag{1}
\]

并令

\[
H=\langle q\bmod R:q^e\Vert K\rangle\le U(R).
\tag{2}
\]

核心 selector 保证 \(-1\in H\)。若 \(z\) 是一条 Jacobi-negative 记录，写

\[
\Phi(z)=-s_z,\qquad s_z\in H\cap\ker\chi_R.
\tag{3}
\]

现固定一个奇素数 \(\ell\mid\operatorname{ord}(s_z)\)。已有 odd-primary
构造会从 \(s_z\) 规范抽出精确 \(\ell\) 阶元 \(\omega_z\)。这个 \(\omega_z\)
适合检查完整 CRT 分量核和 \(V_\ell\) 的秩；但 source role 必须来自一条实际记录
关系，故这里首先检测的是 **\(s_z\)**，而不是只检测 \(\omega_z\)。

对任意 \(u\in H\) 且 \(\ell\mid\operatorname{ord}(u)\)，定义其 \(H\) 内的
\(\ell\)-角色高度

\[
\boxed{
h_\ell^H(u)=\max\{j\ge0:u\in H^{\ell^j}\},
\qquad
H^{\ell^j}=\{v^{\ell^j}:v\in H\}.
}
\tag{4}
\]

由于 \(u\) 的 \(\ell\)-primary 分量非平凡，(4) 的最大值有限。注意这不是
\(u\) 在 \(U(R)\) 中的阶，也不是指数向量的 content；它测量的是 \(u\) 在实际
由 \(K\) 的因子生成的群 \(H\) 中还能被取多少次 \(\ell\) 次根。

## 2. 最小 character height 定理

令 \(h=h_\ell^H(u)\)。则有精确二分：

\[
\boxed{
\begin{aligned}
&\exists\ \chi:H\longrightarrow C_{\ell^{h+1}}
  &&\text{使 }\chi(u)\text{ 精确为 }\ell\text{ 阶},\\
&\operatorname{Hom}(H,C_{\ell^m})\ni\psi
  &&\Longrightarrow\ \psi(u)=1\qquad(1\le m\le h).
\end{aligned}}
\tag{5}
\]

所以 \(h+1\) 恰为检测 \(u\) 所需的最小 cyclic \(\ell\)-primary character
height。特别地，

\[
\boxed{h_\ell^H(u)=0\quad\Longleftrightarrow\quad u\notin H^\ell
\quad\Longleftrightarrow\quad
\exists\chi:H\to C_\ell,\ \chi(u)\ne1.}
\tag{6}
\]

式 (6) 的最后一个等价已在 source-carrier 卡中作为有限阿贝尔群的 elementary
visibility 条件出现；这里的新增内容是 (5) 的最小高度、它对**实际记录对**的拉回，
以及 record phase/top torsion 的必要区分。

### 证明

将 \(H\) 的 \(\ell\)-primary 部分写为

\[
H_\ell\simeq\bigoplus_i C_{\ell^{a_i}}.
\tag{7}
\]

在第 \(i\) 个循环坐标中，将 \(u\) 的 \(\ell\)-primary 分量写成
\(\ell^{b_i}c_i\)，其中非零坐标满足 \(0\le b_i<a_i\) 且
\(\ell\nmid c_i\)。于是

\[
h=\min_{u_i\ne0}b_i.
\tag{8}
\]

取达到最小值的坐标 \(i\)，先投影到 \(C_{\ell^{a_i}}\)，再模
\(\ell^{h+1}\)；得到的同态把该坐标送到 \(\ell^hc_i\)，故其像精确为
\(\ell\) 阶。这给出 (5) 的第一行。反过来，若 \(m\le h\)，由
\(u\in H^{\ell^m}\) 可写 \(u=v^{\ell^m}\)，而任何到
\(C_{\ell^m}\) 的同态都满足

\[
\psi(u)=\psi(v)^{\ell^m}=1.
\tag{9}
\]

这证明最小性和 (6)。

## 3. 反向负记录给出真实 source relation

对 (3) 取 \(u=s_z\)，令 \(h=h_\ell^H(s_z)\)，并按 (5) 选择 \(\chi\)。
因为 \(-1\) 的阶为 2 而 \(C_{\ell^{h+1}}\) 是奇阶群，

\[
\chi(-1)=1,\qquad \chi(\Phi(z))=\chi(s_z)\ne1.
\tag{10}
\]

负记录集合在反演下封闭：\(-z\) 仍是负记录。因而它们的实际指数差

\[
\delta=z-(-z)=2z
\tag{11}
\]

不只是一个 target anchor。由 \(\Phi\) 与 \(\chi\) 都是同态，

\[
\boxed{
\gamma:=\chi\circ\Phi:\mathbb Z^r\longrightarrow C_{\ell^{h+1}},
\qquad
\gamma(2z)=\chi(s_z)^2\ne1.
}
\tag{12}
\]

最后一个不等式使用 \(\ell\) 为奇素数。式 (12) 给出了 named record、实际反向
endpoint、完整 ambient exponent lattice pullback 和非零 source relation；它没有
把单点 Fourier anchor 冒充成 source rank。

若 \(h=0\)，(12) 的余域就是 \(C_\ell\)，并且

\[
\ell\nmid\operatorname{content}(2z).
\tag{13}
\]

否则 \(2z=\ell w\) 会使任何 \(C_\ell\)-valued ambient homomorphism 在
\(2z\) 上为零，矛盾于 (12)。故现有 rank-one source-line 定理的深度为

\[
d_\ell(\mathbb Z(2z),\gamma)=v_\ell(\operatorname{content}(2z))=0.
\tag{14}
\]

这时可发出严格但局部的回执

~~~text
ODD_PRIMARY_AMBIENT_SOURCE_ROLE_READY
  source_role = SOURCE_RANK_DEMAND(ell, 1)
  named_record_pair = (z, -z)
  relation = 2z
  character_height = 1
  whole_ambient_pullback = true
  source_line_qheight_depth = 0
~~~

之后仍须经过既有 carrier 的范围、occurrence、既定标签、target state 和 E4/E5 门。
本卡只关闭了该 residual 在 E1/source-role 前的 "abstract torsion but no ambient
pullback" 缺口，绝不把 (12) 升级为全局递降。

若 \(h>0\)，(5) 的第二行则给出精确阻碍：从这个记录相位导出的 every elementary
\(C_\ell\) character 都为零。可登记

~~~text
ODD_PRIMARY_CHARACTER_HEIGHT_ESCALATION
  minimum_character_height = h + 1
  elementary_C_ell_source_role = obstructed_for_this_record_phase
~~~

这是高 primary source-carrier 的明确输入，而不是证明没有别的 terminal、source 或
descent。

## 4. 两个 full-component 控制与对象区分

### \(p=97,R=67,\ell=11\)：可见的原始 record

这里 \(K=5^3\cdot13\)，\(H=U(67)\simeq C_{66}\)。取负记录
\(z=(-3,0)\)，有

\[
\Phi(z)=52,\qquad s_z=15,\qquad \operatorname{ord}(s_z)=11,
\qquad \omega_z=24.
\tag{15}
\]

以 \(2\) 为 \(H\) 的生成元，离散对数模 11 给出

\[
\log_2\Phi(z)=10,\qquad \log_2s_z=10,\qquad
\log_2\omega_z=9.
\tag{16}
\]

故 \(h_{11}^H(s_z)=0\)，而 \(\gamma(2z)=9\ne0\pmod {11}\)。这里
\(\operatorname{content}(2z)=6\)，验证了 (13)--(14)。它是早先 full-component
residual 的一个真实 E1 source-role 正例；它是否通过后续 carrier range 和完整 lift
是另一个问题。

### \(p=2521,R=163,\ell=3\)：top torsion 隐形不等于 record 隐形

这里 \(K=17\cdot6043\)，\(H=U(163)\simeq C_{162}\)。负记录
\(z=(0,1)\) 给出

\[
\Phi(z)=12,\qquad s_z=151,\qquad \operatorname{ord}(s_z)=81,
\qquad
\omega_z=104.
\tag{17}
\]

以 \(2\) 为生成元，

\[
\log_2s_z=22\pmod{162},\qquad
\log_2\omega_z=54\pmod{162}.
\tag{18}
\]

所以 \(s_z\notin H^3\)，它已经在 \(C_3\) 中可见，且
\(\gamma(2z)=2\ne0\pmod3\)。但

\[
\omega_z\in H^{3^3}\setminus H^{3^4},
\qquad h_3^H(\omega_z)=3.
\tag{19}
\]

所有到 \(C_3,C_9,C_{27}\) 的角色都杀掉 \(\omega_z\)，而到 \(C_{81}\) 的角色将
它送到 \(54\)，仍为精确三阶。这证明用 \(\omega_z\notin H^3\) 作为
record-source admission 条件会错误地拒绝一个已经存在的 ambient \(C_3\) source
role。正确测试对象是 (3) 的 \(s_z\)。

## 聚焦验证

```bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_odd_primary_character_height_antipodal_source.py --verify
```

验证器只重算上述两个核心 F 控制的记录、生成群、幂像高度、cyclic character、反向
差分和 content；不运行历史扫描或结果枚举。
