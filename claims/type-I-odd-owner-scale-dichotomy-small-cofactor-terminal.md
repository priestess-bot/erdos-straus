---
kind: claim
claim_id: type-I-odd-owner-scale-dichotomy-small-cofactor-terminal
title: odd-owner 窗口的尺度二分与深层小余因子 Type II 终端菜单
statement: >-
  固定核心素数 p、奇素数 q 不整除 p 和 j>=1。若 p>4q^(j+1)，标准 owner
  窗口覆盖全部 F_q 横向数字，故已有完整跨纤维关联格 phase lift。互补情形
  p<4q^(j+1) 中，任一深 owner s 满足 q^(j+1)|p+4s、4s<p，并必有
  p+4s=kq^(j+1)，其中 k 属于 {1,3,5,7}。写 s=A^2C=AD、C 平方自由，则该
  owner 的全部 Type II 终端恰由有限菜单 h|kq^(j+1)、h=-1 mod 4D 给出；
  命中时 K=(h+1)/(4D)、B=(Kp+A)/h 构造直接证书，菜单空则是严格的
  deep-owner terminal obstruction。p=409,q=11,s=49 的 k=5 菜单由 h=55
  给出 4/409=1/105+1/5726+1/12270；p=97,q=11,s=6 的 k=1 菜单为空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-odd-owner-fiber-incidence-lattice-source-map
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-raw-ray-certificate
topics:
  - type-I
  - type-II
  - owner
  - q-primary
  - scale-dichotomy
  - small-cofactor
  - terminal-menu
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-odd-owner-fiber-incidence-lattice-source-map
    role: full-window-and-owner-cofactor-input
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: exact-fixed-fiber-terminal-criterion
  - reproduction: reproductions/type_i_odd_owner_scale_dichotomy_small_cofactor_terminal.py
    role: focused-positive-negative-and-scale-boundary-controls
visibility: public
last_checked: '2026-08-09'
---

# odd-owner 窗口的尺度二分与深层小余因子 Type II 终端菜单

## 1. 大窗口或小余因子的无缝尺度二分

设 \(p\equiv1\pmod {24}\) 为素数，\(q\nmid p\) 为奇素数，\(j\ge1\)。
因为 \(p\) 为奇数而 \(4q^{j+1}\) 为偶数，恰有一个严格分支成立：

\[
p>4q^{j+1}
\qquad\text{或}\qquad
p<4q^{j+1}.
\tag{1}
\]

第一种情形已由 owner-window 容量定理处理：标准窗口含首 \(q\) 个
\(q^j\)-prefix owner，横向数字覆盖全部 \(\mathbb F_q\)，任意
\(\mathbb F_q\) phase support 都有完整跨纤维关联格 lift。

现在进入第二种情形，并设标准窗口中有一个深 owner \(s\)，即

\[
0<s,\qquad4s<p,\qquad q^{j+1}\mid p+4s.
\tag{2}
\]

定义

\[
k=\frac{p+4s}{q^{j+1}}\in\mathbb N.
\tag{3}
\]

由 \(4s<p\) 与第二个尺度分支，

\[
0<p+4s<2p<8q^{j+1},
\]

故 \(0<k<8\)。分子与分母都是奇数，所以 \(k\) 为奇数。于是

\[
\boxed{k\in\{1,3,5,7\}.}
\tag{4}
\]

这不是渐近估计，而是每个小尺度深 owner 的精确有限分派。若小尺度窗口没有深
owner，则应返回 DEEP_OWNER_MISSING；不能虚构一个 \(k\)-菜单。

## 2. 深 owner 的完整 Type II 终端菜单

把 \(s\) 规范分解为

\[
s=A^2C=AD,
\qquad C\text{ 平方自由},
\qquad D=AC.
\tag{5}
\]

于是 \(A\mid D\)、\(D/A=C\)，且 \(4AD<p\)。由 (3)--(4)，该参数纤维的完整
来源整数就是

\[
p+4AD=kq^{j+1}.
\tag{6}
\]

固定 \((D,A)\) 的 Type II 因子判据说明：直接终端存在，当且仅当有

\[
\boxed{
h\mid kq^{j+1},
\qquad
h\equiv-1\pmod {4D}.}
\tag{7}
\]

因此完整终端搜索只需枚举

\[
\mathcal H_{q,j,k}(D)
=\{h:h\mid kq^{j+1},\ h\equiv-1\pmod {4D}\}.
\tag{8}
\]

小余因子 \(k\) 只有四种；所有其它变化都在一个 \(q\)-幂块中。若
\(\mathcal H_{q,j,k}(D)=\varnothing\)，则不存在任何由该深 owner 的完整
\(p+4s\) 因子集合产生的 Type II 终端，准确回执为
DEEP_OWNER_SMALL_COFACTOR_TERMINAL_MISS。式 (8) 已穷尽该固定参数纤维的全部除数。

若 \(h\in\mathcal H_{q,j,k}(D)\)，定义

\[
K=\frac{h+1}{4D},
\qquad
B=\frac{Kp+A}{h}.
\tag{9}
\]

因为 \(h\mid p+4AD\) 且 \(4DK=h+1\)，有

\[
K(p+4AD)=Kp+A(h+1)\equiv Kp+A\pmod h,
\]

故 \(B\in\mathbb N\)。同时

\[
B-A
=\frac{K(p-4AD)+2A}{h}>0.
\tag{10}
\]

于是

\[
x=ABC,\qquad y=pACK,\qquad z=pBCK
\tag{11}
\]

满足

\[
\boxed{\frac4p=\frac1x+\frac1y+\frac1z.}
\tag{12}
\]

所以式 (8) 不是容量启发式，而是小尺度深 owner 的充要 Type II 终端菜单。

## 3. 聚焦控制

### 3.1 \(p=409,q=11,j=1,s=49\)：\(k=5\) 的真实终端

\[
409<4\cdot11^2,\qquad
409+4\cdot49=605=5\cdot11^2,
\qquad
(A,C,D)=(7,1,7).
\]

在 \(4D=28\) 下，\(605\) 的除数中唯一负一剩余因子为

\[
h=55\equiv-1\pmod {28}.
\]

式 (9) 给出 \(K=2,B=15\)，因此

\[
\boxed{
\frac4{409}
=\frac1{105}+\frac1{5726}+\frac1{12270}.}
\tag{13}
\]

该控制验证的是 owner 尺度分支与 Type II 菜单的算术闭合；它不声称
\(p=409\) 的某个已选核心 Jacobi 记录必然产生这个 11 阶角色。

### 3.2 \(p=97,q=11,j=1,s=6\)：\(k=1\) 的严格菜单空

\[
97<4\cdot11^2,\qquad
97+4\cdot6=121=11^2,
\qquad(A,C,D)=(1,6,6).
\]

\(4D=24\)，而

\[
\{1,11,121\}\pmod {24}=\{1,11,1\},
\]

不含 \(-1\equiv23\)。所以式 (8) 为空；失败来自完整小余因子菜单，而非单位群
搜索不足。

### 3.3 大尺度边界不能删除

对 \(p=97,q=3,j=1,s=5\)，有

\[
97>4\cdot3^2,\qquad
\frac{97+4\cdot5}{3^2}=13>7.
\]

所以四值结论依赖小尺度假设；大尺度情形应走完整 owner-window phase lift。

## 4. 对选择器的增量与边界

odd-Hall owner 路线现在具有如下尺度分派：

~~~text
OWNER_FIBER_INCIDENCE_C_q
  -> p > 4 q^(j+1): FULL_OWNER_DIGIT_PHASE_LIFT
  -> p < 4 q^(j+1):
       -> no depth-(j+1) owner: DEEP_OWNER_MISSING
       -> deep owner:
            k in {1,3,5,7}
            -> H_{q,j,k}(D) nonempty: TYPE_II_TERMINAL
            -> H_{q,j,k}(D) empty: SMALL_COFACTOR_TERMINAL_MISS
~~~

该结果把大尺度交给完整横向 phase lift，把小尺度深 owner 交给一个完整 Type II
菜单。它没有关闭 DEEP_OWNER_MISSING，也没有把菜单空自动升级为递降；这些分支仍
需利用 exact-height owner、余因子差分加法证书或跨纤维良基势。

## 聚焦验证

~~~bash
python3 reproductions/type_i_odd_owner_scale_dichotomy_small_cofactor_terminal.py --verify
~~~

该 verifier 只重算上述三个控制、完整除数菜单与直接单位分数恒等式。
