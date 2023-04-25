# Java Program for Feature Selection.

#### You:
Write a configurable Java program that implements four features and their selections, namely, Hello, Beautiful, Wonderful, and World... If the feature is selected, then we print the name of the feature. For instance, we could well print "Hello Beautiful World", "Hello World", "Hello", "World" etc. The four features should be implemented following object-oriented good practices

#### ChatGPT:
To implement the four features and their selections using object-oriented good practices, we can create a class for each feature with a method to print its name. Then, we can create a `FeatureSelector` class that will hold the selected features and a method to print them in the desired order. Here's a configurable Java program that demonstrates this:

```java
// Feature.java
public abstract class Feature {
    public abstract void printName();
}

// HelloFeature.java
public class HelloFeature extends Feature {
    public void printName() {
        System.out.print("Hello ");
    }
}

// BeautifulFeature.java
public class BeautifulFeature extends Feature {
    public void printName() {
        System.out.print("Beautiful ");
    }
}

// WonderfulFeature.java
public class WonderfulFeature extends Feature {
    public void printName() {
        System.out.print("Wonderful ");
    }
}

// WorldFeature.java
public class WorldFeature extends Feature {
    public void printName() {
        System.out.print("World");
    }
}

// FeatureSelector.java
import java.util.ArrayList;
import java.util.List;

public class FeatureSelector {
    private List<Feature> selectedFeatures = new ArrayList<>();

    public void addFeature(Feature feature) {
        selectedFeatures.add(feature);
    }

    public void printSelectedFeatures() {
        for (Feature feature : selectedFeatures) {
            feature.printName();
        }
        System.out.println();
    }
}

// Main.java
public class Main {
    public static void main(String[] args) {
        FeatureSelector selector = new FeatureSelector();

        // Configure the features you want to use
        selector.addFeature(new HelloFeature());
        selector.addFeature(new BeautifulFeature());
        selector.addFeature(new WorldFeature());

        // Print the selected features
        selector.printSelectedFeatures();
    }
}
```

This Java program allows you to configure the desired features easily by adding or removing instances of feature classes to the `FeatureSelector` instance in the `main` method. For example, if you want to print "Hello World", you can remove the line `selector.addFeature(new BeautifulFeature());`.
