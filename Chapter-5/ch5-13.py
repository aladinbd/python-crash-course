available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'peineaple', 'extra cheese']
requested_toppings = ['mushrooms', 'fresh fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
