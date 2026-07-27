---
kind: claim
claim_id: h19-k23-multisource-marked-state
title: H19-k23 十四条残存进程的多源标记状态编译
statement: H19-k23 经统一仿射、混合因子与小 h 二次审计后保留14条进程。每条进程具有相同的37个全程外部尺度 k|1800 或 k=23 和19条 H19 射线；每个源 n_k=F_kN_k 的完整平方尾残数目标均失败，H19 射线也均无证书。37个源的所有跨源公因子只需40个尺度差碰撞素数标记；连同源-射线和射线-射线碰撞后，联合标记为368个显式素数。该数据给出后续多源标记递降桥接引理的完整有限状态输入。
claim_status: computationally_reproduced
topics:
- descent
- external-source
- multisource
- collision
- state-transition
- conditional-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: external-source-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19-k23 十四条残存进程的多源标记状态编译

## 状态对象

先经以下三类整进程叶子审计：统一仿射 Type I/II、单源统一仿射混合因子、以及
\(d=x^2/h\) 的平方专用小 \(h\) 二次 Type I。余下的 H19-k23 进程共有 14 条。

对每条进程 \(p=Pn+C\)，编译全部静态外部源

\[
n_k=\frac{(4k-1)p+1}{4k}=F_kN_k,
\qquad k\in\{d:d\mid1800\}\cup\{23\}. \tag{1}
\]

编译输出逐源保存 \(q_k=4k-1\)、仿射源形式、固定因子 \(F_k\)、私有仿射形式
\(N_k\)，以及完整平方尾的目标残数和可达除子残数数目。14 条状态均满足：

| 项目 | 数目 |
|---|---:|
| 残存进程 | 14 |
| 每状态静态来源 | 37 |
| H19 射线 | 19 |
| 已有 H19 射线证书 | 0 |
| 已有完整来源平方尾递降 | 0 |

## 有限碰撞标签

对不同尺度，已有恒等式给出

\[
\gcd(n_k,n_\ell)\mid\frac{|k-\ell|}{\gcd(k,\ell)}. \tag{2}
\]

对源与 H19 移位整数，有

\[
\gcd(n_k,p+4s)\mid|4s(4k-1)-1|. \tag{3}
\]

因此把这些固定整数以及移位差的素因子剥离后，剩余私有部分两两互素。针对本尺度集，
由 (2) 得到的来源碰撞标签恰有 40 个素数；再加入 (3) 与射线差，联合标签恰有 368 个
素数。它们都只依赖于固定尺度集与 H19，而不依赖进程参数。

## 使用方式与边界

这个编译状态不是新的覆盖定理。它的作用是消除后续证明中的隐含自由度：任何声称从
“多源共同失败”推出证书或严格递降的桥接引理，都必须在这 14 个显式状态、37 个来源、
19 条射线和有限碰撞标签上成立。

另一方面，私有部分的互素性本身不制造一个目标除子。下一步仍须把不同 \(N_k\) 的差值
关系、来源残数目标或新的标记解提升结合起来，构造真正的选择机制。

运行

```bash
python3 reproductions/h19_k23_multisource_marked_state.py
python3 -m unittest tests/test_h19_k23_multisource_marked_state.py -q
```

可重建完整状态 JSON 与有限碰撞标签。
