#!/usr/bin/env python3
"""Apply the corrected H4 clean-q relative-closure patch to an erdos-straus checkout.

Usage:
    python apply_h4_closure.py /path/to/erdos-straus

The script is deliberately idempotent where practical.  It refuses to silently
continue when the old formula anchor cannot be found, because that usually means
main has changed and the patch must be rebased deliberately.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent

NEW_FILES = {
    PACKAGE / "claims/type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure.md":
        "claims/type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure.md",
    PACKAGE / "reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py":
        "reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py",
    PACKAGE / "tests/test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py":
        "tests/test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py",
}

OLD_FORMULA = r"""在表的第二、三行，分别定义

\[
M_q=
\begin{cases}
\operatorname{lcm}(M_4,Q_x),&\text{恰一块非平凡时},\\
\operatorname{lcm}(M_4,Q_x,Q_y),&\text{两块皆非平凡时},
\end{cases}
\tag{13}
\]

\[
L_q=\frac{M_q}{M_4}.
\tag{14}
\]

由于 \(M_4\mid K_4\)，每个完整超额块都使 \(L_q>1\)。该行 p-free 时
"""

NEW_FORMULA = r"""对所有 actual p-free endpoint 统一定义

\[
\boxed{M_q=\operatorname{lcm}(M_4,Q_x,Q_y)}.
\tag{13}
\]

\[
L_q=\frac{M_q}{M_4}.
\tag{14}
\]

这里不能再按“恰一块非平凡”只写 \(\operatorname{lcm}(M_4,Q_x)\)：actual single-side
已由后续 endpoint 分类收缩为 \(Q_x=1<Q_y\)，旧写法会退化为 \(M_q=M_4\) 并漏掉唯一
非平凡的 y-block。统一公式与后续 complete-excess stutter reduction 的
\(L_q=E_xE_y=(L_0/q)E_x\) 完全一致。又因 actual 域已有 \(Q_y>1\)，且 \(Q_y\) 的完整
超额指数超过 \(K_4\)（从而也超过 \(M_4\mid K_4\) 的对应指数），故修正后的
\(M_q>M_4\)、\(L_q>1\)。该行 p-free 时
"""

OLD_FIX_MARKER = "## 9. 2026-08-17 公式修正与相对宏闭包"
OLD_FIX_NOTE = r"""

## 9. 2026-08-17 公式修正与相对宏闭包

本卡第 5 节旧版本对“恰一块非平凡”使用
\(\operatorname{lcm}(M_4,Q_x)\)。在后续已经证明的 actual single-side
\(Q_x=1<Q_y\) 中，该式会错误退化为 \(M_4\)，遗漏唯一非平凡 y-block。现已统一修正为

\[
\boxed{M_q=\operatorname{lcm}(M_4,Q_x,Q_y)}.
\]

后续 `complete-excess-stutter-reduction` 原本就使用这一统一公式，所以其 stutter
推导不受该旧接口错误影响。完整 E1--E5 相对闭包见
[H4 clean q-bridge 的修正版 E1--E5 相对宏闭包](type-II-q-one-c-two-19-phase-h4-clean-q-e1-e5-relative-macro-closure.md)。
"""

PENDING_MARKER = "### 2.3a `pending_dispatch` 的合法惰性正规化"
PENDING_DISPATCH_BLOCK = r"""

### 2.3a `pending_dispatch` 的合法惰性正规化

`linear_absorbed_support_v1` 的数学状态身份由版本、\(p_0,R_S,A_S\) 与
`source_tree_scope` 决定，而 \(K_S\)、F/G/hit、目标纤维、缺陷和证书字段是这些整数的
确定性派生数据。因此对一种**图表无关 marked set** 的 support-switch macro，允许把已经
通过整数 chart/source/scope/rank 核验的 target 暂时序列化为

```text
dispatch_status = pending_dispatch
selector_consumable = false
inherited_type_label = false
mandatory_next_step = normalize_target_state
```

但只限于同时满足：

1. source 与 target 都使用 \(W=\operatorname{Sol}(p_0)\)，当前 E4 不读取 F/G/hit；
2. 当前 edge 的 E1、E2、E5 只读取 canonical integer chart、charged support、真实
   source/path receipt 和预定义 rank；
3. `state_id` 仍按本节既有 canonical 字段生成，不把 `pending_dispatch` 或缓存标签纳入
   数学身份；
4. 当前 edge receipt 明确记录 `inherited_type_label=false`；
5. 任何下一条读取 F/G/hit、target fiber、signed defect 或 certificate context 的 action，
   在消费该 target 前必须从 canonical integers 运行完整 `normalize_target_state`，并把
   正规化结果纳入该下一 action 的 E3 receipt。

这只是**惰性重算**，不是继承旧标签，也不是新增一种数学图表。`pending_dispatch` target
可以作为 verified edge 的数学终点，但在正规化完成前不得被任何 type-specific selector
消费；惰性字段不得用于当前 E5 或 owner/capacity 收费。
"""

E3_MARKER = "### E3. normal_form_verifier"
E4_MARKER = "### E4. solution_lift"
E3_NOTE_MARKER = "#### E3 的 `pending_dispatch` 实现约定"
E3_NOTE = r"""

#### E3 的 `pending_dispatch` 实现约定

若 target 满足第 2.3a 节的全部条件，则 `verify_state(T)` 可以接受其 canonical
`linear_absorbed_support_v1` core 与 `pending_dispatch` queue status；这时 verifier 必须
同时验证 `selector_consumable=false`、`inherited_type_label=false` 与强制下一步
`normalize_target_state`。后续 type-specific action 不能把这一惰性状态当作已有 F/G/hit
分类。此约定不削弱 E3 的确定性：同一 canonical target 的正规化结果仍必须唯一并可重算。
"""

README_MARKER = "### H4 clean q-bridge E1–E5 相对宏验证器"
FRONTIER_MARKER = "## 2026-08-17：H4 clean q-bridge 已形成修正版 E1–E5 相对宏闭包"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def copy_new_files(repo: Path) -> None:
    for src, rel in NEW_FILES.items():
        dst = repo / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        if dst.suffix == ".py":
            dst.chmod(dst.stat().st_mode | 0o111)
        print(f"write {rel}")


def patch_old_claim(repo: Path) -> None:
    path = repo / "claims/type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge.md"
    s = read(path)
    if OLD_FORMULA in s:
        s = s.replace(OLD_FORMULA, NEW_FORMULA, 1)
    elif "\\boxed{M_q=\\operatorname{lcm}(M_4,Q_x,Q_y)}" not in s:
        raise SystemExit("old H4 formula anchor not found; rebase patch against current main")
    if OLD_FIX_MARKER not in s:
        s = s.rstrip() + OLD_FIX_NOTE + "\n"
    s = s.replace("last_checked: '2026-08-16'", "last_checked: '2026-08-17'", 1)
    write(path, s)
    print(f"patch {path.relative_to(repo)}")


def patch_contract(repo: Path) -> None:
    path = repo / "concepts/denominator-escape-state-contract.md"
    s = read(path)
    if PENDING_MARKER not in s:
        anchor = "### 2.3 累积外部支撑状态"
        idx = s.find(anchor)
        if idx < 0:
            raise SystemExit("state-contract 2.3 anchor not found")
        # Put 2.3a immediately after the introductory identity paragraph of 2.3,
        # i.e. after the sentence that forbids inherited F/G labels.
        end_anchor = "重图表时不得继承旧 F/G 标签，也不得只记录新的模数。"
        end = s.find(end_anchor, idx)
        if end < 0:
            raise SystemExit("state-contract 2.3 identity paragraph anchor not found")
        end += len(end_anchor)
        s = s[:end] + PENDING_DISPATCH_BLOCK + s[end:]
    if E3_NOTE_MARKER not in s:
        e3 = s.find(E3_MARKER)
        e4 = s.find(E4_MARKER, e3)
        if e3 < 0 or e4 < 0:
            raise SystemExit("E3/E4 anchors not found")
        s = s[:e4] + E3_NOTE + "\n" + s[e4:]
    # Update only the first matching last_checked field when present in front matter.
    s = s.replace("last_checked: '2026-08-16'", "last_checked: '2026-08-17'", 1)
    write(path, s)
    print(f"patch {path.relative_to(repo)}")


def append_fragment(repo: Path, rel: str, fragment: Path, marker: str) -> None:
    path = repo / rel
    s = read(path)
    if marker not in s:
        s = s.rstrip() + "\n\n" + read(fragment).strip() + "\n"
        write(path, s)
        print(f"append {rel}")
    else:
        print(f"skip {rel}: marker already present")


def patch_ci(repo: Path) -> None:
    path = repo / ".github/workflows/research-kb-ci.yml"
    s = read(path)
    test_mod = "tests.test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier"
    verifier = "reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py"
    test_file = "tests/test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py"
    if test_mod not in s:
        anchor = "            tests.test_type_i_tail_reverse_even_source_min_source_distance"
        if anchor not in s:
            raise SystemExit("CI focused-test anchor not found")
        s = s.replace(anchor, anchor + " \\\n            " + test_mod, 1)
    if verifier not in s:
        anchor = "            reproductions/type_i_tail_reverse_even_source_min_source_distance.py \\\n"
        if anchor not in s:
            raise SystemExit("CI verifier-lint anchor not found")
        s = s.replace(anchor, anchor + "            " + verifier + " \\\n", 1)
    if test_file not in s:
        # Replace the final occurrence in the lint list, not the focused test module above.
        anchor = "            tests/test_type_i_tail_reverse_even_source_min_source_distance.py"
        if anchor not in s:
            raise SystemExit("CI test-lint anchor not found")
        s = s.replace(anchor, anchor + " \\\n            " + test_file, 1)
    write(path, s)
    print(f"patch {path.relative_to(repo)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()
    required = [
        repo / "scripts/kb.py",
        repo / "claims/type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge.md",
        repo / "concepts/denominator-escape-state-contract.md",
        repo / ".github/workflows/research-kb-ci.yml",
    ]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise SystemExit("not an expected erdos-straus checkout; missing:\n" + "\n".join(missing))

    copy_new_files(repo)
    patch_old_claim(repo)
    patch_contract(repo)
    append_fragment(
        repo,
        "reproductions/README.md",
        PACKAGE / "reproductions/README.addition.md",
        README_MARKER,
    )
    append_fragment(
        repo,
        "concepts/current-frontier-2026-07-29.md",
        PACKAGE / "index/CURRENT_FRONTIER_2026-08-17_ADDITION.md",
        FRONTIER_MARKER,
    )
    patch_ci(repo)
    print("\nPatch applied. Recommended verification commands:")
    print("  python scripts/kb.py validate")
    print("  python -m unittest tests.test_type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier -v")
    print("  python reproductions/type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier.py --verify-controls")
    print("  python scripts/kb.py build")
    print("  git diff --check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
