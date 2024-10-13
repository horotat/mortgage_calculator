from django import forms

class MortgageForm(forms.Form):
    interest_rate = forms.FloatField(
        label="Interest Rate (%)",
        initial=3.23  # Default value for interest rate
    )
    home_price = forms.FloatField(
        label="Home Purchase Price (SEK)",
        initial=2000000  # Default value for home price
    )
    deposit = forms.FloatField(
        label="Deposit (SEK)",
        initial=600000  # Default value for deposit
    )
    amortisation = forms.FloatField(
        label="Amortisation Amount per Month (SEK)",
        initial=20000  # Default value for amortisation
    )
    association_fee = forms.FloatField(
        label="Association Fees per Month (SEK)",
        initial=4000  # Default value for association fee
    )
    purchase_date = forms.DateField(
        label="Purchase Date",
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
        initial="2025-01-01"  # Default value for purchase date
    )
    reinvest_tax_deduction = forms.BooleanField(
        label="Tax Deduction Value Invested as Loan Payback",
        required=False,
        initial=False  # Default value for checkbox (unchecked)
    )
