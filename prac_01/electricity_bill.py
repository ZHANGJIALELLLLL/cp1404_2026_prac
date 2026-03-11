#1
print("Electricity bill estimator")
cents_per_kwh = float(input("Enter cents per kWh:"))
daily_use = float(input("Enter daily use in kWh:"))
billing_days = int(input("Enter number of billing days:"))
estimated_bill = cents_per_kwh * daily_use * billing_days / 100
print(f"Estimated bill: ${estimated_bill:.2f}")
print()

#2
print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_choice = input("Which tariff? 11 or 31: ")
if tariff_choice == '11':
    cents_per_kwh = TARIFF_11
elif tariff_choice == '31':
    cents_per_kwh = TARIFF_31
daily_use = float(input("Enter daily use in kWh:"))
billing_days = int(input("Enter number of billing days:"))
estimated_bill = cents_per_kwh * daily_use * billing_days
print(f"Estimated bill: ${estimated_bill:.2f}")
print()
