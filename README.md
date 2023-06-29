# Python Exercises

Coding exercises in Python

* [andornaut@github /python-cli-app](https://github.com/andornaut/python-cli-app)
* [andornaut@github /til/python](https://github.com/andornaut/til/blob/master/docs/python.md)

## Usage

```bash
# Install application dependencies into a virtualenv
pipenv install

# List available commands
exercises

# Run a command
exercises gift-exchange

# Run a subcommand
# expenditure=[10, 20, 30, 40, 50]
# days=3
exercises hackerrank fraudulent-activity-notifications 10 20 30 40 50 3

# Supply multiple values to a command
# https://typer.tiangolo.com/tutorial/multiple-values/multiple-options/
# a=[1, 3, 5]
# b=[2, 3]
# c=[1, 2, 3]
exercises hackerrank triple-sum --a 1 --a 3 --a 5 --b 2 --b 3 --c 1 --c 2 --c 3
```

## Developing

See [.vscode](./.vscode) for [VS Code](https://code.visualstudio.com/) integration files.

```bash
# Install application and development dependencies into a virtualenv
pipenv install --dev

# Format Python files
black .

# Check code style
flake8

# Run tests
pytest

# Run only tests whose names contain "triple_sum"
pytest -k triple_sum

```
