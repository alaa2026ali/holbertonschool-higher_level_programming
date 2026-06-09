# Python - Test-Driven Development (TDD)

## Description
This project focuses on Test-Driven Development (TDD) in Python. It involves writing interactive test cases inside the `tests/` directory and using the `doctest` module to validate code execution before final deployment.

## Requirements
- **Environment:** Ubuntu 20.04 LTS & Python 3.8.5
- **Style Guide:** `pycodestyle` (version 2.8.*)
- **Constraints:** All scripts must be executable (`chmod +x`) and start with `#!/usr/bin/python3`.
- **Documentation:** All modules, classes, and functions must have docstrings.

## Repository Structure & Tasks
- `0-add_integer.py`: Adds two integers safely (Tests: `tests/0-add_integer.txt`).
- `2-matrix_divided.py`: Divides all elements of a matrix.
- `3-say_my_name.py`: Prints a formatted string containing full names.
- `4-print_square.py`: Prints a square using the `#` symbol.
- `5-text_indentation.py`: Formats text with specific spacing rules.

## Testing Execution
To run all docstring test files simultaneously, execute:
```bash
python3 -m doctest -v ./tests/*
```

## Author
Alaa Aldwasari

