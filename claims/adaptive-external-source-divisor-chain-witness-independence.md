---
kind: claim
claim_id: adaptive-external-source-divisor-chain-witness-independence
title: 自适应外部源分母链的精确 gcd 与见证不复用
statement: >-
  对核心素数 p，令 H=(p-1)/4。若 k|l|H、l=ks、s>1，并令
  n_k=((4k-1)p+1)/(4k)、n_l=((4l-1)p+1)/(4l)，则
  gcd(n_k,n_l)=gcd(n_k,s-1)。所以任何两个分母共享的素因子都整除 s-1。
  特别地，外部源见证集合 W_k={f>1:f|n_k, f=-1 (mod 4k-1)} 与 W_l
  没有共同元素；更大的 l 分支的单素数见证不可能来自两分母的共享素因子。
  因而在任一严格整除链上，所有实际二尾 lift 的完整因子见证可无重计地并入
  一个 source-witness ledger。该容量公式不保证任一 W_k 非空，不能替代变量因子
  选择、terminal-first 检查或未命中状态的其它出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - adaptive-external-source-descent
topics:
  - type-I
  - external-source
  - descent
  - divisor-chain
  - gcd
  - witness-ledger
  - capacity-map
  - strict-obstruction
  - proof-program
sources:
  - claim: adaptive-external-source-descent
    role: each-witness-to-explicit-two-tail-lift
  - reproduction: reproductions/adaptive_external_source_divisor_chain_witness_independence.py
    role: exact-gcd-and-witness-no-reuse-controls
visibility: public
last_checked: '2026-08-12'
---

# 自适应外部源分母链的精确 gcd 与见证不复用

## 1. 分母链

固定核心素数 \(p\)，令

\[
H=\frac{p-1}{4},\qquad
q_k=4k-1,\qquad
n_k=\frac{q_kp+1}{q_k+1}=p-\frac Hk
\tag{1}
\]

对每个 \(k\mid H\) 成立。定义完整因子见证菜单

\[
W_k=\{f>1:f\mid n_k,\ f\equiv-1\pmod{q_k}\}.
\tag{2}
\]

每个 \(f\in W_k\) 都是已有自适应外部源定理的一条显式严格两尾 lift 的输入。
这里的 \(f\) 可以是合数；不能把 (2) 错缩为存在一个 \(-1\) 残数的素因子。

## 2. 精确 gcd 公式

设 \(k\mid l\mid H\)、\(l=ks\)、\(s>1\)，并令 \(t=H/k\)。于是 \(s\mid t\)，且

\[
n_k=(4k-1)t+1,\qquad
n_l=(4ks-1)\frac ts+1,
\qquad
n_l-n_k=\frac ts(s-1).
\tag{3}
\]

因为 \(n_k\equiv1\pmod t\)，有 \(\gcd(n_k,t/s)=1\)。所以

\[
\boxed{
\gcd(n_k,n_l)
=\gcd\left(n_k,\frac ts(s-1)\right)
=\gcd(n_k,s-1).}
\tag{4}
\]

每个共享素因子因此都被显式的小参数 \(s-1=l/k-1\) 控制。

## 3. 完整见证不复用

若 \(f\in W_k\cap W_l\)，则由 (4) 有 \(f\mid s-1\)。但 \(f\in W_l\) 蕴含

\[
f\ge q_l-1=4ks-2>s-1,
\tag{5}
\]

矛盾。故

\[
\boxed{W_k\cap W_l=\varnothing\qquad(k\mid l,\ k<l).}
\tag{6}
\]

若素数 \(\ell\) 同时整除 \(n_k,n_l\)，则 \(\ell\mid s-1<q_l-1\)，故它不可能
单独成为 \(l\) 分支的见证。它仍可参与一个更大的合数见证；本结论只禁止完整 \(f\)
或共享单素数被重复登记。

对 \(H\) 的任一严格整除链 \(\mathcal C\)，任意两个元素可比，因而

\[
\boxed{
\left|\bigcup_{k\in\mathcal C}W_k\right|
=\sum_{k\in\mathcal C}|W_k|.}
\tag{7}
\]

这是 variable-\(k\) 的精确 source-witness capacity map。每条记录都有自己的
\((k,n_k,f)\) 和既有 \(n_k<p\) 两尾 lift，而不会和同链的另一记录共用 witness id。

## 4. 聚焦控制

对 \(p=193\)、\(H=48\)，取 \(k=1\mid2=l\)，则

\[
(n_1,n_2)=(145,169),\quad
\gcd(n_1,n_2)=1=\gcd(145,1),\quad
5\in W_1,\quad13\in W_2.
\tag{8}
\]

两条正外部源见证不同。对 \(p=73\)、\(k=2\mid6=l\)，则

\[
(n_2,n_6)=(64,70),\quad
\gcd(n_2,n_6)=2=\gcd(64,2),\quad
W_2=W_6=\varnothing.
\tag{9}
\]

共享素因子 \(2<q_6-1=22\)，所以它不是较大分支的直接见证。这个失败控制说明
公式只提供去重容量，绝不伪造证书。

## 5. 选择器接口

~~~text
choose k_0 | k_1 | ... | k_t in H=(p-1)/4
  -> enumerate complete factor menus W_k
  -> each f in W_k: strict two-tail lift to n_k < p
  -> key the witness by (k, n_k, f)
  -> comparable k,l: W_k and W_l have no common key
  -> all menus empty: EXTERNAL_SOURCE_DIVISOR_CHAIN_EMPTY
                      requires another terminal or descent mechanism
~~~

本引理不保证链上有见证，也不把不同 \(n_k\) 合并成一个递归状态；每个正分支仍使用
已有的显式 lift。它只使 variable-\(k\) 外部源的多分支选择可无重计地进入容量账本。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/adaptive_external_source_divisor_chain_witness_independence.py \
  --verify
~~~
