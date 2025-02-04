import json


def validate_rollup(node):
    print(f"Checking: {node['name']}")

    # if current node is a parent
    if "items" in node:
        # recursively check that each child is accurate
        calculated_sum = sum(validate_rollup(child) for child in node["items"])
        actual_value = float(node["value"])

        # round two decimal places to eliminate false positives
        if round(calculated_sum, 2) != round(actual_value, 2):
            print(
                f"Discrepancy found in '{node['name']}': Computed={calculated_sum}, Reported={actual_value}"
            )
        else:
            print(f"{node['name']} is correct.")

        return calculated_sum
    # if current node has no child nodes, return value
    else:
        return float(node["value"])


def main():
    with open("data.json", "r") as file:
        data = json.load(file)

    for key, value in data.items():
        validate_rollup(value)


if __name__ == "__main__":
    main()
