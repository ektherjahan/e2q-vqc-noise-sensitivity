# Processed evidence tables

These files are the frozen processed outputs used by the E2Q manuscript. They are not raw IBM credential-bearing exports.

| File | Rows | Columns | Leading fields |
|---|---:|---:|---|
| `analysis_table_seed_averaged.csv` | 576 | 25 | dataset, backend, snapshot, architecture_id, entanglement, reps, twoq_count, logical_depth ... |
| `calibration_provenance.csv` | 12 | 6 | backend, snapshot, requested_timestamp, returned_timestamp, physical_qubits, raw_sha256 |
| `cell_proxy_correlations.csv` | 45 | 9 | dataset, backend, proxy, spearman_rho, kendall_tau, ci95_low, ci95_high, n_architectures ... |
| `dataset_metadata.csv` | 3 | 7 | dataset, fit_n, val_n, test_n, noisy_test_n, positive_rate_fit, pca_explained_variance_sum |
| `h2_complexity_value_add.csv` | 9 | 9 | dataset, backend, CARE, Depth, E2Q, N2Q, OLD, structural_best ... |
| `hierarchical_pooled_proxy_summary.csv` | 5 | 7 | proxy, pooled_rho_median, pooled_ci95_low, pooled_ci95_high, temporal_rho_median, temporal_ci95_low, temporal_ci95_high |
| `ideal_training_summary.csv` | 240 | 16 | dataset, seed, architecture_id, rotations, entanglement, reps, twoq_count, logical_depth ... |
| `leave_one_entanglement_family_out.csv` | 36 | 6 | dataset, backend, left_out_family, spearman_rho, n_architectures, n_rows |
| `seed_level_e2q_robustness.csv` | 27 | 6 | dataset, backend, seed, E2Q, N2Q, Depth |
| `temporal_demeaned_correlations.csv` | 45 | 7 | dataset, backend, proxy, demeaned_spearman_rho, demeaned_kendall_tau, ci95_low, ci95_high |

The benchmark configuration and frozen 16-architecture panel are in `../config/`.
See `../docs/E2Q_FULL_BENCHMARK_REPORT.md` for the benchmark-level readout.
