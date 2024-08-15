# โจทย์ 3 : การหาทางเดินที่สั้นที่สุดในกราฟ (Shortest Path in Graph)
# รายละเอียด: เขียนโปรแกรมที่รับกราฟที่เป็นการเชื่อมต่อระหว่างจุดต่างๆ และหาทางเดินที่สั้นที่สุดระหว่างจุดเริ่มต้นและจุดสิ้นสุด
# โดยใช้ Dijkstra's Algorithm

from collections import defaultdict
import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end:
            return current_distance
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return float('inf')

def build_graph(edges):
    graph = defaultdict(dict)
    for u, v, weight in edges:
        graph[u][v] = weight
        graph[v][u] = weight  # ถ้ากราฟเป็นแบบไม่ชี้ทิศทาง
    return graph

def parse_edges(edges_input):
    # ลบช่องว่างที่ไม่จำเป็นออกจากสตริง
    edges_input = edges_input.replace(" ", "").strip().split('),(')
    edges_input[0] = edges_input[0].lstrip('(')
    edges_input[-1] = edges_input[-1].rstrip(')')
    
    edges = []
    for edge_str in edges_input:
        u, v, w = map(int, edge_str.split(','))
        edges.append((u, v, w))
    
    return edges

def main():
    edges_input = input("กรุณากรอกข้อมูลของกราฟ (รูปแบบ: (u, v, w), (u, v, w), ...): ")
    edges = parse_edges(edges_input)
    
    start = int(input("กรุณากรอกจุดเริ่มต้น: "))
    end = int(input("กรุณากรอกจุดสิ้นสุด: "))
    
    graph = build_graph(edges)
    shortest_path_length = dijkstra(graph, start, end)
    
    if shortest_path_length == float('inf'):
        print("No path exists")
    else:
        print("ความยาวของทางเดินที่สั้นที่สุด:", shortest_path_length)

if __name__ == "__main__":
    main()
