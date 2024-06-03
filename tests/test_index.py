import qsv
import pytest
from pathlib import Path
from .test_data import test_data


class TestIndexFunc:
    @pytest.mark.parametrize(
        "file_name",
        [("fruits.csv")],
    )
    def test_index(self, file_name, tmp_path: Path):
        """Generate an index for a given file path at `filename.ext.idx` where `.ext` is the file's extension."""

        # Make a temporary data file in a temporary directory
        tmp_file = tmp_path.joinpath(file_name).resolve()
        tmp_file.write_text(test_data[file_name].read_text(), encoding="utf-8")

        qsv.index(tmp_file, run=True)
        idx_file = tmp_path.joinpath(f"{file_name}.idx").resolve()

        assert idx_file.exists()

    @pytest.mark.parametrize(
        "file_name",
        [("fruits.csv")],
    )
    def test_output(self, file_name, tmp_path: Path):
        """Generate an index for a given file path at a specified output path."""

        # Make a temporary data file in a temporary directory
        tmp_file = tmp_path.joinpath(file_name).resolve()
        tmp_file.write_text(test_data[file_name].read_text(), encoding="utf-8")
        output_file = tmp_path.joinpath(
            f"arbitrary_path{''.join(test_data[file_name].suffixes)}.idx"
        ).resolve()

        qsv.index(tmp_file, output=output_file.as_posix(), run=True)

        assert output_file.exists()
