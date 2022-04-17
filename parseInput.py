def parseInput(request):
    print('request es', request.get_json(silent=True))
    parsedJson = request.get_json(
        force=True, silent=False, cache=True)  # Allow for type errors
    return parsedJson
