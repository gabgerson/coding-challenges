def checkMagazine(magazine, note):

    magazine_dict = dict()
    for word in magazine:
        if not magazine_dict.get(word):
            magazine_dict[word] = 1
        else:
            magazine_dict[word] += 1
    
    result = "Yes"

    for word in note:
        if magazine_dict.get(word) is not None and magazine_dict.get(word) > 0:
            magazine_dict[word] -=1
        else:
            
            result = "No"
            break
    print(result)
