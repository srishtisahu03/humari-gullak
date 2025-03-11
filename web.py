import streamlit as st
import matplotlib.pyplot as plt

def calculate_risk_profile():
    st.title('💸 Humari Gullak - Risk Profiling Model')

    # Questions
    questions = [
        ("How many years will you allow your investments to grow?", ['1-2 years', '3-5 years', '6-10 years', 'More than 10 years']),
        ("When are you going to retire?", ['Already Retired', '1-5 years to retire', '6-9 years to retire', '10-15 years to retire', 'More than 15 years to retire']),
        ("What is your planned cash flow in the next 3-5 years?", ['Withdraw money regularly', 'Do nothing', 'Add new money a few times', 'Add sizable new money regularly']),
        ("Beyond your normal contributions & withdrawals, any major withdrawals in next 3-5 years?", ['My entire investments may be required', 'Significant withdrawal expected', 'Minor withdrawals expected', 'No withdrawals foreseen']),
        ("Please select the ideal volatility and return combination you are most comfortable with:", ['8% return, 3-4% possible loss', '8-10% return, 5-7% possible loss', '10-12% return, 8-10% possible loss', '12-15% return, 15-20% possible loss']),
        ("If your portfolio fell 25% in value, what would you do?", ['Sell all units', 'Partially redeem', 'Hold onto units', 'Buy more units']),
        ("If the market sentiment is weak after a recovery, what would you do?", ['Sell all units', 'Sell some units', 'Wait & watch', 'Buy more units']),
        ("How much do you believe in long-term investing principles?", ['No belief', 'Some belief', 'Full belief']),
        ("How do you react to portfolio value changes?", ['Very concerned, check daily', 'Worried, might sell if fall >10%', 'Investments should perform long-term', 'Short-term falls are great buying opportunities']),
        ("How would you select an asset class for investment?", ['Based on past performance', 'Based on partner advice', 'Based on market sentiment', 'Based on fixed return products'])
    ]

    points = 0

    # Form for user inputs
    with st.form("risk_profile_form"):
        for i, (question, options) in enumerate(questions):
            answer = st.radio(f"Q{i+1}. {question}", options)
            points += options.index(answer) + 1

        age = st.number_input("Enter your age:", min_value=18, max_value=100)
        submit = st.form_submit_button("Calculate Risk Profile")

    if submit:
        # Determine risk profile
        if points <= 19:
            risk_profile = 'Conservative'
        elif 20 <= points <= 29:
            risk_profile = 'Moderate'
        else:
            risk_profile = 'Aggressive'

        # Determine equity/debt ratio based on age
        if age <= 30:
            if risk_profile == 'Conservative':
                equity, debt = 70, 30
            elif risk_profile == 'Moderate':
                equity, debt = 80, 20
            else:
                equity, debt = 90, 10
        elif 30 < age <= 45:
            if risk_profile == 'Conservative':
                equity, debt = 60, 40
            elif risk_profile == 'Moderate':
                equity, debt = 70, 30
            else:
                equity, debt = 80, 20
        elif 45 < age <= 55:
            if risk_profile == 'Conservative':
                equity, debt = 50, 50
            elif risk_profile == 'Moderate':
                equity, debt = 60, 40
            else:
                equity, debt = 70, 30
        else:
            if risk_profile == 'Conservative':
                equity, debt = 30, 70
            else:
                equity, debt = 40, 60

        # Display results
        st.write(f"### Your Risk Profile: {risk_profile}")
        st.write(f"### Recommended Investment Distribution:")
        st.write(f"- 📈 Equity: {equity}%")
        st.write(f"- 💵 Debt: {debt}%")

        # Plot Pie Chart
        fig, ax = plt.subplots()
        ax.pie([equity, debt], labels=['Equity', 'Debt'], autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107'])
        ax.axis('equal')
        st.pyplot(fig)

if __name__ == "__main__":
    calculate_risk_profile()