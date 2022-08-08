from pydandy.table import PydandyTable


def test_dynamic_attrs(db_factory, test_model):
    db = db_factory()
    db.add_model(test_model)
    assert isinstance(db.Test, PydandyTable)


def test_add(db_factory, test_model):
    db = db_factory()
    for i in range(5):
        db.Test.add(test_model(id=i))
    assert len(db.Test) == 5


def test_get(db_factory, test_model):
    db = db_factory()
    model = test_model(id=1)
    db.Test.add(model)
    assert model == db.Test.get(1)


def test_filter(db_factory, test_model):
    db = db_factory()

    for i in range(5):
        db.Test.add(test_model(id=i))
    results = db.Test.filter(lambda r: r.id % 2 == 0)

    assert [r.id for r in results.records] == [0, 2, 4]


def test_update(db_factory, test_model):
    db = db_factory()
    record = test_model(id=1, name="Foo")
    db.Test.add(record)
    pre_update = db.Test.get(1)
    record.name = "Bar"
    db.Test.update(record)
    post_update = db.Test.get(1)

    assert record.name != pre_update.name
    assert record.name == post_update.name


def test_delete(db_factory, test_model):
    db = db_factory()
    model = test_model(id=1)
    db.Test.add(model)
    db.Test.delete(1)
    assert len(db.Test) == 0
