from random import randint 
def shuffle_in_place(int_list):
    #loop through list
    for i in range(len(int_list)):
        #get a randrom index from i to end of list

        random_index = randint(i, len(int_list) - 1)
        # swap num at random index  into current index and put num at current index into random index
        if i != random_index:
            
            int_list[i], int_list[random_index] = int_list[random_index], int_list[i]
    return int_list


print(shuffle_in_place([1,2,3,4, 5]))