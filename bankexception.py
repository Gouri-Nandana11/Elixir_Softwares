balance = 400

withdrawal_amount = int(input("Enter the amount to withdraw: "))
deposit_amount = int(input("Enter the amount to deposit: "))

try:
    if withdrawal_amount > balance:
        raise ValueError("No sufficient balance")
    else:
        balance -= withdrawal_amount
        print("Withdrawal successful. Current balance:", balance)

    if deposit_amount < 0:
        raise ValueError("Deposit amount cannot be less than zero")
    else:
        balance += deposit_amount
        print("Deposit successful. Current balance:", balance)

except ValueError as e:
    print("Error:", e)