import os

STATS_FILE = 'stats.txt'

def load_best():
    """Загружает лучшее количество попыток (минимальное)."""
    if not os.path.exists(STATS_FILE):
        return None
    with open(STATS_FILE, 'r') as f:
        try:
            return int(f.read().strip())
        except ValueError:
            return None

def save_best(attempts):
    """Сохраняет новое лучшее достижение."""
    with open(STATS_FILE, 'w') as f:
        f.write(str(attempts))