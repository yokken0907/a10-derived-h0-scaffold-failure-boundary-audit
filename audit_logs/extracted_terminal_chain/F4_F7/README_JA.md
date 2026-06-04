# A10 Cosmology v0.5.0 — Mode F4–F7 Compound Package

このパッケージは、Mode F3 の `physical-status / derivation-gap matrix` を受けて、F4〜F7相当を1本にまとめた compound package である。

目的は、単発フェーズの連打を避け、想定済みの整理工程をまとめて処理し、想定外フラグが立った箇所だけを後続で分岐再検証できるようにすること。

## 範囲

- F4: derivation-gap closure plan / minimal physical-interface contract draft
- F5: minimal physical-interface contract guard matrix
- F6: D2 precondition and no-go/go gate matrix
- F7: F-branch compound checkpoint closeout / next-mode handoff

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

本パッケージは、A10 cosmology candidate proxy から物理的 `E(z)` / `H(z)` へ進むための条件整理であり、物理方程式の確定ではない。
