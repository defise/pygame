import os

def load_level(filename):
    # Определяем путь к папке levels относительно этого файла
    base_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'levels')
    full_path = os.path.join(base_path, filename)
    with open(full_path, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile if line.strip()]
    max_width = max(map(len, level_map))
    return [line.ljust(max_width, '.') for line in level_map]
