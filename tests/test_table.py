import qsv
import pathlib
import pytest

data_path = pathlib.Path().resolve().joinpath("tests/data")
test_data = {
    file_name: data_path.joinpath(file_name)
    for file_name in ["fruits.csv", "constituents_altnames.csv"]
}


class TestTableFunc:
    @pytest.mark.parametrize(
        "file_name,expected",
        [
            (
                "fruits.csv",
                """fruit       price
apple       2.50
banana      3.00
strawberry  1.50""",
            )
        ],
    )
    def test_table(self, file_name, expected):
        """Basic `qsv table` output for a basic CSV file."""

        result = qsv.table(test_data[file_name]).read()
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [
            (
                "fruits.csv",
                """fruit                 price
apple                 2.50
banana                3.00
strawberry            1.50""",
            )
        ],
    )
    def test_width(self, file_name, expected):
        """Table with minimum width of 20."""

        result = qsv.table(test_data[file_name], width=20).read()
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [
            (
                "fruits.csv",
                """fruit         price
apple         2.50
banana        3.00
strawberry    1.50""",
            )
        ],
    )
    def test_pad(self, file_name, expected):
        """Table with a minimum of 4 spaces between each column."""

        result = qsv.table(test_data[file_name], pad=4).read()
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [
            (
                "fruits.csv",
                """     fruit  price
     apple  2.50
    banana  3.00
strawberry  1.50""",
            )
        ],
    )
    def test_align_right(self, file_name, expected):
        """Table with entries aligned to the right in a column."""

        result = qsv.table(test_data[file_name], align="right").read()
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [
            (
                "fruits.csv",
                """  fruit     price
  apple     2.50
  banana    3.00
strawberry  1.50""",
            )
        ],
    )
    def test_align_center(self, file_name, expected):
        """Table with entries aligned in the center in a column."""

        result = qsv.table(test_data[file_name], align="center").read()
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [
            (
                "fruits.csv",
                """fruit     price
apple     2.50
banan...  3.00
straw...  1.50""",
            )
        ],
    )
    def test_condense(self, file_name, expected):
        """Table with each field limited to a specific length."""

        result = qsv.table(test_data[file_name], condense=5).read()
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [
            (
                "fruits.csv",
                """fruit   price
apple   2.50
banana  3.00""",
            )
        ],
    )
    def test_pipe_slice(self, file_name, expected):
        """Get a slice of a CSV file using `qsv.slice` then pipe the output to `qsv.table`."""

        result = qsv.slice(test_data[file_name], length=2).pipe(qsv.table()).read()
        assert result == expected
