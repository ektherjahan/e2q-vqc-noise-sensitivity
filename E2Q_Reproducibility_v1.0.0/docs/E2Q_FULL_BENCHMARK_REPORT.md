# E2Q Proxy Full Benchmark Report

**Verdict:** `PASS`

## Frozen hypotheses

- H1 predictive validity: **True**
- H2 calibration value-add beyond N2Q/depth: **True**
- H3 within-architecture temporal sensitivity: **True**
- Leave-one-family robustness: **True**

## E2Q predictive validity by dataset/backend

| dataset       | backend       |   spearman_rho |   kendall_tau |   ci95_low |   ci95_high |
|:--------------|:--------------|---------------:|--------------:|-----------:|------------:|
| breast_cancer | ibm_fez       |         0.9104 |        0.7468 |     0.7878 |      0.9531 |
| breast_cancer | ibm_kingston  |         0.5213 |        0.3749 |     0.3669 |      0.6696 |
| breast_cancer | ibm_marrakesh |         0.6706 |        0.4836 |     0.3841 |      0.8050 |
| iris_binary   | ibm_fez       |         0.9045 |        0.7438 |     0.7943 |      0.9625 |
| iris_binary   | ibm_kingston  |         0.3323 |        0.2253 |     0.1637 |      0.5548 |
| iris_binary   | ibm_marrakesh |         0.5616 |        0.3958 |     0.2673 |      0.7750 |
| digits_01     | ibm_fez       |         0.8196 |        0.6411 |     0.6239 |      0.9340 |
| digits_01     | ibm_kingston  |         0.5057 |        0.3639 |     0.2216 |      0.7383 |
| digits_01     | ibm_marrakesh |         0.6226 |        0.4576 |     0.3077 |      0.8118 |

## E2Q within-architecture temporal sensitivity

| dataset       | backend       |   demeaned_spearman_rho |   ci95_low |   ci95_high |
|:--------------|:--------------|------------------------:|-----------:|------------:|
| breast_cancer | ibm_fez       |                  0.9304 |     0.8622 |      0.9617 |
| breast_cancer | ibm_kingston  |                  0.8428 |     0.7815 |      0.8821 |
| breast_cancer | ibm_marrakesh |                  0.3423 |     0.2611 |      0.4009 |
| iris_binary   | ibm_fez       |                  0.9326 |     0.8648 |      0.9670 |
| iris_binary   | ibm_kingston  |                  0.7936 |     0.7525 |      0.8450 |
| iris_binary   | ibm_marrakesh |                  0.3627 |     0.2688 |      0.4284 |
| digits_01     | ibm_fez       |                  0.9163 |     0.8498 |      0.9563 |
| digits_01     | ibm_kingston  |                  0.8152 |     0.7349 |      0.8784 |
| digits_01     | ibm_marrakesh |                  0.3049 |     0.2157 |      0.3715 |

## Proxy comparison across nine cells

| proxy   |   mean_rho |   median_rho |   min_rho |   max_rho |
|:--------|-----------:|-------------:|----------:|----------:|
| CARE    |     0.6377 |       0.6213 |    0.4129 |    0.8390 |
| Depth   |     0.4122 |       0.4759 |    0.1244 |    0.6188 |
| E2Q     |     0.6499 |       0.6226 |    0.3323 |    0.9104 |
| N2Q     |     0.4211 |       0.4758 |    0.0901 |    0.6016 |
| OLD     |     0.6342 |       0.6128 |    0.4107 |    0.8415 |

## Pooled summary

| proxy   |   pooled_rho_median |   pooled_ci95_low |   pooled_ci95_high |   temporal_rho_median |   temporal_ci95_low |   temporal_ci95_high |
|:--------|--------------------:|------------------:|-------------------:|----------------------:|--------------------:|---------------------:|
| N2Q     |              0.4330 |          nan      |           nan      |              nan      |            nan      |             nan      |
| Depth   |              0.4232 |          nan      |           nan      |              nan      |            nan      |             nan      |
| E2Q     |              0.7044 |            0.5472 |             0.8289 |                0.7807 |              0.6136 |               0.8812 |
| OLD     |              0.6578 |          nan      |           nan      |                0.6738 |            nan      |             nan      |
| CARE    |              0.6600 |          nan      |           nan      |                0.6720 |            nan      |             nan      |

## H2 complexity comparison

| dataset       | backend       |   CARE |   Depth |    E2Q |    N2Q |    OLD |   structural_best |   E2Q_advantage |
|:--------------|:--------------|-------:|--------:|-------:|-------:|-------:|------------------:|----------------:|
| breast_cancer | ibm_fez       | 0.8390 |  0.5342 | 0.9104 | 0.5789 | 0.8415 |            0.5789 |          0.3315 |
| breast_cancer | ibm_kingston  | 0.5322 |  0.2412 | 0.5213 | 0.2938 | 0.5277 |            0.2938 |          0.2275 |
| breast_cancer | ibm_marrakesh | 0.6645 |  0.4759 | 0.6706 | 0.5340 | 0.6580 |            0.5340 |          0.1365 |
| digits_01     | ibm_fez       | 0.7893 |  0.6188 | 0.8196 | 0.6016 | 0.7902 |            0.6188 |          0.2008 |
| digits_01     | ibm_kingston  | 0.5265 |  0.2866 | 0.5057 | 0.2769 | 0.5165 |            0.2866 |          0.2191 |
| digits_01     | ibm_marrakesh | 0.6213 |  0.5429 | 0.6226 | 0.5321 | 0.6128 |            0.5429 |          0.0797 |
| iris_binary   | ibm_fez       | 0.7841 |  0.4770 | 0.9045 | 0.4758 | 0.7886 |            0.4770 |          0.4275 |
| iris_binary   | ibm_kingston  | 0.4129 |  0.1244 | 0.3323 | 0.0901 | 0.4107 |            0.1244 |          0.2079 |
| iris_binary   | ibm_marrakesh | 0.5690 |  0.4087 | 0.5616 | 0.4068 | 0.5621 |            0.4087 |          0.1529 |

## Interpretation rules

The frozen E2Q proxy satisfies all prespecified cross-dataset validity, calibration-value-add, temporal-sensitivity, and family-robustness criteria. Proceed to manuscript preparation; direct real-QPU confirmation is optional future work and is not part of this release.

## Scope caveats

- Noise validation uses sparse four-qubit Aer models reconstructed from historical compact IBM calibration data, not real-QPU executions.
- Readout is approximated symmetrically from the stored average readout error.
- The architecture panel is the exact 16-circuit panel frozen in the prior proxy-validation stage.
- Exact density-matrix probabilities remove shot noise; training-seed variability is handled separately.