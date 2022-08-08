from pathlib import Path

import pytest

from pydandy import DataMode, PydandyDB
from pydandy.types import SoftFileLock


@pytest.mark.parametrize(
    "test_path, create",
    (
        ("test.json", False),
        ("test/test.json", False),
        ("test.json", True),
    ),
)
def test_mode_init(tmp_path: Path, test_path: str, create: bool):
    data_path = tmp_path / test_path
    if create:
        data_path.parent.mkdir(parents=True, exist_ok=True)
        data_path.touch()

    db = PydandyDB(data_path)

    assert data_path.exists()
    assert data_path == db.data_source
    assert db.mode == DataMode.FILE
    assert isinstance(db._lock, SoftFileLock)
