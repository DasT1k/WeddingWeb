import os, pytest
from app import create_app
from app.models import Quest, db


@pytest.fixture
def test_client():
    os.environ['CONFIG_TYPE'] = 'config.TestConfig'

    app = create_app()

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture
def init_database(test_client):
    db.create_all()

    quest1 = Quest(
        name="Roman",
        zags=True,
        drink="Whiskey",
        food="bird"
    )

    quest2 = Quest(
        name="Evgenia",
        zags=False,
        drink="",
        food="fish"
    )

    db.session.add(quest1)
    db.session.add(quest2)
    db.session.commit()

    yield

    db.drop_all()
