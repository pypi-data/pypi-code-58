import pytest

from dcicutils.qa_utils import notice_pytest_fixtures
from pyramid.config import Configurator
from ..interfaces import DBSESSION
from .serverfixtures import DBSession
from .testappfixtures import testapp


notice_pytest_fixtures(DBSession, testapp)


# Test for storage.keys

items = [
    {'name': 'one', 'accession': 'TEST1'},
    {'name': 'two', 'accession': 'TEST2'},
]

bad_items = [
    {'name': 'one', 'accession': 'BAD1'},
    {'name': 'bad', 'accession': 'TEST1'},
]


@pytest.fixture(scope='session')
def app(DBSession):
    notice_pytest_fixtures(DBSession)
    config = Configurator()
    config.registry[DBSESSION] = DBSession
    config.include('snovault')
    config.include('.testing_key')
    return config.make_wsgi_app()


@pytest.fixture
def content(testapp):
    notice_pytest_fixtures(testapp)
    url = '/testing-keys/'
    for item in items:
        testapp.post_json(url, item, status=201)


@pytest.mark.parametrize('item', items)
def test_unique_key(testapp, content, item):
    notice_pytest_fixtures(testapp, content)
    url = '/testing-keys/' + item['accession']
    res = testapp.get(url).maybe_follow()
    assert res.json['name'] == item['name']


def test_keys_bad_items(testapp, content):
    notice_pytest_fixtures(testapp, content)
    url = '/testing-keys/'
    for item in bad_items:
        testapp.post_json(url, item, status=409)


def test_keys_update(testapp):
    notice_pytest_fixtures(testapp)
    url = '/testing-keys/'
    item = items[0]
    res = testapp.post_json(url, item, status=201)
    location = res.location
    new_item = {'name': 'new_one', 'accession': 'NEW1'}
    testapp.put_json(location, new_item, status=200)
    testapp.post_json(url, item, status=201)
    testapp.put_json(location, item, status=409)


def test_keys_conflict(testapp):
    notice_pytest_fixtures(testapp)
    url = '/testing-keys/'
    item = items[1]
    initial = testapp.get(url).json['@graph']
    testapp.post_json(url, item, status=201)
    posted = testapp.get(url).json['@graph']
    assert(len(initial)+1 == len(posted))
    conflict = testapp.post_json(url, item, status=409)
    assert(conflict.status_code == 409)
    conflicted = testapp.get(url).json['@graph']
    assert(len(posted) == len(conflicted))
