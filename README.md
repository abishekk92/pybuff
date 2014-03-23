pybuff
======

Python Library for interacting with BufferApp's API

Installation

```bash
    pip install -e git+ssh://git@github.com/abishekk92/pybuff.git#egg=pybuff
```

Usage
=====

Authenticate and create a client

```python
client = Buffer(ENV('buff_access_token'), ENV('buff_client_id'),
                ENV('buff_client_secret'))
```

Once authenticated and a client is created, the interaction is pretty straight forward.

To get the details of a user.

```python
   user = client.get_user()
```

To get all the profiles associated with the account

```python
   profiles = client.get_profiles()
```

To get a profile by id

```python
   profile = client.get_profile(profile_id)
```

To find out how many times a link has been shared

```python
  share_count = client.get_shares(link)
```

To post an update

```python
    client.create_update({"text" : "your-text", "profile_ids" : <list-of-profile-ids>})
``` 

To update an update

```python
    client.update(update_id, extension, params)
```

Extensions and params for any methods which allows them can be controlled as defined in the [API docs](https://bufferapp.com/developers/api/updates)

TODO:

* Add examples
* Instuctions for installing via pip
* Include coveralls and travis.

