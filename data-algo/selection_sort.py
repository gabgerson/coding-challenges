def selection_sort(ls):

    #keep track of current and current lowest
    current_lowest = ls[0]
    index_of_current_lowest = 0
    #loop
    for i in range(len(ls)):
        current_lowest = ls[i]
        index_of_current_lowest = i
    
        for j in range(i , len(ls)):

            if ls[j] < current_lowest:
                current_lowest = ls[j]
                index_of_current_lowest = j
              

   

        ls[i], ls[index_of_current_lowest] = ls[index_of_current_lowest], ls[i]
       
    return ls

print(selection_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))