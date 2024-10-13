# Mortgage Calculator Web Application (With features for Swedish Market)

This is a web application built using Django for calculating mortgage payment details, including amortization, interest payments, and tax deductions. The app provides a detailed breakdown of the loan balance and payment details, along with informative charts to help visualize the mortgage situation.

I had need to calculate mortgage payments for me to facilitate my financial choices. Many banks already provide this information but I wanted to have a tool that would allow me to see the impact of different choices on my mortgage easily. I also wanted to have a tool that would allow me to see the impact of reinvesting tax deductions on my mortgage. This is why I decided to build this tool. Such tool, especially if expanded is to facilitate informed financial choices for people who are struggling with deciding what to do with their money.

## Features

- **Mortgage Payment Calculator**: Calculate monthly payments including interest, amortization, and association fees.
- **Tax Deduction Reinvestment Option**: Option to reinvest tax deductions back into the loan to reduce the remaining balance.
- **Visual Analysis**: Interactive charts and tables for easy visualization of the mortgage situation.
- **Yearly and Monthly Breakdown**: Detailed table and yearly summaries.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap, jQuery, Chart.js
- **Database**: PostgreSQL (for deployment)
- **Deployment Tools**: Railway, Render, or PythonAnywhere

## Installation and Setup

### Prerequisites

- **Python 3.8+** installed on your machine.
- **pip**: Package installer for Python.
- **Virtualenv** (optional but recommended).

### Installation Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/mortgage-calculator.git
   cd mortgage-calculator
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file and add the following:

   ```
   DEBUG=True
   SECRET_KEY=your_secret_key_here
   ALLOWED_HOSTS=*
   DATABASE_URL=postgres://user:password@localhost:5432/dbname
   ```

5. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the application**:

   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Deployment

To deploy the application, you can use a platform like **Railway**, **Render**, or **PythonAnywhere**. Make sure to update the settings for production, including setting `DEBUG=False` and properly configuring `ALLOWED_HOSTS` and the database connection.

### Deployment Steps (Railway)

1. **Create a Railway Account** and link your GitHub repository.
2. **Configure environment variables** in Railway.
3. **Deploy** the project. Railway will build and deploy the container for you.

## Usage

1. **Enter Mortgage Details**: Fill in the interest rate, purchase price, deposit, monthly amortization, and association fees.
2. **Calculate**: Click the "Calculate" button to generate a detailed breakdown.
3. **View Results**: See a table with monthly breakdowns, yearly summaries, and visual charts.

## Screenshots

- **Form Page**: Clean form layout to input mortgage details.
- **Results Page**: Detailed summary, informative tables, and charts.

## Requirements

See `requirements.txt` for dependencies.

## Contributing

Feel free to submit pull requests and report issues. Contributions are welcome!

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a pull request.

## Upcoming Features

I'd like to add the following features in the future:
- **Comparison Tool**: Compare different mortgage options side by side. Especially comparing taking out a mortgage to buy a house vs. renting and investing the money instead with expected returns and profits compared to real estate.
- **User Authentication**: Allow users to save mortgage details and compare different scenarios.
- **Slider in the summary**: Allow users to change the mortgage details in the summary box at the top of the results page, to see how the charts and the tables change with slight adjustments to the mortgage details.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.