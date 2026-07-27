---
kind: claim
claim_id: h19-k23-full-global-tail-closure-1048576
title: H19-k23 1048576 层的全局尾菜单普通递降闭合
statement: H19-k23 的1048576层普通双尾闭合中的2270418条实际素数记录均可使用共同因子G=165600所导出的全局尾m+1|G完成严格递降。其中2265164条保留已有共享缺口的直接全局证书；其余5254条逐条重写为全局尾上的规范 Type II 证书，均有支持缺陷至多2，精确分布为2497条0、2717条1、40条2，零遗漏。观测到的全局尾仅为3,7,11,15,19,23,31,35,39,47,59,71,79,91,95,99,159。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- p-minus-one
- affine-progressions
- factor-support
- h19
- computation
sources:
- paper: bradford2024
  locator: Proposition 2
  role: ordinary-Type-II-tail-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 1,048,576 层的全局尾菜单普通递降闭合

14 条 H19-k23 残存进程共有

\[
G=\gcd(A,C_1-1,\ldots,C_{14}-1)=165\,600. \tag{1}
\]

所以每个 \(m=4q-1\) 且 \(m+1\mid G\) 的尾都对每条进程、每个参数满足
\(m+1\mid p-1\)。这给出 72 个固定的全局普通尾候选。

此前的百万层普通双尾闭合已逐条验证 2,270,418 个实际素数记录，但其中一部分首次证书或
首次普通尾并不全局。这里对全部记录重新分类：若原共享缺口已经全局，则保留其已核验的
普通双尾证书；其余记录从原普通尾开始，按完整排序的全局菜单穷尽规范基底的零、一、二
新增素因子选择，并以平方根补全标准形重新核验。

结果为

\[
2\,270\,418=2\,265\,164_{\text{direct global}}
+5\,254_{\text{rewritten global}}+0_{\text{misses}}. \tag{2}
\]

重写来源按原共享缺口为

\[
5\,081_{27}+84_{43}+33_{51}+33_{55}+17_{63}+1_{67}
+2_{75}+1_{83}+2_{87}=5\,254. \tag{3}
\]

所有重写证书满足规范支持缺陷至多二，精确为

\[
5\,254=2\,497_{\delta=0}+2\,717_{\delta=1}+40_{\delta=2}. \tag{4}
\]

它们实际使用的全局尾频数为

\[
3\,730_{31}+736_{35}+293_{39}+279_{47}+143_{59}+49_{71}
+14_{79}+3_{91}+4_{95}+1_{99}+2_{159}. \tag{5}
\]

合并直接记录，整个有限产物只出现

\[
\{3,7,11,15,19,23,31,35,39,47,59,71,79,91,95,99,159\}. \tag{6}
\]

特别地，原先的非全局 \(m=63\)、\(107\) 尾均被更大的全局尾替换；这包括原来直接但
非全局的十条 \(m=63\) 证书。因而这一有限层不再需要参数依赖的 \(p-1\) 尾缺口。

这仍然不是原猜想的证明：它没有说明 72 尾菜单对无限参数范围的覆盖性，也没有给出所有
重写记录缺陷至多二的全称引理。它将当前理论目标严格压缩为固定菜单上的变量因子联合覆盖，
可与 [全局尾菜单的私有余因子分离](h19-k23-global-tail-private-cofactors.md) 直接结合。

重建命令：

~~~bash
python3 reproductions/h19_k23_full_global_tail_closure.py \\
  --input reproductions/h19-k23-shared-selector-tail-descent-1048576.json \\
  --output reproductions/h19-k23-full-global-tail-closure-1048576.json
python3 -m unittest tests/test_h19_k23_full_global_tail_closure.py -q
~~~
