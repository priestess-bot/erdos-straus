---
kind: claim
claim_id: type-II-h19-external-scale-fixed-trap-boundary
title: H19-k23 残存进程的固定因子 Type II 陷阱完备边界
statement: H19-k23 模二十九分裂留下的18个可采纳进程均形如 p=P*n+C。对每个进程，固定因子进程陷阱所允许的全部未来 Type II 缺口 m 必整除 S=P/4；在自然范围内每个进程恰有564个 m=3 mod4 候选。对全部10152个候选，逐一枚举 E=gcd(S,(C+m)/4) 的全部除子 a，均不存在 a*((C+m)/(4E))=-(C+m)/4 modm。因此这18条进程都没有 d=a*x/E 形式的统一新增 Type II 证书。
claim_status: computationally_reproduced
topics:
- type-II
- arithmetic-progression
- external-source
- fixed-factor
- state-transition
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# H19-k23 残存进程的固定因子 Type II 陷阱完备边界

## 审计对象

[H19-k23 模二十九出口分类](type-II-h19-external-scale-k23-branching.md) 留下 18 个
可采纳仿射进程

\[
p=Pn+C.
\]

考虑固定因子进程陷阱的最一般形式。对一个未来缺口
\(m\equiv3\pmod4\)，令

\[
x=\frac{p+m}{4}=Sn+x_0,\qquad
S=\frac P4,\qquad x_0=\frac{C+m}{4},\qquad
E=\gcd(S,x_0). \tag{1}
\]

若存在统一的 Type II 除子

\[
d=a\frac{x}{E},\qquad a\mid E, \tag{2}
\]

则必须有

\[
m\mid\frac SE,
\qquad
a\frac{x_0}{E}\equiv-x_0\pmod m. \tag{3}
\]

特别地 \(m\mid S\)，所以枚举 \(S\) 的全部因子已经穷尽 (2) 的所有未来缺口，
不是设置了任意移位上界。

## 完整结果

对每个残存进程，满足

\[
4\cdot19-1<m\le C-2,\qquad m\equiv3\pmod4,\qquad m\mid S
\]

的候选恰有 564 个。逐个计算 (1)、检查 (3) 的第一式，再枚举 \(E\) 的所有除子
\(a\)，18 个进程的结果均为：

| 量 | 数目 |
|---|---:|
| 残存进程 | 18 |
| 每进程完整候选缺口 | 564 |
| 总候选 \((\text{进程},m)\) | 10,152 |
| 命中固定因子陷阱 | 0 |

## 含义

这排除了从当前 18 个条件性残存进程到“一个未来固定缺口、一个冻结因子”的最直接
正向桥。它不排除多因子 Type II 除子、随参数变化的移位、其它 Type I/II 证书，或
严格递降；因此不是对原猜想或整个自适应移位路线的否定。

对下一步而言，任何桥接引理必须使用 (2) 之外的额外状态，例如多个固定因子的积集、
与外部源尺度的联合残数，或一个真正改变源分母的递降构造。

运行

```bash
python3 reproductions/type_ii_h19_external_scale_fixed_trap_boundary.py
python3 -m unittest tests/test_type_ii_h19_external_scale_fixed_trap_boundary.py -q
```

可重建 18 条进程、10,152 个候选和所有空结果。
