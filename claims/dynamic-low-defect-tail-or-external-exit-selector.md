---
kind: claim
claim_id: dynamic-low-defect-tail-or-external-exit-selector
title: 动态低缺陷尾或外源出口选择器：Selector-Enew 的反例与 Selector-Pressure 定理
statement: 对核心素数 p，令 B=(p-1)/4。二分候选要求：要么存在 q|B，使相应 p-1 Type II 尾的精确支持缺陷 delta(p,q) 至多为 2；要么存在 k|B，使相应动态外部源满足完整平方尾除子判据。这个 Selector-Enew 的全称版本已被 p=214729、297049、878089 属于 E_new(1000000,20) 的完整穷尽反例否定：三点在任意 q|B 上均无普通 Type II 尾除子，且在任意 k|B 上均无完整平方尾外源出口。相反，H19-k23 两条无固定外源桥的压力进程均由整条进程有效、支持缺陷至多1的固定 Type II 见证证明。该反例否定当前二分选择器，不反驳 Erdos--Straus 猜想。
claim_status: contradicted
proof_provenance: mixed
review_status: independent_review
topics:
- type-II
- type-I
- pure-new-factor
- support-defect
- external-source
- selector
- h19
- pressure-family
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I/II-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 动态低缺陷尾或外源出口选择器：Enew 反例与 Pressure 定理

## 共同接口

令 \(p\equiv1\pmod{24}\) 为素数，并置

\[
B=\frac{p-1}{4}.
\]

这里的“或”是包含性的；同一个 \(p\) 可以同时命中两个分支。

### 分支 T：动态低缺陷 \(p-1\) 尾

对任意 \(q\mid B\)，定义

\[
m_q=4q-1,\qquad u_q=\frac{B}{q}+1,\qquad x_q=qu_q=B+q.
\]

于是

\[
p=4q(u_q-1)+1,\qquad 3\le m_q\le p-2.
\]

定义精确支持缺陷

\[
\delta(p,q)=
\min_{\substack{d\mid x_q^2,\ d\le x_q\\
d\equiv-x_q\pmod{m_q}}}
\left|\operatorname{Supp}(d)\setminus\operatorname{Supp}(q)\right|,
\]

若候选集合为空，则令 \(\delta(p,q)=\infty\)。分支 T 要求存在某个
\(q\mid B\) 使

\[
\delta(p,q)\le2. \tag{T}
\]

每个见证 \(d\) 都必须由精确整数验证器核对 \(d\mid x_q^2\)、\(d\le x_q\) 和
同余条件。由
[普通 Type II 双尾选择器的支持度缺陷判据](type-II-tail-support-defect-criterion.md)，
该见证恢复一张合法 Type II 证书；“至多 2”衡量选择器复杂度，不是数值拟合阈值。

### 分支 E：动态外部源出口

对任意 \(k\mid B\)，定义

\[
r_k=4k-1,\qquad
n_k=\frac{r_kp+1}{4k}=p-\frac{B}{k}<p,
\qquad M_k=kn_k=\frac{r_kp+1}{4}.
\]

分支 E 要求存在 \(k\mid B\) 和整数 \(e\)，使

\[
e\mid M_k^2,\qquad e\le M_k,
\qquad e\equiv-M_k\pmod{r_k}. \tag{E}
\]

因为 \(\gcd(M_k,r_k)=1\)，补除子同余自动成立。令

\[
y=\frac{M_k+e}{r_k},\qquad z=\frac{M_ky}{e},
\]

即可得到可逐项验证的平方尾恒等式

\[
\frac4{n_k}=\frac1{M_k}+\frac1y+\frac1z,
\qquad
\frac4p=\frac1{M_kp}+\frac1y+\frac1z.
\]

因此 (E) 是动态尺度上的严格外源出口；它不要求某个固定 \(k\) 对整条进程有效。

## 两个独立作用域的不同结局

### Selector-Enew（已反驳）

对给定 \(X,H\ge20\)，令 \(E_{\mathrm{new}}(X,H)\) 为所有满足
\(p\le X\)、\(p\equiv1\pmod{24}\) 的素数 \(p\)，并且对每个
\(20\le s\le H\) 都不存在素数 \(\ell\) 满足

\[
\ell\mid p+4s,\qquad
\ell\equiv-1\pmod{M_s},\qquad
\ell\notin\bigcup_{1\le t\le19}\operatorname{Supp}(p+4t),
\]

其中 \(s=a_s^2c_s\)、\(c_s\) 平方自由且 \(M_s=4a_sc_s\)。

`Selector-Enew` 原本断言：每个 \(p\in E_{\mathrm{new}}(X,H)\) 都满足 (T) 或 (E)。
这里的量词必须落在程序实际生成的 \(E_{\mathrm{new}}(X,H)\) 上；211 个同证书
marked bridge 遗漏和 664 个 H19 残余不能替代这个集合。

该全称命题现已被 \(H=20\) 的精确有限反例否定：

\[
p\in\{214729,\ 297049,\ 878089\}\subset E_{\mathrm{new}}(1000000,20).
\]

对三个素数分别穷尽全部 \(q\mid B\) 和 \(d\mid(B+q)^2\) 后，甚至不存在任何满足普通
Type II 同余的 \(d\)，所以分支 T 的缺陷为 \(\infty\)，而不只是大于 2；再穷尽全部
\(k\mid B\) 和 \(e\mid M_k^2\)、\(e\le M_k\) 后，分支 E 也无解。独立实现直接使用
SymPy 的完整除子列表，而不导入主 SPF 选择器；两种实现都给出同一组三点，见
[H=20 完整反例审计](type-II-pure-new-exception-selector-counterexample-1m-h20.md)。

这不与 \(H=50\) 或 \(H=100\) 的零遗漏结果矛盾：增大 \(H\) 会缩小
\(E_{\mathrm{new}}(X,H)\)，而三点在较小窗口 \(H=20\) 的真实补集中。较大窗口的
[10 万](type-II-pure-new-exception-dynamic-selector-100k-h50.md)、
[100 万](type-II-pure-new-exception-dynamic-selector-1m-h100.md) 和
[1000 万](type-II-pure-new-exception-dynamic-selector-10m-h100.md) 复现仍是机制资料，
但不能恢复已被反例否定的全称析取。

### Selector-Pressure

`Selector-Pressure` 断言：H19-k23 中下列两条没有固定因子外部源桥的仿射
压力进程，其每个素数值都满足 (T) 或 (E)：

\[
\begin{aligned}
p_1(n)={}&2\,220\,549\,727\,681\,245\,601\\
&+49\,068\,587\,550\,212\,671\,345\,120\,057\,635\,115\,477\,793\,111\,416\,021\,127\,579\,217\,121\,972\,635\,986\,580\,932\,179\,068\,032\,592\,375\,819\,929\,585\,130\,230\,925\,247\,821\,597\,558\,737\,517\,655\,510\,532\,815\,033\,987\,315\,228\,693\,602\,403\,211\,673\,600\,000\,n,\\
p_2(n)={}&748\,375\,048\,866\,405\,601\\
&+45\,162\,267\,963\,207\,459\,462\,254\,640\,546\,819\,956\,553\,175\,436\,886\,320\,625\,840\,383\,903\,095\,668\,586\,715\,781\,375\,038\,435\,217\,151\,139\,878\,314\,003\,947\,683\,170\,800\,065\,584\,898\,085\,903\,873\,991\,712\,140\,981\,305\,409\,322\,649\,393\,494\,272\,000\,000\,n,
\end{aligned}
\]

其中 \(n\ge0\)。这些步长逐位取自
[固定因子外部源桥审计](h19-k23-global-tail-pressure-external-source-bridge-2097152.md)
及其
[`JSON` 产物](../reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json)，
而不是从两个种子外推得到。

两个种子本身已有变量因子外源出口，见
[压力种子外源剖面](h19-k23-pressure-external-source-seed-profile-2097152.md)；单独的种子
事实原本不足以证明整条仿射进程。不过，进一步的仿射不变量审计已经得到更强结论：

\[
(q_1,d_1)=(15,37845),\qquad
(q_2,d_2)=(90,121014)
\]

分别在两条原始步长 \(P_1,P_2\) 上对每个 \(n\ge0\) 保持 Type II 除子判据，且

\[
\left|\operatorname{Supp}(d_1)\setminus\operatorname{Supp}(q_1)\right|
=
\left|\operatorname{Supp}(d_2)\setminus\operatorname{Supp}(q_2)\right|=1.
\]

因此 Selector-Pressure 已经由分支 T 无条件证明，详见
[两条原压力进程的全体低缺陷尾定理](h19-k23-unbridged-pressure-full-low-defect-rays.md)。
此前的固定尺度、固定外源和固定尾菜单逃逸结果不与此矛盾：新见证来自允许在
\((p-1)/4\) 的全部除子尺度中重新选择 \(q\) 的动态接口。

## 证伪见证与边界

对一个实际素数 \(p\)，完整分解 \(B\)，穷尽全部 \(q\mid B\) 和 \(k\mid B\)，
再完整分解每个 \(x_q\) 与 \(M_k\)，用全部平方除子证明 (T)、(E) 均失败，
即构成该作用域上当前选择器的有限反例。
这样的反例只说明“支持缺陷至多 2 或此外源出口”的二分法过窄；它不说明 \(p\) 没有
其他 Type I/II 证书，更不是 Erdős--Straus 猜想的反例。三个反例事实上已有直接 AC
Type II 终端证书，所以后续路线应加入短证书分支；但不能仅把“支持缺陷至多 2”放宽为
更大常数，因为这里所有普通 Type II 尾除子已经失败。
