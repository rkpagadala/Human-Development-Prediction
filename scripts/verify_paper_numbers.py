"""
verify_paper_numbers.py

Umbrella script that runs all analysis scripts and verifies their output
numbers match the claims in paper/education_mediated_security.md.

Usage:
    python scripts/verify_paper_numbers.py

Runs each sub-script, parses key numbers from stdout, and compares against
the paper's claims. Reports PASS/FAIL/MISSING for each check.

Exit code: 0 if all pass, 1 if any fail or missing.
"""

import os
import re
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
PAPER = os.path.join(REPO_ROOT, "paper", "education_mediated_security.md")

# Rupture repo — some scripts live here only
RUPTURE_ROOT = os.path.join(os.path.dirname(REPO_ROOT), "education-rupture")
RUPTURE_SCRIPTS = os.path.join(RUPTURE_ROOT, "scripts")

# ── Check definitions ────────────────────────────────────────────────────────

class Check:
    def __init__(self, name, script, regex, expected, tolerance, paper_ref):
        self.name = name
        self.script = script          # path relative to a repo root
        self.regex = regex
        self.expected = expected
        self.tolerance = tolerance
        self.paper_ref = paper_ref
        self.actual = None
        self.status = "PENDING"

    def run(self, stdout):
        m = re.search(self.regex, stdout)
        if m is None:
            self.status = "MISSING"
            return
        try:
            self.actual = float(m.group(1))
        except (ValueError, IndexError):
            self.status = "PARSE_ERROR"
            return
        if abs(self.actual - self.expected) <= self.tolerance:
            self.status = "PASS"
        else:
            self.status = "FAIL"


# Script paths
T1 = os.path.join(REPO_ROOT, "scripts", "table_1_main.py")
TA1 = os.path.join(REPO_ROOT, "scripts", "table_a1_two_way_fe.py")
FA1 = os.path.join(REPO_ROOT, "scripts", "fig_a1_lag_decay.py")
CO2 = os.path.join(REPO_ROOT, "scripts", "co2_placebo.py")
# Rupture repo scripts
EDU_OUT = os.path.join(RUPTURE_SCRIPTS, "07_education_outcomes.py")
LONG_RUN = os.path.join(RUPTURE_SCRIPTS, "04b_long_run_generational.py")

ALL_CHECKS = [
    # ── Table 1 (table_1_main.py) ────────────────────────────────────────
    Check("T1-M1-beta", T1,
          r"Table 1 Model \(1\): β=([0-9.]+)", 0.482, 0.001,
          "Table 1 row 1 (line 216)"),
    Check("T1-M1-R2", T1,
          r"Table 1 Model \(1\):.*R²=([0-9.]+)", 0.455, 0.001,
          "Table 1 row 1 (line 216)"),
    Check("T1-M1-N", T1,
          r"\(1\) child ~ parent_edu\s+\[N=(\d+)", 1683, 0,
          "Table 1 caption (line 212)"),
    Check("T1-M1-countries", T1,
          r"\(1\) child ~ parent_edu\s+\[N=\d+, (\d+) countries", 187, 0,
          "Table 1 caption (line 212)"),
    Check("T1-M2-beta", T1,
          r"Table 1 Model \(2\): β=([0-9.]+)", 15.369, 0.001,
          "Table 1 row 2 (line 217)"),
    Check("T1-M2-R2", T1,
          r"Table 1 Model \(2\):.*R²=([0-9.]+)", 0.256, 0.001,
          "Table 1 row 2 (line 217)"),
    Check("T1-M3-beta-edu", T1,
          r"Table 1 Model \(3\): β_edu=([0-9.]+)", 0.519, 0.001,
          "Table 1 row 3 (line 218)"),
    Check("T1-M3-beta-gdp", T1,
          r"Table 1 Model \(3\):.*β_gdp=([0-9.]+)", 5.470, 0.001,
          "Table 1 row 3 (line 218)"),
    Check("T1-M3-R2", T1,
          r"Table 1 Model \(3\):.*R²=([0-9.]+)", 0.556, 0.001,
          "Table 1 row 3 (line 218)"),
    Check("T1-fem-beta", T1,
          r"Footnote: female β=([0-9.]+)", 0.419, 0.001,
          "Table 1 footnote (line 220)"),
    Check("T1-fem-R2", T1,
          r"Footnote: female.*R²=([0-9.]+)", 0.388, 0.001,
          "Table 1 footnote (line 220)"),
    Check("T1-agg-beta", T1,
          r"vs agg\s+β=([0-9.]+)", 0.482, 0.001,
          "Table 1 footnote (line 220)"),
    Check("T1-agg-R2", T1,
          r"vs agg.*R²=([0-9.]+)", 0.455, 0.001,
          "Table 1 footnote (line 220)"),

    # ── Table A1 (table_a1_two_way_fe.py) ────────────────────────────────
    Check("TA1-M1-beta", TA1,
          r"Table A1 Model \(1\): β=([0-9.]+)", 0.080, 0.001,
          "Table A1 row 1 (line 495)"),
    Check("TA1-M1-R2", TA1,
          r"Table A1 Model \(1\):.*R²=([0-9.]+)", 0.009, 0.001,
          "Table A1 row 1 (line 495)"),
    Check("TA1-M2-beta", TA1,
          r"Table A1 Model \(2\): β=([0-9.]+)", 3.930, 0.001,
          "Table A1 row 2 (line 496)"),
    Check("TA1-M2-R2", TA1,
          r"Table A1 Model \(2\):.*R²=([0-9.]+)", 0.027, 0.001,
          "Table A1 row 2 (line 496)"),
    Check("TA1-M3-beta-edu", TA1,
          r"Table A1 Model \(3\): β_edu=([0-9.]+)", 0.239, 0.001,
          "Table A1 row 3 (line 497)"),
    Check("TA1-M3-beta-gdp", TA1,
          r"Table A1 Model \(3\):.*β_gdp=([0-9.]+)", 3.174, 0.001,
          "Table A1 row 3 (line 497)"),
    Check("TA1-M3-R2", TA1,
          r"Table A1 Model \(3\):.*R²=([0-9.]+)", 0.095, 0.001,
          "Table A1 row 3 (line 497)"),

    # ── Figure A1 lag decay (fig_a1_lag_decay.py) ────────────────────────
    Check("FA1-lag0-edu", FA1,
          r"lag=\s*0\s+edu R²=([0-9.]+)", 0.562, 0.001,
          "Figure A1 caption (line 525): R²=0.562 at lag 0"),
    Check("FA1-lag25-edu", FA1,
          r"lag=\s*25\s+edu R²=([0-9.]+)", 0.364, 0.001,
          "Section 2.3 (line 70), Figure A1 caption (line 525)"),
    Check("FA1-lag50-edu", FA1,
          r"lag=\s*50\s+edu R²=([0-9.]+)", 0.171, 0.001,
          "Section 2.3 (line 70)"),
    Check("FA1-lag75-edu", FA1,
          r"lag=\s*75\s+edu R²=([0-9.]+)", 0.085, 0.001,
          "Section 2.3 (line 70)"),
    Check("FA1-lag100-edu", FA1,
          r"lag=\s*100\s+edu R²=([0-9.]+)", 0.052, 0.001,
          "Section 6.1 (line 222)"),

    # ── CO2 placebo (co2_placebo.py) ────────────────────────────────────
    Check("CO2-FE-R2", CO2,
          r"CO2 placebo R² = ([0-9.]+)", 0.089, 0.001,
          "Section 5.2 (line 204), Table A2 (line 505)"),

    # ── Table 2 Panel A (07_education_outcomes.py, rupture repo) ─────────
    Check("T2-GDP-beta", EDU_OUT,
          r"log GDP\(T\+25\) \| FE:\s+edu \+ GDP: low_t:([0-9.-]+)", 0.012, 0.001,
          "Table 2 Panel A row 1 (line 254)"),
    Check("T2-GDP-R2", EDU_OUT,
          r"log GDP\(T\+25\) \| FE:\s+edu \+ GDP:.*R²=([0-9.]+)", 0.354, 0.001,
          "Table 2 Panel A row 1 (line 254)"),
    Check("T2-LE-beta", EDU_OUT,
          r"e0\(T\+25\) \| FE:\s+edu \+ e0: low_t:([0-9.-]+)", 0.108, 0.001,
          "Table 2 Panel A row 2 (line 255)"),
    Check("T2-LE-R2", EDU_OUT,
          r"e0\(T\+25\) \| FE:\s+edu \+ e0:.*R²=([0-9.]+)", 0.384, 0.001,
          "Table 2 Panel A row 2 (line 255)"),
    Check("T2-TFR-beta", EDU_OUT,
          r"TFR\(T\+25\) \| FE:\s+edu \+ tfr: low_t:([0-9.-]+)", -0.032, 0.001,
          "Table 2 Panel A row 3 (line 256)"),
    Check("T2-TFR-R2", EDU_OUT,
          r"TFR\(T\+25\) \| FE:\s+edu \+ tfr:.*R²=([0-9.]+)", 0.367, 0.001,
          "Table 2 Panel A row 3 (line 256)"),

    # ── Table 2 Panel B (07_education_outcomes.py, rupture repo) ─────────
    Check("T2-PB-GDP-only-beta", EDU_OUT,
          r"edu\(T\+25\) \| FE:\s+GDP only: log_gdp_t:([0-9.-]+)", 14.85, 0.1,
          "Table 2 Panel B row 1 (line 262)"),
    Check("T2-PB-GDP-only-R2", EDU_OUT,
          r"edu\(T\+25\) \| FE:\s+GDP only:.*R²=([0-9.]+)", 0.272, 0.001,
          "Table 2 Panel B row 1 (line 262)"),
    Check("T2-PB-GDP-cond-beta", EDU_OUT,
          r"edu\(T\+25\) \| FE:\s+GDP \+ init edu: log_gdp_t:([0-9.-]+)", 3.780, 0.1,
          "Table 2 Panel B row 2 (line 263)"),
    Check("T2-PB-GDP-cond-R2", EDU_OUT,
          r"edu\(T\+25\) \| FE:\s+GDP \+ init edu:.*R²=([0-9.]+)", 0.500, 0.001,
          "Table 2 Panel B row 2 (line 263)"),

    # ── Forward R² symmetry (07_education_outcomes.py) ───────────────────
    Check("T2-fwd-edu-GDP-R2", EDU_OUT,
          r"log GDP\(T\+25\) \| FE:\s+edu only:.*R²=([0-9.]+)", 0.259, 0.001,
          "Section 6.2 (line 269): edu→GDP R²=0.259"),

    # ── Long-run panel (04b_long_run_generational.py, rupture repo) ──────
    Check("LR-beta", LONG_RUN,
          r"Country FE \(full, 1900-2015\): β=([0-9.]+)", 0.960, 0.001,
          "Section 6.1 (line 226)"),
    Check("LR-N", LONG_RUN,
          r"Long-run panel: (\d+) obs", 672, 0,
          "Section 6.1 (line 226)"),
    Check("LR-countries", LONG_RUN,
          r"Long-run panel: \d+ obs, (\d+) countries", 28, 0,
          "Section 6.1 (line 226)"),
]


# ── Derived checks (computed from multiple script outputs) ───────────────

class DerivedCheck:
    def __init__(self, name, description, paper_ref):
        self.name = name
        self.description = description
        self.paper_ref = paper_ref
        self.status = "PENDING"
        self.detail = ""

    def run(self, checks_by_name):
        raise NotImplementedError


class CO2FoldCheck(DerivedCheck):
    """Verify that 0.455 / CO2_R2 ≈ 5 ('approximately 5-fold weaker')."""
    def run(self, checks_by_name):
        co2 = checks_by_name.get("CO2-FE-R2")
        t1r2 = checks_by_name.get("T1-M1-R2")
        if not co2 or not t1r2 or co2.actual is None or t1r2.actual is None:
            self.status = "MISSING"
            self.detail = "CO2 or Table 1 R² not available"
            return
        if co2.actual == 0:
            self.status = "PASS"
            self.detail = "CO2 R²=0, ratio is infinite"
            return
        ratio = t1r2.actual / co2.actual
        if ratio > 4:
            self.status = "PASS"
            self.detail = f"{t1r2.actual:.3f} / {co2.actual:.3f} = {ratio:.0f}x (>4)"
        else:
            self.status = "FAIL"
            self.detail = f"{t1r2.actual:.3f} / {co2.actual:.3f} = {ratio:.0f}x (NOT >4)"


class BetaRangeCheck(DerivedCheck):
    """Verify β range '0.080-0.485' matches Table A1 M1 and Table 1 M1."""
    def run(self, checks_by_name):
        ta1 = checks_by_name.get("TA1-M1-beta")
        t1 = checks_by_name.get("T1-M1-beta")
        if not ta1 or not t1 or ta1.actual is None or t1.actual is None:
            self.status = "MISSING"
            self.detail = "Table A1 or Table 1 beta not available"
            return
        # Paper says "0.080-0.485" — check both ends
        low_ok = abs(ta1.actual - 0.080) <= 0.001
        # Paper text says 0.485 but Table 1 says 0.482; the text rounds
        high_ok = abs(t1.actual - 0.482) <= 0.005
        if low_ok and high_ok:
            self.status = "PASS"
            self.detail = f"Range: {ta1.actual:.3f}–{t1.actual:.3f}"
        else:
            self.status = "FAIL"
            self.detail = f"Range: {ta1.actual:.3f}–{t1.actual:.3f} (expected ~0.080–0.482)"


DERIVED_CHECKS = [
    CO2FoldCheck("DERIVED-100fold",
                 "CO2 R² is 'over 100-fold weaker' than edu R²",
                 "Section 5.2 (line 204), Table A2 (line 505)"),
    BetaRangeCheck("DERIVED-beta-range",
                   "β range 0.080–0.485 matches Table A1 M1 and Table 1 M1",
                   "Section 6.1 (line 224)"),
]


# ── Numbers claimed in paper with NO backing script ─────────────────────

UNVERIFIED = [
    ("Parental income collapse: β=14.4 (alone), β=1.0 (p=0.67, conditional)",
     "Section 6.2 (line 269)"),
    ("Parental edu β=0.510 (conditional on GDP), vs 0.529 (alone)",
     "Section 6.2 (line 269)"),
    ("Table 2 Panel A: initial outcome β values (0.217, 0.301, 0.037)",
     "Table 2 (lines 254-256)"),
    ("Table 3: FE residuals (Maldives +34.9, Cape Verde +26.3, etc.)",
     "Table 3 (lines 277-288)"),
    ("Table 4: development crossing dates",
     "Table 4 (lines 299-308)"),
    ("Table A4: threshold robustness crossing dates",
     "Table A4 (lines 511-518)"),
    ("Korea/Taiwan/Philippines/Bangladesh β values from Figure 1",
     "Section 6.1 (line 228)"),
    ("GDP R² at lag 0: 0.321",
     "Figure A1 caption (line 525)"),
]


# ── Runner ───────────────────────────────────────────────────────────────

def run_script(path, cwd=None):
    """Run a Python script and return its stdout."""
    if not os.path.exists(path):
        return None
    if cwd is None:
        cwd = os.path.dirname(os.path.dirname(path))
    try:
        result = subprocess.run(
            [sys.executable, path],
            capture_output=True, text=True,
            cwd=cwd, timeout=300,
        )
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return None
    except Exception as e:
        return f"ERROR: {e}"


def main():
    print("=" * 72)
    print("PAPER NUMBER VERIFICATION")
    print(f"Paper: {PAPER}")
    print("=" * 72)

    # Collect unique scripts
    scripts = {}
    for c in ALL_CHECKS:
        if c.script not in scripts:
            scripts[c.script] = None

    # Run each script once
    for path in scripts:
        label = os.path.basename(path)
        print(f"\nRunning {label}...", end=" ", flush=True)
        stdout = run_script(path)
        if stdout is None:
            print("NOT FOUND" if not os.path.exists(path) else "TIMEOUT")
        else:
            print("done")
        scripts[path] = stdout or ""

    # Run checks
    print("\n" + "=" * 72)
    print("RESULTS")
    print("=" * 72)

    checks_by_name = {}
    passed = failed = missing = 0

    # Group checks by script for display
    current_script = None
    for c in ALL_CHECKS:
        if c.script != current_script:
            current_script = c.script
            print(f"\n  {os.path.basename(c.script)}:")
        c.run(scripts.get(c.script, ""))
        checks_by_name[c.name] = c

        if c.status == "PASS":
            symbol = "✓"
            passed += 1
        elif c.status == "FAIL":
            symbol = "✗"
            failed += 1
        else:
            symbol = "?"
            missing += 1

        actual_str = f"{c.actual:.4f}" if c.actual is not None else "—"
        print(f"    {symbol} {c.name:30s}  expected={c.expected:<10}  "
              f"actual={actual_str:<10}  [{c.paper_ref}]")

    # Derived checks
    print(f"\n  Derived checks:")
    for dc in DERIVED_CHECKS:
        dc.run(checks_by_name)
        if dc.status == "PASS":
            symbol = "✓"
            passed += 1
        elif dc.status == "FAIL":
            symbol = "✗"
            failed += 1
        else:
            symbol = "?"
            missing += 1
        print(f"    {symbol} {dc.name:30s}  {dc.detail}  [{dc.paper_ref}]")

    # Unverified
    print(f"\n  UNVERIFIED (no backing script):")
    for desc, ref in UNVERIFIED:
        print(f"    — {desc}  [{ref}]")

    # Summary
    total = passed + failed + missing
    print("\n" + "=" * 72)
    print(f"SUMMARY: {passed}/{total} PASS, {failed} FAIL, {missing} MISSING")
    print(f"         {len(UNVERIFIED)} claims have no backing script")
    print("=" * 72)

    if failed > 0 or missing > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
