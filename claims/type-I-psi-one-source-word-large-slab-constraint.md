---
kind: claim
claim_id: type-I-psi-one-source-word-large-slab-constraint
title: Psi 一层缺陷到 single-external slab 的规范路径字约束
statement: 对 Psi_0=1 的 F 状态，把一层见证定向为 A_0|K、B_0=q_*H、A_0H|K 且 q_* 是唯一容量超额。首条 formal 边唯一并由 q_* 标记；首步正规约分后得到 U_1=H/g_0|K，而补坐标 V_1 必越出 K 容量。若从该后继经标签 r_i、正规公因子 g_i 到达 m=1 的 single-external slab，令 Theta=prod_i(r_i g_i)，并按 U_1、V_1 的后代定向终点为 X_U、X_V，则存在非负整数 u,v 使 Theta X_U=U_1+Ru、Theta X_V=V_1+Rv 且 u+v=Theta-m_1；固定 slab 定向后等价恢复 epsilon 属于 {+1,-1} 的原路径字公式。因此路径证书必须保留累计正规公因子乘积或等价信息，终端外素数也只能首次出生于某条仿射补坐标。该必要条件与线性源、奇偶和模24约束仍不强制现有 slab 终端或容量下降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-psi-one-nearest-fiber-escape-boundary
  - type-I-formal-ranked-pruning-and-external-gap-selector
  - type-I-formal-linear-chart-p-transience-large-slab-anchor
topics:
  - type-I
  - F-state
  - psi-one
  - formal-target-pair
  - path-word
  - q-adic
  - external-slab
  - linear-source
  - proof-boundary
sources:
  - claim: type-I-f-psi-one-nearest-fiber-escape-boundary
    role: one-layer-defect-source
  - claim: type-I-formal-ranked-pruning-and-external-gap-selector
    role: exact-normalized-formal-transition
  - claim: type-I-formal-linear-chart-p-transience-large-slab-anchor
    role: large-slab-and-anchor-interface
visibility: public
last_checked: '2026-08-01'
---

# Psi 一层缺陷到 single-external slab 的规范路径字约束

## 1. 一层源的首边强制性

固定一个线性 F 状态

\[
4K=pR+1.
\tag{1}
\]

把一条 \(\Psi_0=1\) 见证作符号反射和互换定向后，可写成

\[
A_0+B_0=Rm_0,
\qquad (A_0,B_0)=1,
\tag{2}
\]

\[
A_0\mid K,
\qquad B_0=q_*H,
\qquad H\mid K,
\qquad A_0H\mid K,
\tag{3}
\]

其中 \(q_*\mid K\)，但 \(B_0\) 的 \(q_*\)-进指数恰比 \(K\) 多一层；其它坐标均未
超出 \(K\) 容量。由 (2) 模 \(q_*\) 化简，

\[
q_*\nmid RA_0m_0.
\tag{4}
\]

所以首条 excess-prime formal 边唯一：它必须选中 \(B_0\)，标签为 \(q_*\)。令

\[
t_0\equiv-m_0\pmod {q_*},
\qquad1\le t_0<q_*,
\tag{5}
\]

并令该步的正规公因子为

\[
g_0=\gcd\left(H,\frac{A_0+Rt_0}{q_*}\right).
\tag{6}
\]

首后继可定向为

\[
U_1=\frac H{g_0},
\qquad
V_1=\frac{A_0+Rt_0}{q_*g_0},
\qquad
m_1=\frac{m_0+t_0}{q_*g_0}.
\tag{7}
\]

显然 \(g_0\mid H\)，故

\[
\boxed{U_1\mid K.}
\tag{8}
\]

若再有 \(V_1\mid K\)，由 \((U_1,V_1)=1\) 得 \(U_1V_1\mid K\)，而
\(U_1+V_1=Rm_1\) 直接给出原 \(K\) 盒中的中心目标表示，与状态为 F 矛盾。因此

\[
\boxed{V_1\nmid K.}
\tag{9}
\]

特别地，若路径继续，下一条边不可能选没有超额的 \(U_1\) 一侧，只能选补坐标
\(V_1\) 中的某个超额素数。这里强制的是“选哪一侧”，不声称 \(V_1\) 只有一个可选
素数。

## 2. 规范路径字

从节点 \(\{U_1,V_1\}\) 继续取任意有限 formal 路径。对第 \(i\) 条边，记标签为
\(r_i\)，正规公因子为 \(g_i\)，并定义

\[
h_i=r_ig_i,
\qquad
\Theta=\prod_i h_i.
\tag{10}
\]

空路径时约定 \(\Theta=1\)。假设终点位于 \(m=1\)，并定向为

\[
X=Q\alpha,
\qquad Y=\beta,
\qquad X+Y=R.
\tag{11}
\]

先按两个原坐标的后代关系定向终点为 \(X_U,X_V\)。则存在

\[
u,v\in\mathbb Z_{\ge0},
\qquad u+v=\Theta-m_1,
\tag{12}
\]

使

\[
\boxed{\Theta X_U=U_1+Ru,}
\qquad
\boxed{\Theta X_V=V_1+Rv.}
\tag{13}
\]

若仍固定使用 (11) 的 slab 定向，则存在
\(\varepsilon\in\{+1,-1\}\) 和整数 \(u_*\)，使

\[
\boxed{
\Theta Q\alpha=\varepsilon U_1+Ru_*,
}
\tag{14}
\]

\[
\boxed{
\Theta\beta=-\varepsilon U_1+R(\Theta-u_*).
}
\tag{15}
\]

### 证明

单条 formal 边若选中旧坐标 \(C\)，另一坐标为 \(D\)，则未计互换的新坐标为

\[
C'=\frac C{r_ig_i},
\qquad
D'=\frac{D+Rt_i}{r_ig_i}.
\]

所以模 \(R\) 有

\[
h_iC'\equiv C,
\qquad
h_iD'\equiv D.
\tag{16}
\]

不只同余被保留，整数商还具有非负性。若剩余路径已给出
\(\Theta_sE=C'+Ra\)、\(a\ge0\)，则选中侧满足

\[
h_i\Theta_sE=C+R(h_i a).
\]

若剩余路径给出 \(\Theta_sF=D'+Rb\)、\(b\ge0\)，则补坐标侧满足

\[
h_i\Theta_sF=D+R(t_i+h_i b).
\]

两种新系数仍非负。逐边反向归纳得到 (13)。两式相加，并使用
\(U_1+V_1=Rm_1\)、\(X_U+X_V=R\)，便有

\[
u+v=\Theta-m_1,
\]

因而 \(\Theta\ge m_1\)。若改回固定 slab 定向并记录最终是否互换，迭代 (16) 得到

\[
\Theta X\equiv\varepsilon U_1\pmod R,
\qquad
\Theta Y\equiv-\varepsilon U_1\pmod R.
\tag{17}
\]

第一式定义整数 \(u_*\)。又因 \(X+Y=R\)，两式的整数商之和必须为 \(\Theta\)，即得
(14)--(15)。

这个证明解释了为什么只记录标签乘积 \(\prod r_i\) 不够：路径证书必须保留累计正规
贡献 \(\prod g_i\) 或能恢复它的等价信息。若再把 large-slab 的 \(e\) 条
\(q\)-peeling 接到锚点，完整路径字乘积变为 \(\Theta Q\)，而 (14) 的左端保持为
\(\Theta Q\alpha\)。

## 3. 外素数的出生位置

源坐标 \(A_0,B_0\) 的全部素数都在 \(\operatorname{supp}(K)\)。一条 formal 边只会：

1. 从被选坐标除去 \(r_i\) 和正规公因子 \(g_i\)；
2. 从另一坐标的仿射量 \(D+Rt_i\) 形成新补坐标；
3. 再由 \(g_i\) 删除公因子。

除法和正规约分都不能创造新素数。因此终点若含 \(q\nmid K\)，它第一次出现时必来自
某一步的仿射补项 \(D+Rt_i\)，不可能来自被除坐标或 \(g_i\)。这给出了追踪
single-external slab 来源边的确定位置，但尚未把该边升级为 E4。

## 4. slab 本身的无条件算术约束

若 (11) 还是 single-external slab，满足

\[
K=\alpha\beta c,
\qquad Q=q^e,
\qquad q\nmid K,
\tag{18}
\]

则由 \(4K=pR+1\) 和 \(R=Q\alpha+\beta\) 直接得到

\[
\boxed{
\beta(4\alpha c-p)=\alpha pQ+1.
}
\tag{19}
\]

因此

\[
\boxed{
\alpha\mid p\beta+1,
\qquad
\beta\mid pQ\alpha+1.
}
\tag{20}
\]

若还有真正线性源

\[
p=a+s+asR,
\tag{21}
\]

则

\[
(aR+1)(sR+1)=4K,
\tag{22}
\]

\[
p-(a+s+as\beta)=\alpha asQ.
\tag{23}
\]

对奇数外素数 \(q\)，由 \(q\nmid4K\) 和 \(R\equiv\beta\pmod q\) 还可推出

\[
(a\beta+1,Q)=(s\beta+1,Q)=1.
\tag{24}
\]

式 (24) 不能不加区分地用于 \(q=2\)，因为此时 \(2\nmid K\) 仍不意味着
\(2\nmid4K\)。

结合 \(p\equiv1\pmod {24}\) 与 large-slab 的
\(\alpha\in\{1,2,3\}\)，还有：

- \(q=2\) 时，\(K\) 为奇数、\(R\equiv3\pmod8\)，且 \(\alpha,\beta\) 为奇数；
- \(q\) 为奇数时，\(K\) 为偶数、\(R\equiv7\pmod8\)，且 \(\alpha,\beta\) 异奇偶；
- \(\alpha=2\) 时 \(q\) 为奇数且 \(\beta\equiv1\pmod4\)；
- \(\alpha=3\) 时 \(q\ne3\)、\(\beta\equiv R\equiv2\pmod3\)；进一步，
  \(q=2\) 时 \(R\equiv11\pmod {24},\beta\equiv5\pmod6\)，\(q\) 为奇数时
  \(R\equiv23\pmod {24},\beta\equiv2\pmod6\)。

## 5. 量词边界

(12)--(24) 都是必要条件，不是新终端。冻结源见证锚定的 formal Reach 中，三个
\(\alpha=1,2,3\) 分支各自都有同时满足这些来源约束、但现有双碰撞和规范容量吸收仍
失败的节点。尤其

\[
(p,R,K)=(5596369,35,48968229),
\qquad(Q,\alpha,\beta)=(32,1,3)
\]

的规范路径中有一步 \(g_i=4\)。相对原始节点的全路径正规乘积为 \(118184\)，全路径
纯标签乘积为 \(29546\)；而定理 (13)--(15) 从首后继开始，故其
\(\Theta=(2\cdot4)\cdot17\cdot11=1496\)，相应后缀纯标签乘积为 \(374\)。取
\(U_1=237,V_1=8,\varepsilon=1,u_*=1361\) 时，

\[
1496\cdot32=237+35\cdot1361,
\qquad
1496\cdot3=-237+35(1496-1361),
\]

逐式验证 (14)--(15)。按祖先坐标追踪的两个非负系数则为

\[
(u,v)=(1361,128),
\qquad1361+128=1496-7.
\]

该节点的完整 formal 后继图也没有任何 good single slab。精确路径、完整
计数及另一个 \(\alpha=3\) 四周期见
[源见证锚定的 formal Reach large-slab 边界](type-I-psi-one-actual-reach-large-slab-boundary.md)。
