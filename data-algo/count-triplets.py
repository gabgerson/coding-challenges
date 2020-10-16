def countTriplets(arr, r):
    triplets_dict = dict()
    count_dict = dict()

    counter = 0
    
    for i in reversed(arr):

        if i*r in triplets_dict:
            counter += triplets_dict[i*r]
        if i*r in count_dict:

            triplets_dict[i] = triplets_dict.get(i, 0) + count_dict[i*r]

        count_dict[i] = count_dict.get(i, 0) + 1

    return counter