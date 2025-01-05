# pylint: disable=invalid-name
"""
countains the logic to get the password
NOT MINE COPIED FROM REDDIT
"""


class LAN:
    """finding password"""

    def __init__(self, filename):
        self.conns = set()
        self.vs = set()
        self.adj = {}
        self.read_input(filename)

    def read_input(self, filename):
        """Read input file and process connections"""

        with open(filename, "r", encoding="utf8") as f:
            c = f.read()[:-1].split("\n")

        for l in c:
            a = l[:2]
            b = l[3:]
            self.conns.add((a, b))
            self.vs.add(a)
            self.vs.add(b)

        for v in self.vs:
            self.adj[v] = []

        for conn in self.conns:
            self.adj[conn[0]].append(conn[1])
            self.adj[conn[1]].append(conn[0])

    def find_path(self, posvs, rem):
        """Recursive function to find a path with a specific length"""

        if rem == 0:
            return []
        for v in posvs:
            posvs2 = filter(lambda x, v=v: x != v and (x in self.adj[v]), posvs)
            ret = self.find_path(posvs2, rem - 1)
            if ret != -1:
                ret.append(v)
                return ret
        return -1

    def solve(self):
        """Main function to try finding paths and output the result"""

        prev = -1
        for i in range(1, 100):
            ret = self.find_path(list(self.vs), i)
            if ret == -1:
                break
            prev = ret

        # Print the result as a sorted list of nodes
        print(",".join(sorted(list(prev))))


# Example usage
graph = LAN("input.txt")
graph.solve()
