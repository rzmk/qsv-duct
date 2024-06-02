from duct import cmd


def index(
    file_path: str, run: bool = False, read: bool = False, output: str | None = None
):
    """
    # qsv index

    Generates an index of the given CSV data, which can make other operations like `qsv.count`, `qsv.slice`, and others faster.

    Note that `qsv.index` does not accept CSV data on stdin.


    ## Example

    Assume we have a file `fruits.csv`. To generate the index we run:

    ```python
    qsv.index("fruits.csv").run()
    # or
    qsv.index("fruits.csv", run=True)
    ```

    The file `fruits.csv.idx` is generated. This can automatically be used by other compatible qsv commands to run faster.

    Args:
        file_path (str): The file to run `qsv index` on.
        run (bool, optional): Execute the command without returning its output. Defaults to False.
        read (bool, optional): Execute the command and return its output. Defaults to False.
        output (str | None, optional): Write index to the path you provide instead of the default location. This may not be useful as the way to use an index is if it is specifically named after the file name followed by `.idx`.
    """

    args = []
    if output:
        args.extend(["-o", output])

    index_cmd = cmd("qsv", "index", file_path, *args)

    if run:
        return index_cmd.run()
    if read:
        return index_cmd.read()
    return index_cmd
