import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Load data from the Game of Thrones dataset
data = pd.read_csv("C:/Users/Lenovo/social-network-analysis/data/edges.csv")
graph = nx.from_pandas_edgelist(data, source='Source', target='Target')

# Visualize the graph
plt.figure(figsize=(10, 8))
nx.draw(graph, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
plt.title("Game of Thrones Character Network")
plt.show()