---
kind: claim
claim_id: internal-support-gap-residue-pullback
title: K 内部缺口的 R 坐标残数拉回与终端选择边界
statement: 设 p≡1 (mod 24) 为素数，4K=pR+1。对任意 M|K、M≡3 (mod 4)、3≤M≤p-2，令 x=(p+M)/4。则对每个整数 d，M|(px+d) 当且仅当 4dR^2≡-1 (mod M)，而 M|(x+d) 当且仅当 4dR≡1 (mod M)。因此在补上 d|x^2 后，两式分别是缺口 M 的精确 Type I 与 Type II 终端判据；Type II 在存在性层面可由互补除子规范到 d≤x。该结论不要求 M 为素数或平方自由数。冻结的 55 个 Psi_0=1 状态上，完整扫描 1102 个合法内部缺口后有 37 个状态命中、18 个遗漏；只取缺陷坐标仅命中 8 个状态，故 Psi_0=1 只提供候选坐标，不保证终端，也不产生递降。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - gap-residue-reachability
  - type-I-coprime-factor-normal-form
  - type-II-coprime-factor-normal-form
  - type-I-f-psi-one-nearest-fiber-escape-boundary
  - gap-seven-congruence-certificates
  - type-II-small-shared-gap-explicit-fan
topics:
  - type-I
  - type-II
  - internal-support
  - gap-residue
  - Psi-one
  - terminal-first
  - canonical-selector
  - proof-boundary
sources:
  - claim: short-certificate-equivalence
    role: exact-gap-certificate-reconstruction
  - claim: gap-residue-reachability
    role: divisor-residue-language
  - claim: type-I-f-psi-one-nearest-fiber-escape-boundary
    role: frozen-Psi-one-input
  - claim: gap-seven-congruence-certificates
    role: existing-gap-seven-coverage
visibility: public
last_checked: '2026-07-31'
---

# \(K\) 内部缺口的 \(R\) 坐标残数拉回与终端选择边界

## 1. 设置与精确拉回

设

\[
p\equiv1\pmod {24},
\qquad
4K=pR+1,
\tag{1}
\]

其中 \(p\) 为素数，\(R,K>0\)。取任意

\[
M\mid K,
\qquad
M\equiv3\pmod4,
\qquad
3\le M\le p-2,
\tag{2}
\]

并令

\[
x=x_M=\frac{p+M}{4}.
\tag{3}
\]

由 \(M\mid K\) 与 (1) 得

\[
pR\equiv-1\pmod M.
\tag{4}
\]

特别地，\(p,R,4\) 都是模 \(M\) 的单位；又由 \(4x=p+M\) 得

\[
4x\equiv p\pmod M.
\tag{5}
\]

对任意整数 \(d\)，把 \(px+d\) 乘以单位 \(4R^2\)，由 (4)--(5) 得

\[
4R^2(px+d)
\equiv p^2R^2+4dR^2
\equiv1+4dR^2\pmod M.
\]

同理，

\[
4R(x+d)
\equiv pR+4dR
\equiv-1+4dR\pmod M.
\]

因此有不要求 \(M\) 素数或平方自由的精确等价：

\[
\boxed{
M\mid px+d
\iff
4dR^2\equiv-1\pmod M,
}
\tag{6}
\]

\[
\boxed{
M\mid x+d
\iff
4dR\equiv1\pmod M.
}
\tag{7}
\]

## 2. 从残数命中恢复 Type I/II 证书

再要求 \(d>0\) 且 \(d\mid x^2\)。若 (6) 命中，令

\[
y=\frac{px+d}{M},
\qquad
z=\frac{p(x+px^2/d)}{M}.
\tag{8}
\]

若 (7) 命中，令

\[
y=\frac{p(x+d)}{M},
\qquad
z=\frac{p(x+x^2/d)}{M}.
\tag{9}
\]

由 \(M\mid K\) 可得 \((M,x)=1\)，因而 \((M,d)=1\)。式 (8)--(9) 的第二个
分母整除性分别来自

\[
d(x+px^2/d)=x(d+px),
\qquad
d(x+x^2/d)=x(d+x).
\tag{10}
\]

直接通分便得到

\[
\frac4p=\frac1x+\frac1y+\frac1z.
\tag{11}
\]

所以在 (2) 的自然缺口范围内，(6) 加 \(d\mid x^2\) 是精确 Type I 终端判据，
(7) 加 \(d\mid x^2\) 是精确 Type II 终端判据。

Type II 还要求规范代表 \(d\le x\)。若某个 \(d\mid x^2\) 命中 (7)，令

\[
d^\vee=\frac{x^2}{d}.
\]

由 \(d\equiv-x\pmod M\) 及 \((d,M)=1\) 得 \(d^\vee\equiv-x\pmod M\)，所以互补
除子仍命中。由于 \(dd^\vee=x^2\)，二者至少一个不超过 \(x\)。因此 \(d\le x\)
在存在性层面没有损失，但证书记录仍应保存这个规范代表。

## 3. \(M=7\) 的 \(R\) 坐标表不是新覆盖

若 \(7\mid K\)，由 \(pR\equiv-1\pmod7\) 可把已有的三条缺口 7 分支重写为

\[
\begin{array}{c|ccc}
R\bmod7&1&2&4\\ \hline
p\bmod7&6&3&5\\
d&2&1&4
\end{array}
\tag{12}
\]

三列都满足 \(4dR\equiv1\pmod7\)。又因 \(p\equiv1\pmod8\)，
\(x=(p+7)/4\) 为偶数，故 \(1,2,4\mid x^2\)，并得到 Type II 证书。

式 (12) 只是把仓库已有的 \(p\equiv6,3,5\pmod7\) 缺口 7 证书改写成 \(R\)
坐标，不是新的剩余类覆盖。冻结样本中实际出现的六个 \(q=7\) 缺陷坐标满足

\[
R\bmod7\in\{3,6,3,3,5,5\},
\]

所以 (12) 在这六个坐标上零命中。

## 4. 冻结 \(\Psi_0=1\) 分支的完整内部菜单

以
`type-i-f-psi-one-nearest-fiber-escape-boundary-results.json`
中哈希冻结的 55 个状态为输入，对每态完整枚举 (2) 中所有 \(M\mid K\)，再完整枚举
\(d\mid x_M^2\)。规范顺序固定为：\(M\) 递增、\(d\) 递增，并在同一 \(d\) 先检查
Type I 再检查 Type II。精确计数为

\[
\begin{array}{l|r}
\text{合法内部缺口 }M&1102\\
\text{除子残数检查}&119922\\
\text{至少一种类型命中的缺口}&62\\
\text{Type I 命中的缺口}&49\\
\text{Type II 命中的缺口}&40\\
\text{两类都命中的缺口}&27\\ \hline
\text{至少一个内部终端的状态}&37/55\\
\text{全部内部缺口均失败的状态}&18/55
\end{array}
\tag{13}
\]

37 张规范首证书分为 13 张 Type I 与 24 张 Type II。若把候选限制为最短壳的缺陷
坐标 \(q\in D\)，120 个状态--坐标中只有 60 个是合法 \(3\pmod4\) 缺口，只有 9 个
坐标、8 个状态命中。因而 \(\Psi_0=1\) 只可用于建议候选 \(M=q\)，既不参与
(6)--(7) 的证明，也不保证命中。

最小的完整内部菜单遗漏为

\[
(p,R,K)
=(37793809,19,179520593),
\qquad
K=7\cdot53\cdot483883.
\tag{14}
\]

它的全部合法内部缺口恰为

\[
7,\quad371,\quad483883,\quad25645799,
\tag{15}
\]

四者的完整 \(x_M^2\) 除子谱都没有 Type I/II 命中。式 (14)--(15) 排除了“允许任意
复合 \(M\mid K\) 后，内部菜单必闭合每个 \(\Psi_0=1\) 状态”的直接推广。

## 5. 量词与递降边界

本卡给出的是同一素数状态上的精确直接终端叶，不是后继状态或递降边：

1. 缺陷坐标 \(q\) 可能满足 \(q\equiv1\pmod4\)，因而不能作缺口；
2. 仅由 \(4K=pR+1\) 与 \(\Psi_0=1\) 不能推出 \(q\le p-2\)。例如
   \((p,R,K)=(73,183,3340)\) 有一层缺陷 \(q=167>p-2\)；
3. 同余命中不替代 \(d\mid x^2\)，一般也不给出常数有界的 \(d\)；
4. 全部内部缺口失败只是一张局部终端障碍，不产生较小实例、解提升或良基势下降。

所以该选择器可放在 `terminal-first` 菜单中；若未命中，仍须另行构造满足 E1--E5 的
合法 support switch 或可提升递降。

## 6. 复现入口

聚焦复现器与结果文件为

```text
reproductions/type_i_internal_support_gap_single_external_selector.py
reproductions/type-i-internal-support-gap-single-external-selector-results.json
```

脚本锁定原 55 态输入哈希，对 (6)--(7) 的直接条件与拉回条件逐除子比较，对每个返回
证书精确重建 (11)，并保存 18 个完整遗漏及最小遗漏的全部合法缺口。式 (6)--(7) 是
上面的整数证明；式 (13) 只是哈希冻结输入上的有限剖面，不是全称覆盖定理。
