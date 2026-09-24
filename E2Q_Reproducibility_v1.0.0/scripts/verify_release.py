from pathlib import Path
import hashlib, json, sys

root = Path(__file__).resolve().parents[1]
manifest = root / "SHA256SUMS.txt"
errors = []
for line in manifest.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    digest, rel = line.split("  ", 1)
    p = root / rel
    if not p.exists():
        errors.append(f"MISSING: {rel}")
        continue
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    if got != digest:
        errors.append(f"HASH MISMATCH: {rel}")

verdict = json.loads((root / "config/benchmark_verdict.json").read_text(encoding="utf-8"))
required = {
    "verdict": "PASS",
    "h1_positive_cells": 9,
    "h2_cells_beating_both_structural_baselines": 9,
    "h3_positive_cells": 9,
    "family_positive_checks": 36,
}
for key, expected in required.items():
    if verdict.get(key) != expected:
        errors.append(f"VERDICT FIELD {key}: expected {expected!r}, got {verdict.get(key)!r}")

if errors:
    print("Release verification FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("Release verification PASSED")
print("Version:", (root / "VERSION").read_text().strip())
print("Frozen benchmark verdict:", verdict["verdict"])
print("Pooled E2Q Spearman rho:", round(verdict["pooled_e2q_rho"], 6))
print("Pooled temporal Spearman rho:", round(verdict["pooled_temporal_rho"], 6))
