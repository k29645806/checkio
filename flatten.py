dic = {
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}


def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            v = '' if v=={} else v     # only add this one
            if isinstance(v, dict):    # if value is still dict refers that it still need to unpack
                stack.append((path + (k,), v))
                #print stack
            else:
                result["/".join((path + (k,)))] = v
    return result

print flatten(dic)
