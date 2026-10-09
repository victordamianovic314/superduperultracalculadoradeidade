

import streamlit as st
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

min_date = datetime.date(1950, 1, 1)
max_date= datetime.date(2030,1,1)
st.sidebar.write("Digite sua data de nacimento")
hoje= date.today()
nascimento= st.sidebar.date_input("Data",value= None, min_value = min_date,max_value=max_date)

idade =relativedelta(hoje, nascimento)
botao=st.sidebar.button("calcular")
if botao:
    if idade.years <0 or (idade.years==0 and idade.months<0) or(idade.years==0 and idade.months==0 and idade.days <0):
        st.write("bem vindo viajante do tempo")
    else:

        st.write("sua idade idade é:", idade.years, "anos")


