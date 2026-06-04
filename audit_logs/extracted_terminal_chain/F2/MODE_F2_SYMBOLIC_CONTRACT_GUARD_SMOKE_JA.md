# Mode F2 — symbolic-contract guard smoke

## 位置づけ

F2は、F1で抽出された symbolic contract を小さな synthetic grid 上で機械的に検査する段階である。
この検査は、物理的宇宙論モデルの成立を意味しない。

## 使用するguard-only定義

```text
B_toy(z) = 1 + alpha * z / (1 + z)
R_A_toy(z) = kappa * z / (1 + z)
E_A_candidate(z; epsilon)
= [B_toy(z) * exp(epsilon * R_A_toy(z))]
  / [B_toy(0) * exp(epsilon * R_A_toy(0))]
```

F2の既定値:

```text
alpha = 0.30
kappa = 0.50
epsilon ∈ {-0.10, 0.00, +0.10}
z ∈ {0.0, 0.1, 0.5, 1.0, 2.0, 3.0}
```

## 重要な限定

この `B_toy` は ΛCDM baseline ではない。
この `R_A_toy` はA10の物理的導出済み残差関数ではない。
この `E_A_candidate` は physical `E(z)` ではない。

F2は「この形のcontractが有限性・正値性・正規化・積分guardを通過し得るか」だけを見る。
