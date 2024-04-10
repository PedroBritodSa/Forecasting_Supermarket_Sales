import streamlit as st 
import pandas as pd
import numpy as np
from prediction import predict
import altair as alt


st.title("Supermarket Sales Forecasting")
st.markdown("Toy model to play to predic supermarket sales")

st.header("Number of months")

col1 = st.columns(1)

#with col1:
#st.text("Sepal characteristics")
Number_of_months = st.slider("Months", 1, 12, 1, step=1)


st.text('')

if st.button("Predict Sales"):
    result = predict(Number_of_months)
    st.text(result)

    df_forecast = pd.DataFrame({'Date': pd.date_range(start='2023-08-01', periods=Number_of_months, freq='MS'),
                                'Forecasted Sales': result})
    
    chart = alt.Chart(df_forecast).mark_line().encode(
        x='Date',
        y=alt.Y('Forecasted Sales', scale=alt.Scale(domain=(90, 125))),
    ).properties(width=600, height=400)

    st.altair_chart(chart)
