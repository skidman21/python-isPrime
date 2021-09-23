# Prime Number Testing Exercises

* [Bug Report](./bug_report.md)
* [Setup](#Setup)
* [Run Tests](#Run-Tests-and-Report-Code-Coverage)
* [100% Code Coverage](#100%-Code-Coverage)

## Setup
- Python Version needs to be 3.7 or higher
- Using Poetry as package manager

1. Clone the repo
2. Run `poetry install` at the project root to install all dependencies
    > or use `pip install -r requirements.txt`
3. Configure the tests if needed (pytest is the test framework)

## Run Tests and Report Code Coverage

```bash
pytest tests --cov=. --cov-report term-missing
```

## 100% Code Coverage

```python
---------- coverage: platform darwin, python 3.9.2-final-0 -----------
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
prime_calculator.py                 20      0   100%
tests/__init__.py                    0      0   100%
tests/test_prime_calculator.py      17      0   100%
--------------------------------------------------------------
TOTAL                               37      0   100%
```
