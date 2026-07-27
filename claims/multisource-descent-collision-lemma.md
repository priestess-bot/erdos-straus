---
kind: claim
claim_id: multisource-descent-collision-lemma
title: 外部源尺度与规范 Type II 移位的有限碰撞分解
statement: 令 p=1 mod24 为素数，B=(p-1)/4，且 k,l|B。定义 n_k=p-B/k。则 gcd(n_k,n_l) 整除 |k-l|/gcd(k,l)，且 gcd(n_k,p+4s) 整除 |4s(4k-1)-1|。因此对任何有限尺度集 K 和移位集 S，剥离由尺度差、移位差和 |4s(4k-1)-1| 的素因子组成的有限集合后，所有 n_k 与所有 p+4s 的剩余私有部分两两互素。对 H19 在 p<=2*10^7 的 65 条多源递降状态路径，该结论逐条验证；其中仅 5 条路径存在实际源碰撞，p=8328961 的最长路径唯一的实际源碰撞为 gcd(n_5,n_12)=7。
claim_status: established
topics:
- descent
- external-source
- factorization
- gcd
- collision
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: external-source-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 外部源尺度与规范 Type II 移位的有限碰撞分解

## 引理

令

\[
B=\frac{p-1}{4},\qquad
n_k=p-\frac Bk
\]

其中 \(k\mid B\)。对两个不同尺度 \(k,\ell\mid B\)，有

\[
\gcd(n_k,n_\ell)\mid
\frac{|k-\ell|}{\gcd(k,\ell)}. \tag{1}
\]

## 证明

写

\[
g=\gcd(k,\ell),\qquad k=ga,\qquad\ell=gb,\qquad B=gabc.
\]

于是

\[
n_k=bc(4ga-1)+1,\qquad
n_\ell=ac(4gb-1)+1.
\]

消去 \(c\) 得

\[
a(4gb-1)n_k-b(4ga-1)n_\ell=b-a. \tag{2}
\]

因此 \(\gcd(n_k,n_\ell)\mid|b-a|\)，而

\[
|b-a|=\frac{|k-\ell|}{g},
\]

即得 (1)。

## 有限碰撞状态

对有限尺度集 \(K\)，定义

\[
\mathcal C(K)=
\left\{q:\ q\text{ 是某个 }
\frac{|k-\ell|}{\gcd(k,\ell)}\ (k\ne\ell,\ k,\ell\in K)
\text{ 的素因子}\right\}.
\]

从每个 \(n_k\) 中剥离 \(\mathcal C(K)\) 的全部幂后所得私有部分两两互素。这是直接由
(1) 得到的；它把多个外部源的所有可能公因子压缩为只依赖于尺度集的有限碰撞状态。

这与规范 Type II 移位中“公因子只来自固定移位差”的分解平行，但对象变为
\(n_k=p-(p-1)/(4k)\) 的多源分母。

## 与 Type II 射线的交叉碰撞

对任意正移位 \(s\)，由

\[
(4k-1)(p+4s)-4kn_k=4s(4k-1)-1 \tag{3}
\]

立即得到

\[
\gcd(n_k,p+4s)\mid |4s(4k-1)-1|. \tag{4}
\]

而 \(p+4s,p+4t\) 都是奇数，且其公因子整除 \(4(s-t)\)，所以

\[
\gcd(p+4s,p+4t)\mid|s-t|. \tag{5}
\]

因此，对有限尺度集 \(K\) 与有限移位集 \(S\)，只要从所有源分母和所有射线整数中
剥离下列三个有限集合的素因子：

1. \(|k-\ell|/\gcd(k,\ell)\)；
2. \(|s-t|\)；
3. \(|4s(4k-1)-1|\)，

其余私有部分在所有源与所有射线之间两两互素。

## H19 状态路径审计

对两千万范围 H19 的 65 个共同残余，取每一点从 \(k=1\) 到首个平方因子递降成功的
尺度路径：

- 所有 65 条路径的剥离后私有源部分均两两互素；
- 仅 5 条路径存在实际源公因子；
- 50 条路径的尺度集根本没有可用碰撞素数；
- 最长路径 \(p=8328961\) 的尺度集为
  \(\{1,2,3,4,5,6,8,9,10,12\}\)，
  \(\mathcal C=\{2,3,5,7,11\}\)，其唯一实际碰撞是
  \(\gcd(n_5,n_{12})=7\)。

将每条路径同时与 H19 的 \(s=1,\ldots,19\) 射线交叉后，65 条路径仍全部通过
联合私有部分两两互素检验。这里的碰撞素数集仍是有限且完全显式的，但随尺度或移位范围
扩大而增大，故这只是状态压缩，不是统一有界性定理。

执行

```bash
python3 reproductions/multisource_descent_collision.py
python3 -m unittest tests/test_multisource_descent_collision.py -q
```

会重建引理在所有路径上的整数验证，结果保存在
`reproductions/multisource-descent-collision-h19-20m-results.json`。

## 对下一步的含义

若一组早期尺度的平方因子残数选择同时失败，困难不再能归因于未知的大公因子：剥离有限
碰撞状态后，失败完全落在互素的私有源和私有射线因子上。下一步应把这些私有除子残数集与

\[
n_k-n_\ell=B\left(\frac1\ell-\frac1k\right)
\]

及规范 Type II 移位的固定差值共同使用，寻找“多源共同失败 \(\Rightarrow\) 新 Type II
因子或更深递降”的桥接引理。

该引理本身不产生某个 \(-M_k\) 的除子，也不证明任何固定尺度集一定成功。
