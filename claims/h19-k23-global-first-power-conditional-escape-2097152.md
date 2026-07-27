---
kind: claim
claim_id: h19-k23-global-first-power-conditional-escape-2097152
title: H19-k23 全局一次幂选择器的 Dickson 条件性逃逸
statement: 假定 Dickson 素数元组猜想，存在无穷多个 H19-k23 实际核心素数，使全部72个全局尾均不存在 d=b*ell 形式的规范 Type II 一新增素因子一次幂证书。构造使用一个压力进程上的73个正、本原、局部可采纳仿射素数型：目标 p 与每个尾剥离基底及固定非基底因子后的余因子同时为素数。故跨全局尾的一次幂选择器不能成为无条件证明路线。
claim_status: conditional
topics:
- type-II
- conditional
- dickson
- prime-tuples
- global-tail-menu
- factor-support
- one-factor
- cross-tail
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局一次幂选择器的 Dickson 条件性逃逸

取全局基底压力种子

\[
p_0=955\,643\,834\,512\,728\,001
\]

所在的 \(v\equiv24\pmod{29}\) 残存进程 \(p=At+C\)。对每个全局尾
\(m=4q-1\)，写

\[
u_m(t)=\frac{p(t)+m}{m+1}.
\]

从 \(u_m(t_0)\) 先剥离规范基底素数的全部固定幂，再剥离其素数已出现在冻结周期中的
全部非基底幂，得到

\[
u_m(t_0+Mn)=H_mK_mL_m(n). \tag{1}
\]

其中 \(H_m\) 只含规范基底素数，\(K_m\) 是固定非基底部分，而 \(L_m(n)\) 是正本原
仿射型。加细周期使 \(H_m,K_m\) 的精确赋值不变，同时每个 \(L_m(n)\) 的模 \(m\)
残数固定。

逐尾穷尽基底除子表明：

\[
\text{每个 }K_m\text{ 的素因子及 }L_m(n)\bmod m
\text{ 都属于一次幂禁止残数集}. \tag{2}
\]

程序得到 73 个型

\[
p(t_0+Mn),\quad L_m(n)\ (m\in\mathcal G), \tag{3}
\]

其中 \(|\mathcal G|=72\)。它们互异、正且本原；对每个不超过 73 的素数，模该素数的
根并不覆盖全体剩余类。因为型的数目为 73，所有更大素数自动也不能被至多 73 个根覆盖，
故 (3) 是 Dickson 意义下可采纳的线性素数元组。

假定 Dickson 猜想，存在无穷多个 \(n\) 使 (3) 的全部值均为素数。取充分大的这类 \(n\)，
每个尾的非基底素因子恰来自 \(K_m\) 的固定因子及唯一的 \(L_m(n)\)，而它们全都由 (2)
禁止。因此对每个全局尾均无

\[
d=b\ell,\qquad
\operatorname{supp}(b)\subseteq\mathcal B_m,\qquad
d\mid\left(\frac{p+m}{4}\right)^2,\qquad
d\le\frac{p+m}{4},\qquad
d\equiv-\frac{p+m}{4}\pmod m. \tag{4}
\]

这在 Dickson 假设下否定
[跨全局尾的一新增素因子一次幂选择器](h19-k23-global-first-power-selector-conjecture.md)。
它不是 Erdős--Straus 猜想的条件性反例。后续的完整除子枚举已表明，在这个固定 72 尾
菜单中，新增素因子的高幂和任意多个非基底素因子也不能恢复 Type II 证书；见
[全局尾完整 Type II 除子的条件性逃逸](h19-k23-global-full-divisor-conditional-escape-2097152.md)。
仍保留的空间是其它全局外尾、不同的递降状态及 Type I 或其它证书类型。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_first_power_conditional_escape.py \
  --input reproductions/h19-k23-global-base-only-prime-obstruction-2097152.json \
  --output reproductions/h19-k23-global-first-power-conditional-escape-2097152.json
python3 -m unittest tests/test_h19_k23_global_first_power_conditional_escape.py -q
~~~
