"""
Find order legs for cross order
quotes = {
  "GBP/AUD": 1.75,

  "GBP/USD": 1.26,

  "USD/CZK": 23.01,
  "CZK/EUR": 0.04,

  "USD/DKK": 6.92,
  "DKK/EUR": 0.13
}


Example 1
Input = ["GBP", "AUD"]
Output = [["GBP/AUD"]]


Example 2
Input = ["GBP", "EUR"]
Output = [["GBP/USD", "USD/DKK", "DKK/EUR"], ["GBP/USD", "USD/CZK", "CZK/EUR"]]
"""

from collections import defaultdict, OrderedDict


class Graph:
    def __init__(self, quotes):
        self.quotes = quotes
        self.graph = self.get_graph()

    @staticmethod
    def get_full_path(path):
        pairs = []

        begin = path[0]
        for current in path[1:]:
            pair = f"{begin}/{current}"
            pairs += [pair]
            begin = current
        return pairs

    def search(self, _from, _to):
        buf = [(_from, [_from])]

        paths = []
        while buf:
            node, path = buf.pop()
            for next in filter(lambda x: x not in path, self.graph[node]):
                if next == _to:
                    paths += [self.get_full_path(path + [next])]
                else:
                    buf += [(next, path + [next])]
        return paths

    def get_graph(self):
        buf = defaultdict(list)
        for quote in self.quotes:
            base, target = quote.split("/")
            buf[base] += [target]
            buf[target] += [base]
        return buf

    def __repr__(self):
        return f"{self.graph}"


def find(input, quotes):
    graph = Graph(quotes)
    paths = graph.search(input[0], input[1])
    return paths


def test1():
    quotes = {
        "GBP/AUD": 1.75,

        "GBP/USD": 1.26,

        "USD/CZK": 23.01,
        "CZK/EUR": 0.04,

        "USD/DKK": 6.92,
        "DKK/EUR": 0.13
    }
    input = ["GBP", "AUD"]
    exp = [["GBP/AUD"]]
    print("exp1: ", exp)
    print("act2: ", find(input, quotes))


def test2():
    quotes = {
        "GBP/AUD": 1.75,

        "GBP/USD": 1.26,

        "USD/CZK": 23.01,
        "CZK/EUR": 0.04,

        "USD/DKK": 6.92,
        "DKK/EUR": 0.13
    }
    input = ["GBP", "EUR"]
    exp = [["GBP/USD", "USD/DKK", "DKK/EUR"], ["GBP/USD", "USD/CZK", "CZK/EUR"]]
    print("exp2: ", exp)
    print("act2: ", find(input, quotes))


def test3():
    quotes = {
        "GBP/AUD": 1.75,

        "GBP/USD": 1.26,

        "USD/CZK": 23.01,
        "CZK/RUB": 0.04,

        "USD/DKK": 6.92,
        "DKK/RUB": 0.13
    }
    input = ["GBP", "EUR"]
    exp = []
    print("exp3: ", exp)
    print("act3: ", find(input, quotes))


def test4():
    quotes = OrderedDict({
        "GBP/EUR": 1.7,
        "GBP/AUD": 1.75,

        "GBP/USD": 1.26,

        "USD/CZK": 23.01,
        "CZK/EUR": 0.04,

        "USD/DKK": 6.92,
        "DKK/EUR": 0.13
    })
    input = ["GBP", "EUR"]
    exp = [["GBP/EUR"], ["GBP/USD", "USD/DKK", "DKK/EUR"], ["GBP/USD", "USD/CZK", "CZK/EUR"]]
    print("exp4: ", exp)
    print("act4: ", find(input, quotes))


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
