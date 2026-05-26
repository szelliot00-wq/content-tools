# Graph Neural Networks Explained: A Clear Guide to GNN Basics & Models

Video ID: `eGoszzMkGfU`

## Summary
This video introduces Graph Neural Networks (GNNs), explaining why graphs are better suited than tables for representing relational data. It covers the fundamentals of nodes, edges, adjacency matrices, and embeddings, then walks through the core message passing mechanism. Five major GNN architectures are explained: GCN, GraphSAGE, GAT, GIN, and Graph Transformers, each with their mathematical formulation and use cases.

## Key insights
- **Graphs capture structure that tables cannot** — nodes represent entities, edges represent relationships, and both can carry feature information encoded as embeddings.
- **Message passing is the core mechanism** — nodes iteratively collect information from neighbors (layer 1 = immediate neighbors, layer 2 = neighbors-of-neighbors), building richer representations with each layer.
- **GCN** performs spectral-style smoothing over neighbor features — simple and effective for semi-supervised classification, but treats all neighbors equally.
- **GraphSAGE** samples a subset of neighbors and concatenates the aggregated neighborhood embedding with the node's own embedding — scales to graphs with millions of nodes.
- **GAT (Graph Attention Networks)** learns attention coefficients (α) per neighbor pair during training, allowing the model to weight important neighbors more heavily.
- **GIN (Graph Isomorphism Network)** uses a sum aggregation + MLP and is the most expressive standard GNN — it matches the power of the Weisfeiler-Leman (WL) test for distinguishing non-isomorphic graphs.
- **The WL test limitation** exposes a key weakness in GCNs: mean/max pooling can collapse structurally distinct graphs into identical representations, which GIN is specifically designed to avoid.
- **Graph Transformers** apply global multi-head attention (any node can attend to any other), augmented with a structural bias term that encodes graph topology (connectivity, distance, edge type) — best for long-range dependencies.
- **Architecture selection guide**: GCN for simplicity, GraphSAGE for scale, GAT for selective focus, GIN for expressivity, Graph Transformer for global reasoning.