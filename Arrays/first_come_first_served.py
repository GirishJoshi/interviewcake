"""
My cake shop is so popular, I'm adding some tables and hiring wait staff so folks can have a 
cute sit-down cake-eating experience.

I have two registers: one for take-out orders, and the other for the other folks eating inside 
the cafe. All the customer orders get combined into one list for the kitchen, where they should be
handled first-come, first-served.

Recently, some customers have been complaining that people who placed orders after them are getting 
their food first. Yikes—that's not good for business!

To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
Each customer order (from either register) as it was finished by the kitchen. (served_orders)
Given all three lists, write a function to check that my service is first-come, first-served. 
All food should come out in the same order customers requested it.

We'll represent each customer order as a unique integer.

As an example,

Take Out Orders: [1, 3, 5]
Dine In Orders: [2, 4, 6]
Served Orders: [1, 2, 4, 6, 5, 3]

would not be first-come, first-served, since order 3 was requested before order 5 but order 5 
was served first.

But,

Take Out Orders: [1, 3, 5]
Dine In Orders: [2, 4, 6]
Served Orders: [1, 2, 3, 5, 4, 6]

would be first-come, first-served.
"""


def is_first_come_first_served(takeout, dinein, served):

    takeout_index, dinein_index, served_index = 0, 0, 0
    len_takeout, len_dinein = len(takeout), len(dinein)

    for order in served:

        # If we still have orders in takeout
        # and the current order in takeout is the same as the current order in served
        if takeout_index < len_takeout and takeout[takeout_index] == order:
            takeout_index += 1
            continue

        # If we still have orders in dinein
        # and the current order in dinein is the same as the current order in served
        if dinein_index < len_dinein and dinein[dinein_index] == order:
            dinein_index += 1
            continue
        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if takeout_index != len_takeout or dinein_index != len_dinein:
        return False

    # All orders in served_orders have been "accounted for"
    # so we're serving first-come, first-served!
    return True


takeout = [1, 3, 5, 3]
dinein = [2, 4, 6, 7]
served = [1, 3, 5, 2, 4, 6, 7, 3]

print(is_first_come_first_served(takeout, dinein, served))
