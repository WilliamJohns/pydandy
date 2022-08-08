from pydandy import DataMode, PydandyDB
from pydandy.types import SoftFileLock


def test_mode_init():
    db = PydandyDB()

    assert db.data_source is None
    assert db.mode == DataMode.IN_MEMORY
    assert isinstance(db._lock, SoftFileLock)
