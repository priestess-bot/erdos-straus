---
kind: claim
claim_id: type-II-congruence-kernel-split-fourier-certificate
title: Type II 同余核分裂的有限 Fourier 证书
statement: 对有限阿贝尔群 G、子群 K 和积集 P，按 G/K 的每个陪集取截面 S_x={k∈K:xk∈P}。P 被 K 饱和当且仅当每个截面为空或等于 K；若目标 t 不在 P 但 pi(t) 在 pi(P)，则目标截面 S_t 是不含 1 的非空真子集。对 n=|S_t|，其非平凡 K-字符满足 sum_{chi!=1}|sum_{k∈S_t}chi(k)|^2=n(|K|-n)，故至少有一个字符系数平方不小于 n(|K|-n)/(|K|-1)。p=97、P={1,11}、K=ker(U(24)->U(4)) 给出 S_{-1}={13} 的显式核 Fourier 证书；该证书是核不包含稳定子时的规范对偶出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-I-f-g-fourier-obstruction-certificate
topics:
- type-II
- congruence-kernel
- kernel-fourier
- split-fiber
- target-fiber
- generalized-dyadic
- dual-certificate
- pseudo-hit
- proof-program
sources:
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: saturated-versus-unsaturated-quotient-branch
  - claim: type-I-f-g-fourier-obstruction-certificate
    role: finite-character-certificate-template
visibility: public
last_checked: '2026-08-04'
---

# Type II 同余核分裂的有限 Fourier 证书

## 陪集截面

令 \(G\) 为有限阿贝尔群，\(K\le G\)，\(\pi:G\to G/K\) 为商映射，且
\(P\subseteq G\)。对每个 \(\bar x\in G/K\) 选代表 \(x\)，定义截面

\[
S_{\bar x}=\{k\in K:xk\in P\}\subseteq K,
\qquad n_{\bar x}=|S_{\bar x}|.
\tag{1}
\]

截面定义与代表选择无关（只差一个 \(K\) 内平移）。显然

\[
P\text{ 被 }K\text{ 饱和}
\iff
n_{\bar x}\in\{0,|K|\}\ \text{对所有 }\bar x.
\tag{2}
\]

## 核分裂的 Fourier 能量

令 \(1_{S}\) 为 \(S=S_{\bar x}\) 的指示函数，对
\(\widehat K\) 中的字符定义未归一化系数

\[
\widehat{1_S}(\chi)=\sum_{k\in S}\overline{\chi(k)}.
\tag{3}
\]

有限阿贝尔群 Parseval 给出

\[
\sum_{\chi\in\widehat K}|\widehat{1_S}(\chi)|^2
=|K|\,n,
\qquad
\widehat{1_S}(1)=n.
\]

所以非平凡字符部分满足精确恒等式

\[
\boxed{
\sum_{\chi\ne1}|\widehat{1_S}(\chi)|^2
=n(|K|-n).
}
\tag{4}
\]

当 \(0<n<|K|\) 时，至少存在一个非平凡字符 \(\chi_*\) 使

\[
\boxed{
|\widehat{1_S}(\chi_*)|^2
\ge \frac{n(|K|-n)}{|K|-1}.
}
\tag{5}
\]

取达到最大值的最小规范字符，就得到一个与回执枚举顺序无关的
KERNEL_SPLIT_FOURIER 证书。式 (4) 还给出全部非平凡核字符的总缺陷能量，
不是只存在性的标签。

## 目标伪命中的专门形式

设 \(t\in G\) 是目标，并满足

\[
t\notin P,\qquad \pi(t)\in\pi(P).
\tag{6}
\]

取目标陪集代表 \(t\)，则

\[
S_t=\{k\in K:tk\in P\}
\]

是非空真子集，且 \(1\notin S_t\)。因此 (4)--(5) 给出一个非平凡核字符，
其系数精确记录“商目标命中但原目标缺失”的核方向分裂。该字符不是低模数
Type II 证书本身；它是必须交给 Fourier/二幂分支或严格 source-fiber 检查的
对偶回执。

若 \(K\) 是 2-群，则 \(\widehat K\) 也是 2-群，\(\chi_*\) 的阶为 \(2^j\)。
因此核分裂自动落入广义 \(2^j\) 字符层；若 \(K\) 含有奇素数阶部分，则
(5) 仍给出一般有限角色，而不能强行标成二次分离。

## \(p=97\) 的显式证书

取

\[
G=U(24),\qquad
K=\ker\bigl(U(24)\to U(4)\bigr)=\{1,5,13,17\},
\qquad
P=\{1,11\},\qquad t=-1=23.
\]

有 \(\pi(P)=\{1,3\}\)，所以 \(\pi(t)=3\in\pi(P)\)，但 \(t\notin P\)。目标截面为

\[
S_t=\{k\in K:-k\pmod{24}\in\{1,11\}\}=\{13\},
\qquad n=1,\ |K|=4.
\]

于是

\[
\sum_{\chi\ne1}|\widehat{1_{S_t}}(\chi)|^2=3,
\qquad
\max_{\chi\ne1}|\widehat{1_{S_t}}(\chi)|^2=1.
\]

例如取 \(\chi(5)=1,\chi(13)=-1,\chi(17)=-1\)，则
\(\widehat{1_{S_t}}(\chi)=-1\)。这给出一个完全显式的
KERNEL_SPLIT_FOURIER 证书，说明模4伪命中恰由核方向的非饱和截面造成。

## 研究边界

(2)--(6) 把稳定子未吸收的同余核转成有限对偶证书，但没有自动产生 Type I/II
证书或核心素数递降。后续若能证明该核字符与真实 q-height/源块标签同态相容，
即可进入跨状态容量；若关系格不相容，则应把 (5) 作为严格的
LIFT_OBSTRUCTED 回执，并寻找保持标记集的商递降。
