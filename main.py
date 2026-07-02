from calculators import (
    compound_interest,
    monthly_loan_payment,
    return_on_investment,
    monthly_savings_required,
)


def get_float(prompt: str) -> float:
    """Safely get a number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_int(prompt: str) -> int:
    """Safely get an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def show_menu() -> None:
    print("\nFinance Python Calculator")
    print("1. Compound interest")
    print("2. Monthly loan payment")
    print("3. Return on investment")
    print("4. Savings goal")
    print("5. Exit")


def main() -> None:
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            principal = get_float("Starting amount: ")
            annual_rate = get_float("Annual interest rate (%): ") / 100
            years = get_float("Years: ")
            compounds = get_int("Compounds per year, for example 12: ")
            result = compound_interest(principal, annual_rate, years, compounds)
            print(f"Future value: {result:,.2f}")

        elif choice == "2":
            principal = get_float("Loan amount: ")
            annual_rate = get_float("Annual interest rate (%): ") / 100
            years = get_float("Loan term in years: ")
            result = monthly_loan_payment(principal, annual_rate, years)
            print(f"Monthly payment: {result:,.2f}")

        elif choice == "3":
            initial = get_float("Initial investment value: ")
            final = get_float("Final investment value: ")
            result = return_on_investment(initial, final)
            print(f"ROI: {result * 100:.2f}%")

        elif choice == "4":
            goal = get_float("Goal amount: ")
            current = get_float("Current savings: ")
            months = get_int("Months until goal: ")
            result = monthly_savings_required(goal, current, months)
            print(f"Required monthly savings: {result:,.2f}")

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please choose 1 to 5.")


if __name__ == "__main__":
    main()
