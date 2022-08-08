from pathlib import Path

import pytest

from pydandy import DataMode, PydandyDB
from pydandy.types import SoftFileLock


@pytest.mark.parametrize(
    "test_path, create",
    (
        ("test/", False),
        ("test/test/", False),
        ("test/", True),
    ),
)
def test_mode_init(tmp_path: Path, test_path: str, create: bool):
    data_path = tmp_path / test_path
    if create:
        data_path.mkdir(parents=True, exist_ok=True)

    db = PydandyDB(data_path)

    assert data_path.exists()
    assert data_path == db.data_source
    assert db.mode == DataMode.DIRECTORY
    assert isinstance(db._lock, SoftFileLock)
