---
kind: claim
claim_id: type-II-factor-box-audit
title: Type II 因子生成器在 10^8 内的有限参数盒审计
statement: 精确计算表明：对所有 p<=10^8 且 p=1 mod24，在 m=3、(p+1)/2、p+4、4p+1 四条直接分支均未覆盖的 21680 个素数中，每个都由 4ACK-1 | Kp+A 的 Type II 生成器在 1<=A,C,K<=29 内命中；此范围所需的最小统一盒为 29，保持者为 p=50370049。盒 20 在同一范围遗漏 7 个素数。
claim_status: computationally_reported
topics:
- type-II
- computation
- bounded-window
- factorization
- proof-program
sources:
- paper: bello2026
  locator: "Theorem 8 and Remarks 23--25"
  role: finite-window-context
visibility: public
last_checked: '2026-07-23'
---

# Type II 因子生成器在 \(10^8\) 内的有限参数盒审计

## 计算结论

运行

```bash
python3 reproductions/type_ii_factor.py --limit 100000000 --parameter-bound 29
```

得到 719,781 个核心素数。先由 `m=3`、\((p+1)/2\)、\(p+4\)、\(4p+1\)
四条已证直接分支删除 698,101 个，余下 21,680 个。对每个余项，脚本精确搜索

\[
q=4ACK-1\mid Kp+A,
\qquad 1\le A,C,K\le29,
\]

并用 `short_certificate.py` 恢复、验证相应的 Type II 证书。结果为全部 21,680 个
命中、零遗漏。逐层扩大参数盒后，最小的统一盒边界为 29；最后的记录保持者是

\[
p=50{,}370{,}049,\qquad (A,C,K)=(19,29,5),
\qquad (m,d)=(4{,}575,10{,}469).
\]

对比运行边界 20 时有 7 个遗漏，最小的是 \(p=23{,}863{,}249\)，故该较小窗口
不能解释为稳定规律。

完整机器可读结果在 `reproductions/type-ii-factor-results.json`。

## 算法与可重复性

脚本按 \(\max(A,C,K)\) 递增、盒内字典序搜索，因此报告的每个素数见证具有最小
参数盒半径。所有候选仅用整数整除判定；接受后由分数恒等式再次验证。单元测试在
小范围独立核对生成器与 Bradford Type II 证书的双向对应。

## 不能推出的结论

这不是对任意素数的统一参数界。`type-II-finite-template-obstruction` 已证明：任何
固定有限 \((A,C,K)\) 集合都会被无穷多个核心素数避开。因此此处的边界 20 是一个
有限范围的经验记录，而不是“短证书或递降”引理的证明。它可用于研究参数随 \(p\)
增长的规律，或寻找未命中时可用的递降机制。
