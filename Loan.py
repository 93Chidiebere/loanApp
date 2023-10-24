import pickle
import streamlit as st

brighta = pickle.load(open('loan.pkl', 'rb'))

# Define a function for making prediction
def main():
    # Create Streamlit APP
    st.title('Accion Digital Loan Assessment')

    # Input Variables
    Amount = st.text_input('Amount')
    LoanTenor = st.radio('Tenor', (1, 2, 3, 4))
    Dependents = st.text_input('Dependents')
    Annual_Rent = st.text_input('Annual_Rent')
    ResidenceType = st.radio('residence', ('Rented', 'Permanent'))
    ResidenceYear = st.text_input('Residence_Year')
    LoanReason = st.radio('loan_reason', ('Business', 'Emergency', 'Rent'))
    Are_you_single = st.radio('Single_Status', ('no', 'yes'))

    # Convert radio button selections to 0 or 1
    ResidenceType = 1 if ResidenceType == 'Rented' else 0
    Are_you_single = 1 if Are_you_single == 'yes' else 0
    if LoanReason == 'Business':
        LoanReason = 0
    elif LoanReason == 'Emergency':
        LoanReason = 1
    else:
        LoanReason = 2

    # Create a button to make a prediction
    if st.button('Predict'):
        makeprediction = brighta.predict([[Amount, LoanTenor, Dependents,
                                           Annual_Rent, ResidenceType, ResidenceYear, LoanReason, Are_you_single]])

        output = round(makeprediction[0], 2)
        st.success('You are qualified for {}'.format(output))

if __name__ == '__main__':
    main()




