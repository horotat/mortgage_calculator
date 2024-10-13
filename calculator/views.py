import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI rendering

from django.shortcuts import render
from .forms import MortgageForm
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime, timedelta

def calculate_tax_deduction(interest_paid):
    deduction = 0
    if interest_paid <= 100000:
        deduction = 0.30 * interest_paid
    else:
        deduction = 0.30 * 100000 + 0.21 * (interest_paid - 100000)
    return deduction

def mortgage_view(request):
    if request.method == 'POST':
        form = MortgageForm(request.POST)
        if form.is_valid():
            interest_rate = form.cleaned_data['interest_rate'] / 100
            home_price = form.cleaned_data['home_price']
            deposit = form.cleaned_data['deposit']
            amortisation = form.cleaned_data['amortisation']
            association_fee = form.cleaned_data['association_fee']
            purchase_date = form.cleaned_data['purchase_date']
            reinvest_tax_deduction = form.cleaned_data['reinvest_tax_deduction']
            
            loan_amount = home_price - deposit
            current_date = purchase_date

            data = []

            while loan_amount > 0:
                monthly_interest_payment = loan_amount * (interest_rate / 12)
                monthly_payment = amortisation + monthly_interest_payment + association_fee
                data.append({
                    'date': current_date.strftime('%B %Y'),
                    'year': current_date.year,
                    'remaining_loan': max(0, loan_amount),
                    'interest_payment': monthly_interest_payment,
                    'monthly_payment': monthly_payment
                })
                loan_amount -= amortisation
                current_date += timedelta(days=30)

            df = pd.DataFrame(data)

            # Group by year and calculate the summary values
            df_summary = df.groupby('year').agg(
                total_interest_payment=('interest_payment', 'sum'),
                average_monthly_interest=('interest_payment', 'mean'),
                average_monthly_payment_total=('monthly_payment', 'mean'),
                remaining_loan_value_start=('remaining_loan', 'first')
            ).reset_index()

            # Apply tax deduction if reinvestment option is selected
            if reinvest_tax_deduction:
                for index, row in df_summary.iterrows():
                    tax_deduction = calculate_tax_deduction(row['total_interest_payment'])
                    # Reduce the remaining loan value by the tax deduction
                    df_summary.at[index, 'remaining_loan_value_start'] -= tax_deduction

                    # Recalculate interest and monthly payments
                    new_loan_amount = df_summary.at[index, 'remaining_loan_value_start']
                    df_summary.at[index, 'total_interest_payment'] = 0
                    for month in range(12):
                        monthly_interest = new_loan_amount * (interest_rate / 12)
                        df_summary.at[index, 'total_interest_payment'] += monthly_interest
                        new_loan_amount -= amortisation
                    df_summary.at[index, 'average_monthly_interest'] = df_summary.at[index, 'total_interest_payment'] / 12
                    df_summary.at[index, 'average_monthly_payment_total'] = (
                        df_summary.at[index, 'total_interest_payment'] / 12 + amortisation + association_fee
                    )

            # Calculate the total interest paid after any tax deduction
            total_interest_paid_after_tax = df_summary['total_interest_payment'].sum()

            # Convert the DataFrames to dictionaries for easier rendering in the template
            df_dict = df.to_dict(orient='records')
            df_summary_dict = df_summary.to_dict(orient='records')

            # Data for JavaScript (chart.js)
            chart_data = {
                'years': df_summary['year'].tolist(),
                'remaining_loan_values': df_summary['remaining_loan_value_start'].tolist(),
                'total_interest_payments': df_summary['total_interest_payment'].tolist(),
            }

            return render(request, 'calculator/results.html', {
                'form': form,
                'table_data': df_dict,
                'summary_table_data': df_summary_dict,
                'chart_data': chart_data,
                'total_purchase_price': home_price,
                'loan_value': home_price - deposit,
                'deposit': deposit,
                'monthly_amortisation': amortisation,
                'monthly_association_fee': association_fee,
                'start_date': purchase_date.strftime("%B %Y"),
                'end_date': current_date.strftime("%B %Y"),
                'total_interest_paid_after_tax': total_interest_paid_after_tax
            })
    else:
        form = MortgageForm()

    return render(request, 'calculator/mortgage_form.html', {'form': form})
