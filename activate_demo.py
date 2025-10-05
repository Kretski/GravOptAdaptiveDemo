import datetime
import os

# [DEMO] Генерирай timestamp за 30 дни
activation_date = datetime.datetime.now()
expiry_date = activation_date + datetime.timedelta(days=30)
timestamp_data = f"Activated: {activation_date.isoformat()}\nExpires: {expiry_date.isoformat()}\nDEMO VERSION - GravOptAdaptiveE"

with open("demo_timestamp.txt", "w") as f:
    f.write(timestamp_data)

print(f"✅ [DEMO] Демо активирано! Работи до {expiry_date.strftime('%Y-%m-%d')}.")
print("[DEMO] За пълна версия – свържи се с автора: gravopt@example.com")