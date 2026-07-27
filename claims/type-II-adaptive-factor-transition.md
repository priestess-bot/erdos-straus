---
kind: claim
claim_id: type-II-adaptive-factor-transition
title: 十九移位残余的自适应新因子过渡谱
statement: 对 p<=2*10^7 的 65 个前十九条规范 Type II 射线共同失败点，逐一枚举其在 20<=s<=50 的首个成功移位全部 Type II 证书因子，并选择旧私有因子重数最小的证书。61 个点可取旧私有重数为零，51 个点的所选证书含有至少一个不整除任何旧 p+4s 的新素因子；仅 p=3361,813121,8283361,14847529 在最早成功移位必须使用一个旧私有因子。四个小 B 混合盒压力点均属于旧私有重数零且新因子重数正的类型。
claim_status: computationally_reproduced
topics:
- type-II
- multishift
- adaptive-family
- factorization
- transition
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# 十九移位残余的自适应新因子过渡谱

## 选择规则

固定旧扇

\[
\mathcal S_{19}=\{1,\ldots,19\}.
\]

对其共同失败素数 \(p\)，令 \(\mathcal C\) 为旧扇碰撞素数，令

\[
\mathcal O_p=\{q:q\mid p+4s\text{ for some }s\in\mathcal S_{19}\}. \tag{1}
\]

在第一个成功的后续规范移位 \(u>19\) 上，完整枚举每个证书因子

\[
h\mid p+4u,\qquad h\equiv-1\pmod{4ac},
\qquad u=a^2c. \tag{2}
\]

对 \(h\) 的素因子重数定义三元组

\[
(\omega_C,\omega_O,\omega_N), \tag{3}
\]

其中 \(\omega_C\) 来自 \(\mathcal C\)，\(\omega_O\) 来自
\(\mathcal O_p\setminus\mathcal C\) 的旧私有因子，\(\omega_N\) 来自
\(\mathcal O_p\) 外的新因子。审计按

\[
(\omega_O,\omega_N,\omega_C,h) \tag{4}
\]

字典序选择一张证书；因此它在该最早成功移位的全部证书中最少使用旧私有因子。

## 两千万结果

运行：

    python3 reproductions/type_ii_adaptive_factor_transition.py \
      --limit 20000000 --base-shift-bound 19 --shift-cap 50 \
      --output reproductions/type-ii-adaptive-factor-transition-h19-20m-results.json

对 65 个旧扇共同失败点，所有点都在 \(20\le u\le50\) 首次命中。选择后的三元组分布为：

| \((\omega_C,\omega_O,\omega_N)\) | 点数 |
|---|---:|
| \((0,0,1)\) | 17 |
| \((0,0,2)\) | 3 |
| \((0,1,1)\) | 3 |
| \((1,0,1)\) | 15 |
| \((1,0,2)\) | 3 |
| \((1,1,1)\) | 1 |
| \((2,0,0)\) | 11 |
| \((2,0,1)\) | 5 |
| \((2,0,2)\) | 1 |
| \((3,0,0)\) | 1 |
| \((3,0,1)\) | 2 |
| \((4,0,0)\) | 1 |
| \((4,0,1)\) | 1 |
| \((5,0,0)\) | 1 |

所以：

\[
\#\{\omega_O=0\}=61,\qquad
\#\{\omega_N>0\}=51. \tag{5}
\]

只有

\[
p=3361,\ 813121,\ 8283361,\ 14847529 \tag{6}
\]

在其最早成功移位上最少也需一个旧私有因子。此前三私有 relay 层仍失败的五点

\[
225289,\ 2031121,\ 3569329,\ 3660721,\ 7378849 \tag{7}
\]

全都满足 \(\omega_O=0,\omega_N>0\)。最新的 H19--小 \(B\) 混合盒四个延伸缺口点也属于
同一类型：

| \(p\) | 首个后续移位 | \((\omega_C,\omega_O,\omega_N)\) |
|---:|---:|---:|
| 7,378,849 | 26 | \((1,0,2)\) |
| 8,955,769 | 25 | \((1,0,2)\) |
| 11,910,361 | 36 | \((0,0,1)\) |
| 12,180,169 | 24 | \((1,0,1)\) |

因此它们并不是需要靠远 Type I 缺口才可处理的新状态；它们首先是“加入新移位即出现
无旧私有因子证书”的样本。相应地，混合盒给出的远 Type I 证书只是同一批点的另一条
受限出口，而非递降机制的独立压力测试。

例如

\[
p=225289,\qquad u=32,\qquad h=2591
\]

给出 \((0,0,1)\)：\(2591\) 不整除旧扇内任何 \(p+4s\)，故必须由新增移位
\(u=32\) 才首次获得来源标签。

## 含义与边界

这不是某个固定后续移位必成功的定理，固定扇本身仍有条件性逃逸边界。它也不说明
新因子为何对所有 \(p\) 必然出现。其精确意义是：在有限过渡样本中，旧私有积集不是
主要的证书来源；多数最早证书改由旧碰撞因子与新增移位的因子组成。

因而下一项全称研究目标应是自适应扩扇的状态转移：加入新移位时，必须同时更新所有旧
\(p+4s\) 的强制因子、碰撞闭包和私有来源，避免强制因子阶梯边界已排除的固定模数
朴素归纳。若这种状态转移仍不能强制一个新因子命中 (2)，才应在该无命中状态上寻找
真正可提升的递降。
