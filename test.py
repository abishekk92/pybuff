from os import getenv as ENV
from api import Buffer
import vcr 


recorder = vcr.VCR(cassette_library_dir = 'fixtures/cassettes',)


client = Buffer(ENV('buff_access_token'), ENV('buff_client_id'),
                ENV('buff_client_secret'))

with recorder.use_cassette('fixtures/cassettes/user.yml') as user:
    response = client.get_user()
    assert user.responses[0]['status']['code'] == 200


with recorder.use_cassette('fixtures/cassettes/profile.yml') as profiles:
    response = client.get_profiles()
    assert profiles.responses[0]['status']['code'] == 200

with recorder.use_cassette('fixtures/cassettes/config.yml') as configs:
    response = client.get_config()
    assert configs.responses[0]['status']['code'] == 200

with recorder.use_cassette('fixtures/cassettes/profile_id.yml') as profile_id:
    response = client.get_profile('4eb854340acb04e870000010')
    assert profile_id.responses[0]['status']['code'] == 404

with recorder.use_cassette('fixtures/cassettes/share.yml') as share:
    response = client.get_shares(url="http://www.google.com")
    assert share.responses[0]['status']['code'] == 200

endpoint = client.normalize_for_extension("12345","foo/bar")
assert endpoint == "12345/foo/bar"


