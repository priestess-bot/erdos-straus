---
kind: claim
claim_id: boundary-gap-27-reverse-two-tail-bridge
title: 五亿边界点 gap-27 证书的二分母保留严格递降
statement: 对p=477015289的三张gap-27 Type I证书，完整枚举每个目标项t的反向二分母保留提升。精确得到两条边，均替换最大项：d=3458361041的证书严格递降到偶数n=32897608，d=1497470330753的证书严格递降到偶数n=475989640。最短证书d=7986977及三张证书的其余七个目标坐标均无此类边。因此该点虽不在当前平移平方外源递降族中，却有不同形状的真实严格递降。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- reverse-lift
- marked-solution
- finite-audit
- boundary-case
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿边界点 gap-27 证书的二分母保留严格递降

设目标解中有一项 $1/t$，其余两项之和为

$$
\frac4p-\frac1t=\frac{4t-p}{pt}.
$$

要保持这两项、将 $t$ 反向替换为源项 $a$，所求严格边为

$$
\frac4n=\frac1a+\frac4p-\frac1t,\qquad2\le n<p. \tag{1}
$$

## 有限除子反演

令 $R=4t-p$，并写

$$
D=4pt-nR. \tag{2}
$$

(1) 等价于

$$
aD=npt. \tag{3}
$$

所以每条边都给出

$$
D\mid4p^2t^2. \tag{4}
$$

事实上，由 (2)--(3)，$D\mid npt$，而

$$
nptR=4p^2t^2-ptD,
$$

故 (4) 必然成立。反过来，枚举 (4) 的正因子；若

$$
R\mid4pt-D,\qquad n=\frac{4pt-D}{R}\in[2,p-1],\qquad D\mid npt, \tag{5}
$$

则令 $a=npt/D$，直接恢复 (1)。因此 (4)--(5) 是对固定目标项的完整有限反向搜索，
不需要逐个枚举五亿个源分母。

若 $t$ 是 Type I 正规形的最大项 $pK$，$D$ 自动具有 $D=p^2E$ 的冗余平方因子，可改为
枚举 $E\mid4K^2$；其精确正规形版本见
[Type I 正规形最大尾的反向二尾选择器](type-I-normal-reverse-two-tail-selector.md)。

## 边界点的两条严格边

对

$$
p=477{,}015{,}289
$$

的全部三张 gap-27 Type I 证书（见
[gap-27 证书层完整图](boundary-gap-27-certificate-landscape.md)），逐项因式分解目标三元组并
枚举 (4)。三张证书共九个可替换坐标中，恰有以下两条边：

$$
\frac4{32{,}897{,}608}
=\frac1{8{,}833{,}617}
+\frac1{119{,}253{,}829}
+\frac1{2{,}106{,}885{,}302{,}338{,}986}
\tag{6}
$$

严格提升为

$$
\frac4{477{,}015{,}289}
=\frac1{34{,}655{,}741{,}427{,}071{,}854{,}577{,}826}
+\frac1{119{,}253{,}829}
+\frac1{2{,}106{,}885{,}302{,}338{,}986},
\tag{7}
$$

以及

$$
\frac4{475{,}989{,}640}
=\frac1{55{,}344{,}063{,}985}
+\frac1{119{,}253{,}829}
+\frac1{2{,}106{,}940{,}636{,}115{,}642}
\tag{8}
$$

严格提升为

$$
\frac4{477{,}015{,}289}
=\frac1{80{,}038{,}456{,}354{,}427{,}554{,}834}
+\frac1{119{,}253{,}829}
+\frac1{2{,}106{,}940{,}636{,}115{,}642}.
\tag{9}
$$

两条源分母均为偶数，故它们位于猜想的无条件已知区。第一条来自正规形
$(A,B,C)=(29,1,4{,}112{,}201)$，正是 gap-27 的 source-29 直接证书；第二条来自
$(12{,}557,1,9497)$。最短证书 $(29,433,9497)$ 没有此类边。

这并不推翻此前的平移平方外源五百万偏移边界：该边不是“保持前两项、把 $p$-倍尾去缩放”
的规范尾形，而是保留目标的前两项、以一个完全不同的源项替换最大项。它把当前压力点从
“该外源族的失败点”提升为“已有不同严格递降出口的点”。

可复现命令：

~~~bash
python3 reproductions/boundary_gap_27_reverse_two_tail_bridge.py \
  --prime 477015289 --gap 27 \
  --output reproductions/boundary-gap-27-reverse-two-tail-477015289-results.json
python3 -m unittest tests/test_boundary_gap_27_reverse_two_tail_bridge.py -q
~~~
