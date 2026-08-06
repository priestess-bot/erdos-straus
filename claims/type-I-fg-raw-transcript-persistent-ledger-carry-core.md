---
kind: claim
claim_id: type-I-fg-raw-transcript-persistent-ledger-carry-core
title: raw transcript 中持续 E2 账本的 gcd carry core
statement: 对同一核心素数的一个已证明 sound 的 raw-to-overflow 物理行 transcript，若同一个旧 ledger A 必须在所有行保留且在指定行通过 E2，则 A 可行当且仅当 A 整除所有 carrier M_i 与所有 C_i(M_i mod p) 的 gcd。该 gcd 是无需预先选择 A 的最大持续 E2 charge；局部边 core 为 gcd(M_w,M_w',C_w'(M_w' mod p))，等于 1 时没有非平凡旧账本可跨边并在目标 E2 通过。p=73 给出严格正、负 overflow 控制；p=5281 的 Jacobi-odd raw rows 则在 E2 之前失败，因为 4M-n=R=p-2<p，不能把它们误作为 cofactor-overflow lift。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-ledger-e2-gate
  - type-I-overflow-e2-fixed-fiber-constancy
  - type-I-fg-physical-carry-arc-lift-interface
  - type-I-g-anchor-jacobi-odd-p5281-physical-row-ledger
topics:
  - type-I
  - F-state
  - G-state
  - source-map
  - raw-transition
  - overflow
  - E2
  - carry
  - gcd
  - proof-boundary
sources:
  - claim: type-I-fg-physical-carry-arc-lift-interface
    role: single-row-carry-interface
  - claim: type-I-g-anchor-jacobi-odd-p5281-physical-row-ledger
    role: physical-raw-scope-control
  - reproduction: reproductions/type_i_raw_transcript_persistent_carry_core.py
    role: carry-core-controls
visibility: public
last_checked: '2026-08-07'
---

# raw transcript 中持续 E2 账本的 gcd carry core

## 1. 输入与定义

固定核心素数 \(p\)。设 \(\mathcal T\) 是一个已经由独立算术命题给出
sound raw-to-overflow 意义的有限物理行 transcript。每行 \(i\) 有

\[
pn_i=4M_i d_i+1,
\qquad
C_i=p-d_i,
\qquad
r_i=M_i\bmod p\in\{1,\ldots,p-1\},
\tag{1}
\]

并满足当前 cofactor-overflow 的严格域条件 \(4M_i-n_i>p\)。令
\(I\) 是其中必须检查 E2 的行集合。定义

\[
\boxed{
\operatorname{CarryCore}(\mathcal T,I)
=\gcd\left(\{M_i:i\in\mathcal T\}
\cup\{C_i r_i:i\in I\}\right).
}
\tag{2}
\]

这里的所有 gcd 都是正整数 gcd。它不是从 Fourier 相位推得的有限群量，而是实际
integer carriers 的共同不变量。

## 2. 持续账本充要判据

设一个旧 ledger \(A>0\) 必须在 transcript 的每行保留：

\[
A\mid M_i\qquad(i\in\mathcal T).
\tag{3}
\]

该行的 E2 条件是

\[
\frac{A}{(A,C_i)}\mid r_i.
\tag{4}
\]

于是有精确等价：

\[
\boxed{
A\text{ 满足 (3) 且在所有 }i\in I\text{ 通过 E2}
\quad\Longleftrightarrow\quad
A\mid\operatorname{CarryCore}(\mathcal T,I).
}
\tag{5}
\]

**证明。** 固定一行，写 \(g=(A,C_i)\)、\(A=ga\)、\(C_i=gc\)。则
\((a,c)=1\)，故

\[
\frac{A}{(A,C_i)}\mid r_i
\Longleftrightarrow a\mid r_i
\Longleftrightarrow A\mid C_i r_i.
\tag{6}
\]

与所有 (3) 和所有 E2 行的 (6) 取交，即为 (5)。证毕。

因此 (2) 是最大的、在整除偏序下可从根持续携带的 E2 charge。若 ledger 允许单调增长

\[
A_0\mid A_i\mid M_i,
\tag{7}
\]

且每个 \(i\in I\) 的 \(A_i\) 在该行通过 E2，则 (6) 仍给出
\(A_0\mid\operatorname{CarryCore}(\mathcal T,I)\)；反过来任意整除 (2) 的 \(A\)
取常值 \(A_i=A\) 即可在 \(I\) 的行实现。故允许中间加账本并不能绕过这个 root
charge 上界。

对一条 raw-to-overflow 边 \(w\to w'\)，目标行需 E2 时的局部版本为

\[
\boxed{
\operatorname{CarryCore}(w,w')
=\gcd(M_w,M_{w'},C_{w'}r_{w'}).
}
\tag{8}
\]

若它等于 \(1\)，任何非平凡旧 ledger 都不能跨这条边并在目标行 E2 通过。

## 3. p=73 的物理 overflow 正、负控制

负控制为

\[
(p,A,M,C,d,n)=(73,34,1598,57,16,1401).
\tag{9}
\]

它确为 physical overflow：

\[
73\cdot1401=4\cdot1598\cdot16+1,
\qquad
4\cdot1598-1401=4991>73.
\tag{10}
\]

此时 \(r=65\)，并且

\[
\operatorname{CarryCore}=\gcd(1598,57\cdot65)=1.
\tag{11}
\]

所以 \(A=34\) 严格失败；等价地

\[
\left\lfloor1598/73\right\rfloor=21\not\equiv0\pmod {34}.
\tag{12}
\]

正控制取

\[
(p,A,M,C,d,n)=(73,69,10626,69,4,2329),
\tag{13}
\]

并有

\[
73\cdot2329=4\cdot10626\cdot4+1,
\qquad r=41,
\qquad
\operatorname{CarryCore}=\gcd(10626,69\cdot41)=69.
\tag{14}
\]

由于 \(A/(A,C)=1\)，完整 \(A=69\) 通过 E2。两例共同证明 (2) 不是只会排除候选的
失败筛，而是精确的正、负判据。

## 4. p=5281 的更早 scope 失败

已有 Jacobi-odd physical raw ledger 的每行满足

\[
n_\delta=4M_\delta-R,
\qquad R=5279=p-2.
\tag{15}
\]

故

\[
4M_\delta-n_\delta=R<p.
\tag{16}
\]

它们不是这里假设的 cofactor-overflow 行；不能把 (2) 误称为这些 raw 边上的合法 E2
gate。即使只作不具递归语义的诊断，菜单首边

\[
7\xrightarrow{13}91
\tag{17}
\]

也已有

\[
M_7=278784,\quad M_{91}=6969600,\quad C_{91}=1,
\quad r_{91}=3961,
\tag{18}
\]

从而

\[
\gcd(M_7,M_{91},C_{91}r_{91})=1.
\tag{19}
\]

这只表明：若未来某个合法 raw-to-overflow map 保留这里的 \(M_7,M_{91},C_{91}\)（或
另证其 carry core 不变），并试图从该边持续携带一个非平凡旧 charge，则会遇到 carry
障碍。它不把当前 G/Jacobi rows 伪装成 overflow E2 edge，也不限制可重图表后具有不同
物理 carrier 的未来 map。

## 5. 接入边界

`CarryCore` 只有在 raw 行与 transition universe 已独立证明 sound/complete、并且行确属
cofactor-overflow 后才能调用。它不创建 source map，不从 finite Fourier/SNF 相位推出
E2，也不提供 E1、E3、E4、E5、解提升或严格递降。其作用是把“一个旧账本能否跨实际
物理 transcript 持续存活”压缩为一个可重算 gcd gate。

窄复现：

```bash
python3 reproductions/type_i_raw_transcript_persistent_carry_core.py --verify
```
