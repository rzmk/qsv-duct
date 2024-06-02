import qsv
import pathlib
import pytest

data_path = pathlib.Path().resolve().joinpath("tests/data")
test_data = {
    file_name: data_path.joinpath(file_name)
    for file_name in ["fruits.csv", "constituents_altnames.csv"]
}


class TestCountFunc:
    @pytest.mark.parametrize(
        "file_name,expected",
        [("fruits.csv", "3"), ("constituents_altnames.csv", "33971")],
    )
    def test_count(self, file_name, expected):
        """Count the total number of non-header rows."""

        result = qsv.count(test_data[file_name]).read()
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [("fruits.csv", "4"), ("constituents_altnames.csv", "33972")],
    )
    def test_include_header_row(self, file_name, expected):
        """Count the total number of rows including the header row."""

        result = qsv.count(test_data[file_name], include_header_row=True).read()
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [("fruits.csv", "3"), ("constituents_altnames.csv", "33,971")],
    )
    def test_human_readable(self, file_name, expected):
        """Count the total number of non-header rows and comma separate the result."""

        result = qsv.count(test_data[file_name], human_readable=True).read()
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [("fruits.csv", "4"), ("constituents_altnames.csv", "33,972")],
    )
    def test_n_H(self, file_name, expected):
        """Count the total number of rows including the header row and comma separate the result."""

        result = qsv.count(
            test_data[file_name], include_header_row=True, human_readable=True
        ).read()
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [("fruits.csv", "3;15"), ("constituents_altnames.csv", "33971;297")],
    )
    def test_width(self, file_name, expected):
        """Count the total number of non-header rows and also the estimated length of the longest record."""

        result = qsv.count(test_data[file_name], width=True).read()
        assert result == expected


class TestCountBuilder:
    def test_count(self):
        """Count the total number of non-header rows."""

        result = qsv.CountBuilder().file(test_data["fruits.csv"]).read()
        assert result == "3"

    def test_include_header_row(self):
        """Count the total number of rows including the header row."""

        result = (
            qsv.CountBuilder().file(test_data["fruits.csv"]).include_header_row().read()
        )
        assert result == "4"

    def test_human_readable(self):
        """Count the total number of non-header rows and comma separate the result."""

        result = (
            qsv.CountBuilder()
            .file(test_data["constituents_altnames.csv"])
            .human_readable()
            .read()
        )
        assert result == "33,971"

    def test_width(self):
        """Count the total number of non-header rows and also the estimated length of the longest record."""

        result = qsv.CountBuilder().file(test_data["fruits.csv"]).width().read()
        assert result == "3;15"
