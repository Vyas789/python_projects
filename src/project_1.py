from datetime import datetime

class BankAccount:
    
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.transaction_history = []

        if balance > 0:
            self.transaction_history.append({
                'type': 'Initial',
                'amount': balance,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return False
        
        self.balance += amount
        self.transaction_history.append({
            'type': 'Deposit',
            'amount': amount,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Deposited {amount}. New balance: {self.balance}")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"Insufficient balance! Available: {self.balance}")
            return False
        
        self.balance -= amount
        self.transaction_history.append({
            'type': 'Withdrawal',
            'amount': amount,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Withdrawn {amount}. New balance: {self.balance}")
        return True
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, target_account):
        if amount <= 0:
            print("Transfer amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"Insufficient balance! Available: {self.balance}")
            return False

        self.balance -= amount
        self.transaction_history.append({
            'type': 'Transfer Out',
            'amount': amount,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'to': target_account.holder_name 
        })

        target_account.balance += amount
        target_account.transaction_history.append({
            'type': 'Transfer In',
            'amount': amount,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'from': self.holder_name
        })
        
        print(f"Transferred {amount} to {target_account.holder_name}")
        return True

    def __str__(self):
        return (f"Account: {self.account_number}\n")
    
print("=== BANKING SYSTEM TEST ===\n")

# 1. Create Accounts
print(" Creating accounts ")
hardik = BankAccount("H001", "Hardik", 1000)
rohit = BankAccount("R045", "Rohit", 500)
print(hardik)
print(rohit)

# 2. Deposit
print("\n Testing deposit")
hardik.deposit(500)

# 3. Withdrawal
print("\n Testing withdrawal")
hardik.withdraw(200)
rohit.withdraw(100)
hardik.withdraw(5000)  # Should show insufficient funds

# 4. Transfer
print("\n--- 4. Testing transfer ---")
hardik.transfer(300, rohit)

# 5. Final Balance Check
print("\n--- 5. Final Account Status ---")
print(f"{hardik.holder_name}'s Balance: {hardik.get_balance()}")
print(f"{rohit.holder_name}'s Balance: {rohit.get_balance()}")

# 6. Transaction History

print("\n--- 6. Transaction history ---")

print(f"\nHistory for {hardik.holder_name}:")
for transaction in hardik.transaction_history:
    print(transaction)

print(f"\nHistory for {rohit.holder_name}:")
for transaction in rohit.transaction_history:
    print(transaction)
