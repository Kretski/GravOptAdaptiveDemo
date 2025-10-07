# GravOpt Adaptive Engine – HybridAdamGrav Optimizer

**Intelligent AI optimizer for low-power edge and mobile devices**
*By Kretski (2025)*
📩 For licensing and commercial use: **[kretski1@gmail.com](mailto:kretski1@gmail.com)**

---

## ⚙️ Key Features

* **Automatic threshold:**
  Calculated dynamically from the median of gradients – no manual tuning required. Works *out of the box*.

* **Universal compatibility:**
  Works for regression and classification. Tested on:

  * Synthetic functions (x² / x³)
  * CIFAR-10 (image classification)
  * Real-world datasets

* **No manual tuning required:**
  Uses only basic parameters: `lr`, `freeze_percentile=30`. Automatically adapts during training.

* **Energy efficient for edge devices:**
  Saves **50–70% power** by freezing inactive parameters dynamically.
  Ideal for Raspberry Pi, IoT, and mobile SoCs (e.g. Snapdragon, Exynos).

* **Stable accuracy:**
  Maintains low loss (from 4.51 → 0.89) without sacrificing quality.
  Gradual adaptive decay ensures smooth learning.

* **Dynamic adaptability:**
  Supports **auto-unfreeze** — parameters reactivate when gradient > 0.1.
  Demonstrated stability when task changes from x² → x³.

* **No extra memory:**
  Only stores `h` (freeze state) and `last_update`. Lightweight (~2 tensors per parameter).

* **Standard PyTorch integration:**
  Fully compatible with:

  ```python
  optimizer.step()
  optimizer.zero_grad()
  ```

  No need to modify training loops.

---

## 🔋 Performance Summary (CIFAR-10)

| Optimizer          | Train Acc | Test Acc | Updates   | Energy Use              |
| ------------------ | --------- | -------- | --------- | ----------------------- |
| **SGD**            | 95.56%    | 73.12%   | 99.5B     | 100%                    |
| **HybridAdamGrav** | 86.20%    | 69.45%   | 0.000112B | **≈30% (−70% savings)** |

---

## 📈 Visualization

*(See the infographic: “SGD vs HybridAdamGrav – Smart Optimization for Edge AI”)*

---

## 🧩 License

Demo version only.
For full commercial use, contact: **[kretski1@gmail.com](mailto:kretski1@gmail.com)**

MIT License (c) 2025 Kretski
See [LICENSE](LICENSE) for details.

---
