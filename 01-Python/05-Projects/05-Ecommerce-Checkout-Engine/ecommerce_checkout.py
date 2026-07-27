print("====================================================================")
print("                     E-COMMERCE CHECKOUT ENGINE")
print("====================================================================")
print()
name = input("Enter Customer Name           : ")
membership = input("Premium Member (Yes/No)       : ")
print()
prod_name = input("Enter Product Name            : ")
price = float(input("Enter Product Price           : "))
qty = int(input("Enter Quantity                : "))
print()
coupon_code = input("Enter Coupon Code             : ")
payment_mode = input("Payment Method (Cash/Card/UPI): ")
membership_discount = 0
coupon_discount = 0
payment_discount = 0
delivery_charge = 0
print()

print("====================================================================")
print("                            CUSTOMER INVOICE")
print("====================================================================")
print()
print(f"Customer Name      : {name}")
print(f"Premium Member     : {membership}")
print()
print("------------------------------------------------------------")
print()
print(f"Product Name       : {prod_name}")
print(f"Unit Price         : ₹{price}")
print(f"Quantity           : {qty}")
print()
print("------------------------------------------------------------")
sub_total = price*qty
print(f"Subtotal           : ₹{sub_total}")
print()

if membership=="Yes" and sub_total>=5000:
    membership_discount = sub_total*0.1

sub_total-=membership_discount
if coupon_code == 'SAVE500' and sub_total >=4000:
    coupon_discount = 500
    
sub_total-=coupon_discount
if payment_mode == 'UPI':
    payment_discount =  0.02*sub_total
elif payment_mode == 'Card':
    payment_discount = 0.01*sub_total


print(f"Membership Discount: -₹{membership_discount}")
print(f"Coupon Discount    : -₹{coupon_discount}")
print(f"Payment Discount   : -₹{payment_discount}")
print()
print("------------------------------------------------------------")
taxable_amount = sub_total-payment_discount
gst = 0.18*taxable_amount
print(f"Taxable Amount     : ₹{taxable_amount}")
print(f"GST (18%)          : ₹{gst}")
print()
if taxable_amount+gst >=3000:
    print("Delivery Charge    : FREE")
else:
    delivery_charge = 150
    print("Delivery Charge    : ₹150")
print()
print("------------------------------------------------------------")
print()
print(f"Final Payable      : ₹{delivery_charge+gst+taxable_amount}")
print()
print("------------------------------------------------------------")
print()
print(f"Payment Method     : {payment_mode}")
if coupon_discount>0:
    print(f"Coupon Applied     : {coupon_code}")
print()
print("====================================================================")
print("           THANK YOU FOR SHOPPING WITH US")
print("====================================================================")