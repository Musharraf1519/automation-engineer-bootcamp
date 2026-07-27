# E-Commerce Checkout Engine

## Project Overview

Imagine you are working as a Python Developer for an online shopping company. Every time a customer purchases a product, the checkout system calculates the bill by applying discounts, taxes, delivery charges and payment offers before generating the final invoice.

Your task is to build this checkout system using only the concepts learned up to Chapter 6.

The application should collect customer information, product details and payment information from the user. Based on predefined business rules, it should calculate the final payable amount and display a professional invoice.

---

## Business Scenario

A customer visits an online shopping website and purchases a product.

Before the order is confirmed, the checkout system performs several checks.

- Premium members receive additional discounts.
- Valid coupon codes reduce the bill.
- Different payment methods provide different offers.
- GST is applied after discounts.
- Delivery charges depend on the final bill amount.

Once every calculation is completed, the customer receives a detailed invoice.

Your application should simulate this complete workflow.

---

## Functional Requirements

The application should collect the following information from the customer.

### Customer Details

- Customer Name
- Membership Status (Yes / No)

### Product Details

- Product Name
- Product Price
- Quantity

### Payment Details

- Coupon Code
- Payment Method

Available payment methods:

- Cash
- Card
- UPI

---

## Business Rules

### Subtotal

Subtotal = Product Price × Quantity

### Membership Discount

Premium members receive a 10% discount only if the subtotal is ₹5000 or more.

Otherwise, no membership discount is applied.

### Coupon Discount

Only one coupon is supported.

Coupon Code:

SAVE500

Conditions:

- Coupon must be SAVE500
- Subtotal must be at least ₹4000

Discount:

₹500

Otherwise:

No coupon discount.

### Payment Discount

UPI

2%

Card

1%

Cash

No discount

### GST

GST Rate = 18%

GST must be calculated after applying all discounts.

### Delivery Charge

If the final amount before delivery charges is ₹3000 or more,

Delivery Charge = FREE

Otherwise,

Delivery Charge = ₹150

---

## Expected Workflow

The application should perform the following operations.

1. Read customer details.
2. Read product details.
3. Calculate subtotal.
4. Apply membership discount.
5. Apply coupon discount.
6. Apply payment discount.
7. Calculate GST.
8. Determine delivery charge.
9. Calculate the final payable amount.
10. Display the invoice.

---

## Expected Output

Refer to **sample_output.txt**.

---

## Folder Structure

05-Ecommerce-Checkout-Engine/

├── README.md

├── ecommerce_checkout.py

├── sample_output.txt

└── screenshots/

---

## Constraints

Use only concepts covered in Chapters 1–6.

Do not use:

- Loops
- Functions
- Lists
- Dictionaries
- Classes
- Exception Handling

---

## Learning Outcomes

After completing this project, you should be able to build a real-world billing application that combines user input, calculations and business rules using conditional statements.