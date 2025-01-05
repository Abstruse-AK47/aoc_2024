# pylint: disable=invalid-name
"""
countains the logic for changing the values and counting the cases

"""


def classify_and_count(test):
    """Counting the cases"""
    # Counters for the four cases
    case_counters = {"case_1": 0, "case_2": 0, "case_3": 0, "case_4": 0}
    results = []  # To store the computed values and their classifications

    # Process each line
    for line in test:
        if not line.strip():  # Skip empty lines
            continue
        parts = line.split()
        p_part = parts[0].split("=")[1]  # Extract p values
        v_part = parts[1].split("=")[1]  # Extract v values

        # Convert to tuples of integers
        p_x, p_y = map(int, p_part.split(","))
        v_x, v_y = map(int, v_part.split(","))

        # Compute the new x and y with modular arithmetic
        x = (p_x + 100 * v_x) % 101
        y = (100 * v_y + p_y) % 103

        if x == 50:
            continue
        if y == 51:
            continue
        # Classify based on conditions
        if x < 50 and y < 51:
            case_counters["case_1"] += 1
            case = "case_1"
        elif x > 50 and y < 51:
            case_counters["case_2"] += 1
            case = "case_2"
        elif x < 50 and y > 51:
            case_counters["case_3"] += 1
            case = "case_3"
        else:
            case_counters["case_4"] += 1
            case = "case_4"

        results.append({"p": (p_x, p_y), "v": (v_x, v_y), "x": x, "y": y, "case": case})
    return case_counters, results


FILE_PATH = "input.txt"
# Open the file and read lines
with open(FILE_PATH, "r", encoding="utf8") as file:
    lines = file.readlines()


case_counter, classified_results = classify_and_count(lines)

# Multiply the counts at the end
PRODUCT_OF_COUNTS = 1
for cases, count in case_counter.items():
    PRODUCT_OF_COUNTS *= count

# Display the results
print("Case Counters:")
for cases, count in case_counter.items():
    print(f"{cases}: {count}")

print(f"\nProduct of counts: {PRODUCT_OF_COUNTS}")
