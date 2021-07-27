character={
    "name": "기사",
    "level" : 12,
    "items" : {
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
        },
    "skill" : ["베기", "세게베기", "아주세게 베기"]
}
for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print("{} : {}".format(k, character[key][k]))
    elif type(character[key]) is list:
        for item in character[key]:
            print("{}:{}".format(key,item))
    else:
             print("{} : {}".format(key, character[key]))
    