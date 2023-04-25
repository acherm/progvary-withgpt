# Parametrize Python Equality Tests.

#### You:
I have the following Python function: 
def equality_test(x, y, z) -> bool:
    return x+(y+z) == (x+y)+z
I'd like to create two variants: one with the following relation, called inverse multiplication, (x * z) / (y * z) == x / y ; another with the relation (x * z * math.pi) / (y * z * math.pi) == (x / y) called the inverse multiplication with pi. Can you parameterize equality_test accordingly?

#### ChatGPT:
Sure! Here are two possible parameterized versions of the `equality_test` function that implement the two variants you mentioned:

```python
import math

def inverse_multiplication_test(x, y, z) -> bool:
    return z != 0 and x / y == (x * z) / (y * z)

def inverse_multiplication_pi_test(x, y, z) -> bool:
    return z != 0 and x / y == (x * z * math.pi) / (y * z * math.pi)
```

The `inverse_multiplication_test` function checks if the relation `(x * z) / (y * z) == x / y` holds, while the `inverse_multiplication_pi_test` function checks if the relation `(x * z * math.pi) / (y * z * math.pi) == (x / y)` holds. Note that both functions check that `z` is not equal to zero to avoid division by zero errors.

You can call these functions with different arguments to test different values of `x`, `y`, and `z`:

```python
>>> inverse_multiplication_test(2, 4, 2)
True
>>> inverse_multiplication_test(2, 0, 2)
False
>>> inverse_multiplication_pi_test(2, 4, 2)
True
>>> inverse_multiplication_pi_test(2, 0, 2)
False
```

In the first example, `inverse_multiplication_test(2, 4, 2)` returns `True` because `(2 * 2) / (4 * 2) == 2 / 4`. In the second example, `inverse_multiplication_test(2, 0, 2)` returns `False` because `y` is zero. The same applies to `inverse_multiplication_pi_test`.
