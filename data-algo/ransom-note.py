def checkMagazine(magazine, note):
    #add magazine words to dictionary
    mag_dict = dict()

    for word in magazine:
        if word not in mag_dict:
            mag_dict[word] = 1
        else:
            mag_dict[word] += 1
    #loop through note and check mag_dict for words and subtract from that word's total
    #in mag_dict

    for word in note:
        if word in mag_dict:
            if mag_dict[word] == 0:
                print("No")
                return
        
            mag_dict[word] -= 1

        else:
            print("No")
            return

    print("Yes")