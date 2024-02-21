def test_index_route(test_client):
    response = test_client.get('/')
    assert response.status_code == 200


def test_submit_route(test_client):
    response = test_client.post('/submit', data={'name': 'Roman',
                                                 'zags': '1',
                                                 'drink': 'Whiskey',
                                                 'food': 'fish'})
    assert response.status_code == 302 and response.headers['Location'] == '/#popup'


def test_quests_route(test_client):
    response = test_client.get('/quests')
    assert response.status_code == 200
    assert b'Evgenia' and b'Whiskey' in response.data  # data from fixture exists in db and represented on page
    assert b'Meat: 0 / Fish: 1 / Bird: 1' in response.data  # sum calculation
    assert b'<th>1</th>' in response.data  # zags field parsing ("0" -> 0 -> False) and calculation


def test_submit_quest(test_client):  # data after submitting exists in db and represented on page, sums recalculated
    test_client.post('/submit', data={'name': 'Vasya',
                                      'zags': '1',
                                      'drink': 'Cola',
                                      'food': 'meat'})
    response = test_client.get('/quests')
    assert b'Vasya' and b'Cola' in response.data
    assert b'Meat: 1 / Fish: 1 / Bird: 1' in response.data
    assert b'<th>2</th>' in response.data
