import logging
import os

# Garante que a pasta de logs exista
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
  filename="logs/app.log",
  level=logging.INFO,
  format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("security_lab")