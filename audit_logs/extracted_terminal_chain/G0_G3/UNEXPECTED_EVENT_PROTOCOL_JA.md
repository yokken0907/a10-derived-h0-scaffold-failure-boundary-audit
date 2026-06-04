# Unexpected-event protocol

本compound packageでは、想定済みの整理・降格・gate判定をG0〜G3としてまとめた。

## 想定外扱いにする条件

- source SHA256が一致しない。
- forbidden operation counter が非ゼロになる。
- `first_principles_physical_E_derivation_found=True` になる。
- `D2_READY=True` になる。
- likelihood / chi-square / MCMC / posterior / evidence が発火する。
- Hubble tension solution claim または Lambda-CDM replacement claim が生成される。
- h0_target_label が物理パラメータとして混入する。
- null-control candidate が primary candidate と同等扱いになる。

## 想定外時の扱い

該当箇所だけを単独モードとして再検証する。compound全体を最初からやり直さない。
