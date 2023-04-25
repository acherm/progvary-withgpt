# Java Graph Utility.

#### You:
Write a configurable graph utility, in Java programming language, using conditional compilation and with the following features: (1) colored nodes (optional); (2) weighted edges (optional); directed or undirected graph

#### ChatGPT:
In Java, we don't have the concept of conditional compilation as in C or C++ with preprocessor directives. Instead, we can create a configurable graph utility by using design patterns and object-oriented principles. Below is an example of a simple graph utility that has optional colored nodes and optional weighted edges. It also allows you to choose between a directed and undirected graph.

```java
import java.util.*;

interface Graph {
    void addEdge(int from, int to);
}

class DirectedGraph implements Graph {
    private final Map<Integer, List<Integer>> adjacencyList = new HashMap<>();

    @Override
    public void addEdge(int from, int to) {
        adjacencyList.computeIfAbsent(from, k -> new ArrayList<>()).add(to);
    }
}

class UndirectedGraph implements Graph {
    private final Map<Integer, List<Integer>> adjacencyList = new HashMap<>();

    @Override
    public void addEdge(int from, int to) {
        adjacencyList.computeIfAbsent(from, k -> new ArrayList<>()).add(to);
        adjacencyList.computeIfAbsent(to, k -> new ArrayList<>()).add(from);
    }
}

class ColoredNode {
    int color;
    int id;

    public ColoredNode(int id, int color) {
        this.id = id;
        this.color = color;
    }
}

class WeightedEdge {
    int from;
    int to;
    double weight;

    public WeightedEdge(int from, int to, double weight) {
        this.from = from;
        this.to = to;
        this.weight = weight;
    }
}

class GraphBuilder {
    private boolean useColoredNodes = false;
    private boolean useWeightedEdges = false;
    private boolean directedGraph = true;

    public GraphBuilder() {
    }

    public GraphBuilder useColoredNodes(boolean useColoredNodes) {
        this.useColoredNodes = useColoredNodes;
        return this;
    }

    public GraphBuilder useWeightedEdges(boolean useWeightedEdges) {
        this.useWeightedEdges = useWeightedEdges;
        return this;
    }

    public GraphBuilder directedGraph(boolean directedGraph) {
        this.directedGraph = directedGraph;
        return this;
    }

    public Graph build() {
        Graph graph = directedGraph ? new DirectedGraph() : new UndirectedGraph();
        // You can further extend this method to build colored nodes and weighted edges.
        return graph;
    }
}

public class GraphUtility {
    public static void main(String[] args) {
        GraphBuilder builder = new GraphBuilder();

        // Configure your graph with desired features
        Graph graph = builder.useColoredNodes(true)
                             .useWeightedEdges(true)
                             .directedGraph(false)
                             .build();

        graph.addEdge(0, 1);
        graph.addEdge(1, 2);
        graph.addEdge(2, 0);
    }
}
```

This implementation utilizes the Builder pattern to create and configure a graph object. The `GraphBuilder` class takes care of setting the desired features for the graph. Currently, the implementation only supports basic functionality, but it can be extended to fully support colored nodes and weighted edges by modifying the `GraphBuilder` class and implementing the appropriate classes for colored nodes and weighted edges.


#### You:
how can I use weighted edges? 

#### ChatGPT:
To use weighted edges, you need to modify the `Graph` interface and the `DirectedGraph` and `UndirectedGraph` classes to handle edge weights. Additionally, you need to update the `GraphBuilder` class to build graphs with weighted edges. Here's an updated version of the previous code with support for weighted edges:

```java
import java.util.*;

interface Graph {
    void addEdge(int from, int to, double weight);
}

class DirectedGraph implements Graph {
    private final Map<Integer, List<WeightedEdge>> adjacencyList = new HashMap<>();

    @Override
    public void addEdge(int from, int to, double weight) {
        adjacencyList.computeIfAbsent(from, k -> new ArrayList<>()).add(new WeightedEdge(from, to, weight));
    }
}

class UndirectedGraph implements Graph {
    private final Map<Integer, List<WeightedEdge>> adjacencyList = new HashMap<>();

    @Override
    public void addEdge(int from, int to, double weight) {
        adjacencyList.computeIfAbsent(from, k -> new ArrayList<>()).add(new WeightedEdge(from, to, weight));
        adjacencyList.computeIfAbsent(to, k -> new ArrayList<>()).add(new WeightedEdge(to, from, weight));
    }
}

class ColoredNode {
    int color;
    int id;

    public ColoredNode(int id, int color) {
        this.id = id;
        this.color = color;
    }
}

class WeightedEdge {
    int from;
    int to;
    double weight;

    public WeightedEdge(int from, int to, double weight) {
        this.from = from;
        this.to = to;
        this.weight = weight;
    }
}

class GraphBuilder {
    private boolean useColoredNodes = false;
    private boolean useWeightedEdges = false;
    private boolean directedGraph = true;

    public GraphBuilder() {
    }

    public GraphBuilder useColoredNodes(boolean useColoredNodes) {
        this.useColoredNodes = useColoredNodes;
        return this;
    }

    public GraphBuilder useWeightedEdges(boolean useWeightedEdges) {
        this.useWeightedEdges = useWeightedEdges;
        return this;
    }

    public GraphBuilder directedGraph(boolean directedGraph) {
        this.directedGraph = directedGraph;
        return this;
    }

    public Graph build() {
        Graph graph = directedGraph ? new DirectedGraph() : new UndirectedGraph();
        return graph;
    }
}

public class GraphUtility {
    public static void main(String[] args) {
        GraphBuilder builder = new GraphBuilder();

        // Configure your graph with desired features
        Graph graph = builder.useColoredNodes(true)
                             .useWeightedEdges(true)
                             .directedGraph(false)
                             .build();

        graph.addEdge(0, 1, 1.0);
        graph.addEdge(1, 2, 2.0);
        graph.addEdge(2, 0, 3.0);
    }
}
```

Now, the `Graph` interface and its implementing classes, `DirectedGraph` and `UndirectedGraph`, support adding edges with weights. The `addEdge` method accepts an additional `double` parameter representing the edge weight.

In the `main` method, you can now add weighted edges to the graph by passing the weight along with the source and destination nodes. In the example above, we added three weighted edges to the graph with weights 1.0, 2.0, and 3.0.
