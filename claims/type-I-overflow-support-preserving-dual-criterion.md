---
kind: claim
claim_id: type-I-overflow-support-preserving-dual-criterion
title: overflow 双对偶载体的支撑保持判据与 q 进阻碍
statement: 对 verified overflow pn=4Md+1，写 M=kp+r、1<=r<p，并令 A|M 为旧 charged support。d 对偶图表的旧支撑可保持且严格增加，当且仅当其图表在 p 以下、d 不整除 A 且 A/gcd(A,d) 整除 k+1；r 对偶图表的对应条件为图表在 p 以下、r 不整除 A 且 A/gcd(A,r) 整除 dn-1。两个失败条件分别由 A/gcd(A,d) 与 A/gcd(A,r) 对相应余数的 q 进剩余因子精确记录。对 12 个代表性 overflow receipt（24 个双通道）逐项核验，等价判据无一失配，3 个通道为支撑保持候选，15 个通道带非平凡支撑阻碍；该判据不声称双对偶必有出口，也不替代 fixed-n 其它因子。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-marked-support-accumulation-rechart-saturation
topics:
- type-I
- overflow
- determinant
- dual-carrier
- charged-support
- q-adic
- support-obstruction
- well-founded-descent
- proof-boundary
- proof-program
sources:
  - claim: type-I-overflow-determinant-fixed-n-dual-support-conflict
    role: symmetric-dual-charts-and-overflow-identity
  - claim: type-I-marked-support-accumulation-rechart-saturation
    role: charged-support-and-potential-contract
visibility: public
last_checked: '2026-08-02'
---

# overflow 双对偶载体的支撑保持判据与 (q) 进阻碍

## 1. 行列式坐标

设一个已经有来源回执的 overflow 满足

\[
pn=4Md+1,
\qquad M>0,
\qquad 1\le d<p,
\]

并写

\[
M=kp+r,
\qquad 1\le r<p.
\]

定义

\[
s=\frac{4rd+1}{p}=n-4kd.
\]

则两个对称算术图表为

\[
(R_d,K_d)=(4d-s,\ d(p-r)),
\qquad
(R_r,K_r)=(4r-s,\ r(p-d)).
\tag{1}
\]

它们分别是载体 \(d\) 和 \(r\) 的规范图表；是否小于 \(p\) 由
\(R_d<p\)、\(R_r<p\) 单独判断。令旧 charged support \(A\mid M\)，并定义

\[
g_d=\gcd(A,d),\quad A_d=A/g_d,
\qquad
g_r=\gcd(A,r),\quad A_r=A/g_r.
\tag{2}
\]

载体增加量由

\[
\frac{\operatorname{lcm}(A,d)}A=\frac d{g_d},
\qquad
\frac{\operatorname{lcm}(A,r)}A=\frac r{g_r}
\tag{3}
\]

精确给出。因而严格增加旧 support 分别等价于 \(d\nmid A\)、\(r\nmid A\)。

## 2. 两个精确模条件

### (d) 通道

由 \(M=kp+r\) 得

\[
p-r=(k+1)p-M.
\tag{4}
\]

由于 \(A_d\mid A\mid M\) 且 \((A_d,p)=1\)，有

\[
A_d\mid(p-r)
\iff
\boxed{A_d\mid k+1}.
\tag{5}
\]

而

\[
\operatorname{lcm}(A,d)\mid K_d=d(p-r)
\iff
A_d\mid(p-r).
\tag{6}
\]

因此，\(d\) 图表给出保持旧 support 的严格候选，当且仅当

\[
\boxed{
R_d<p,
\qquad
d\nmid A,
\qquad
A/\gcd(A,d)\mid k+1.
}
\tag{7}
\]

### (r) 通道

同理

\[
\operatorname{lcm}(A,r)\mid K_r=r(p-d)
\iff
A_r\mid(p-d).
\tag{8}
\]

由 overflow 恒等式和 \(A_r\mid M\) 得

\[
pn\equiv1pmod {A_r}.
\tag{9}
\]

这里 \((p,A_r)=(n,A_r)=1\)，所以乘以 \(n\) 不改变整除等价性：

\[
A_r\mid(p-d)
\iff
\boxed{A_r\mid dn-1}.
\tag{10}
\]

因此，\(r\) 图表给出保持旧 support 的严格候选，当且仅当

\[
\boxed{
R_r<p,
\qquad
r\nmid A,
\qquad
A/\gcd(A,r)\mid dn-1.
}
\tag{11}
\]

式 (7) 和 (11) 是对称双载体条件的完整消元；不需要假设 \(\gcd(d,r)=1\)。

## 3. q 进支撑阻碍字典

定义两个残余因子

\[
\mathcal O_d(A;M,d)
=\frac{A_d}{\gcd(A_d,k+1)},
\qquad
\mathcal O_r(A;M,d)
=\frac{A_r}{\gcd(A_r,dn-1)}.
\tag{12}
\]

它们的每个素数幂指数都是旧 support 在对应 determinant 通道中无法被保留的精确
\(q\) 进层数。于是：

- \(\mathcal O_d=1\) 且 \(R_d<p\)、\(d\nmid A\) 时，\(d\) 通道通过支撑整除；
- \(\mathcal O_r=1\) 且 \(R_r<p\)、\(r\nmid A\) 时，\(r\) 通道通过支撑整除；
- 若小图表存在但相应 \(\mathcal O_t>1\)，其失败不是未知的“大整除问题”，而是一个
  可分解的旧 support q 进阻碍；若 \(t\mid A\)，则阻碍来自严格性而非整除性。

这给出从 determinant 对偶坐标到容量账本的有向输入：

\[
\text{overflow}
\longrightarrow
(\mathcal O_d,\mathcal O_r, d/g_d, r/g_r).
\]

它仍不说明阻碍素数必在另一状态形成相同标签，也不自动产生 Type I/II 或 E1--E5
递归边；这些才是下一层跨状态容量/alternate-source 命题的内容。

## 4. 聚焦回执

脚本
`reproductions/type_i_overflow_support_preserving_dual_criterion.py --verify`
读取已有通用 overflow 对偶回执，不重跑历史扫描。12 个代表性 overflow 共给出 24 个
对称通道：

| 字段 | 数值 |
|---|---:|
| overflow case | 12 |
| 双通道 | 24 |
| 支撑保持候选 | 3 |
| 非平凡支撑阻碍通道 | 15 |

每个通道同时重算规范图表、\(K_t\)、\(\operatorname{lcm}(A,t)\) 整除、支持增量和
式 (12) 的因子分解；解析判据与直接整除检查逐项一致。代表性失败包括
\((p,A,M)=(241,38,190)\) 的 \(d\) 通道阻碍
\(\mathcal O_d=38=2\cdot19\)，以及 \(p=73,A=19\) 的四个可达冲突回执中分别出现
19 层旧 support 阻碍。\(A=1\) 与一个已知累积成功边也被纳入对照。

## 5. 逻辑边界和下一步

本卡把“对称小图表不保旧 support”从黑盒整除失败压成两个显式 q 进余项，但它没有
关闭 (A>1) overflow。要把它接到统一选择器，还需证明以下至少一项：

1. \(\mathcal O_d\) 或 \(\mathcal O_r\) 必须在另一个来源/状态形成可比较的标签链，并触发容量超载；
2. 阻碍因子本身构造一个保尾或改尾且标记集非空的 alternate/source-switch；
3. 在两个图表都大于 \(p\) 或载体不严格增加时，给出带外层秩的合法 reset。

因此这是一条严格的新中间定理和 typed `candidate_transition` 接口，不是 Erdős--Straus
猜想的全称证明。

## 复现

```bash
python3 reproductions/type_i_overflow_support_preserving_dual_criterion.py --verify
```

结果文件为
`reproductions/type-i-overflow-support-preserving-dual-criterion-results.json`。
