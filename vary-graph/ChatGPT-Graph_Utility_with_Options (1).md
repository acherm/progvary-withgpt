# Graph Utility with Options.

#### You:
Write a configurable graph utility, in C programming language, using conditional compilation and with the following features: (1) colored nodes (optional); (2) weighted edges (optional); directed or undirected graph

#### ChatGPT:
Here's a simple configurable graph utility in C programming language, using conditional compilation and incorporating the requested features.

```c
#include <stdio.h>
#include <stdlib.h>

// Uncomment the following lines to enable the respective features
// #define ENABLE_COLOR
// #define ENABLE_WEIGHTED_EDGES

typedef struct Node {
    int id;
#ifdef ENABLE_COLOR
    char color[10];
#endif
    struct Node* next;
} Node;

typedef struct Edge {
    int src;
    int dest;
#ifdef ENABLE_WEIGHTED_EDGES
    int weight;
#endif
    struct Edge* next;
} Edge;

typedef struct Graph {
    int num_nodes;
    int num_edges;
    Node** nodes;
    Edge** edges;
    int is_directed;
} Graph;

Node* create_node(int id) {
    Node* node = (Node*) malloc(sizeof(Node));
    node->id = id;
#ifdef ENABLE_COLOR
    sprintf(node->color, "default");
#endif
    node->next = NULL;
    return node;
}

Edge* create_edge(int src, int dest, int weight) {
    Edge* edge = (Edge*) malloc(sizeof(Edge));
    edge->src = src;
    edge->dest = dest;
#ifdef ENABLE_WEIGHTED_EDGES
    edge->weight = weight;
#endif
    edge->next = NULL;
    return edge;
}

Graph* create_graph(int num_nodes, int is_directed) {
    Graph* graph = (Graph*) malloc(sizeof(Graph));
    graph->num_nodes = num_nodes;
    graph->num_edges = 0;
    graph->nodes = (Node**) malloc(num_nodes * sizeof(Node*));
    graph->edges = (Edge**) malloc(num_nodes * sizeof(Edge*));
    graph->is_directed = is_directed;

    for (int i = 0; i < num_nodes; i++) {
        graph->nodes[i] = create_node(i);
        graph->edges[i] = NULL;
    }

    return graph;
}

void add_edge(Graph* graph, int src, int dest, int weight) {
    Edge* edge = create_edge(src, dest, weight);
    edge->next = graph->edges[src];
    graph->edges[src] = edge;
    graph->num_edges++;

    if (!graph->is_directed) {
        Edge* reverse_edge = create_edge(dest, src, weight);
        reverse_edge->next = graph->edges[dest];
        graph->edges[dest] = reverse_edge;
    }
}

#ifdef ENABLE_COLOR
void set_node_color(Graph* graph, int node_id, const char* color) {
    if (node_id >= 0 && node_id < graph->num_nodes) {
        sprintf(graph->nodes[node_id]->color, "%s", color);
    }
}
#endif

void print_graph(Graph* graph) {
    for (int i = 0; i < graph->num_nodes; i++) {
        printf("Node %d", graph->nodes[i]->id);
#ifdef ENABLE_COLOR
        printf(" (Color: %s)", graph->nodes[i]->color);
#endif
        printf(": ");
        Edge* edge = graph->edges[i];
        while (edge) {
            printf("%d", edge->dest);
#ifdef ENABLE_WEIGHTED_EDGES
            printf("(Weight: %d)", edge->weight);
#endif
            printf(" -> ");
            edge = edge->next;
        }
        printf("NULL\n");
    }
}

int main() {
    Graph* graph = create_graph(5, 0); // Change 0 to 1 for a directed graph
    add_edge(graph, 0, 1, 10);
    add_edge(graph, 0, 4, 
```


#### You:
void add_edge(Graph* graph, int src, int dest, int weight) { means that the third argument (weight) is necessarily included... whereas weighted edges are optional

#### ChatGPT:
You are correct, I'll modify the implementation to make the weight parameter optional using conditional compilation:

```c
// ...

void add_edge(Graph* graph, int src, int dest
#ifdef ENABLE_WEIGHTED_EDGES
    , int weight
#endif
) {
    Edge* edge = create_edge(src, dest
#ifdef ENABLE_WEIGHTED_EDGES
        , weight
#endif
    );
    edge->next = graph->edges[src];
    graph->edges[src] = edge;
    graph->num_edges++;

    if (!graph->is_directed) {
        Edge* reverse_edge = create_edge(dest, src
#ifdef ENABLE_WEIGHTED_EDGES
            , weight
#endif
        );
        reverse_edge->next = graph->edges[dest];
        graph->edges[dest] = reverse_edge;
    }
}

// ...
```

Now, the `add_edge` function accepts an optional weight parameter only when the `ENABLE_WEIGHTED_EDGES` macro is defined.


#### You:
should I also modify create_edge?

#### ChatGPT:
Yes, you should modify the `create_edge` function as well to make the `weight` parameter optional using conditional compilation. Here's the updated `create_edge` function:

```c
Edge* create_edge(int src, int dest
#ifdef ENABLE_WEIGHTED_EDGES
    , int weight
#endif
) {
    Edge* edge = (Edge*) malloc(sizeof(Edge));
    edge->src = src;
    edge->dest = dest;
#ifdef ENABLE_WEIGHTED_EDGES
    edge->weight = weight;
#endif
    edge->next = NULL;
    return edge;
}
```

Now, the `create_edge` function also accepts an optional `weight` parameter only when the `ENABLE_WEIGHTED_EDGES` macro is defined.
