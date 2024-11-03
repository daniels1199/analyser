import streamlit as st
import pandas as pd
import plotly.express as px

def analyse():    
    
    st.set_page_config(
        page_title="Petróleo no Brasil",
        layout="wide"
    )

    st.markdown("<h1 style='text-align: center'>O Petróleo no Brasil<br></h1>", unsafe_allow_html=True)    
    file = "Refinarias.xlsx"
        
    df = pd.read_excel(file, engine="openpyxl")
    st.columns(3)[1].dataframe(df.sort_values("BPD", ignore_index=True, ascending=False), height=250)
        
    soma = df["BPD"].sum()        
    st.columns(3)[1].write(f"#### Capacidade total de barris por dia[BPD]: {soma:,}")
    st.columns(3)[1].write(f"#### Receita mensal aproximada: {(soma*73*30):,} USD")        
        
    bpd_regiao = df.groupby("Região")["BPD"].sum().reset_index()
    bpd_uf = df.groupby("UF")["BPD"].sum().reset_index()
    bpd_nome = df.groupby("Nome")["BPD"].sum().reset_index()        
        
    fig1 = px.bar(bpd_nome, x="BPD", y="Nome", title="Principais Refinarias do Brasil")
    st.columns(3)[1].plotly_chart(fig1.update_yaxes(categoryorder="total ascending"))        
        
    fig2 = px.pie(bpd_uf, values="BPD", names="UF", title="Capacidade por Estado")
    st.columns(3)[1].plotly_chart(fig2)        
        
    fig3 = px.pie(bpd_regiao, values="BPD", names="Região", title="Capacidade por Região")
    st.columns(3)[1].plotly_chart(fig3)      

if __name__ == "__main__":    

    analyse()
    
