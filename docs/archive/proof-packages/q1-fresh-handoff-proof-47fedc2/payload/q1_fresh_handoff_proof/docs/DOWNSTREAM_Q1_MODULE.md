# q=1 full-carrier 专属模块的下游组合闭包

本文档不是证明 T6。它说明 T4 handoff 后，`47fedc2` 中已有哪些 q=1 专属算术继续被闭合，以及这些结果如何组合。

## 1. 第一 strict child

从 root

\[
R_X=16t+3,
\qquad
K_X=(6t+1)(16t+1),
\qquad A=1
\]

出发，anchor excess 为

\[
M=R_X-1=16t+2.
\]

因为 `(M,K_X)=1`，首步无选择。

- `t` 奇：

\[
R_H=20t+3,
\quad
K_H=(8t+1)(15t+1),
\quad
A=16t+2.
\]

- `t=2s` 偶：

\[
R_H=12s-1,
\quad
K_H=9s(16s-1),
\quad
A=9s.
\]

两者均有 strict local support decrease。

## 2. 第二 anchor 必 high overflow

### 奇支

\[
R_H-1=2(10t+1).
\]

完整超额为

\[
Q=10t+1,
\quad\beta=2,
\quad
M=2(8t+1)(10t+1).
\]

所有携带旧 support `A=2(8t+1)` 的 low chart 同余于 `R_H mod 4A`。低区间只包含原 chart；但新 `M` 不整除原 `K_H`，故不能低重图表：

\[
R_M>p.
\]

### 偶支

令 `t=2s`。anchor 为

\[
2(6s-1).
\]

若 `6s-1` 的全部素数幂都不超出 `K_H=9s(16s-1)` 的容量，则由 `(6s-1,9s)=1` 会有

\[
6s-1\mid16s-1.
\]

但

\[
16(6s-1)-6(16s-1)=-10,
\]

迫使 `6s-1 | 10`，与 `s>=2` 矛盾。因此完整超额含某个

\[
q\mid6s-1.
\]

该 `q` 不整除

\[
B_p=576s^2.
\]

低同余窗只有原 chart 与 `p-2`；前者违反 complete-excess，后者的 `K=B_p` 又不能承载 `q`。所以

\[
R_M>p.
\]

## 3. 第二 anchor fixed-`n` strict macro

transient overflow 统一给出

\[
pn=4Md+1,
\qquad1\le d<p.
\]

若 `L|Md`，写

\[
\frac{Md}{L}=ph+\delta,
\qquad1\le\delta<p,
\]

定义

\[
n_T=n-4Lh,
\quad
R_T=4L-n_T,
\quad
K_T=L(p-\delta).
\]

则

\[
pn_T=4L\delta+1,
\qquad
pR_T+1=4K_T,
\qquad
L\mid K_T.
\]

### 奇支 carrier

取

\[
L_o=2(10t+1).
\]

有

\[
L_o>A,
\quad
L_o\mid M,
\quad
L_o\le B_p,
\]

且

\[
\left\lfloor\frac{B_p}{L_o}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

这是 paid-reset strict macro。

### 偶支 carrier

取 complete-excess 中最小的

\[
q_*\mid6s-1
\]

并令

\[
L_e=9sq_*.
\]

因为

\[
q_*<64s=B_p/A,
\]

有

\[
A<L_e\le B_p
\]

并严格下降

\[
\left\lfloor\frac{B_p}{L_e}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

## 4. unit defect 被统一排除

fixed-`n` remainder `delta` 满足

\[
\delta=1
\iff
p\mid4L+1.
\]

对 odd carrier `L_o` 和 even carrier `L_e` 均可直接排除该整除，所以

\[
\boxed{\delta\ge2.}
\]

若第一 macro target 仍 high，则取 full product

\[
S_T=L\delta
\]

作为下一 carrier，得到 persistent `d=1` receiver：

\[
A=S_T,
\quad
R=(p-1)n_T-1,
\quad
K=A(p-1).
\]

因为 `delta>=2`，该第二 edge 继续严格下降。

## 5. immediate `d=1` receiver 的 p-free failure 不可能

一般 `d=1` receiver 唯一的 p-free arithmetic gate 是

\[
n\equiv-2\pmod p.
\]

### 奇支

fixed-`n` 公式给出唯一 `1<=j<=13`：

\[
14\delta+3=jp,
\]

以及

\[
21n=5jp+7j-15.
\]

若 `n=-2 mod p`，则

\[
p\mid7j+27.
\]

由于 `p>=73` 且 `34<=7j+27<=118<2p`，只能

\[
p=7j+27.
\]

再结合 `p=1 mod 24` 得唯一形式

\[
j=10,\quad p=97,\quad t=4,
\]

与奇 `t` 矛盾。

### 偶支

有

\[
3q_*\delta-4=jp,
\qquad1\le j<3q_*<p,
\]

且

\[
j\equiv2\pmod3,
\qquad
4n=jp+4-j.
\]

若 `n=-2 mod p`，则 `j=12`，但

\[
12\not\equiv2\pmod3.
\]

矛盾。

所以 q=1 immediate receiver 总通过 p-free bundle gate。

## 6. regeneration 最多一次

令

\[
\alpha=(p+1)/2=ga,
\qquad
v=(n+1)/2=gb,
\]

完整超额 multiplier 为

\[
E=(p-1)b-a.
\]

regeneration 等价于

\[
E\equiv1\pmod p.
\]

### 奇支

可推出必要条件

\[
p\mid N=7j+42g+27,
\]

且 `N<=790`。于是只需检查由该不等式**理论上强制出来**的有限素数候选；全部矛盾。因此奇支从不 regeneration。

### 偶支

regeneration 强制

\[
g=1,
\quad j=20,
\quad n=5p-4,
\quad q_*=23.
\]

并且

\[
E-1=p\frac{5p-9}{2},
\]

所以

\[
\nu_p(E-1)=1.
\]

下一 relay 有

\[
E'\not\equiv1\pmod p,
\]

故不再 regeneration，并严格降到某个

\[
1\le c\le p-2.
\]

因此 immediate q=1 `d=1` receiver 在至多两条 strict relay 后离开 regeneration tail。

## 7. 组合结论

从 ordinary `q=1 G` endpoint 出发：

1. fresh root-entry；
2. 第一 strict child；
3. 第二 anchor fixed-`n` strict macro；
4. 若仍 high，full-product strict edge 到 `d=1` receiver；
5. complete-excess relay；
6. 若发生唯一 even regeneration，再做一条 strict relay。

因此 q=1 **专属** top-capacity / regeneration machinery 不会无限停留。

但第 6 步后的 target 通常已经是一般 Type I state。它是否总能继续 terminal/strict，属于 T6。
