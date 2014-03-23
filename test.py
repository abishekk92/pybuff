from os import getenv as ENV
from api import Buffer
from utils import normalize_for_extension
import vcr


recorder = vcr.VCR(cassette_library_dir = 'fixtures/cassettes',)


client = Buffer(ENV('buff_access_token'), ENV('buff_client_id'),
                ENV('buff_client_secret'))


def test_user():
    with recorder.use_cassette('fixtures/cassettes/user.yml') as user:
        response = client.get_user()
        assert user.responses[0]['status']['code'] == 200

def test_profile():
    with recorder.use_cassette('fixtures/cassettes/profile.yml') as profiles:
        response = client.get_profiles()
        assert profiles.responses[0]['status']['code'] == 200

def test_config():
    with recorder.use_cassette('fixtures/cassettes/config.yml') as configs:
        response = client.get_config()
        assert configs.responses[0]['status']['code'] == 200

def test_get_by_profile_id():
    with recorder.use_cassette('fixtures/cassettes/profile_id.yml') as profile_id:
        response = client.get_profile('4eb854340acb04e870000010')
        assert profile_id.responses[0]['status']['code'] == 404

def test_get_shares():
    with recorder.use_cassette('fixtures/cassettes/share.yml') as share:
        response = client.get_shares(url="http://www.google.com")
        assert share.responses[0]['status']['code'] == 200

def test_get_updates():
    with recorder.use_cassette('fixtures/cassettes/updates.yml') as update:
        response = client.get_updates('5226f9b66771ca867e000013')
        assert update.responses[0]['status']['code'] == 200

def test_update_with_interactions():
    with recorder.use_cassette('fixtures/cassettes/updates_ineraction.yml') as update:
        response = client.get_updates('5226f9b66771ca867e000013', 'interactions', {'event' : 'retweet'})
        assert update.responses[0]['status']['code'] == 200

def test_pending_update():
    with recorder.use_cassette('fixtures/cassettes/pending_update.yml') as pending:
        response = client.get_profile_updates('522386eaacd4e52a21000010', 'pending')
        assert pending.responses[0]['status']['code'] == 200

def test_sent_update():
    with recorder.use_cassette('fixtures/cassettes/sent_update.yml') as sent:
        response = client.get_profile_updates('522386eaacd4e52a21000010', 'sent')
        assert sent.responses[0]['status']['code'] == 200

def test_pending_update_with_params():
    with recorder.use_cassette('fixtures/cassettes/pending_update_with_params.yml') as pending_with_params:
        response = client.get_profile_updates('522386eaacd4e52a21000010', 'pending', params={'count' : 10})
        assert pending_with_params.responses[0]['status']['code'] == 200

def test_sent_update_with_params():
    with recorder.use_cassette('fixtures/cassettes/sent_update.yml') as sent_with_params:
        response = client.get_profile_updates('522386eaacd4e52a21000010', 'sent', params={'count' : 10})
        assert sent_with_params.responses[0]['status']['code'] == 200

def test_create_update():
    with recorder.use_cassette('fixtures/cassettes/create_update.yml') as create_update:
        response = client.create_update(params={'text' : 'foobar', 'profile_ids' :['522386eaacd4e52a21000010']})
        assert create_update.responses[0]['status']['code'] == 200

def test_shuffle_update():
    with recorder.use_cassette('fixtures/cassettes/shuffle.yml') as shuffle:
        response = client.update_profile('522386eaacd4e52a21000010', "shuffle")
        assert shuffle.responses[0]['status']['code'] == 200

def test_normalize_extension():
    endpoint = normalize_for_extension("12345","foo/bar")
    assert endpoint == "12345/foo/bar"
