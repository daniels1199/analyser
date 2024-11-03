import streamlit as st
import pandas as pd
import plotly.express as px

def analyse():    
    st.title("O Petróleo no Brasil")
    file = st.file_uploader("Escolha o arquivo a ser analisado.",type=["xlsx"])    
    
    if file is not None:
        
        df = pd.read_excel(file, engine="openpyxl")
        st.dataframe(df.sort_values("BPD", ignore_index=True, ascending=False))
        
        soma = df["BPD"].sum()        
        st.write(f"### Capacidade total de barris por dia[BPD]: {soma:,}")
        st.write(f"### Receita mensal aproximada: {(soma*73*30):,} USD")        
        
        bpd_regiao = df.groupby("Região")["BPD"].sum().reset_index()
        bpd_uf = df.groupby("UF")["BPD"].sum().reset_index()
        bpd_nome = df.groupby("Nome")["BPD"].sum().reset_index()        
        
        fig1 = px.bar(bpd_nome, x="BPD", y="Nome", title="Principais Refinarias do Brasil")
        st.plotly_chart(fig1.update_yaxes(categoryorder="total ascending"))        
        
        fig2 = px.pie(bpd_uf, values="BPD", names="UF", title="Capacidade por Estado")
        st.plotly_chart(fig2)        
        
        fig3 = px.pie(bpd_regiao, values="BPD", names="Região", title="Capacidade por Região")
        st.plotly_chart(fig3)      

if __name__ == "__main__":    

    analyse()
    
