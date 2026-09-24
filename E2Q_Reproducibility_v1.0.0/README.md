# E2Q: Calibration-Weighted Two-Qubit Exposure

Reproducibility package for the manuscript **"E2Q: Calibration-Weighted Two-Qubit Exposure for Screening Noise Sensitivity in Variational Quantum Classifiers"**.

**Authors:** Ekther Jahan; Md. Hasibul Hassan Himal  
**Affiliation:** Department of Computer Science and Engineering, Bangladesh University, Dhaka, Bangladesh  
**Version:** 1.0.0 (2026-09-21)

## What E2Q is

For architecture `a` at calibration state `t`, the proxy is

```text
E2Q_t(a) = sum over two-qubit gates g in a of  -log(1 - epsilon_{g,t})
```

where `epsilon_{g,t}` is the hardware-reported two-qubit gate error for the physical edge used by the circuit.

The primary outcome is noise-induced probability distortion:

```text
D(a,t) = mean_i | p_i^ideal - p_i,t^noisy |
```

This release supports a simulation-based study using historical IBM calibration snapshots. It **does not** claim physical-QPU validation, improved classification accuracy, quantum advantage, or a new quantum-architecture-search optimizer.

## Frozen benchmark

- Datasets: Breast Cancer, Iris binary, Digits 0-vs-1
- Backends: `ibm_fez`, `ibm_kingston`, `ibm_marrakesh`
- Four frozen historical calibration states per backend
- Frozen 16-architecture validation panel
- Five ideal-training seeds; three prespecified trained seeds for noisy validation
- Exact density-matrix probability simulation (shot-noise-free)
- Primary association: Spearman correlation between E2Q and probability MAE

Frozen verdict: **PASS**.

Selected benchmark summaries from `config/benchmark_verdict.json`:

- E2Q positive in 9/9 dataset-backend cells
- E2Q >= 0.40 in 8/9 cells
- E2Q beat both structural baselines (`N2Q` and logical depth) in 9/9 cells
- within-architecture temporal association positive in 9/9 cells
- leave-one-entanglement-family-out checks positive in 36/36 cases
- pooled E2Q Spearman rho = 0.7044, 95% CI [0.5472, 0.8289]
- pooled temporal Spearman rho = 0.7807, 95% CI [0.6136, 0.8812]

## Repository layout

```text
.
├── CITATION.cff
├── LICENSE
├── LICENSE_DATA.md
├── README.md
├── VERSION
├── requirements.txt
├── GITHUB_ZENODO_INSTRUCTIONS.md
├── ZENODO_METADATA.md
├── RELEASE_NOTES_v1.0.0.md
├── SHA256SUMS.txt
├── notebooks/
│   └── E2Q_Proxy_Full_Benchmark.ipynb
├── config/
│   ├── benchmark_config.json
│   ├── benchmark_verdict.json
│   └── source_panel_16.csv
├── data/
│   ├── README.md
│   └── processed/
├── docs/
│   └── E2Q_FULL_BENCHMARK_REPORT.md
├── figures/
│   ├── Fig1.png
│   ├── Fig2.png
│   ├── Fig3.png
│   └── Fig4.png
└── scripts/
    └── verify_release.py
```

## Quick integrity check

No Qiskit installation is needed to verify the archived files and frozen verdict:

```bash
python scripts/verify_release.py
```

## Reproduce the full benchmark

### Option A - Google Colab

1. Open `notebooks/E2Q_Proxy_Full_Benchmark.ipynb` in Colab.
2. Run the notebook top-to-bottom.
3. The notebook installs its required scientific stack and restores its embedded frozen source bundle.
4. No IBM Quantum token or IBM Runtime login is required for this historical-calibration simulation benchmark.

### Option B - local Jupyter

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab notebooks/E2Q_Proxy_Full_Benchmark.ipynb
```

Run all cells in order. The full benchmark includes training and sparse four-qubit density-matrix simulations, so runtime depends on CPU/RAM and may be substantial.

## Protocol terminology

The hypotheses, thresholds, architecture panel, calibration indices, and seed choices were **prespecified and frozen internally before the full benchmark was evaluated**. They were not registered in a public preregistration registry. Public-release wording has been normalized to reflect that distinction; numerical methods and results are unchanged.

## Data provenance

The notebook embeds compact historical calibration/source artifacts previously frozen for this project. The public release contains no IBM API key, token, account CRN, password, or other credential. Calibration provenance used in the manuscript is provided in `data/processed/calibration_provenance.csv`.

## Citation

GitHub will expose a **Cite this repository** panel from `CITATION.cff`. After the GitHub release is archived by Zenodo, cite the **version-specific Zenodo DOI** for the exact release used in the manuscript.

## Licensing

- Notebook and scripts: MIT License (`LICENSE`).
- Project-generated processed evidence tables and figures: CC BY 4.0 (`LICENSE_DATA.md`).
- Third-party packages and source datasets retain their own licenses and terms.

## Contact

Corresponding author: **Ekther Jahan**  
Department of Computer Science and Engineering, Bangladesh University, Dhaka, Bangladesh  
Email: `ektherjahan.bu@gmail.com`
