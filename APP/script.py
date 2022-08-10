from operator import index
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import geopandas
import folium

@st.cache( allow_output_mutation=True )
def read_csv_file(filename):
    data = pd.read_csv(filename, index_col=0)

    return data

def main():
    st.set_page_config(layout="wide")
    st.title( 'Relatório de Insights da House Rocket' )

    # Primeira Seção
    st.header( 'Relatório #1' )
    st.subheader('Quais os imóveis que a House \
Rocket deveria comprar e por qual preço?')
    filename = f'./report1.csv'

    data = read_csv_file( filename )

    st.dataframe(data)

    # Segunda Seção
    st.header( 'Relatório #2' )
    st.subheader('Uma vez comprados, \
quando será a melhor época para revender e por qual preço?')
    filename = f'./report2.csv'

    data = read_csv_file( filename )

    st.dataframe(data)

    # Terceira Seção
    st.header( 'Validando Hipóteses de Negócio' )


if __name__ == '__main__':
    main()