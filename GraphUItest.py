from GraphUI import*

#graph=Graph([[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]])

#graph=Graph([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]) # 1 - 2 - 3 -4

#graph=Graph([[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]) # Tous relies

graph=Graph([[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]) # Tous relies a 5 cotes

graph.show_connection()
graph.set_colors(["red","blue","blue","red","red","blue","blue","red"])
graph.show_graph(200)
