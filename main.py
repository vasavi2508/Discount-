
# Retail Billing with Multiple Discount Rules

# Category-wise tax rates
TAX_RATES = {
    "grocery": 5,
    "clothing": 12,
    "electronics": 18,
    "books": 0
}

MAX_DISCOUNT = 1000


# Function to calculate discount percentage
def calculate_discount(subtotal):

    if subtotal >= 5000:
        return 10
    elif subtotal >= 3000:
        return 5
    else:
        return 0


# Function to calculate total discount
def calculate_total_discount(subtotal):

    discount_rate = calculate_discount(subtotal)

    discount = subtotal * discount_rate / 100

    if discount > MAX_DISCOUNT:
        discount = MAX_DISCOUNT

    return discount


# Function to calculate product details
def calculate_product(price, quantity, tax_rate, discount):

    amount = price * quantity

    # Allocate discount proportionally
    item_discount = discount * amount / subtotal

    discounted_amount = amount - item_discount

    tax = discounted_amount * tax_rate / 100

    total = discounted_amount + tax

    return amount, item_discount, tax, total


# Main program
print("==========================================")
print("          RETAIL BILLING SYSTEM")
print("==========================================")

products = []

n = int(input("Enter number of products: "))

# Collect product information
for i in range(n):

    print("\nEnter details of Product", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category: ").lower()

    while category not in TAX_RATES:
        print("Invalid category!")
        print("Available categories:", list(TAX_RATES.keys()))
        category = input("Enter category again: ").lower()

    price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    product = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "amount": amount
    }

    products.append(product)


# Calculate subtotal
subtotal = 0

for product in products:
    subtotal = subtotal + product["amount"]


# Calculate total discount
discount = calculate_total_discount(subtotal)

# Calculate final product-wise tax
total_tax = 0
final_amount = 0

print("\n==========================================")
print("               RETAIL INVOICE")
print("==========================================")

print("Product\tQty\tPrice\tAmount\tTax\tTotal")

for product in products:

    category = product["category"]
    tax_rate = TAX_RATES[category]

    amount, item_discount, tax, total = calculate_product(
        product["price"],
        product["quantity"],
        tax_rate,
        discount
    )

    total_tax = total_tax + tax
    final_amount = final_amount + total

    print(
        product["name"], "\t",
        product["quantity"], "\t",
        product["price"], "\t",
        round(amount, 2), "\t",
        round(tax, 2), "\t",
        round(total, 2)
    )


# Display bill summary
print("\n------------------------------------------")
print("Subtotal          : Rs.", round(subtotal, 2))
print("Total Discount    : Rs.", round(discount, 2))
print("Total Tax         : Rs.", round(total_tax, 2))
print("------------------------------------------")
print("FINAL BILL AMOUNT : Rs.", round(final_amount, 2))
print("==========================================")

print("Thank you for shopping!")
