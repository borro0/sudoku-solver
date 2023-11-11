# Sudoku Solver
This is a hobby project to create a sudoku solver using TDD.

## Run test
Tests are run using PyTest. Before you run a test, install the sudoku solver as editable package: `pip install -e .`. If you're working with an old version of `setuptools` this will not work out of the box. Apply the following workaround:
```bash
touch setup.cfg
pip install -e .
rm setup.cfg
```