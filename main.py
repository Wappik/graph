names_index_dict = {
    "боинг-747": 1,
    "самолет": 2,
    "мотор": 3,
    "пилот": 4,
    "бензин": 5,
    "крылья": 6,
    "летать": 7,
    "аэродинамика": 8,
    "сокол": 9,
    "птица": 10,
    "орел": 11,
    "клюв": 12,
    "оперение": 13,
}

index_names_dict = {
    1: "боинг-747",
    2: "самолет",
    3: "мотор",
    4: "пилот",
    5: "бензин",
    6: "крылья",
    7: "летать",
    8: "аэродинамика",
    9: "сокол",
    10: "птица",
    11: "орел",
    12: "клюв",
    13: "оперение",
}


class Node:
    def __init__(self, vertex, next=None, previous=None):
        self.vertex = vertex
        # vertex = 1
        # next = [
        #     ["имеет", 3],
        #     ["имеет", 4],
        #     ["имеет", 6],
        #     ["умеет", 7],
        #     ["использует", 8]
        # ]
        # previous = [["является", 1]]
        self.next = [] if next is None else next
        self.previous = [] if next is None else previous

    def print_node(self):
        print(f"{index_names_dict[self.vertex].title()}:")
        if not (self.previous is None):
            for value in self.previous:
                print(f"\t{index_names_dict[value[1]].title()}--->\t{value[0]}\t--->{index_names_dict[self.vertex].title()}")
        if not (self.next is None):
            for value in self.next:
                print(f"\t{index_names_dict[self.vertex].title()}--->\t{value[0]}\t--->{index_names_dict[value[1]].title()}")

    def print_node_next(self):
        print(f"{index_names_dict[self.vertex].title()}:")
        if not (self.next is None):
            for value in self.next:
                print(f"\t{index_names_dict[self.vertex].title()}--->\t{value[0]}\t--->{index_names_dict[value[1]].title()}")


class Graph:
    def __init__(self, graph):
        self.graph = graph

    def print(self):
        for value in self.graph:
            value.print_node()

    def min_distance(self, start, end):
        all_path = [[start]]
        isEnd = False
        path_index = -1

        while not isEnd:
            for i in all_path:
                isFirst = True
                for j in self.graph[i[-1] - 1].next:
                    if isFirst:
                        i.append(j[1])
                        isFirst = False
                    else:
                        path = i[:-1]
                        path.append(j[1])
                        all_path.append(path)

            for index, value in enumerate(all_path):
                if end == value[-1]:
                    isEnd = True
                    path_index = index

        print(all_path[path_index])
        result = all_path[path_index]

        result_str = ""
        for i in range(len(result) - 1):
            result_str += index_names_dict[result[i]] + " ---> "
            for j in self.graph[result[i] - 1].next:
                if j[1] == result[i + 1]:
                    result_str += j[0] + " ---> "
                    break
            if result[i + 1] == result[-1]:
                result_str += index_names_dict[result[i + 1]]

        print(result_str)

    def all_node(self, vertex):
        self.graph[vertex - 1].print_node()





graph = [
    Node(1,  [["является", 2]]),
    Node(2,  [
            ["имеет", 3],
            ["имеет", 4],
            ["имеет", 6],
            ["умеет", 7],
            ["использует", 8]
        ], [["является", 1]]),
    Node(3,  [["использует", 5]], [["имеет", 2]]),
    Node(4,  [], [["имеет", 2]]),
    Node(5,  [], [["использует", 3]]),
    Node(6,  [], [
        ["имеет", 2],
        ["имеет", 10],
        ["широкие", 11]]),
    Node(7,  [], [
        ["умеет", 2],
        ["умеет", 10],
        ["умеет", 11]]),
    Node(8,  [], [
        ["использует", 2],
        ["использует", 10],
        ["планирующий", 11]]),
    Node(9,  [["является", 10]]),
    Node(10, [
        ["имеет", 6],
        ["умеет", 7],
        ["использует", 8],
        ["имеет", 12],
        ["имеет", 13]], [
        ["является", 9],
        ["является", 11]]),
    Node(11, [
        ["широкие", 6],
        ["умеет", 7],
        ["планирующий", 8],
        ["является", 10],
        ["имеет", 12],
        ["имеет", 13]]),
    Node(12, [], [
        ["имеет", 10],
        ["имеет", 11]]),
    Node(13, [], [
        ["имеет", 10],
        ["имеет", 11]]),
]

obj = Graph(graph)
obj.print()
obj.min_distance(9, 7)
obj.all_node(11)
vertex = 10
obj.graph[vertex - 1].print_node_next()


request = [
    "Получить все о Орел",
    "Получить отношение для узла Птица",
    "Получить пары узлов Летать",
    "",
]
