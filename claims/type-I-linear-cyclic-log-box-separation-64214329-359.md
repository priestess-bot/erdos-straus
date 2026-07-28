---
kind: claim
claim_id: type-I-linear-cyclic-log-box-separation-64214329-359
title: 64214329 的 F 状态中子群可见与有限指数盒分离
statement: 在 p=64214329、R=359、线性源 (a,s)=(7154,25) 的 F 状态中，K=5763236028 分解为 gamma=2244 与 L=2568287=19*135173。模359有 135173=19^{-1} 且 19 为原根，因此仿射块有限差集只有5个残类而其生成子群是整个 U(359)。共享层拉回与目标反足点交有60个残类，全部进入该子群但与有限仿射差集交为空；将两个仿射指数坐标各自预算扩大 delta 后，60个类的精确最小溢出范围为12到77。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- finite-exponent
- cyclic-log
- subgroup-obstruction
- shared-layer
- negative-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# \(64214329\) 的循环对数有限盒分离

## 状态

取七谱审计中的

\[
p=64{,}214{,}329,\qquad R=359,\qquad (a,s)=(7154,25).
\]

这里

\[
K=\frac{pR+1}{4}=5{,}763{,}236{,}028,
\]

并且线性源的两个块为

\[
\gamma=\frac{sR+1}{4}=2244=2^2\cdot3\cdot11\cdot17,
\]

\[
L=aR+1=2{,}568{,}287=19\cdot135173,
\qquad K=\gamma L.
\]

跨源共享层为

\[
S_R=42{,}636=2^2\cdot3\cdot11\cdot17\cdot19.
\]

## 有限盒与生成子群

模 \(359\) 的单位群阶为 \(358\)，原根可取 \(g=7\)。直接计算得到

\[
\log_g(19)=157,
\qquad
\log_g(135173)=201=-157\pmod{358}.
\]

因此

\[
135173\equiv19^{-1}\pmod{359},
\]

仿射块的中心化差集只有

\[
D_R(L)=\{19^j:-2\le j\le2\}
 =\{1,2,19,180,189\}.
\]

另一方面，\(\gcd(157,358)=1\)，所以 \(19\) 生成整个 \(U(359)\)，从而

\[
H_L=\langle D_R(L)\rangle=U(359).
\]

这说明生成子群层面没有任何障碍，但有限指数盒仍然极小。

## 共享回拉的精确结果

令

\[
D_R(X)=\left\{\prod_{q\mid X}q^{z_q}:|z_q|\le v_q(X)\right\},
\qquad
T_\gamma=\{-x^{-1}:x\in D_R(\gamma)\}.
\]

逐项枚举得到

\[
|D_R(\gamma)|=105,
\qquad
|D_R(S_R)\cap T_\gamma|=60.
\]

由于 \(H_L=U(359)\)，这 60 个类全部为子群可见：

\[
|D_R(S_R)\cap T_\gamma\cap H_L|=60.
\]

但有限仿射盒完全不相交：

\[
\boxed{
D_R(S_R)\cap T_\gamma\cap D_R(L)=\varnothing.
}
\]

所以该状态精确反驳了以下加强命题：

> 共享层把目标拉回类送入仿射块生成子群，就能完成有限 Type I 对齐。

## 指数溢出

对每个 60 个子群可见类，令 \(\delta(t)\) 是把两个仿射坐标的预算

\[
|z_{19}|,|z_{135173}|\le1
\]

同时扩大为 \(1+\delta(t)\) 后首次表示该类所需的最小额外预算。以原根对数逐项穷举完整单位群，
得到

\[
\min_t\delta(t)=12,
\qquad
\max_t\delta(t)=77.
\]

精确分布为：每个 \(\delta\in\{12,13,\ldots,21\}\)、\(\{34,\ldots,39\}\)、\(\{50,\ldots,54\}\) 以及
\(\{68,69,70,71,72,74,75,76,77\}\) 都出现 2 次，合计 60 个类。

这给出当前最明确的“有限指数预算”边界：即使共享层和仿射块生成整个单位群，
预算缺口也可能远大于一个坐标。

## 结论与范围

该结果是一个精确的单状态负边界，不是混合终端选择引理的反例。它不排除改变
源状态、正规形或使用普通 Type II 证书，也不证明任何全称溢出下界。它证明的是：

\[
\boxed{
\text{子群成员关系不能替代有限指数预算控制。}
\]

因此，任何“短证书或递降”证明必须给出额外机制：要么把超出预算的指数转移到一个仍合法的
源/正规形状态并严格下降，要么从同一核心素数的另一状态构造直接终端证书。

## 复现

~~~bash
python3 reproductions/type_i_linear_cyclic_log_box_separation_64214329.py
python3 -m unittest tests.test_type_i_linear_cyclic_log_box_separation_64214329 -q
~~~

结果文件：
[type-i-linear-cyclic-log-box-separation-64214329-359.json](../reproductions/type-i-linear-cyclic-log-box-separation-64214329-359.json)
