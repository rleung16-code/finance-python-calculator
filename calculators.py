"""Financial calculation functions for the Finance Python Calculator project."""

def compound_interest(principal: float, annual_rate: float, years: float, compounds_per_year: int = 12) -> float:
    """Calculate future value with periodic compound interest.

    Formula:
        A = P(1 + r/n)^(nt)

    Args:
        principal: Starting amount.
        annual_rate: Annual interest rate as a decimal. Example: 0.05 for 5%.
        years: Number of years.
        compounds_per_year: Number of compounding periods per year.

    Returns:
        Future value.
    """
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    if compounds_per_year <= 0:
        raise ValueError("Compounds per year must be positive.")
    return principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)


def monthly_loan_payment(principal: float, annual_rate: float, years: float) -> float:
    """Calculate monthly loan payment.

    Formula:
        PMT = P * r(1+r)^n / ((1+r)^n - 1)

    Args:
        principal: Loan amount.
        annual_rate: Annual interest rate as a decimal.
        years: Loan term in years.

    Returns:
        Monthly payment.
    """
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    months = int(years * 12)
    if months <= 0:
        raise ValueError("Loan term must be positive.")
    monthly_rate = annual_rate / 12

    if monthly_rate == 0:
        return principal / months

    return principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)


def return_on_investment(initial_value: float, final_value: float) -> float:
    """Calculate return on investment as a decimal.

    Formula:
        ROI = (Final Value - Initial Value) / Initial Value
    """
    if initial_value <= 0:
        raise ValueError("Initial value must be positive.")
    return (final_value - initial_value) / initial_value


def monthly_savings_required(goal_amount: float, current_savings: float, months: int) -> float:
    """Calculate required monthly savings to reach a goal without interest."""
    if months <= 0:
        raise ValueError("Months must be positive.")
    remaining = goal_amount - current_savings
    if remaining <= 0:
        return 0
    return remaining / months
