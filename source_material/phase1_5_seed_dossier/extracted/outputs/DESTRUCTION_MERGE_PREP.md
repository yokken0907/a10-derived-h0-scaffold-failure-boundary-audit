# Destruction Merge Preparation

Use `data/destruction_merge_template.csv` as the receiving table for the separate ΛCDM destruction-test outputs.

Required merge fields:

```text
lcdm_comparator_result
benchmark_delta_neff_result
benchmark_ede_result
cmb_tt_cost
cmb_ee_te_cost
bao_sn_cost
prior_sensitivity
recommendation_after_merge
```

Promotion rule:

```text
A component may only move from candidate to usable seed if it survives comparator, benchmark, perturbative, residual-cost, and prior-sensitivity checks.
```
