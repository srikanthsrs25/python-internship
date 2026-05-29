# Global variable (GLOBAL SCOPE)
shop_name = "Smart Mart"
def generate_bill(customer_name, *items, discount=0):
    """
    Generates a bill for a customer.

    Parameters:
        customer_name (str): Name of the customer (positional argument)
        *items (tuple): Variable number of purchased items (positional variable-length)
        discount (int, optional): Discount percentage (default = 0)  
        str: Final bill summary
    """
    total = 0

    for price in items:
        total += price

    total_after_discount = total - (total * discount / 100)
    final_amount = total_after_discount 

    bill = (f"""
Shop: {shop_name}
Customer: {customer_name}
Subtotal: {total}
Discount: {discount}%
Final Amount: {final_amount}
""")

    return bill

bill1 = generate_bill("Arjun", 200, 150)
bill2 = generate_bill(
    "Meena",
    500, 300,
    discount=10,)

print(bill1)
print(bill2)