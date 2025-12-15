

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



calc_log = []

def eval_expr(expr):
    expr = expr.strip()
    calc_log.append(f"Вычисляем: {expr}")

    if expr.isdigit():
        result = int(expr)
        calc_log.append(f"Результат: {result}")
        return result

    expr = expr[1:-1]
    depth = 0

    for i, ch in enumerate(expr):
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        elif ch in '+-*' and depth == 0:
            left = eval_expr(expr[:i])
            right = eval_expr(expr[i+1:])
            result = eval(f"{left}{ch}{right}")
            calc_log.append(f"{left} {ch} {right} = {result}")
            return result





perm_log = []

def permutations(items, current=[]):
    perm_log.append(f"Текущий путь: {current}")

    if not items:
        perm_log.append(f"Готовая перестановка: {current}")
        return [current]

    result = []
    for i in range(len(items)):
        result.extend(
            permutations(
                items[:i] + items[i+1:],
                current + [items[i]]
            )
        )
    return result





json_log = []

def traverse_json(data, depth=0, path="root"):
    json_log.append((depth, path, data))

    if isinstance(data, dict):
        for k, v in data.items():
            traverse_json(v, depth + 1, f"{path}.{k}")

    elif isinstance(data, list):
        for i, item in enumerate(data):
            traverse_json(item, depth + 1, f"{path}[{i}]")




path_log = []

def shortest_path(graph, current, target, visited=None, cost=0, path=None):
    if visited is None:
        visited = set()
        path = []

    visited.add(current)
    path.append(current)
    path_log.append((path[:], cost))

    if current == target:
        return cost, path[:]

    best = (float('inf'), None)

    for neighbor, weight in graph[current].items():
        if neighbor not in visited:
            result = shortest_path(
                graph, neighbor, target,
                visited.copy(), cost + weight, path[:]
            )
            if result and result[0] < best[0]:
                best = result

    return best





cycle_log = []
cycles = []

def find_cycles(graph, start, current, visited, path):
    visited.add(current)
    path.append(current)
    cycle_log.append((visited.copy(), path[:]))

    for neighbor in graph[current]:
        if neighbor == start and len(path) > 2:
            cycles.append(path[:] + [start])
        elif neighbor not in visited:
            find_cycles(graph, start, neighbor, visited.copy(), path[:])
