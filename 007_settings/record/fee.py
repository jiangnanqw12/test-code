

"""
To calculate the amount needed for an early repayment and the amount for each installment, follow these steps:

1. **Identify Your Loan Details**

   - Principal amount (P) - the original amount of the loan.
   - Annual interest rate (r) - the annual interest rate on the loan.
   - Loan term (t) - the total number of periods (months or years) for the loan.

2. **Calculate Monthly Interest Rate**

   The monthly interest rate can be calculated as:

   \[
   \text{Monthly Interest Rate} = \left(\frac{\text{Annual Interest Rate}}{12}\right)
   \]

3. **Calculate Monthly Installment**

   Using the monthly interest rate, you can calculate the monthly installment using the formula for an installment loan:

   \[
   M = \frac{P \cdot i \cdot (1+i)^n}{(1+i)^n-1}
   \]

   Where:
   - \( M \) is the monthly installment
   - \( P \) is the principal amount
   - \( i \) is the monthly interest rate
   - \( n \) is the number of installments (months)

4. **Calculate Outstanding Balance**

   To calculate the outstanding balance at any point during the loan term, you can use the formula:

   \[
   B = P \cdot \left(1 - \left(\frac{1}{(1+i)^t}\right)\right)
   \]

   Where:
   - \( B \) is the outstanding balance
   - \( P \) is the principal amount
   - \( i \) is the monthly interest rate
   - \( t \) is the number of installments (months) already paid

5. **Calculate Early Repayment Amount**

   The early repayment amount would be the outstanding balance at the point you intend to repay the loan early.

6. **Adjust for any Early Repayment Fees**

   Some loans have fees for early repayment. You would need to add any such fees to the early repayment amount to find the total amount needed for early repayment.

By following these steps, you should be able to find both the amount needed for an early repayment and the amount for each installment. Please consult with a financial advisor or your lender for exact calculations as they might have specific terms and conditions that affect the calculations.
"""

def calculate_loan_details(principal, annual_interest_rate, loan_term, months_paid):
    # Step 2: Calculate monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Step 3: Calculate monthly installment
    monthly_installment = (principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** loan_term)) / (((1 + monthly_interest_rate) ** loan_term) - 1)

    # Step 4: Calculate outstanding balance
    outstanding_balance = principal * ((1 + monthly_interest_rate) ** loan_term - (1 + monthly_interest_rate) ** months_paid) / ((1 + monthly_interest_rate) ** loan_term - 1)

    # Step 5: Print early repayment amount
    early_repayment_amount = outstanding_balance

    return monthly_installment, early_repayment_amount

# Input your loan details here
principal = 450000  # For example, 100,000 as the principal amount
annual_interest_rate = 4.48  # For example, 5% as the annual interest rate
loan_term = 24  # For example, 360 months (30 years) as the loan term
months_paid = 0  # For example, 120 months (10 years) already paid

monthly_installment, early_repayment_amount = calculate_loan_details(principal, annual_interest_rate, loan_term, months_paid)

print(f"The monthly installment amount is: {monthly_installment:.2f}")
print(f"The early repayment amount is: {early_repayment_amount:.2f}")

# Input your loan details here
principal = 200000  # For example, 100,000 as the principal amount
annual_interest_rate = 3.38004  # For example, 5% as the annual interest rate
loan_term = 36  # For example, 360 months (30 years) as the loan term
months_paid = 0  # For example, 120 months (10 years) already paid

monthly_installment, early_repayment_amount = calculate_loan_details(principal, annual_interest_rate, loan_term, months_paid)

print(f"The monthly installment amount is: {monthly_installment:.2f}")
print(f"The early repayment amount is: {early_repayment_amount:.2f}")


# Input your loan details here
principal = 100000  # For example, 100,000 as the principal amount
annual_interest_rate = 10.8  # For example, 5% as the annual interest rate
loan_term = 12  # For example, 360 months (30 years) as the loan term
months_paid = 1  # For example, 120 months (10 years) already paid

monthly_installment, early_repayment_amount = calculate_loan_details(principal, annual_interest_rate, loan_term, months_paid)

print(f"The monthly installment amount is: {monthly_installment:.2f}")
print(f"The early repayment amount is: {early_repayment_amount:.2f}")

# Input your loan details here
principal = 100000  # For example, 100,000 as the principal amount
annual_interest_rate = 10.8  # For example, 5% as the annual interest rate
loan_term = 12  # For example, 360 months (30 years) as the loan term
months_paid = 0  # For example, 120 months (10 years) already paid

monthly_installment, early_repayment_amount = calculate_loan_details(principal, annual_interest_rate, loan_term, months_paid)

print(f"The monthly installment amount is: {monthly_installment:.2f}")
print(f"The early repayment amount is: {early_repayment_amount:.2f}")

# Loan details
principal = 100000
annual_interest_rate = 10.8
loan_term = 12

# Calculate the monthly interest rate
monthly_interest_rate = (annual_interest_rate / 100) / 12

# Calculate the equal principal monthly repayment
equal_principal_monthly_repayment = [((principal / loan_term) + (principal - (principal * (k-1) / loan_term)) * monthly_interest_rate) for k in range(1, loan_term+1)]

# Print each monthly repayment
for month, repayment in enumerate(equal_principal_monthly_repayment, 1):
    print(f"The monthly repayment for month {month} is: {repayment:.2f}")

# Loan details
principal = 100000
annual_interest_rate = 10.8
loan_term = 12

# Calculate the monthly interest rate
monthly_interest_rate = (annual_interest_rate / 100) / 12

# Calculate the equal principal monthly repayment with the adjustment for the first month
equal_principal_monthly_repayment = [
    ((principal / loan_term) + (principal - (principal * (k-1) / loan_term)) * monthly_interest_rate * (33/30) if k == 1 else
     (principal / loan_term) + (principal - (principal * (k-1) / loan_term)) * monthly_interest_rate)
    for k in range(1, loan_term+1)
]

# Print each monthly repayment
for month, repayment in enumerate(equal_principal_monthly_repayment, 1):
    print(f"The monthly repayment for month {month} is: {repayment:.2f}")
