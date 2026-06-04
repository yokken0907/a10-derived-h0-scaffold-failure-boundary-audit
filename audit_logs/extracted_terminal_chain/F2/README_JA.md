# A10 Cosmology v0.5.0 — Mode F2

## 名称

symbolic-contract guard smoke

## 目的

Mode F1では、Candidate A の bridge scaffold を symbolic contract として分解した。
Mode F2では、その symbolic contract が synthetic nonnegative z-grid 上で最低限の機械的 guard を満たすかだけを確認する。

これは実データ検証ではない。likelihood、chi-square、matched LCDM comparison、MCMC、posterior、evidence は実行しない。

## Guard対象

検査対象は以下の contract-only candidate である。

```text
E_A_candidate(z; theta)
= Normalize_0[ B(z; theta_bg) * exp(epsilon * R_A(z; theta_proxy)) ]
```

F2では、`B` と `R_A` は物理方程式ではなく、synthetic guard smoke用の toy-positive / bounded proxy として扱う。

## F2で確認すること

- `E_A_candidate(z)` が finite である。
- `E_A_candidate(z) > 0` である。
- `E_A_candidate(0)=1` である。
- `1/E_A_candidate(z)` が finite / positive である。
- distance-like integral が finite / nonnegative / monotone nondecreasing である。
- negative-z domain を拒否する。
- `h0_target_label` を数値計算に使わない。

## F2で確認しないこと

- physical `E(z)` / `H(z)=H0E(z)` の成立。
- 観測距離としての妥当性。
- SN/BAO/CMB likelihood。
- ΛCDMとの比較。
- Hubble tension solution。
- ΛCDM replacement。

## 判定

`PASS_WITH_SYMBOLIC_CONTRACT_GUARD_HOLD`

F2は symbolic contract の guard smoke を通したが、D2へは進まない。
次に進む場合は Mode F3 で、guard結果を physical-status / derivation-gap matrix として整理する。
