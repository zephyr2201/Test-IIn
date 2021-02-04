from .models import Person
from freezegun import freeze_time


def test_auth_post(db, client):
    iin = {"iin": "010222501966"}
    response = client.post('/people/', iin)
    assert response.status_code == 201
    data = response.json()
    assert 'iin' in data
    assert 'age' in data
    iin_get = iin['iin']
    response_get = client.get(f'/people/{iin_get}')
    assert response_get.status_code == 200
    data_get = response.json()
    assert 'iin' in data_get
    assert 'age' in data_get


@freeze_time("2009-03-17")
def test_person_create(db, client):
    iin = "010222501966"
    person = Person.objects.create(iin=iin)
    print('\nIIN: ' + person.iin + ' Age: ' + str(person.calculated_age))
    assert person.iin
    assert person.calculated_age == 8


def test_not_valid_len(db, client):
    iin = {"iin": "010222501966222"}  # Max length 12
    response = client.post('/people/', iin)
    assert response.status_code == 400


def test_not_valid_data(db, client):
    iin = {"iin": "010230501995"}  # February 30
    response = client.post('/people/', iin)
    assert response.status_code == 400


def test_not_valid(db, client):
    iin = {"iin": "eeeeee"}
    response = client.post('/people/', iin)
    assert response.status_code == 400


def test_get_not_ok(db, client):
    iin = {"iin": "123456789123"}
    try:
        client.get(f'/people/{iin}')
    except Exception as e:
        print('Dont Exist')
