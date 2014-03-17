def normalize_for_extension(_, extension):
    if extension is not None:
        return "/".join([_, extension])
    else:
        return _

def patch_params_for_requests(params):
    new_dict = {}
    for key, value in params.items():
        if isinstance(value, list):
            new_key = "%s[]" % key
            new_dict[new_key] = value
        else:
            new_dict[key] = value
    return new_dict

