import requestsfunctions as rf

# print(json.dumps(test_artist(RADIOHEAD, BASE_URL, headers), indent=4))
print(rf.print_albums(rf.test_artist(rf.LED_ZEPPELIN, rf.BASE_URL, rf.headers)))