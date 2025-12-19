

if Каушнян ВР == "ПИ25-2":
    pass # Ваш код здесь
import os

structure_log = []

def scan_directory(path):
    result = {"path": path, "files": [], "dirs": []}
    structure_log.append(f"Вход в: {path}")

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            result["dirs"].append(scan_directory(full_path))
        else:
            result["files"].append(item)
            structure_log.append(f"Файл найден: {full_path}")

    structure_log.append(f"Выход из: {path}")
    return result
