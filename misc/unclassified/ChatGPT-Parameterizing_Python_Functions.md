# Parameterizing Python Functions.

#### You:
I have the following Python function: 
def equality_test(x, y, z) -> bool:
    return x+(y+z) == (x+y)+z
I'd like to create two variants: one with the following relation, called inverse multiplication, (x * z) / (y * z) == x / y ; another with the relation (x * z * math.pi) / (y * z * math.pi) == (x / y) called the inverse multiplication with pi. Can you parameterize equality_test accordingly?

#### ChatGPT:
Yes, I can help you create two parameterized variants of the `equality_test` function according to the relations you provided. First, you'll need to import the `math` module to use `math.pi`. Here's how the modified functions would look like:

```python
import math

def equality_test(x, y, z, test_type='addition') -> bool:
    if test_type == 'addition':
        return x + (y + z) == (x + y) + z
    elif test_type == 'inverse_multiplication':
        return (x * z) / (y * z) == x / y
    elif test_type == 'inverse_multiplication_with_pi':
        return (x * z * math.pi) / (y * z * math.pi) == x / y
    else:
        raise ValueError("Invalid test_type. Please choose from 'addition', 'inverse_multiplication', or 'inverse_multiplication_with_pi'.")

# Usage:
print(equality_test(3, 4, 5))  # Test the default addition case
print(equality_test(3, 4, 5, test_type='inverse_multiplication'))
print(equality_test(3, 4, 5, test_type='inverse_multiplication_with_pi'))
```

Now, the `equality_test` function takes an additional argument `test_type` which defaults to 'addition', but can also be set to 'inverse\_multiplication' or 'inverse\_multiplication\_with\_pi' for the two new variants.


#### You:
can you use an enum to parameterize?

#### ChatGPT:
Sure! You can use an `Enum` class to define the available test types and parameterize the `equality_test` function. First, you'll need to import the `Enum` class from the `enum` module. Here's how the modified function would look like:

```python
import math
from enum import Enum

class TestType(Enum):
    ADDITION = "addition"
    INVERSE_MULTIPLICATION = "inverse_multiplication"
    INVERSE_MULTIPLICATION_WITH_PI = "inverse_multiplication_with_pi"

def equality_test(x, y, z, test_type: TestType = TestType.ADDITION) -> bool:
    if test_type == TestType.ADDITION:
        return x + (y + z) == (x + y) + z
    elif test_type == TestType.INVERSE_MULTIPLICATION:
        return (x * z) / (y * z) == x / y
    elif test_type == TestType.INVERSE_MULTIPLICATION_WITH_PI:
        return (x * z * math.pi) / (y * z * math.pi) == x / y
    else:
        raise ValueError("Invalid test_type. Please choose from TestType.ADDITION, TestType.INVERSE_MULTIPLICATION, or TestType.INVERSE_MULTIPLICATION_WITH_PI.")

# Usage:
print(equality_test(3, 4, 5))  # Test the default addition case
print(equality_test(3, 4, 5, test_type=TestType.INVERSE_MULTIPLICATION))
print(equality_test(3, 4, 5, test_type=TestType.INVERSE_MULTIPLICATION_WITH_PI))
```

Now, the `equality_test` function takes a `TestType` enum value as the `test_type` argument, which defaults to `TestType.ADDITION`.
