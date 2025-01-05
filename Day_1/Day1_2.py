# pylint: disable=invalid-name
"""
Getting the total distance between the left and right list

"""


class Similarity:
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

        return list_1, list_2

    def similarity_score(self):
        """Calculating Total Distance"""
        SIMILARITY_SCORE = 0
        list_1, list_2 = self.sorted_list
        for value2 in list_2:
            sim = int(value2) * int(list_1.count(value2))
            SIMILARITY_SCORE += sim
        return SIMILARITY_SCORE


# Example usage:
FILE_PATH_INPUT = "input.txt"  # Replace with your actual file path

# Create an instance of RelationProcessor
relation_processor = Similarity(FILE_PATH_INPUT)

# Display the transitive relations
relation_processor.similarity_score()
