# pylint: disable=invalid-name
"""
countains the logic for getting the number of possible computers of chief historian

"""

from collections import defaultdict


class LAN:
    """The main logic for the problem"""

    def __init__(self, file_path):
        """Initialize with the file path."""

        self.file_path = file_path
        self.relations = self.read_relations_from_file()
        self.triplet = self.find_transitive_relation(self.relations)

    def read_relations_from_file(self):
        """Read relations from a text file."""

        relations_of_files = []

        with open(self.file_path, "r", encoding="utf8") as file:
            for line in file:
                line = line.strip()
                value1, value2 = line.split("-")
                relations_of_files.append((value1, value2))

        graph = defaultdict(set)

        for a, b in relations_of_files:
            graph[a].add(b)
            graph[b].add(a)

        return graph

    def find_transitive_relation(self, graph):
        """Calculate the transitive relations."""

        triplets = set()

        # Iterate through each pair of connections
        for ax in graph:
            for bx in graph[ax]:
                if bx > ax:
                    for c in graph[bx]:
                        if c > bx and c in graph[ax]:
                            triplet = tuple(sorted([ax, bx, c]))
                            triplets.add(triplet)

        return triplets

    def find_triplets_with_t(self):
        """Find and display triplets containing the letter 't'."""
        filtered_triplets = [
            triplet
            for triplet in self.triplet
            if any(elements.startswith("t") for elements in triplet)
        ]
        return len(filtered_triplets)


# Example usage:
FILE_PATH_INPUT = "input.txt"  # Replace with your actual file path

# Create an instance of RelationProcessor
relation_processor = LAN(FILE_PATH_INPUT)

# Display the transitive relations
relation_processor.find_triplets_with_t()
