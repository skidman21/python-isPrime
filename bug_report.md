## Bug Report

### `NicePrimeCalculator.is_prime()` values failed
| Input       | Expected    | Actual   |
| ----------- | ----------- | -------- |
| 1           | False       |   True   |
| -1          | False       |   math domain error   |


### `NicePrimeCalculator.next()` values failed
| Input       | Expected    | Actual   |
| ----------- | ----------- | -------- |
| -10         | 2           |    math domain error    |
| -1          | 2           |    1    | 
| 0           | 2           |    1    | 
| 1           | 2           |   3     | 

## Questions and Experiments

> How should we handle non-integers values?

| Input       | is_prime    | next     |
| ----------- | ----------- | -------- |
| 2.5         | `False`, got: `True`        |  3       |
| "one"       | `False`, got: `TypeError 'str'`           |    ?, got: `TypeError 'str'`   | 
| None          | `False`, got: `TypeError 'None'`           |    ?, got: `TypeError 'None'`     | 
| 2️⃣          | `False`, got: `TypeError 'string formatting'`           |    ?, got: `TypeError 'string formatting'`     | 

Negative Test Cases:

1. Negative numbers
2. Decimals
3. Strings (including unicode/emoji)
4. None
