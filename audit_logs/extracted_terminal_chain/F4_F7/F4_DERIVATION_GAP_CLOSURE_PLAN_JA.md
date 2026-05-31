# F4 — derivation-gap closure plan / minimal physical-interface contract draft

## F4の目的

F3で明示された derivation gap を、次に何を満たせば閉じられるかという contract として整理する。

## 最小 physical-interface contract 候補

候補は、以下のような形式の scaffold に限定される。

```text
E_candidate(z; theta)
= Normalize_0[ B(z; theta_bg) * exp(epsilon * R_A(z; theta_proxy)) ]
```

ただし、これはまだ physical `E(z)` ではない。

## physical `E(z)` と呼ぶために必要なもの

1. `B(z; theta_bg)` が物理的背景項として定義されること。
2. `R_A(z; theta_proxy)` が単なる曲線ではなく、A10側の構造から導出または明確に仮説化されること。
3. `epsilon` が任意調整つまみではなく、許容範囲・符号・次元・解釈を持つこと。
4. `Normalize_0` が `E(0)=1` を満たすための数学操作であることを明示し、観測値への後付け調整として扱わないこと。
5. `h0_target_label` が物理パラメータとして侵入しないこと。
6. null-control bridge が分離されること。
7. observable distance への写像は、distance-like integral とは別に定義されること。

## F4判定

- derivation gap の位置は特定済み。
- 最小 contract は書ける。
- 物理導出はまだ成立していない。
- D2へは進まない。
