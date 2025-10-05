import torch
from GravOptAdaptiveE_demo import GravOptAdaptiveE  # Импорт от obfuscated

# По-голям модел за повече замръзване
model = torch.nn.Linear(10, 10)  # 200 параметъра – по-добре за тест
optimizer = GravOptAdaptiveE(model.parameters(), lr=0.01, freeze_percentile=30)

print("Diagnostics: median_grad =", torch.median(torch.abs(list(model.parameters())[0].grad)).item() if list(model.parameters())[0].grad is not None else "N/A")  # Твоят custom print (ако искаш)

for step in range(100):
    x = torch.randn(32, 10)  # По-голям batch за разнообразие
    y = x ** 2  # Нормализирай за стабилност
    if step == 50:
        y = x ** 3
        print("🔄 ПРОМЯНА НА ЗАДАЧАТА!")
    y_hat = model(x)
    loss = torch.mean((y_hat - y) ** 2)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    if step % 20 == 0:
        print(f"Стъпка {step}: Loss = {loss.item():.2f}")

print("✅ Тест завършен – виж принтовете за замръзване/размразяване!")