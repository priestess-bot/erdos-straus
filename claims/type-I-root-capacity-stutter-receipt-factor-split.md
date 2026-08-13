---
kind: claim
claim_id: type-I-root-capacity-stutter-receipt-factor-split
title: 根容量端点实际 D 的 cyclotomic 排除与 p±1/T 因子分裂
statement: >-
  对核心素数 p≡1 mod24 的根容量端点，令 M0=(p^2+p+1)/3、u=gcd(2r+1,M0)、h=3u，
  并使用实际 maximal complete-excess receipt z=R-h=E D、D|K。则 gcd(D,M0)=1；
  任意 q|M0 若出现在 z 中，其全部 q-幂只进入 E 而不进入 D。进一步令
  C=(p^2-1)/2、K=C T、D_C=gcd(D,C)、D_T=D/D_C，则
  D_C|(h^2-1)、D_T|(h^2-h-2r)，从而 D|(h^2-1)(h^2-h-2r)。
  这些是 actual receipt 的必要算术约束；它们尚未证明 proper-root stutter 门为空，
  也不单独给出 Type I/II 证书或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
topics:
  - type-I
  - overflow
  - root-capacity
  - stutter
  - complete-excess
  - cyclotomic
  - valuations
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: root-endpoint-receipt-and-D-divides-ph-plus-one
  - reproduction: reproductions/type_i_root_capacity_stutter_receipt_factor_split.py
    role: fixed-integer-factor-split-controls
visibility: public
last_checked: '2026-08-13'
---

# 根容量端点实际 \(D\) 的 cyclotomic 排除与因子分裂

## 1. 设置

固定核心素数 \(p\equiv1\pmod {24}\)，并写

\[
M_0=\frac{p^2+p+1}{3},\qquad
u=(2r+1,M_0),\qquad h=3u,
\]

\[
g=\frac{p+1}{2},\qquad T=p^2r-g,\qquad A=gT,\qquad K=A(p-1),
\]

\[
R=2p^3r-p^2-2pr-p+1,\qquad z=R-h.
\]

在真实根容量 endpoint receipt 中，已有

\[
h\mid K,\qquad (h,z)=1,\qquad z=E D,
\qquad D\mid K,\qquad D\mid ph+1.
\tag{1}
\]

这里 \(D\) 是 maximal complete-excess 归一化后的实际除子，不是任意满足同余的抽象
divisor。

## 2. Cyclotomic 排除

### 引理 1

\[
\boxed{(D,M_0)=1.}
\tag{2}
\]

**证明。** 先记 \(p-1=3t\)。由

\[
M_0=t(p+2)+1
\]

可知 \(M_0\) 与 \(p-1\) 互素：素因子 2 不出现，因为 \(M_0\) 为奇数；素因子
3 不出现，因为写 \(p=1+3t\) 得

\[
M_0=1+3t+3t^2\equiv1\pmod3;
\]

其余素因子 \(\ell\mid p-1\) 也满足 \(\ell\mid t\)，故 \(M_0\equiv1\pmod\ell\)。同理，
\((M_0,p+1)=1\)：\(\ell=2\) 不出现，\(\ell=3\) 不整除 \(p+1\)，而对其它
\(\ell\mid p+1\)，有 \(3M_0=p^2+p+1\equiv1\pmod\ell\)。

假设某个素数幂 \(q^d\mid(D,M_0)\)。于是 \(q\ne2,3\)，并且
\(q\nmid(p-1)(p+1)\)。由 \(q^d\mid D\mid K=gT(p-1)\) 得 \(q^d\mid T\)，其中
\(g=(p+1)/2\) 也与 \(q\) 互素。另一方面 \(q^d\mid M_0\) 给出

\[
p^2+p+1\equiv0\pmod {q^d}.
\]

因此

\[
2T=2p^2r-(p+1)
\equiv-(2r+1)(p+1)\pmod {q^d}.
\]

由于 \(q\nmid p+1\)，得到 \(q^d\mid2r+1\)，从而 \(q^d\mid u\) 和 \(q^d\mid h\)。
但 \(q^d\mid D\mid z\)，这与 \((h,z)=1\) 矛盾。故 (2) 成立。证毕。

这个证明同时给出逐素数结论：若 \(q\mid M_0\) 且 \(q\mid z\)，则 \(q\nmid K\)。否则同样的
计算会推出 \(q\mid h\)，再与 \((h,z)=1\) 矛盾。于是该 \(q\)-幂没有旧 \(K\)-容量
可被扣除，按 maximal receipt 的定义全部留在 \(E\) 中：

\[
\boxed{q\mid M_0, q\mid z\Longrightarrow
v_q(D)=0,\quad v_q(E)=v_q(z).}
\tag{3}
\]

## 3. 逐赋值正规形

对每个素数 \(q\)，置

\[
a_q=v_q(A),\qquad c_q=v_q(p-1),\qquad k_q=a_q+c_q=v_q(K),
\qquad b_q=v_q(z).
\]

maximal complete-excess 块的指数为

\[
v_q(Q)=
\begin{cases}
b_q,&b_q>k_q,\\
0,&b_q\le k_q.
\end{cases}
\]

由 \(E=Q/(A,Q)\)、\(D=(z/Q)(A,Q)\) 得

\[
v_q(D)=
\begin{cases}
b_q,&b_q\le k_q,\\
a_q,&b_q>k_q,
\end{cases}
\qquad
v_q(E)=
\begin{cases}
0,&b_q\le k_q,\\
b_q-a_q,&b_q>k_q.
\end{cases}
\tag{4}
\]

式 (4) 说明 (3) 不是把 \(M_0\) 从 \(D\) 中手工删掉：对于 \(M_0\)-素因子，实际
\(K\) 容量先被证明为零，随后 maximal normalization 才强制它们进入 \(E\)。

## 4. \(p\pm1\) 与 \(T\) 的因子分裂

令

\[
C=\frac{p^2-1}{2},\qquad K=CT,\qquad
D_C=(D,C),\qquad D_T=\frac D{D_C}.
\]

允许 \(D_C,D_T\) 共享素因子。逐素数使用 \(D\mid CT\) 可得

\[
D_T\mid T.
\tag{5}
\]

又 \(D_C\mid D\mid ph+1\) 且 \(D_C\mid C\mid p^2-1\)。在模 \(D_C\) 下，
\(ph\equiv-1\) 与 \(p^2\equiv1\) 合起来给出 \(h^2\equiv1\)，故

\[
D_C\mid h^2-1.
\tag{6}
\]

对任意 \(q^d\mid D_T\)，由 \(D_T\mid T\) 和 \(D_T\mid ph+1\)，把恒等式
\(2T=2p^2r-(p+1)\) 乘以 \(h^2\)，并使用 \(ph\equiv-1\pmod {q^d}\)，得到

\[
0\equiv2r-h^2(p+1)\equiv2r-(h^2-h)\pmod {q^d}.
\]

所以

\[
\boxed{D_T\mid h^2-h-2r.}
\tag{7}
\]

综合 (6)--(7)，得到必要的有限因子分裂

\[
\boxed{D\mid (h^2-1)(h^2-h-2r).}
\tag{8}
\]

另外，直接从 \(D\mid ph+1\) 还可读出

\[
(D,p-1)\mid h+1,\qquad (D,p+1)\mid h-1.
\tag{9}
\]

## 5. 对 stutter 门的含义与边界

proper-root 的唯一非严格同余门仍是

\[
D\equiv1-h\pmod p,\qquad D\mid ph+1.
\tag{10}
\]

本引理把 (10) 的实际候选进一步限制为：其 cyclotomic \(M_0\)-部分必须全部位于
\(E\)，而 \(D\) 的 \(p\pm1\) 部分由 \(h^2-1\) 控制，剩余 \(T\)-部分由
\(h^2-h-2r\) 控制。它没有证明 (10) 在核心素数上为空；也没有从 (8) 单独构造
Type I/II 短证书、解提升或严格全局势。下一步若要关闭 hard root，必须把 (8)--(10)
与 actual source/path provenance 或容量素因子 terminal menu 联立，而不能只枚举抽象
divisor gate。

## 6. 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_receipt_factor_split.py --verify
~~~

该 verifier 只重放四个固定核心整数控制（包括 proper-root、饱和根和非平凡 \(T\)-
部分），不执行范围搜索。
