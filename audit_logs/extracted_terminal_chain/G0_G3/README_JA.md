# A10 Cosmology v0.5.0 — Mode G0–G3 Compound Package

このパッケージは、Mode F4–F7 compound package を受けて、G0〜G3相当を1本にまとめた compound package である。

目的は、`physical bridge equation derivation` を無理に成功扱いせず、現行成果物から first-principles derivation が成立するか、成立しないならどこで止めるかを明文化すること。

## 範囲

- G0: physical bridge derivation attempt / first-principles-or-null decision
- G1: first-principles requirement inventory
- G2: candidate scaffold downgrade / derivation failure boundary
- G3: G-branch compound checkpoint closeout / next-mode handoff

## 実行していないこと

- 実データ使用
- parser 実行
- adapter 実行
- likelihood 実行
- chi-square 計算
- matched LCDM baseline 比較
- MCMC
- posterior / evidence
- Hubble tension solution claim
- Lambda-CDM replacement claim

## 現在の主張境界

本パッケージは、candidate proxy から物理的 `E(z)` / `H(z)` へ至る導出可能性の監査であり、物理方程式の導出成功を主張しない。
