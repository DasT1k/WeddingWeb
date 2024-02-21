import os, pytest
from app import create_app
from app.models import Quest, db


@pytest.fixture
def test_client():
    os.environ['CONFIG_TYPE'] = 'config.TestConfig'

    app = create_app()
    app.testing = True

    quest1 = Quest(  # test data to put in db
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

    with app.test_client() as testing_client:
        with app.app_context():
            db.session.add(quest1)
            db.session.add(quest2)
            db.session.commit()

            yield testing_client

            db.drop_all()
