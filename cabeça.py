import streamlit as st
import pandas as pd

st.title('COPA VERA')
st.text('Grupo 1')
tabela = pd.read_excel('Copavera.xlsx',sheet_name="Planilha1")
st.table(tabela)

st.markdown('')
st.markdown('')
tab1, tab2= st.tabs(["ARTILHEIROS","JOGOS"])
with tab1:
    artilhei = pd.read_excel('Copavera.xlsx',sheet_name="Planilha6")
    st.table(artilhei)
with tab2:
    st.image('chave.png')
st.markdown('')
st.markdown('')
st.sidebar.title('gostosa') #mostando o título da barra do lado
st.markdown('')
st.markdown('')

option = st.selectbox(
    'QUAL TIME VOÊ QUER VER',
    ('Rebu','Dinastia','Vera de Munique','Takanelas'))

if option == 'Rebu':
    st.markdown("<h2 style='text-align: center; color: white;'>Rebu FC</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>Time do Segundo Colegial</p>", unsafe_allow_html=True)
    st.markdown('')
    st.markdown('')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="POSIÇÃO", value="4°")
    with col2:
        st.metric(label="GOLS", value="6")
    with col3:
        st.metric(label='SOFRIDOS',value='4')

    df = pd.read_excel('Copavera.xlsx',sheet_name='Planilha3')
    st.table(df)
elif option == 'Dinastia':
    st.text('Ruins')