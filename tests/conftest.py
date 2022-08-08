import pytest
from pydantic import BaseModel

from pydandy import PydandyDB


class TestModel(BaseModel):
    id: int = 0
    name: str = "Foo"

    def __hash__(self):
        return hash(self.id)


@pytest.fixture
def test_model():
    return TestModel


@pytest.fixture
def db_factory(test_model):
    def _factory():
        db = PydandyDB()
        db.add_model(test_model, "Test")
        return db

    return _factory
