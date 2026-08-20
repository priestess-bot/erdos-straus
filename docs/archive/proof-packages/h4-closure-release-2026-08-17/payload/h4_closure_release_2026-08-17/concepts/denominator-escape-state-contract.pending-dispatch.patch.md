### E3 补充：chart-independent identity-lift macro 的 `pending_dispatch`

当且仅当一个 macro 同时满足：

1. source 与 target 的 marked set 都是完整的 \(\operatorname{Sol}(p)\)；
2. 当前 edge 的合法性只依赖 canonical integer chart、support、source/path receipt 和 rank，不依赖 target 的 F/G/hit 标签；
3. target state ID 从 canonical \((p,R,K,A)\)、scope/origin 与 adapter version 确定生成；
4. receipt 明确记录 `inherited_type_label=false`；

E3 可以把 target 序列化为

```text
dispatch_status = pending_dispatch
```

而不在同一个 macro 内提前运行 F/G/hit classifier。

这只是**延迟重算**，不是标签继承。任何后续依赖 F/G/hit 的 selector action 在消费该 target 前，必须从 canonical target integers 重新运行其完整 normal-form classifier，并把结果纳入下一条 edge 的 E3 receipt。任何 `pending_dispatch` 字段都不得用于 E5 排名或当前 edge 的合法性证明。
