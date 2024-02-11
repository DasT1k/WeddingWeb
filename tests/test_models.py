from app.models import Quest


def test_quest():
    quest = Quest(
        name="Roman",
        zags=True,
        drink="Whiskey",
        food="bird"
    )
    assert quest.name == "Roman"
    assert quest.zags
    assert quest.drink == "Whiskey"
    assert quest.food == "bird"
