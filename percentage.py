import streamlit as st 
import matplotlib.pyplot as plt 
import pandas as pd

st.title("Attendance Percentage Calculator")
def main():
    w_days=st.number_input("Enter Total Days :",value=0)
    a_days=st.number_input("Enter Absent Days :",value=0)
   
    data = {'TotalDays': [w_days],'Present Days':[w_days-a_days], 'AbsentDays': [a_days]}
    df = pd.DataFrame(data)
   

    if st.button("Submit"):
        st.write("Total Days = ",w_days)
        st.write("Present Days = ",w_days-a_days)
        st.write("Absent Days = ",a_days)
        per=(w_days-a_days)/w_days*100
        st.write("Your Total Percentage ",per,"%")
    
        fig, ax = plt.subplots()
        ax.bar(df.columns, df.iloc[0])
        ax.set_ylabel('Total Days')
        st.pyplot(fig)
        
if __name__ == '__main__':
    main()

