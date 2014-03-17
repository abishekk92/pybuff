def normalize_for_extension(_, extension):
    if extension is not None:
        return "/".join([_, extension])
    else:
        return _
