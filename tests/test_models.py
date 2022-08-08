import pytest
from pydantic import BaseModel

from pydandy import PydandyDB


@pytest.mark.parametrize(
    "name, expected_name",
    (
        (None, "Bar"),
        ("Baz", "Baz"),
    ),
)
def test_register_decorator(name: str | None, expected_name: str):
    db = PydandyDB()

    assert expected_name not in db._data

    @db.register(name)
    class Bar(BaseModel):
        pass

    assert expected_name in db._data


@pytest.mark.parametrize(
    "name, expected_name",
    (
        ("Foo", "Foo"),
        ("Baz", "Baz"),
    ),
)
def test_add_model(name: str | None, expected_name: str, test_model):
    db = PydandyDB()
    assert expected_name not in db._data
    db.add_model(test_model, name)
    assert expected_name in db._data
