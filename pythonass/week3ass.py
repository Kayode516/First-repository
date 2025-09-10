# week three assginment, function name
def calculate_discount(price, discount_percent):
    if discount_percent >= 25:
        discount_amount = price * discount_percent / 100
        final_price = price - discount_amount 
        print("Discounted Price", final_price)
    else:
        print("Original Price", price)  
calculate_discount(5000, 25)

# section 2
price_input = int(input("Enter the original price "))
discount_input = int(input("Enter the discount percentage "))
calculate_discount(price_input, discount_input)