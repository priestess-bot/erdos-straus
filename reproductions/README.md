# 小尺度复现

`esc_reproduce.py` 用精确整数算术复现四个可独立检查的环节：

1. 三个经典约化恒等式；
2. `S_5`、`S_7` 与 `p = 1 mod 24` 合并后模 840 的六个残余类；
3. 固定首分母后的完整因子对证书 `(ay-b)(az-b)=b^2`；
4. Bradford 2025 的 Type I/II 除子同余到显式分母的对应。

运行：

```bash
python3 reproductions/esc_reproduce.py
python3 -m unittest discover -s tests -v
```

生成的 `results.json` 记录运行范围和脚本 SHA-256。它是有限范围的交叉核对，
不是 Salez `10^17` 或 Mihnea–Dumitru `10^18` 搜索的全量复现。
