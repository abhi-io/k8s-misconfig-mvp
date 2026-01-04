def extract_values(obj, path):
    """
    Supports paths like:
    spec.containers[*].securityContext.runAsNonRoot
    """
    parts = path.split(".")

    def walk(current, index):
        if current is None:
            return []

        if index == len(parts):
            return [current]

        part = parts[index]

        if part.endswith("[*]"):
            key = part[:-3]
            results = []
            for item in current.get(key, []):
                results.extend(walk(item, index + 1))
            return results

        return walk(current.get(part), index + 1)

    return walk(obj, 0)
