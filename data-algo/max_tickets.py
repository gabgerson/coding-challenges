def max_tickets(tickets):
    #if len tickets == 1 return 1
    if len(tickets) == 1:
        return 1
    # sort the tickets list
    sorted_tickets = sorted(tickets)
    # keep track of current sub-sequence length
    curr_sub_len = 1
    #max sub sequesce
    max_sub = 1
    #prev num
    prev_price = sorted_tickets[0]
    # loop through tickets
    
    for i in range(1, len(sorted_tickets)):
    # if check if current num is equal to plus 1 previous num or equal to previous num
        if prev_price == sorted_tickets[i] or prev_price + 1 == sorted_tickets[i]:
    #add 1 to current subsquence length
            curr_sub_len += 1 
    # if current not eqaul to +1 prev or equal to prev
    
    # current subsequence length reset to 1
        else:
            curr_sub_len = 1
        # max subsequnce === max( max_sub, current sub)
        max_sub = max(max_sub, curr_sub_len)
    #set prev_price to sorted_tickets[i]
        prev_price = sorted_tickets[i]

    # max_sub = max(max_sub, curr_sub_len)
    
    return max_sub

print(max_tickets([4,13,2,3]))

print(max_tickets([4,5,3,2,11,12,13,10,13]))

print(max_tickets([1]))