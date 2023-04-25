# Java graph with nodes and edges.

#### You:
I'd like to program in Java a basic graph with nodes and edges with two possible variations: (1) coloured nodes; (2) weighted edges (the two can be combined)

#### ChatGPT:
Sure, I can help you create a basic graph in Java with colored nodes and weighted edges. We'll create a simple Graph class that supports these two variations. For the colored nodes, we'll use a simple string to represent the color. For the weighted edges, we'll use a double to represent the weight.

```java
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

class Node {
    String id;
    String color;

    Node(String id, String color) {
        this.id = id;
        this.color = color;
    }
}

class Edge {
    Node src;
    Node dest;
    double weight;

    Edge(Node src, Node dest, double weight) {
        this.src = src;
        this.dest = dest;
        this.weight = weight;
    }
}

class Graph {
    Map<String, Node> nodes;
    LinkedList<Edge> edges;

    Graph() {
        this.nodes = new HashMap<>();
        this.edges = new LinkedList<>();
    }

    void addNode(String id, String color) {
        Node node = new Node(id, color);
        nodes.put(id, node);
    }

    void addEdge(String srcId, String destId, double weight) {
        Node src = nodes.get(srcId);
        Node dest = nodes.get(destId);
        if (src != null && dest != null) {
            Edge edge = new Edge(src, dest, weight);
            edges.add(edge);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Graph graph = new Graph();

        // Adding colored nodes
        graph.addNode("A", "red");
        graph.addNode("B", "blue");
        graph.addNode("C", "green");

        // Adding weighted edges
        graph.addEdge("A", "B", 3.0);
        graph.addEdge("B", "C", 4.5);

        // Adding colored nodes and weighted edges
        graph.addNode("D", "yellow");
        graph.addEdge("C", "D", 2.7);
    }
}
```

This code creates a Graph class with the ability to add nodes and edges. Nodes have a unique identifier and a color, and edges have a source and destination node along with a weight. You can combine colored nodes and weighted edges as needed.

In the `main` method, I've demonstrated how to create a graph with colored nodes, weighted edges, and a combination of both. You can modify the `main` method or the Graph class to suit your needs.


#### You:
great but here you propose a graph that has necessarily colored nodes and weighted edges... I want both "features" optional eg I can have basic graph, or graph with only weighted edges. Can you refactor the program?

#### ChatGPT:
Sure, I can modify the program to make both colored nodes and weighted edges optional. I'll add constructors for the Node and Edge classes, allowing you to create instances without specifying a color or weight. I'll also update the Graph class to support adding edges without weights.

```java
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

class Node {
    String id;
    String color;

    Node(String id) {
        this.id = id;
    }

    Node(String id, String color) {
        this(id);
        this.color = color;
    }
}

class Edge {
    Node src;
    Node dest;
    Double weight;

    Edge(Node src, Node dest) {
        this.src = src;
        this.dest = dest;
    }

    Edge(Node src, Node dest, double weight) {
        this(src, dest);
        this.weight = weight;
    }
}

class Graph {
    Map<String, Node> nodes;
    LinkedList<Edge> edges;

    Graph() {
        this.nodes = new HashMap<>();
        this.edges = new LinkedList<>();
    }

    void addNode(String id) {
        addNode(id, null);
    }

    void addNode(String id, String color) {
        Node node = color == null ? new Node(id) : new Node(id, color);
        nodes.put(id, node);
    }

    void addEdge(String srcId, String destId) {
        addEdge(srcId, destId, null);
    }

    void addEdge(String srcId, String destId, Double weight) {
        Node src = nodes.get(srcId);
        Node dest = nodes.get(destId);
        if (src != null && dest != null) {
            Edge edge = weight == null ? new Edge(src, dest) : new Edge(src, dest, weight);
            edges.add(edge);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Graph graph = new Graph();

        // Adding basic nodes
        graph.addNode("A");
        graph.addNode("B");

        // Adding colored nodes
        graph.addNode("C", "red");
        graph.addNode("D", "blue");

        // Adding basic edges
        graph.addEdge("A", "B");

        // Adding weighted edges
        graph.addEdge("B", "C", 3.0);

        // Adding colored nodes and weighted edges
        graph.addNode("E", "green");
        graph.addEdge("D", "E", 4.5);
    }
}
```

Now you can create a basic graph, a graph with colored nodes, a graph with weighted edges, or a graph with both colored nodes and weighted edges. In the `main` method, I've demonstrated how to create these variations. You can modify the `main` method or the Graph class to suit your needs.


#### You:
great, you introduce the flexibility of adding weights or colors through different methods... But I'd like to have a more clear design in which you separate concerns and have explicit kinds of graphs 

#### ChatGPT:
I understand your concern, and I'll refactor the code by creating separate classes for each type of graph. We'll have a base Graph class, and then we'll create subclasses for each variation: ColoredGraph, WeightedGraph, and ColoredWeightedGraph.

```java
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

class Node {
    String id;

    Node(String id) {
        this.id = id;
    }
}

class Edge {
    Node src;
    Node dest;

    Edge(Node src, Node dest) {
        this.src = src;
        this.dest = dest;
    }
}

class Graph {
    Map<String, Node> nodes;
    LinkedList<Edge> edges;

    Graph() {
        this.nodes = new HashMap<>();
        this.edges = new LinkedList<>();
    }

    void addNode(String id) {
        Node node = new Node(id);
        nodes.put(id, node);
    }

    void addEdge(String srcId, String destId) {
        Node src = nodes.get(srcId);
        Node dest = nodes.get(destId);
        if (src != null && dest != null) {
            Edge edge = new Edge(src, dest);
            edges.add(edge);
        }
    }
}

class ColoredNode extends Node {
    String color;

    ColoredNode(String id, String color) {
        super(id);
        this.color = color;
    }
}

class ColoredGraph extends Graph {

    void addNode(String id, String color) {
        ColoredNode node = new ColoredNode(id, color);
        nodes.put(id, node);
    }
}

class WeightedEdge extends Edge {
    double weight;

    WeightedEdge(Node src, Node dest, double weight) {
        super(src, dest);
        this.weight = weight;
    }
}

class WeightedGraph extends Graph {

    void addEdge(String srcId, String destId, double weight) {
        Node src = nodes.get(srcId);
        Node dest = nodes.get(destId);
        if (src != null && dest != null) {
            WeightedEdge edge = new WeightedEdge(src, dest, weight);
            edges.add(edge);
        }
    }
}

class ColoredWeightedGraph extends ColoredGraph {

    void addEdge(String srcId, String destId, double weight) {
        Node src = nodes.get(srcId);
        Node dest = nodes.get(destId);
        if (src != null && dest != null) {
            WeightedEdge edge = new WeightedEdge(src, dest, weight);
            edges.add(edge);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // Basic graph
        Graph basicGraph = new Graph();
        basicGraph.addNode("A");
        basicGraph.addNode("B");
        basicGraph.addEdge("A", "B");

        // Colored graph
        ColoredGraph coloredGraph = new ColoredGraph();
        coloredGraph.addNode("C", "red");
        coloredGraph.addNode("D", "blue");
        coloredGraph.addEdge("C", "D");

        // Weighted graph
        WeightedGraph weightedGraph = new WeightedGraph();
        weightedGraph.addNode("E");
        weightedGraph.addNode("F");
        weightedGraph.addEdge("E", "F", 3.0);

        // Colored and weighted graph
        ColoredWeightedGraph coloredWeightedGraph = new ColoredWeightedGraph();
        coloredWeightedGraph.addNode("G", "green");
        coloredWeightedGraph.addNode("H", "yellow");
        coloredWeightedGraph.addEdge("G", "H", 4.5);
    }
}
```

Now, we have separate classes for each type of graph, providing a clearer design
