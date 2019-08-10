#combo of my solution and official solution
def my_merge_lists(my_list, alices_list):
    # Make a list big enough to fit the elements from both lists
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size
    index = 0
    my_index = 0
    alice_index = 0
  


    while index < merged_list_size:
  

        if my_index >= len(my_list):
            merged_list[index] = alices_list[alice_index]
            alice_index += 1

        elif alice_index >= len(alices_list):
            merged_list[index] = my_list[my_index]
            alice_index += 1
    

        elif my_list[my_index] < alices_list[alice_index]:
        # Case: 0th comes from my list
            merged_list[index] = my_list[my_index]
            # print(merged_list)
            my_index += 1
   
           
        else:
        # Case: 0th comes from Alice's list
            merged_list[index] = alices_list[alice_index]
            alice_index += 1

        
        index += 1
     
        
        
        # print(index)
       
        
    # Eventually we'll want to return the merged list
    return merged_list




def merge_lists(my_list, alices_list):
    # Set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)
        if (not is_my_list_exhausted and (is_alices_list_exhausted or my_list[current_index_mine] < alices_list[current_index_alices])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list


print(merge_lists([3,  4,  6, 10, 11, 15], [1,  5,  8, 12, 14, 19]))
print(my_merge_lists([3,  4,  6, 10, 11, 15], [1,  5,  8, 12, 14, 19]))