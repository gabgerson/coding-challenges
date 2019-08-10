#better solution pop costs time when removing from front
def check_customer_orders(take_out, dine_in, served_orders):
    # look at the first item of served_orders and see that it matches either 
    # the first one in take_out or dine_in
    # then keep doing that
    
    while served_orders:
        if not take_out:
            if served_orders[0] == dine_in[0]:
                dine_in.pop(0)
        elif not dine_in:
            if served_orders[0] == take_out[0]:
                take_out.pop(0)
        elif served_orders[0] != take_out[0] and served_orders[0] != dine_in[0]:
            return False
        elif served_orders[0] == take_out[0]:
            take_out.pop(0)
        elif served_orders[0] == dine_in[0]:
            dine_in.pop(0)

        served_orders.pop(0)
    
    return True
        

print(check_customer_orders([1,3,4,6,8],[2,5,7,9],[1,2,3,4,5,6,7,8,9]))
print(check_customer_orders([1,3,4,6,8],[2,5,7,9],[1,2,3,4,5,7,8,9]))
def check_customer_orders_recursive(take_out, dine_in, served_orders):
    
    if not served_orders:
        return True
    if not take_out:
        if served_orders[0] == dine_in[0]:
            dine_in.pop(0)
    elif not dine_in:
        if served_orders[0] == take_out[0]:
            take_out.pop(0)

    elif served_orders[0] != take_out[0] and served_orders[0] != dine_in[0]:
            return False
    
    elif served_orders[0] == take_out[0]:
            take_out.pop(0)
    elif served_orders[0] == dine_in[0]:
            dine_in.pop(0)
    
    served_orders.pop(0)

    return check_customer_orders_recursive(take_out, dine_in, served_orders)

print(check_customer_orders_recursive([1,3,4,6,8],[2,5,7,9],[1,2,3,4,5,6,7,8,9]))
print(check_customer_orders_recursive([1,3,4,6,8],[2,5,7,9],[1,2,3,4,5,7,8,9]))


#official solution
def is_first_come_first_served(take_out, dine_in, served_orders):
    take_out_index = 0
    dine_in_index = 0
    take_out_max_index = len(take_out) - 1
    dine_in_max_index = len(dine_in) - 1

    for order in served_orders:
        # If we still have orders in take_out
        # and the current order in take_out is the same
        # as the current order in served_orders
        if take_out_index <= take_out_max_index and order == take_out[take_out_index]:
            take_out_index += 1

        # If we still have orders in dine_in
        # and the current order in dine_in is the same
        # as the current order in served_orders
        elif dine_in_index <= dine_in_max_index and order == dine_in[dine_in_index]:
            dine_in_index += 1

        # If the current order in served_orders doesn't match the current
        # order in take_out or dine_in, then we're not serving first-come,
        # first-served.
        else:
            return False

    # All orders in served_orders have been "accounted for"
    # so we're serving first-come, first-served!
    return True

print(is_first_come_first_served([1,3,4,6,8],[2,5,7,9],[1,2,3,4,5,6,7,8,9]))
print(is_first_come_first_served([1,3,4,6,8],[2,5,7,9],[1,2,3,4,5,7,8,9]))