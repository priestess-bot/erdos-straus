# sol-ultra 对 F1 constructor surface 的独立 delta

> 基线：`c851bd213936b3bc8b3103b469292c139d229e97`
>
> 日期：2026-08-23
>
> 方法：只从活动源码重建入口与 target shape；未读取 Codex inventory 的结论字段。
>
> 结论：`UNRESOLVED_DELTA_BLOCKS_F1_FREEZE_AND_F3_INTEGRATION`。

## 1. 独立发现的活动入口

源码中可以辨认出以下互不统一的 producer/serializer surface：

1. `type_ii_initial_q_one_root_dispatch.initial_dispatch`：gap-3 terminal 或 q=1 G handoff；
2. proper-endpoint 与 gcd-shadow endpoint dispatch：输出 signed-box F/G profile；
3. q=1/positive-q/c=3 G handoff：至少三种 target schema；
4. second-anchor、d=1 relay 与 C=2 macro：分别输出 state、局部 target 或仅整数摘要；
5. total-cofactor adapter：唯一显式接受 `persistent_queue` 的活动接口，但没有 frozen edge ID；
6. representation-dual atlas：多个函数直接输出 `recursive_edge_eligible=True`；
7. 两个 high-R same-chart serializers；
8. H4/c=8 atomic controls：只到 `pending_dispatch`/capacity data，没有完成 target enqueue。

全活动树没有 `normalize_target_state` 的实现，也没有统一 queue mutation API。

## 2. 与 frozen registry 的 delta

### 2.1 源码多出的 producer-shaped 输出

- `type_i_overflow_total_cofactor_typed_adapter.verify_transition`；
- fixed-s 与 smooth23 overflow constructors；
- 两个 high-R same-chart serializers；
- representation-dual atlas 中没有唯一 registry mapping 的 eligible outputs。

其中 smooth23 输出同时含 `source_reach_status="unproved"` 与
`recursive_edge_eligible=True`。这类对象必须先降级为 control，或补齐 producer rule、
source receipt、terminal-first 与 admission；不能由布尔字段自行取得 queue 权限。

### 2.2 Registry 中没有完整运行链的条目

H4、c=8、q=1 d=1 relay、high-C=2 macro 和 high-support selector 均缺少至少一项：

```text
terminal-first -> serialized target -> common admission -> persistent queue
```

所以 registered edge name 不能作为 executable constructor 的替代证据。

### 2.3 不兼容 target schema

至少并存 endpoint profile、full-carrier root、macro state、total-cofactor state、H4 pending
state 和 representation-dual state 六种结构。当前没有共同 extractor 对这些真实输出逐项重算
family/owner，也没有从 emitted target 重放 T3 mark invariant。

## 3. 最早的 trace 断点

无需等到复杂 overflow，第一条根路径已经暴露缺口：

```text
initial_dispatch
  -> q=1 full-carrier root
  -> first_type_i_step
```

`first_type_i_step` 只是 `{kind,R,K,support}` rail dictionary，没有统一 persistent header、
serializer、normalizer、owner predicate 或 enqueue gate。随后 second-anchor macro 又从 `prime`
重新构造 parent，而不是消费并验证前一个 serialized successor。因此 initializer 后的第一步
successor induction 尚未建立。

## 4. 对两条研究线的含义

- F1 不能发布 grammar freeze；准确状态为 `OPEN_MINIMAL_GAPS`。
- F3 的 domain theorem 和 $p^2$ source normal form 可以独立成立，但任何新 target 只能作为
  candidate receipt，不能加入活动 graph。
- 下一条最小合同定理是逐 producer 的 projection/exclusive-admission theorem，而不是继续增加
  registry name。

本 delta 不声称某个 producer-shaped fixture 实际可达，也不反驳抽象 F1 命题；它反驳的是
“当前 frozen registry 已经等于全部 executable persistent constructor”这一识别。
