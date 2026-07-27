---
kind: claim
claim_id: type-I-h19-reverse-two-tail-terminal-1b
title: H19 十亿残余的零溢出反向二尾终止闭合
statement: 对存储的p<=10^9的664个H19源自由残余，只枚举m<=127、B=1的Type I正规形并施加最大尾反向二尾选择器，664点全部有严格更小源；最大所选缺口为79。每个源分母还含有q不congruent to 1 modulo 24的素因子，故可缩放终止于已知非核心素数类；所选q最大为2417。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- reduction
- h19
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: certificate-context
- salez2014
visibility: public
last_checked: '2026-07-27'
---

# H19 十亿残余的零溢出反向二尾终止闭合

H19 残余是前 $19$ 条规范 Type II 射线都未给出 source-free 证书的 $664$ 个核心素数，
是不同于五亿普通尾遗漏的独立压力集。对每个这样的 $p$，完整枚举

$$
3\le m\le127,\qquad m\equiv3\pmod4,\qquad B=1
$$

的 Type I 正规形，并对每个证书使用[最大尾反向二尾选择器](type-I-normal-reverse-two-tail-selector.md)。
结果为

$$
664=664_{\text{严格反向二尾递降}},
$$

无遗漏；实际首命中缺口最大为 $79$，唯一达到该值的是

$$
p=334{,}152{,}361,\qquad(m,A,B,C)=(79,101,1,827110).
$$

每个构造出的严格源 $n<p$ 都完整试除分解，并选取最小的

$$
q\mid n,\qquad q\not\equiv1\pmod{24}.
$$

因而源可按比例缩放到经典已解的非核心素数 $q$，如[素数分母约化](reduction-to-primes.md)
和[困难素数约化](reduction-to-one-mod-24.md)所述。没有源仅由核心类素因子构成；所选
终止素因子的最大值为 $2417$。

这给出两种独立有限输入上的相同现象：普通 Type II 尾遗漏的五亿集在最大缺口 $127$、
$B\le5$ 时闭合，而 H19 source-free 残余的十亿集在更小的最大缺口 $79$、甚至 $B=1$
时闭合。它强化了反向二尾选择器值得寻找统一源侧解释的动机，但并不建立对任意核心素数的界，
也不证明 $m$ 或 $B$ 可以全称有界。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_reverse_two_tail_terminal_closure.py \
  --h19 reproductions/type-ii-source-free-transition-h19-1b-results.json \
  --gap-cap 127 --b-cap 1 \
  --output reproductions/type-i-h19-reverse-two-tail-terminal-b1-1b-results.json
python3 -m unittest tests/test_type_i_h19_reverse_two_tail_terminal_closure.py -q
~~~
