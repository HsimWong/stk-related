import dijkstra
import csv
satellite_number = 210

class Patcher:
    def __init__(self, description):
        self.__graph = dijkstra.Graph()
        self.__dumpDescription(description)
        
    def __dumpDescription(self, description):
        weights = [float(x) for x in description]
        weights_indexed = 0
        for i in range(satellite_number):
            for j in range(i + 1, satellite_number):
                if weights[weights_indexed] >= 0:
                    self.__graph.add_edge(i, j, weights[weights_indexed])
                    self.__graph.add_edge(j, i, weights[weights_indexed])
                weights_indexed += 1

    def get_shortest_paths(self, max_jump):
        paths = []
        for i in range(satellite_number):
            paths_sourced_from_i = []
            dijk_instance = dijkstra.DijkstraSPF(self.__graph, i)
            for j in range(satellite_number):
                distance = dijk_instance.get_distance(j)
                path = tuple(dijk_instance.get_path(j))
                if len(path) <= max_jump:
                    paths_sourced_from_i.append((path, distance))
                else:
                    paths_sourced_from_i.append((None, None))
            paths.append(paths_sourced_from_i)
        return paths

def extract_paths_from_file(line_number, file_dir, max_jump):
    src_file = open(file_dir, 'r')
    reader = csv.reader(src_file)
    line = ""
    for ln, x in enumerate(reader):
        if ln == line_number:
            line = [float(item) for item in x]
    p = Patcher(line)
    src_file.close()
    return p.get_shortest_paths(max_jump)
              