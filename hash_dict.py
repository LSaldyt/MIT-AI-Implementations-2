from json import dumps

def hash_dict(d):
    return json.dumps(d, sort_keys=True)

def retrieve_dict(dstr):
    return json.loads(dstr)
