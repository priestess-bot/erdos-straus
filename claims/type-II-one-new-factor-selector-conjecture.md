---
kind: claim
claim_id: type-II-one-new-factor-selector-conjecture
title: H19 后单新因子 Type II 选择器猜想
statement: 设 p=1 mod24 为未被 H19 直接 Type II 射线或固定碰撞射线捕获的素数。令 C={3,5,7,11,13,17}，令 O_p 为所有 H19 数 p+4s (1<=s<=19) 的素因子集。猜想存在 s=a^2c>19、C-平滑整数 e 与素数 q 不属于 O_p，使 eq|p+4a^2c 且 eq=-1 mod4ac。该条件给出 Type II 证书，故该选择器猜想蕴含 Erdős--Straus 猜想。
claim_status: open
topics:
- type-II
- conjecture
- multishift
- factorization
- new-factor
- short-certificate
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-27'
---

# H19 后单新因子 Type II 选择器猜想

## 精确命题

令 H19 的碰撞素因子集为

\[
\mathcal C=\{3,5,7,11,13,17\},
\]

并对每个核心素数 \(p\) 记

\[
\mathcal O_p=\{r:r\mid p+4s,\ 1\le s\le19\}. \tag{1}
\]

先剥离 H19 直接射线及
[首次无旧私有因子深度谱](type-II-source-free-transition-profile.md) 中的静态碰撞射线。
猜想每个剩余 \(p\) 都存在正整数 \(a,c\)、素数 \(q\) 和 \(\mathcal C\)-平滑整数 \(e\)，
使

\[
s=a^2c>19,\qquad q\notin\mathcal O_p,\qquad
eq\mid p+4a^2c,\qquad eq\equiv-1\pmod{4ac}. \tag{2}
\]

这里 \(e=1\) 被允许。\(q\notin\mathcal O_p\) 是来源标签意义的“新”，而不是要求
\(q\) 大于某个数值阈值。

## 为什么它足够

令 \(h=eq\)、\(k=(h+1)/(4ac)\)。由 (2)，\(k\) 为正整数且

\[
h=4ack-1,\qquad h\mid p+4a^2c. \tag{3}
\]

这正是规范 Type II 射线的因子条件；`type_ii_raw_ray_certificate` 重建一张目标
\(4/p\) 的 Type II 证书。因此 (2) 是直接短证书选择器，并非未经证明的递降步骤。

## 当前证据

在 \(p\le5\cdot10^8\)、\(s\le200\) 的精确审计中，425 个 H19 残余中 84 个先由
碰撞专用证书捕获。剩余 341 个全部有 (2) 形的单新因子证书，见
[最小碰撞支持审计](type-II-minimal-collision-support.md)。

将同一来源标签审计扩至存储的 \(p\le10^9\) H19 状态，并把后续移位窗口延至
\(s\le500\) 后，541 个新因子状态全部有 (2) 形证书；539 个可取 \(e=1\)，其余两点
仅取一次碰撞因子 \(e=5,17\)。最大最小碰撞移位为 \(484\)，由
\(p=372{,}271{,}201\) 的纯新因子 \(3343\) 达到。见
[H19 十亿新因子状态在五百移位内零/一碰撞闭合](type-II-h19-zero-one-collision-500-1b.md)。

继续把同一完整状态集延至 \(s\le1008\) 后，541 个状态全都取得 \(e=1\) 的纯新因子
见证；最大首次纯新移位为 \(p=178{,}400{,}041\) 的 \(s=1008\)、\(q=9743\)。这说明
碰撞平滑因子在这份有限样本中最终都可消去，但不提供统一释放深度。见
[H19 十亿新因子状态在移位一千零八内纯新闭合](type-II-h19-pure-new-1008-1b.md)。

纯新方向还具有不依赖有限样本的密度支撑：令
\(H=\lfloor\delta\log\log X\rfloor\)，在完整规范移位扇
\(s=a_s^2c_s\)、\(20\le s\le H\) 上只寻找
\(q\equiv-1\pmod{4a_sc_s}\) 的 H19 新素因子，则共同失败的核心素数至多为
\(X\exp[-c(\log\log X)\log\log\log X]\)。因此纯新单素因子证书已对相对密度一的
核心素数成立，且移位只需 \(O(\log\log X)\)；剩余困难仍是从稀薄到逐点的提升。见
[增长规范移位扇上的纯新单素因子证书具有超对数稀薄尾部](type-II-pure-new-canonical-fan-superlog-tail.md)。
其中平方 \(C=1\) 子扇是根几何最简单的特例，但其逐点边界已知，见
[增长平方移位上的纯新单素因子 Type II 射线具有超对数稀薄尾部](type-II-pure-new-square-ray-superlog-tail.md)。

这个归纳是刻意比“任意除子积集命中”更窄的：它把非碰撞部分压缩到一个素数，保留了
真正需要解释的因子来源。

## 已知边界

该猜想不能被弱化为固定 \(s\)、固定 \(k\)、固定 \(e\) 或固定有限射线表。H19 及其
静态扩展已有条件性共同逃逸；单新因子证书的实际 \(k\) 也不有界。故可能的证明必须
根据 \(p\) 的当前来源标记选择 \(s,e,q\)，或在选择失败时导出严格递降。

碰撞平滑因子也不能在当前五亿窗口内一概删为 \(e=1\)：341 个新因子状态中有九个在
\(s\le200\) 内没有纯新因子证书，尽管它们仍有 (2) 形的证书，见
[纯新因子选择边界](type-II-pure-new-factor-boundary.md)。这是有限范围的边界，不是这些点
对强化命题的永久反例；但它排除了用“新素数单独命中”代替乘积 \(eq\) 的证明策略。
其中八点只需一次碰撞，但 \(p=372{,}271{,}201\) 在窗口内需
\(e=3\cdot7\)，余下332点可取 \(e=1\)，见
[最小碰撞支持审计](type-II-minimal-collision-support.md)。这排除把碰撞部分一概限制为
\(e\in\{1\}\cup\mathcal C\) 的固定窗口版本。把它进一步收紧为“零或一个碰撞素数”并保留来源
同余约束的精确版本见
[零/一碰撞素数选择器](type-II-zero-one-collision-selector-conjecture.md)；它目前仍仅是
比原命题更强的研究目标。

这仍是一个与原猜想强度相近的充分命题，而不是证明。它的价值在于把下一步的失败状态
具体化为：“所有新素因子与全部可用碰撞平滑因子都避开目标残数”。这为角色残数、乘法
群轨道或跨移位差值关系提供了明确入口。
