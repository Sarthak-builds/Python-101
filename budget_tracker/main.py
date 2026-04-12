expenses = [
    {"amount": 450.75, "category": "Food",   "paid": True},
    {"amount": 200.00, "category": "Travel", "paid": False},
    {"amount": 1200.50,"category": "Rent",   "paid": True},
    {"amount": 89.99,  "category": "Food",   "paid": False},
]

total       = 0
unpaid      = 0

for expense in expenses:
    total += expense["amount"]

    if not expense["paid"]:
        unpaid += expense["amount"]

    if expense["amount"] > 1000:
        print(f"  Large expense: {expense['category']} ₹{expense['amount']:.2f}")

print(f"\nTotal spent : ₹{total:.2f}")
print(f"Unpaid      : ₹{unpaid:.2f}")