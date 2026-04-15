starting_customers = int(input("Starting customers: "))
customers_lost  = int(input("Customers lost this month: "))
new_customers = int(input("New customers acquired: "))
churn_rate = (customers_lost/starting_customers)*100
net_growth = new_customers - customers_lost
ending_customers = starting_customers-customers_lost+new_customers
print("=== Customer Churn Analysis ===\n")
print(f"Starting customers: {starting_customers}")
print(f"Customers lost: {customers_lost}")
print(f"New customers: {new_customers}\n")
print("--- Results ---")
print(f"Churn rate: {churn_rate:.2f}")
print(f"Net Growth: {net_growth:+d}")
print(f"Ending Customers: {ending_customers}")