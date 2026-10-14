"""Synthetic dataset of Brazilian clients for personal finance analysis.
 
Generates NUM_CLIENTS fictional clients using Faker and random distributions,
then saves the result as a CSV file (semicolon separated, comma as decimal mark).
"""
 
import random
 
import pandas as pd
from faker import Faker
 
SEED = 42
NUM_CLIENTS = 500
MIN_INCOME = 1621  # lower bound of the income range (BRL)
MAX_INCOME = 30000  # upper bound of the income range (BRL)
EMPLOYMENT_TYPE = "CLT"
OUTPUT_FILE = "finhealth_data.csv"
 
fake = Faker("pt_BR")
 
def generate_income():
    """Pick an income band (low, middle, high) and draw an income inside it."""
    band = random.choices(["low", "middle", "high"], weights=[50, 35, 15])[0]
    if band == "low":
        return round(random.uniform(MIN_INCOME, 3500), 2)
    if band == "middle":
        return round(random.uniform(3500, 10000), 2)
    return round(random.uniform(10000, MAX_INCOME), 2)
 
def private_pension_probability(income):
    """Higher income means a higher chance of having a private pension plan."""
    if income > 20000:
        return 0.80
    if income > 10000:
        return 0.45
    return 0.15
 
def generate_client(client_id):
    """Generate one fictional client as a dictionary (one row of the dataset)."""
    income = generate_income()
    age = fake.random_int(min=18, max=70)
 
    # Monthly expenses, as a share of income
    fixed_expenses = round(income * random.uniform(0.30, 0.50), 2)
    food_expenses = round(income * random.uniform(0.10, 0.25), 2)
    leisure_expenses = round(income * random.uniform(0.05, 0.20), 2)
    health_expenses = round(income * random.uniform(0.02, 0.10), 2)
    total_expenses = round(
        fixed_expenses + food_expenses + leisure_expenses + health_expenses, 2
    )
    expenses_pct_income = round(total_expenses / income * 100, 1)
 
    marital_status = random.choices(
        ["single", "married", "divorced", "widowed"], weights=[45, 40, 12, 3]
    )[0]
    years_employed = random.randint(0, min(30, age - 18))
 
    # Debt
    total_debt = round(random.uniform(income * 0.01, income * 3), 2)
    monthly_debt_payment = round(total_debt * random.uniform(0.02, 0.08), 2)
    monthly_debt_payment_pct_income = round(monthly_debt_payment / income * 100, 1)
    total_debt_pct_income = round(total_debt / income * 100, 1)
 
    # Emergency fund: longer employment makes it more likely
    emergency_fund_probability = min(0.20 + years_employed * 0.02, 0.80)
    has_emergency_fund = random.random() < emergency_fund_probability
    emergency_fund_months = random.randint(1, 12) if has_emergency_fund else 0
    emergency_fund_value = round(emergency_fund_months * total_expenses, 2)
 
    # Private pension
    has_private_pension = random.random() < private_pension_probability(income)
    private_pension_contribution = (
        round(income * random.uniform(0.05, 0.15), 2) if has_private_pension else 0
    )
 
    # Financial products
    has_credit_card = random.choices([True, False], weights=[60, 40])[0]
    has_investments = random.choices([True, False], weights=[25, 75])[0]
    has_credit_limit = random.choices([True, False], weights=[40, 60])[0]
 
    investment_value = (
        round(random.uniform(500, income * 24), 2) if has_investments else 0
    )
    credit_limit = (
        round(income * random.uniform(1, 3), 2) if has_credit_limit else 0
    )
 
    return {
        "id": client_id,
        "age": age,
        "employment_type": EMPLOYMENT_TYPE,
        "marital_status": marital_status,
        "state": fake.state(),
        "years_employed": years_employed,
        "income": income,
        "fixed_expenses": fixed_expenses,
        "food_expenses": food_expenses,
        "leisure_expenses": leisure_expenses,
        "health_expenses": health_expenses,
        "total_expenses": total_expenses,
        "expenses_pct_income": expenses_pct_income,
        "total_debt": total_debt,
        "total_debt_pct_income": total_debt_pct_income,
        "monthly_debt_payment": monthly_debt_payment,
        "monthly_debt_payment_pct_income": monthly_debt_payment_pct_income,
        "has_emergency_fund": has_emergency_fund,
        "emergency_fund_months": emergency_fund_months,
        "emergency_fund_value": emergency_fund_value,
        "has_credit_card": has_credit_card,
        "has_investments": has_investments,
        "investment_value": investment_value,
        "has_private_pension": has_private_pension,
        "private_pension_contribution": private_pension_contribution,
        "has_credit_limit": has_credit_limit,
        "credit_limit": credit_limit,
    }
 
def main():
    random.seed(SEED)
    Faker.seed(SEED)
 
    clients = [generate_client(client_id) for client_id in range(1, NUM_CLIENTS + 1)]
    df = pd.DataFrame(clients)
 
    print(df.head())
    print(f"\nDataset generated: {len(df)} clients")
    print(f"Columns: {list(df.columns)}")
 
    # utf-8-sig keeps accented state names readable when opened in Excel
    df.to_csv(OUTPUT_FILE, index=False, sep=";", decimal=",", encoding="utf-8-sig")
 
if __name__ == "__main__":
    main()
 