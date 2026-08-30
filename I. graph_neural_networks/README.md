**Graph Neural Network:**


Encodes:

- Node features  
- Local neighborhood structure  
- Global graph context  

---

## Summary

| Component            | Role                                      |
|---------------------|-------------------------------------------|
| Graph               | Defines relational structure              |
| Node Features       | Input attributes                          |
| Adjacency Matrix    | Connectivity encoding                     |
| Message Passing     | Information propagation mechanism         |
| Message Function    | Edge-level transformation                 |
| Aggregation         | Neighbor information fusion               |
| Update              | Representation refinement                 |
| Multi-hop           | Expands receptive field                   |
| Graph Convolution   | Convolutional operator on graphs          |
| Node Embeddings     | Final learned representations             |


---

## Example:-

<img width="988" height="641" alt="image" src="https://github.com/user-attachments/assets/7c67a797-1a3e-4d90-8306-1a23e46f436d" />

# Graph Neural Networks (GNNs) — Core Concepts

<img width="447" height="657" alt="image" src="https://github.com/user-attachments/assets/47ec94c4-8624-45b1-874f-97c15f9682ed" />

## 1. Graph Preliminaries
A graph is defined as G = (V, E), where V is the set of nodes and E is the set of edges.  
Nodes represent entities, and edges represent relationships between them.  
Graphs provide a flexible structure for modeling non-Euclidean data.

## 2. Node and Edge Features
Each node is associated with a feature vector h_i ∈ ℝ^F.  
Edges may also have features e_ij ∈ ℝ^d depending on the application.  
These features encode attributes and relational properties used for learning.

## 3. Adjacency Matrix
The adjacency matrix A ∈ ℝ^(N × N) represents graph connectivity.  
Each entry A_ij indicates whether an edge exists between nodes i and j.  
It serves as the structure guiding information flow.

## 4. Message Passing Framework
GNNs iteratively update node representations through neighbor interactions.  
At each layer, nodes aggregate information from their neighbors.  
This enables local information propagation across the graph.

## 5. Message Function
The message function computes information transmitted between nodes.  
It depends on node features and optionally edge attributes.  
This defines how information flows along edges.

## 6. Aggregation Function
Aggregation combines messages from neighboring nodes into one representation.  
It must be permutation invariant to ensure consistency.  
Common operations include sum, mean, and max.

## 7. Node Update
The update function integrates aggregated messages with current node states.  
It is typically implemented using neural networks such as MLPs.  
This refines node embeddings at each layer.

## 8. Multi-Hop Propagation
Stacking layers allows nodes to access distant neighbors.  
After K layers, a node captures K-hop neighborhood information.  
This expands the receptive field.

## 9. Graph Convolution (GCN)
Graph convolution generalizes convolution to graph structures.  
It propagates and smooths features using normalized adjacency matrices.  
This enables efficient learning on graphs.

## 10. Node Embeddings
The final output is a vector representation for each node.  
Embeddings encode both feature and structural information.  
They are used for tasks like classification and link prediction.



 



