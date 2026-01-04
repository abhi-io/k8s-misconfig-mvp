from app.engine.json_path import extract_values


def evaluate_rule(raw_pod: dict, rule: dict) -> bool:
    values = extract_values(raw_pod, rule["condition"]["path"])

    if not values:
        return False

    expected = rule["condition"]["equals"]
    return any(value == expected for value in values)
