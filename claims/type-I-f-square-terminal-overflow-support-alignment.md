---
kind: claim
claim_id: type-I-f-square-terminal-overflow-support-alignment
title: 平方终端 F 证书的低秩支撑与盒溢出错位
statement: 对冻结的 253 个平方终端 F 状态，将规范低秩支撑与半径不超过 6 的目标仿射格首个盒外见证对齐后，144 个状态的溢出支撑完全在规范支撑之外，109 个状态部分重合，没有状态的溢出支撑完全包含于规范支撑；788 个溢出层中 121 个属于规范支撑、667 个属于支撑外坐标。该有限边界说明低秩支撑不能直接作为几何溢出的统一 q 进收费载体。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-linear-half-block-kneser-square-terminal-profile
  - type-I-f-square-terminal-relation-certificate
topics:
- type-I
- F-state
- square-terminal
- relation-lattice
- overflow-radius
- support
- q-adic
- capacity
- proof-program
sources:
- claim: type-I-f-overflow-active-support-boundary
  role: affine-overflow-witness-interface
- claim: type-I-f-square-terminal-relation-certificate
  role: exact-F-box-certificate
visibility: public
last_checked: '2026-07-30'
---

# 平方终端 F 证书的低秩支撑与盒溢出错位

## 对齐对象

对 253 个平方终端 F 状态，取半块 Kneser 剖面给出的规范支撑
\(Q_{\mathrm{low}}\)，并从已有半径不超过 6 的目标仿射格搜索中取首个确定性见证
\(z\)。令

\[
Q_{\mathrm{overflow}}(z)
=\{q_i:|z_i|>\nu_i\}.
\]

脚本按集合交集把状态分成：

- `canonical_only`：溢出支撑完全包含于规范支撑；
- `mixed`：两者有交但存在支撑外坐标；
- `outside_only`：两者完全不交。

## 结果

结果文件
`reproductions/type-i-f-square-terminal-overflow-support-alignment-results.json` 的
SHA-256 为

```text
21e11db9ad527fc566c58c62b4458c25865cc14319baad6790ba53c9e2eb667a
```

得到：

```text
record_count: 253
category_counts: {"mixed": 109, "outside_only": 144}
radius_histogram: {"1": 87, "2": 73, "3": 36, "4": 27, "5": 17, "6": 13}
overflow_layer_counts: {"canonical": 121, "outside": 667}
```

因此在这批样本中没有 `canonical_only` 状态；144 个状态的首个溢出见证完全落在
低秩支撑之外，109 个状态还需要至少一个支撑外素因子。788 个溢出层中只有 121 个
属于低秩支撑，667 个属于其它 (K) 素因子坐标。

## 含义与边界

该结果否定了一个自然但未经证明的简化：把“生成整个支撑子群所需的 1–3 个素因子”
直接当作“最小盒外溢出必然消耗的载体”。支撑子群是群论对象，盒外见证是带指数预算
的几何对象；两者在当前样本中大幅错位。

这不是目标不存在的证明。首个见证只在半径 6 内定义；其它见证、目标命中、偶终端
或不同下降源仍可能使用其它坐标。可靠的下一步是把支撑外溢出纳入多支持容量，或从
关系格的溢出向量构造严格的 (q)-进高度/算术势函数。

## 复现

```text
python3 reproductions/type_i_f_square_terminal_overflow_support_alignment.py
```

脚本锁定平方终端、半块支撑和已有溢出见证三个输入哈希。
