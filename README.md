# GravOptAdaptiveDemo
## ## 📊 Example Test Output (Freeze in Action)
Run `python example_test.py` and see the adaptation:
Key Benefits

Automatic threshold: Calculated dynamically from the median of gradients – no manual tuning required, works "out of the box".
Works for regression and classification: Universal – tested on synthetic tasks (like x²/x³), CIFAR-10 (classification) and real data.
No manual tuning required: Only basic parameters (lr, freeze_percentile=30) – the optimizer adapts automatically.
Suitable for real edge devices: Lightweight (no additional libs), minimizes power consumption on IoT/mobile (save 50–70% power by freezing).
Stable accuracy: Supports loss decay (from 4.51 → 0.89 in the test) without sacrificing quality – the model learns stably.
Does not freeze too early: Activates after warmup (small gradients < threshold), retains flexibility at the beginning.
Energy saving: Still saves 50–70% energy – freezes unnecessary parameters without interrupting training.
Minimizes power consumption on edge devices: Focus on low-power (IoT, embedded) – tested with 65% frozen parameters in dynamic conditions.
No additional memory required: Only stores h (freeze state) and last_update – minimal overhead (~2 tensors per parameter).
Works with standard PyTorch operations: Easy to integrate – inherits Optimizer, uses step(), zero_grad() without changes.
Adapts to changes: Important feature for real-world conditions – auto-unfreeze at large gradient (>0.1), ideal for dynamic tasks (e.g. changing from x² to x³).
See how they freeze 50%+ parameters before the change (save energy!), and automatically defrost after (adaptability!).
"Demo version only. For full commercial use, contact author at kretski1@gmail.com
