---
kind: claim
claim_id: type-II-reverse-two-tail-bridge-boundary
title: 首个复合递降逃逸点的 Type II 二尾反向桥接障碍
statement: 对目标分母 t，所有通过替换 t 而保留其余两个目标分母的严格反向提升，都唯一由 n=2,...,p-1 且 a=npt/(np+4t(p-n)) 为正整数给出。对 p=2451289 的原始 Type II 射线 (A,C,K)=(1,2,13)，恢复的目标三元组为 (618772,63733514,19718256962404)；三个 t 的上述枚举均为空。更强地，在 A,C<=14 的 21 张不同原始 Type II 目标解中，逐张替换首分母并保留两条尾分母的反向枚举也均为空。因此在该证书盒内不存在这种首坐标二尾桥接。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- obstruction
- two-tail-lift
- computation
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 2 and 4"
  role: Type-II-certificate-reconstruction
visibility: public
last_checked: '2026-07-24'
---

# 首个复合递降逃逸点的 Type II 二尾反向桥接障碍

## 反向枚举公式

固定素数 \(p\) 的一个目标解，并选择其中待替换的目标分母 \(t\)。若存在
\(2\le n<p\) 及正整数 \(a\)，使源解通过只把 \(a\) 替换为 \(t\) 而保留目标解
其余两项，则必有

\[
\frac4n=\frac1a+\frac4p-\frac1t.
\]

解出 \(a\) 得到

\[
a=\frac{npt}{np+4t(p-n)}. \tag{1}
\]

反过来，(1) 是正整数时直接代回即给出这种严格源提升。因此对固定 \(p,t\)，
枚举 \(2\le n<p\) 中使 (1) 为整数的点，完整穷尽了“保留这两个目标尾项”的
反向桥接，而不需要枚举源解。

## \(p=2{,}451{,}289\) 的审计

取 `adaptive-external-source-escape-audit` 的原始 Type II 射线

\[
(A,C,K,h)=(1,2,13,103).
\]

它给出的证书和目标三元组为

\[
(m,d)=(23799,2),
\]

\[
(x,y,z)=(618772,\ 63733514,\ 19718256962404). \tag{2}
\]

对 (2) 中每个 \(t\)，逐一枚举全部 \(2\le n<p\) 并检查 (1)，三份结果均为空。
因此这张 Type II 解没有任何保留另外两项的严格反向源。

运行

```bash
python3 reproductions/targeted_descent_bridge.py \
  --output reproductions/targeted-bridge-2451289-results.json
```

会生成逐目标分母的空列表，并对每个非空候选以有理数恒等式复核。

## 有界 Type II 盒的首坐标审计

为避免只挑选最小半径射线，进一步枚举全部

\[
1\le A,C\le14
\]

的原始 Type II 射线，并以完整目标三元组去重。得到 21 张不同目标解，首分母介于
\(612840\) 与 \(620580\) 之间。对每一张的首分母 \(x\)，枚举 (1) 的全部
\(2\le n<p\)，结果仍全部为空：

\[
\#\{\text{不同目标解}\}=21,\qquad
\#\{\text{有首坐标二尾桥的解}\}=0.
\]

运行

```bash
python3 reproductions/targeted_descent_bridge.py --ac-bound 14 \
  --output reproductions/targeted-bridge-2451289-ac14-results.json
```

可复核此盒审计。这里仅测试替换目标的首分母、保留两条尾分母；并未对每张解的
两个巨大尾分母重复做三次全枚举。

## 边界

该结论只针对 (2) 的这张目标解，以及只改动一个目标分母的桥接模板。它不排除：

1. \(A,C>14\) 的其它 Type II 或任意 Type I 证书；
2. 同时改变两个或三个目标分母的提升；
3. 使用不同标记源状态的递降。

它的作用是排除一种最自然、但在该首个共同逃逸点上失败的直接证书到递降转换。
