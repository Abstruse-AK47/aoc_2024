# pylint: disable=invalid-name
"""
Getting the total distance between the left and right list

"""


class Smallest:
    """The main logic for the problem"""

    def __init__(self, file_path):
        """Initialize with the file path."""

        self.file_path = file_path
        self.sorted_list = self.create_sorted_list_from_file()

    def create_sorted_list_from_file(self):
        """Read relations from a text file."""

        list_1 = []
        list_2 = []

        with open(self.file_path, "r", encoding="utf8") as file:
            for line in file:
                line = line.strip()
                value1, value2 = line.split("   ")
                list_1.append(value1)
                list_2.append(value2)

        list_1_sorted = sorted(list_1)
        list_2_sorted = sorted(list_2)
        return list_1_sorted, list_2_sorted

    def total_distance(self):
        """Calculating Total Distance"""
        distance = 0
        list_1_sorted, list_2_sorted = self.sorted_list
        for i, value2 in enumerate(list_2_sorted):
            diff = int(list_1_sorted[i]) - int(value2)
            distance += abs(diff)
        return distance


# Example usage:
FILE_PATH_INPUT = "input.txt"  # Replace with your actual file path

# Create an instance of RelationProcessor
relation_processor = Smallest(FILE_PATH_INPUT)

# Display the transitive relations
relation_processor.total_distance()
