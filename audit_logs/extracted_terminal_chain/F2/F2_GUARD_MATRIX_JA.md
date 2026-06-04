# F2 guard matrix

| Guard | Status | Interpretation |
|---|---:|---|
| finite `E_A_candidate(z)` | PASS | symbolic contract can emit finite values on synthetic nonnegative grid |
| positive `E_A_candidate(z)` | PASS | no zero/negative expansion-proxy values in this toy guard |
| `E_A_candidate(0)=1` | PASS | normalization operator works in this toy guard |
| finite/positive `1/E_A_candidate(z)` | PASS | distance-like integral input is numerically well-defined |
| distance-like integral finite/nonnegative/monotone | PASS | mathematical integral guard passes |
| negative-z rejection | PASS | domain guard present |
| h0_target_label leakage | PASS | no h0 target label used as numeric input |
| real data | NOT USED | no external assets or observations |
| likelihood/comparison/MCMC | NOT EXECUTED | D2 remains blocked |

## F2 interpretation

F2 upgrades the scaffold from “only drafted” to “guard-smoke-clean as a symbolic contract”.
It does **not** upgrade the scaffold to physical cosmology.
