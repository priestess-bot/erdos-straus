---
kind: claim
claim_id: type-I-g-anchor-jacobi-raw-terminal-source-switch-bridge
title: G-anchor Jacobi-odd raw 终端唯一性与 source-switch 退化
statement: 对核心素数 p，G-anchor 的每个实际 Jacobi-odd raw 端点都不是固定 (R,K) 图表的 Type I 汇点。gap=3 仍是同一 p 的独立精确终端检验；若 7|Q，则同一标签条件平行地给出 gap=7 Type II 叶。更强地，对候选原始因子 h=delta>0，若 delta|Q、delta=3 (mod 4)，则其 raw normal form 非空当且仅当 delta=7，且唯一参数为 (A,C,k,h)=(1,1,2,7)。它给出一张 raw Type II 叶，但压缩后的 canonical D 等于 1；故此 G-anchor raw 分支不能产生严格 canonical D-lattice source-switch 或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - gap-three-criterion
  - type-II-a-one-gap-three-factor-terminal
  - type-II-raw-ray-certificate
  - type-I-linear-escape-canonical-d-lattice-source-menu
topics:
- type-I
- G-state
- G-anchor
- Jacobi-symbol
- raw-path
- Type-I-terminal-boundary
- Type-II
- gap-three
- gap-seven
- raw-ray
- source-switch
- no-go
- proof-program
sources:
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: actual-Jacobi-odd-raw-path-menu
  - claim: gap-three-criterion
    role: exact-gap-three-iff
  - claim: type-II-a-one-gap-three-factor-terminal
    role: explicit-gap-three-Type-II-leaf
  - claim: type-II-raw-ray-certificate
    role: raw-normal-form-to-Type-II-leaf
  - claim: type-I-linear-escape-canonical-d-lattice-source-menu
    role: canonical-D-lattice-interpretation
  - reproduction: reproductions/type_i_g_anchor_jacobi_raw_terminal_source_switch_fixture.py
    role: constant-size terminal and source-switch-degeneracy fixture
visibility: public
last_checked: '2026-08-05'
---

# G-anchor Jacobi-odd raw 终端唯一性与 source-switch 退化

## 1. 所有 Jacobi-odd 端点都不是固定图表的 Type I 汇点

固定

\[
p\equiv1\pmod {24},
\qquad
R=p-2,
\qquad
K=\frac{(p-1)^2}{4},
\qquad
Q=\frac{p-3}{2}.
\tag{1}
\]

对每个 \(\delta\mid Q\)，G-anchor 的实际 raw 路径可达

\[
X_\delta=\frac{2Q}{\delta},
\qquad
Y_\delta=R-X_\delta.
\tag{2}
\]

这里不必先假设 \(\delta\) Jacobi-odd。因为 \(X_\delta\mid R-1\)，有
\((X_\delta,R)=(Y_\delta,R)=1\)，并且

\[
Y_\delta\equiv-X_\delta\pmod R.
\tag{3}
\]

G 图表的 Jacobi 角色满足 \(\chi_R(-1)=-1\)，而每个 \(q\mid K\) 都有
\(\chi_R(q)=1\)。故

\[
\chi_R(X_\delta Y_\delta)
=\chi_R(-X_\delta^2)
=-1.
\tag{4}
\]

可是 \(K\) 的任一正除子在 \(\chi_R\) 下的像均为 \(+1\)。于是

\[
\boxed{X_\delta Y_\delta\nmid K\qquad(\delta\mid Q).}
\tag{5}
\]

特别地，\(\mathcal D_p^-\) 中的每个 Jacobi-odd 路径端点都不是同一
\((R,K)\) 图表的 Type I 汇点。这只排除固定图表内的直接 terminal，不排除后续 raw
步、其它 Type I/II 正规形或递归提升。

## 2. 同一核心素数上的两个独立 terminal 门

### 2.1 gap \(=3\) 的 companion test

\(\delta=Q\) 总在 \(\mathcal D_p^-\)，并给出实际端点

\[
(1,2Q,1)\leadsto(2,p-4,1),
\qquad
3\mid p-4.
\tag{6}
\]

它不强制任何 gap \(=3\) 因子；但同一素数的 terminal-first companion 是

\[
x_3=\frac{p+3}{4}.
\tag{7}
\]

由 gap \(=3\) 判据，

\[
\boxed{
x_3\text{ 含一个 }q\equiv2\pmod3\text{ 的素因子}
\Longleftrightarrow
\text{存在 gap }3\text{ 的 Type I/II 直接证书}.
}
\tag{8}
\]

若 \(q\mid x_3\) 且 \(q\equiv2\pmod3\)，一张显式 Type II 证书为

\[
\frac4p
=\frac1{x_3}
+\frac1{p(x_3+q)/3}
+\frac1{p x_3(x_3+q)/(3q)}.
\tag{9}
\]

这是同一 \(p\) 上的独立 terminal test，不是从 (6) 单独推出的递归边。
而 \(p=24t+1\) 时 full label \(\delta=Q=12t-1\equiv11\pmod {12}\)，故它不可能是
第 3 节的 \(\delta=7\) raw 命中；gap \(=3\) companion、full-\(Q\) 路径和 raw
\(h=7\) 是三个不同分支，不能串成一条递归链。

### 2.2 \(7\mid Q\) 的平行 gap \(=7\) 叶

若 \(7\mid Q\)，则 \(p\equiv3\pmod7\)、\(R\equiv1\pmod7\)。二次互反律给出

\[
\chi_R(7)=\left(\frac7R\right)=-1,
\qquad
7\mid p+4.
\tag{10}
\]

因此 \(7\in\mathcal D_p^-\)，而同一标签条件平行地触发 \(p+4\) 的 gap \(=7\)
Type II 叶。令 \(x_7=(p+7)/4\)，则 \(7\mid x_7+1\)，且

\[
\boxed{
\frac4p
=\frac1{x_7}
+\frac1{p(x_7+1)/7}
+\frac1{p x_7(x_7+1)/7}.
}
\tag{11}
\]

若 \(h>1\) 是 \(Q\) 的因子且 \(h\mid p+4\)，则

\[
h\mid\gcd(p-3,p+4)=7,
\tag{12}
\]

所以 \(h=7\)。这不是下节 raw 叶与 gap \(=7\) 叶相同的断言；它们只共享同一个
\(7\mid Q\) 条件。

## 3. Jacobi-odd raw normal form 的唯一命中

现在固定候选原始因子 \(\delta=h>0\)，满足

\[
\delta\in\mathcal D_p^-,
\qquad
\delta\mid Q,
\qquad
\delta\equiv3\pmod4.
\tag{13}
\]

令 \(\mathscr R_p(\delta)\) 表示全部 raw normal-form 参数对：

\[
\mathscr R_p(\delta)=
\left\{(A,C):
\begin{array}{l}
A,C\in\mathbb N,\quad AC\mid(\delta+1)/4,\\
\delta\mid4A^2C+3,\\
k(p-4A^2C)+2A\ge0,
\quad k=\dfrac{\delta+1}{4AC}
\end{array}
\right\}.
\tag{14}
\]

这正是既有 raw normal form 的 \(h=\delta\) 专门化，而不是“\(\delta\mid h\)”的
宽泛表述。设 \((A,C)\in\mathscr R_p(\delta)\)。则

\[
\delta=4ACk-1.
\tag{15}
\]

又 \(\delta\mid Q\) 蕴含 \(p\equiv3\pmod\delta\)。结合第二个条件，

\[
k(4A^2C+3)
=A(4ACk-1)+(A+3k)
=A\delta+A+3k,
\tag{16}
\]

所以 \(\delta\mid A+3k\)。两边为正，故

\[
4ACk-1\le A+3k,
\qquad
A(4Ck-1)\le3k+1.
\tag{17}
\]

若 \(k=1\)，(17) 只允许 \(A=C=1\)，此时 \(\delta=3\) 而
\(3\nmid A+3k=4\)，矛盾。若 \(k\ge3\)，即使 \(A=C=1\) 也有
\(4Ck-1>3k+1\)，矛盾。若 \(k=2\)，则

\[
A(8C-1)\le7,
\tag{18}
\]

强制 \(A=C=1\)，从而 \(\delta=7\)。反过来，若 \(7\mid Q\)，取

\[
(A,C,k,\delta)=(1,1,2,7)
\tag{19}
\]

满足 (14) 的全部条件，且 \(B=(2p+1)/7>A\)。因此

\[
\boxed{
\mathscr R_p(\delta)\ne\varnothing
\Longleftrightarrow
\delta=7,
\qquad
\mathscr R_p(7)=\{(1,1)\}.
}
\tag{20}
\]

唯一 raw Type II 叶的首分母与 gap 参数为

\[
x_{\rm raw}=B=\frac{2p+1}{7},
\qquad
d_{\rm raw}=1,
\qquad
m_{\rm raw}=\frac{p+4}{7}.
\tag{21}
\]

它通常不同于 (11) 的 \(x_7=(p+7)/4\)、\(m=7\)：二者不是同一证书，也不是
原 raw 路径的互译，只是同由 \(7\mid Q\) 触发。

## 4. source-switch 退化 no-go

唯一命中 (19) 有

\[
s=A^2C=1.
\tag{22}
\]

把 \(s=a^2c\) 作平方自由压缩，只能得到

\[
a=c=D=1.
\tag{23}
\]

而 \(\mathcal L_1(p)=\{(1,1)\}\)。所以该 raw 叶只产生 self target，且不存在
\(D'<D\)。因此

\[
\boxed{
\text{本卡的 }\delta=h,\ \delta\mid Q\text{ Jacobi-odd raw normal-form branch 不产生严格 canonical D-格 source-switch。}
}
\tag{24}
\]

该结论只关闭本卡定义的 raw normal form 到严格 D-格边的桥。它不排除 (9)、(11)、
其它 raw 参数化、F/G 外部来源、Fourier/SNF 证书或改变方程目标的路径。

## 5. 常数边界

\[
\begin{array}{c|c|c|c}
p&\mathcal D_p^-&\text{直接 terminal}&\text{raw normal form}\\ \hline
73&\{7,35\}&7\mid Q\text{，gap }7\text{ 叶}&h=7\text{ 唯一 raw 叶，且 }D=1\\
97&\{47\}&x_3=25\text{，gap }3\text{ 叶}&\mathscr R_{97}(47)=\varnothing\\
193&\{19,95\}&\text{无本卡的简单叶}&\mathscr R_{193}(19)=\mathscr R_{193}(95)=\varnothing
\end{array}
\tag{25}
\]

常数规模复现见
[G-anchor raw terminal and degeneracy fixture](../reproductions/type_i_g_anchor_jacobi_raw_terminal_source_switch_fixture.py)。
