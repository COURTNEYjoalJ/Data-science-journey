variant_a = int(input("No of visitors for variant A: "))
conversions_a = int(input("No of conversions for variant A: "))
variant_b = int(input("No of visitors for variant B: "))
conversions_b = int(input("No of conversions for variant B: "))
print(f"Variant A Conversion Rate: {conversions_a/variant_a*100:.2f}%")
print(f"Variant B Conversion Rate: {conversions_b/variant_b*100:.2f}%")
if conversions_a/variant_a > conversions_b/variant_b:
    print("Winner: Variant A")
else:
    print("Winner: Variant B")