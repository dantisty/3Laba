from app.finance_calculator import FinanceCalculator


def main():
    calc = FinanceCalculator()

    calc.add_income(100000)
    calc.add_expense(650)
    calc.add_income(500)
    calc.add_expense(300)

    print("= RESULT =")
    print(f"Current balance: {calc.get_balance()}")


if __name__ == "__main__":
    main()
