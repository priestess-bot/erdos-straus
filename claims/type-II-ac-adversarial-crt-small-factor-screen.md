---
kind: claim
claim_id: type-II-ac-adversarial-crt-small-factor-screen
title: Type II 规范扇的 CRT 小好因子屏蔽与六射线压力点
statement: 对有限规范 Type II 扇的每条射线任选 r 映到负 r 逆的半大小横截面，并对有限个不整除扇模数的素数逐一避开会令 p+4s 落入横截面补集的根；只要每个局部禁根集保留非零余类，CRT 给出原始核心素数等差进程，其中没有被筛选的小好因子。对移位 s=1,...,6、确定横截面 T4={1}, T8={1,3}, T12={1,5}, T20={1,3,7,9}, T24={1,5,7,11} 及素数不大于29的屏蔽，进程 p=1 mod 5175754584 的首个六射线共同失败核心素数 p=87987827929；六条失败均为负一不在素因子残数生成子群中的支撑外型。该屏蔽仅控制有限小素因子；实际完整分解仍必须检查，结果不是 Erdős--Straus 反例或任何有界 AC 盒的反例。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-II
- ac-rays
- crt
- adversarial-search
- factorization
- divisor-residues
- canonicalization
- finite-experiment
- proof-program
sources:
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
- paper: grynkiewicz_marchan_ordaz2009
  locator: subsequence-product framework
  role: half-transversal-failure-necessary-condition-context
visibility: public
last_checked: '2026-07-28'
---

# Type II 规范扇的 CRT 小好因子屏蔽与六射线压力点

## 有限屏蔽构造

令 \(\mathcal S\) 为有限个不同的规范移位，写

\[
s=a_s^2c_s,\qquad c_s\ \text{平方自由},\qquad
M_s=4a_sc_s,\qquad N_s=p+4s. \tag{1}
\]

在 \(U(M_s)\) 中，映射

\[
r\longmapsto-r^{-1} \tag{2}
\]

没有不动点。取每个二元轨道的一个代表，得到任意一个半大小横截面
\(T_s\subset U(M_s)\)。若第 \(s\) 条射线失败，则 \(N_s\) 的全部素因子残数必须落在某个这样的横截面内；固定一个 \(T_s\) 只是选择这个必要条件的一支。

现在取有限个与所有 \(M_s\) 互素的奇素数 \(\ell\)。若

\[
\ell\bmod M_s\notin T_s, \tag{3}
\]

则要求 \(\ell\nmid N_s\) 等价于避免唯一根

\[
p\not\equiv-4s\pmod\ell. \tag{4}
\]

将所有这样的根汇为 \(F_\ell\subset\mathbb Z/\ell\mathbb Z\)。只要

\[
(\mathbb Z/\ell\mathbb Z)^\times\setminus F_\ell\ne\varnothing \tag{5}
\]

对每个筛选素数成立，就可任选一个剩余 \(b_\ell\) 并与 \(p\equiv1\pmod{24}\) 合并。
中国剩余定理给出一个原始等差进程

\[
p\equiv b\pmod Q,\qquad (b,Q)=1,\qquad b\equiv1\pmod{24}. \tag{6}
\]

进程中的每一个素数都满足：没有被筛选的素数会作为落在 \(T_s\) 补集的因子整除任一 \(N_s\)。

这只是有限小因子屏蔽。横截面条件本身只是射线失败的必要条件，且 (6) 对大素因子没有限制；所以不能从 (6) 推出某条射线失败，更不能推出 Erdős--Straus 反例。

## 六射线实例

取

\[
\mathcal S=\{1,2,3,4,5,6\}.
\]

其规范对与模数为

\[
(a_s,c_s,M_s)=(1,1,4),(1,2,8),(1,3,12),(2,1,8),(1,5,20),(1,6,24). \tag{7}
\]

使用确定横截面

\[
T_4=\{1\},\quad T_8=\{1,3\},\quad T_{12}=\{1,5\},\quad
T_{20}=\{1,3,7,9\},\quad T_{24}=\{1,5,7,11\}. \tag{8}
\]

对所有 \(\ell\le29\) 且 (4) 实际给出禁根的素数，逐项选择 \(p\equiv1\pmod\ell\)。禁根均不包含 \(1\)，于是 (6) 具体成为

\[
\boxed{p\equiv1\pmod Q,\qquad
Q=5\,175\,754\,584.} \tag{9}
\]

按正 multiplier 递增枚举这个进程的核心素数后，首个六条射线同时失败的点为

\[
p=87\,987\,827\,929=1+17Q. \tag{10}
\]

对其六个移位数完整分解：

\[
\begin{array}{c|l}
s&N_s=p+4s\\ \hline
1&87987827933\\
2&3\cdot29329275979\\
3&13\cdot53\cdot127703669\\
4&5\cdot17\cdot1035150917\\
5&3\cdot7\cdot61\cdot68686829\\
6&1747\cdot50365099.
\end{array} \tag{11}
\]

逐一枚举每个 \(N_s\) 的**全部**因子，均没有

\[
h>1,\qquad h\equiv-1\pmod{M_s}. \tag{12}
\]

因此这六条规范 AC 射线都失败。完整 JSON 同时保存此前四个进程素数的实际因子和出口；
其中一些未筛选大因子立即释放证书，这正是本工具必须完整验因子、不能仅报告 CRT 屏蔽的原因。

## 六条失败的支撑诊断

对每条射线，令 (G_s) 为其素因子残数在
((\mathbb Z/M_s\mathbb Z)^\times) 中生成的子群。该点的六条失败都属于

\[
-1\notin G_s. \tag{13}
\]

也就是说，它们全是“支撑外”失败，并非一孔临界或有限指数饱和。工件对每个完整分解保存
素因子残数、生成子群、实际除子残数和缺失残数；独立测试重新计算这些集合。故这个例子给出
一个精确的有限压力样本：跨移位的坏字符/子群障碍可在至少六条规范 AC 射线上同时相容。
这仍不排除更宽扇、其它 AC 射线、普通尾或 Type I 出口。

\[
\begin{array}{c|c|c|c}
s&M_s&\text{素因子残数生成的 }G_s&-1\bmod M_s\\ \hline
1&4&\{1\}&3\\
2&8&\{1,3\}&7\\
3&12&\{1,5\}&11\\
4&8&\{1,5\}&7\\
5&20&\{1,3,7,9\}&19\\
6&24&\{1,19\}&23
\end{array} \tag{14}
\]

## 研究用途和边界

这给出一个按用户选择的横截面和筛选阈值生成困难点的确定性程序，而不是顺序扫描。它适合记录：

- 多条射线的真实失败数；
- 碰撞因子与私有因子的残数状态；
- 首个未筛选因子如何重新释放证书；
- 同一点的普通尾、外源和 Type I 出口。

当前实现只冻结前六条规范射线；\(p=87\,987\,827\,929\) 仍可能有扇外 AC 证书或其它机制的证书，且本卡没有对它们作否定。因此该点是跨移位字符/积集理论的训练样本，不是猜想的候选反例。

可复现：

~~~bash
python3 reproductions/type_ii_ac_adversarial_crt_search.py
python3 -m unittest tests.test_type_ii_ac_adversarial_crt_search -v
~~~
