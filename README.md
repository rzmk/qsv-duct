# qsv-duct

Python wrapper you may use to call [qsv](https://github.com/jqnatividad/qsv) commands using [duct.py](https://github.com/oconnor663/duct.py) for composability.

This library is compatible with qsv v0.128.0. Not all commands are available (see [`src/qsv/__init__.py`](src/qsv/__init__.py) for available commands).

**Make sure you have qsv installed on your system first and can access it anywhere as a `PATH` command.**

To install this library run:

```bash
pip install qsv-duct
```

## Basic example

We have a file `fruits.csv` with the following contents:

```csv
fruit,price
apple,2.50
banana,3.00
strawberry,1.50
```

Let's count the total number of non-header rows in `fruits.csv` using `qsv.count`:

```python
import qsv

qsv.count("fruits.csv", run=True)
```

The following output gets printed to stdout:

```console
3
```

## Reading output to a variable

You may want to save the output value to a variable and use it in your code. Use the `read` parameter instead of `run`. For example:

```python
non_header_row_count = qsv.count("fruits.csv", read=True)
print(non_header_row_count)
```

## Piping commands

Since this library uses duct.py, you may access the command as an `Expression` type by not passing `read` and `run`.

For example, let's say we want to get the first two rows of `fruits.csv` with `qsv.slice`. Normally we would use `run` to run the command:

```python
qsv.slice("fruits.csv", length=2, run=True)
```

```console
fruit,price
apple,2.50
banana,3.00
```

If we want to display this output in a pretty format, we can pipe `qsv.slice` into `qsv.table`:

```python
qsv.slice("fruits.csv", length=2).pipe(qsv.table()).run()
```

```console
fruit   price
apple   2.50
banana  3.00
```

If you use the `duct.py` library you can also pipe qsv commands with other bash-related commands using the `duct` library's `cmd` function. For example:

```python
import qsv
from duct import cmd

cmd("cat", "fruits.csv").pipe(qsv.table()).run()
```

```console
fruit       price
apple       2.50
banana      3.00
strawberry  1.50
```

## Testing

You can run the tests with the pytest package:

```bash
pytest
```
