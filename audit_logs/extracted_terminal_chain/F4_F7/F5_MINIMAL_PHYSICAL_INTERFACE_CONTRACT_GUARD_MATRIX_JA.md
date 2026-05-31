# F5 — minimal physical-interface contract guard matrix

F5は、F4の contract が少なくとも機械的に守るべき guard を整理する。

| guard | 要求 | status |
|---|---|---|
| domain | z >= 0 only | REQUIRED |
| finite E | E_candidate(z) finite | REQUIRED |
| positivity | E_candidate(z) > 0 | REQUIRED |
| normalization | E_candidate(0)=1 | REQUIRED |
| reciprocal | 1/E_candidate(z) finite and positive | REQUIRED |
| distance-like integral | finite, nonnegative, monotone nondecreasing | REQUIRED_AS_SCAFFOLD |
| h0_target leakage | h0_target_label not used as physical parameter | REQUIRED |
| null-control | Candidate N remains null-control only | REQUIRED |
| physical claim | no physical E/H claim | REQUIRED_BOUNDARY |
| D2 transition | blocked until physical derivation and observable mapping exist | HOLD |

## F5判定

F5は guard matrix として成立する。これは物理式の検証ではない。
