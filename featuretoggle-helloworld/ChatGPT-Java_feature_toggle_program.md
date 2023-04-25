# Java feature toggle program.

#### You:
Write a configurable Java program that implements four features and their selections, namely, Hello, Beautiful, Wonderful, and World... If the feature is selected, then we print the name of the feature. For instance, we could well print "Hello Beautiful World", "Hello World", "Hello", "World" etc. The four features should be implemented as feature toggles, leveraging Togglz framework 

#### ChatGPT:
I've written a configurable Java program using the Togglz framework to implement the four features you mentioned. You'll need to include Togglz in your project dependencies first. For instance, if you are using Maven, add the following dependencies to your pom.xml:

```xml
<dependencies>
    <dependency>
        <groupId>org.togglz</groupId>
        <artifactId>togglz-core</artifactId>
        <version>2.9.9</version>
    </dependency>
    <dependency>
        <groupId>org.togglz</groupId>
        <artifactId>togglz-console</artifactId>
        <version>2.9.9</version>
    </dependency>
</dependencies>
```

Next, create an enumeration to define the features:

```java
package com.example;

import org.togglz.core.Feature;
import org.togglz.core.annotation.EnabledByDefault;
import org.togglz.core.annotation.Label;
import org.togglz.core.context.FeatureContext;

public enum MyFeatures implements Feature {

    @EnabledByDefault
    @Label("Hello")
    HELLO,

    @Label("Beautiful")
    BEAUTIFUL,

    @Label("Wonderful")
    WONDERFUL,

    @EnabledByDefault
    @Label("World")
    WORLD;

    public boolean isActive() {
        return FeatureContext.getFeatureManager().isActive(this);
    }
}
```

Now, implement a simple Java class to print the features:

```java
package com.example;

public class FeaturePrinter {

    public static void main(String[] args) {
        StringBuilder result = new StringBuilder();

        if (MyFeatures.HELLO.isActive()) {
            result.append("Hello");
        }

        if (MyFeatures.BEAUTIFUL.isActive()) {
            if (result.length() > 0) {
                result.append(" ");
            }
            result.append("Beautiful");
        }

        if (MyFeatures.WONDERFUL.isActive()) {
            if (result.length() > 0) {
                result.append(" ");
            }
            result.append("Wonderful");
        }

        if (MyFeatures.WORLD.isActive()) {
            if (result.length() > 0) {
                result.append(" ");
            }
            result.append("World");
        }

        System.out.println(result.toString());
    }
}
```

Finally, create a Togglz configuration file to enable or disable features:

```java
package com.example;

import org.togglz.core.Feature;
import org.togglz.core.manager.EnumBasedFeatureProvider;
import org.togglz.core.spi.FeatureProvider;
import org.togglz.core.user.NoOpUserProvider;
import org.togglz.core.user.UserProvider;
import org.togglz.servlet.user.ServletUserProvider;

public class MyTogglzConfiguration implements org.togglz.core.config.TogglzConfig {

    public Class<? extends Feature> getFeatureClass() {
        return MyFeatures.class;
    }

    public FeatureProvider featureProvider() {
        return new EnumBasedFeatureProvider(MyFeatures.class);
    }

    public UserProvider userProvider() {
        return new NoOpUserProvider();
    }
}
```

By default, the "Hello" and "World" features are enabled. To change the active features, modify the `@EnabledByDefault` annotations in the `MyFeatures` enumeration. Alternatively, you can implement a custom `StateRepository` in the `MyTogglzConfiguration` class to load feature states from a file, database, or any other source.
