---
kind: claim
claim_id: type-II-multishift-finite-collision-reduction
title: Type II 规范多移位的有限碰撞状态分解
statement: 对有限个两两不同的规范移位 s，令 N_s=p+4s。任意 s!=t 满足 gcd(N_s,N_t)|s-t；故删去所有整除某个移位差 s-t 的有限素数后，各 N_s 的私有余因子两两互素。若 p 与各规范射线模数互素，则每条射线的完整除子残数集精确等于碰撞部分与私有部分的乘积集，且射线失败当且仅当私有残数集避开碰撞残数诱导出的有限目标集。在 s=1,...,14、p<=10^6 的 24 个共同失败点上，此分解逐项通过：碰撞素数为 {2,3,5,7,11,13}，每一点的十四个私有余因子均两两互素。
claim_status: established
topics:
- type-II
- canonicalization
- divisor-residues
- factorization
- multishift
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: "subsequence-product framework; Theorem C"
  role: product-set-language
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# Type II 规范多移位的有限碰撞状态分解

## 大公因子只来自有限差值

取有限个两两不同的正整数移位 $\mathcal S$，并令

\[
N_s=p+4s\qquad(s\in\mathcal S),
\]

其中 $p$ 是奇素数。对 $s\ne t$，有

\[
\gcd(N_s,N_t)\mid N_t-N_s=4(t-s). \tag{1}
\]

两个 $N_s$ 都是奇数，故其公因子为奇数；由 (1) 得到更强的

\[
\gcd(N_s,N_t)\mid t-s. \tag{2}
\]

令

\[
\mathcal P_{\mathcal S}=
\{\ell:\ell\text{ 为某个 }s-t\ (s\ne t)\text{ 的素因子}\}. \tag{3}
\]

将 $N_s$ 的所有 $\mathcal P_{\mathcal S}$-素因子幂取出，记剩余私有余因子为

\[
R_s=\frac{N_s}{\prod_{\ell\in\mathcal P_{\mathcal S}}
\ell^{v_\ell(N_s)}}. \tag{4}
\]

由 (2)，不同 $s$ 的 $R_s$ 两两互素。这是确定性结论，不需要随机素因子模型或
筛法。

## 每条射线的有限状态化

将 $s=a_s^2c_s$ 写成平方自由规范形式，并令

\[
M_s=4a_sc_s. \tag{5}
\]

假设 $p\nmid M_s$；在固定有限扇且 $p$ 足够大时自动成立。于是 $N_s$ 的所有
素因子都是 $U(M_s)$ 的单位。将 (4) 中除去的碰撞部分记为 $E_s$，则

\[
N_s=E_sR_s.
\]

记 $\Pi_m(n)$ 为 $n$ 的全体除子模 $m$ 的残数集。由因子分解，恰有

\[
\Pi_{M_s}(N_s)=
\Pi_{M_s}(E_s)\,\Pi_{M_s}(R_s). \tag{6}
\]

其中右侧是群内集合乘积。故规范射线失败

\[
-1\notin\Pi_{M_s}(N_s)
\]

当且仅当对每个 $e\in\Pi_{M_s}(E_s)$，私有残数集都避开

\[
-e^{-1}\pmod {M_s}. \tag{7}
\]

碰撞部分的可能残数状态是有限的：每个 $U(M_s)$ 有限，且 $\mathcal P_{\mathcal S}$
有限。因而多移位共同失败被精确分成“有限碰撞状态”与各条私有因子的避靶条件。

## 前十四个规范移位的审计

对

\[
\mathcal S=\{1,2,\ldots,14\},
\]

有

\[
\mathcal P_{\mathcal S}=\{2,3,5,7,11,13\}. \tag{8}
\]

在 $p\le10^6$ 的 24 个共同失败点，完整因子分解和 (6)--(7) 均已逐项核验；每个
目标点的十四个 $R_s$ 两两互素。碰撞素数的实际出现次数中，3、5、7、11、13
分别出现 120、72、48、27、29 次；2 因所有 $N_s$ 为奇数而不出现。

同一审计扩展到 `p <= 10^7` 的 82,887 个核心素数时，小扇留下 128 个共同失败点，
每一点仍满足私有余因子两两互素；碰撞素数 3、5、7、11、13 分别出现
640、384、256、146、141 次。该扩展仅验证有限范围内的分解与实现，不能推出共同
失败的渐近结构。

运行

```bash
python3 reproductions/type_ii_multishift_collision.py --limit 1000000 \
  --base-shift-bound 14 \
  --output reproductions/type-ii-canonical-collision-1m-results.json
```

会重建每一个私有/碰撞因子分解、残数集大小和 (7) 的避靶检查。
将 `--limit` 改为 `10000000` 可复现扩展输出。

## 对证明路线的含义

该分解没有证明至少一条射线成功。它排除了一个不精确的希望：不同移位数不可能通过
未受控的大公共因子形成无限复杂耦合。共同的大素因子已全部压进有限集 (3)。

但私有余因子的两两互素也意味着，仅凭它们之间的公共因子无法推出矛盾。要完成下一步，
必须证明在每个允许的有限碰撞状态中，某条私有因子残数集不能同时避开 (7)；这需要利用
这些数同时等于 $p+4s$ 的加性关系、它们的逐素因子分布，或额外的直接证书/递降结构。
只保留总积字符值仍受
`type-II-character-product-congruence-compatibility-boundary` 的限制。
