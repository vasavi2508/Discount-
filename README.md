# Discount-
# Retail Billing with Multiple Discount Rules

## 1. Project Overview

The **Retail Billing with Multiple Discount Rules** is a Python-based application designed to generate itemized bills for retail customers.

The system processes multiple products, calculates quantities and prices, applies category-specific taxes, and provides discounts based on purchase amount.

It also ensures that the discount does not exceed the maximum concession limit and generates the final invoice automatically.

## 2. Objectives

- To process multiple products in a single bill.
- To calculate product prices based on quantity.
- To apply category-specific tax rates.
- To calculate discounts based on purchase thresholds.
- To maintain a maximum concession limit.
- To calculate the final payable amount.
- To generate an itemized retail invoice.

## 3. Assumptions

1. Customers can purchase multiple products.
2. Each product belongs to a predefined category.
3. Product prices and quantities are positive values.
4. Tax rates are different for different product categories.
5. Discounts depend on the total purchase amount.
6. The maximum discount allowed is ₹1,000.
7. Discounts are distributed proportionally among products.
8. Tax is calculated after applying the discount.

## 4. Category-Specific Tax Rates

| Product Category | Tax Rate |
|---|---:|
| Grocery | 5% |
| Clothing | 12% |
| Electronics | 18% |
| Books | 0% |

## 5. Discount Rules

| Purchase Amount | Discount Percentage |
|---|---:|
| Below ₹3,000 | 0% |
| ₹3,000 – ₹4,999 | 5% |
| ₹5,000 and above | 10% |

**Maximum Concession Limit:** ₹1,000.

## 6. Formula Used

### Product Amount

Product Amount = Unit Price × Quantity

### Subtotal

Subtotal = Sum of All Product Amounts

### Discount

Discount = Subtotal × Discount Percentage / 100

If the discount exceeds ₹1,000, the discount is limited to ₹1,000.

### Taxable Amount

Taxable Amount = Product Amount − Allocated Discount

### Category Tax

Tax = Taxable Amount × Tax Rate / 100

### Final Bill Amount

Final Bill Amount = Discounted Subtotal + Total Tax

## 7. Algorithm

1. Start the program.
2. Display the retail billing system heading.
3. Enter the number of products.
4. Read product name and category.
5. Check whether the category is valid.
6. Enter unit price and quantity.
7. Calculate the amount for each product.
8. Calculate the total purchase subtotal.
9. Determine the discount percentage based on the subtotal.
10. Calculate the discount amount.
11. Check the maximum concession limit.
12. Distribute the discount proportionally among products.
13. Calculate category-specific tax for each product.
14. Calculate the final amount for each product.
15. Calculate the total tax and final bill amount.
16. Display the itemized invoice.
17. Stop the program.

## 8. Pseudocode

```text
START

DEFINE category tax rates

INPUT number of products

FOR each product:

    INPUT product name
    INPUT category

    CHECK category validity

    INPUT unit price
    INPUT quantity

    amount = unit price * quantity

    STORE product details

CALCULATE subtotal

IF subtotal >= 5000:
    discount rate = 10%

ELSE IF subtotal >= 3000:
    discount rate = 5%

ELSE:
    discount rate = 0%

discount = subtotal * discount rate / 100

IF discount > 1000:
    discount = 1000

FOR each product:

    allocated discount =
        discount * product amount / subtotal

    taxable amount =
        product amount - allocated discount

    tax = taxable amount * category tax rate / 100

    product total = taxable amount + tax

CALCULATE total tax
CALCULATE final bill amount

DISPLAY itemized invoice
DISPLAY final bill amount

STOP
```

## 9. Test Cases

| Test Case | Subtotal | Discount | Expected Result |
|---|---:|---:|---|
| 1 | ₹2,000 | ₹0 | No discount |
| 2 | ₹3,500 | ₹175 | 5% discount |
| 3 | ₹6,000 | ₹600 | 10% discount |
| 4 | ₹15,000 | ₹1,000 | Maximum discount applied |

### Sample Test Case

**Input:**

| Product | Category | Price | Quantity |
|---|---|---:|---:|
| Laptop | Electronics | ₹5,000 | 1 |
| Shirt | Clothing | ₹1,000 | 1 |

**Expected Output:**

```text
==========================================
                RETAIL INVOICE
==========================================

Product | Qty | Amount | Discount | Tax | Total

Laptop  | 1 | 5000 | 500 | 810 | 5310
Shirt   | 1 | 1000 | 100 | 108 | 1008

------------------------------------------
Subtotal          : Rs. 6000.0
Total Discount    : Rs. 600.0
Total Tax         : Rs. 918.0
------------------------------------------
FINAL BILL AMOUNT : Rs. 6318.0
==========================================

Thank you for shopping!
```

## 10. Python Concepts Used

- Variables and data types
- Input and output statements
- Arithmetic operators
- Conditional statements (if, elif, else)
- For loops and while loops
- Lists
- Dictionaries
- Functions
- Return statements
- Basic calculations

## 11. Conclusion

The Retail Billing with Multiple Discount Rules system successfully generates retail invoices by processing multiple products, quantities, category-specific taxes, and threshold-based discounts.

It applies the maximum concession limit and calculates the final bill amount automatically.

This project demonstrates the practical application of Python programming concepts in solving real-world retail billing problems. It reduces manual calculations and makes the billing process simple, accurate, and efficient.

## 12. Project Structure

```text
Retail-Billing-System/
│
├── retail_billing.py
├── README.md
│
└── screenshots/
    └── output.png
```

## 13. Execution Instructions

1. Install Python on your computer.
2. Open the project folder in Visual Studio Code.
3. Open `retail_billing.py`.
4. Run the program using:

```bash
python retail_billing.py
```

5. Enter the product details.
6. Check the generated retail invoice.
7. Capture the actual output screenshot.
8. Upload the Python file, README, and screenshot to GitHub.

## 14. Author Details

- **Name:** v.v.s.s.gayathri
- **Roll Number:** N26V01A0388
- **Branch:** CSE
- **Section:** Section-5
- **Subject:** Python Programming
- **Project:** Retail billing
