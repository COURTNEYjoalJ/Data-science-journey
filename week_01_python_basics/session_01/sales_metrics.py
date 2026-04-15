total_visitors = 15000
added_to_cart = 4500
completed_purchase = 3200
requested_refund = 150
print(f"Total Visitors: {total_visitors}\nAdded to Cart: {added_to_cart}\nCompleted Purchases: {completed_purchase}\nRefunds: {requested_refund}")
print(f"Conversion Rate: {completed_purchase/total_visitors*100}")
print(f"Cart Abandonment Rate: {(added_to_cart-completed_purchase)/added_to_cart*100}")
print(f"Refund Rate: {requested_refund/completed_purchase*100}")
print(f"Net Successful Transaction {completed_purchase-requested_refund}")