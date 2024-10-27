from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    payments = years * 12
    if monthly_rate == 0:  # Handle zero interest rate
        return principal / payments
    monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -payments)
    total_payment = monthly_payment * payments
    total_interest = total_payment - principal
    return monthly_payment, total_payment, total_interest

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        annual_rate = float(request.form['interest_rate'])
        years = int(request.form['loan_term'])
        monthly_payment, total_payment, total_interest = calculate_monthly_payment(principal, annual_rate, years)
        return render_template('index.html', monthly_payment=monthly_payment,
                               total_payment=total_payment,
                               total_interest=total_interest,
                               principal=principal,
                               annual_rate=annual_rate,
                               years=years)

    return render_template('index.html', monthly_payment=None)

if __name__ == '__main__':
    app.run(debug=True)
