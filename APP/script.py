import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st
import folium
import geopandas

from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from streamlit_option_menu import option_menu
from folium.plugins import MarkerCluster
from PIL import Image
from datetime import datetime

st.set_page_config(layout='wide')

st.markdown("<h1 style='text-align: left; color: #5c3934;'><i>Dashboard de Insights da House Rocket</i></h1><hr>", unsafe_allow_html=True)

with st.sidebar:
    # Images used.
    sidebar_icon = Image.open('images/icon_dash.png')
    st.sidebar.image(sidebar_icon)

    st.sidebar.markdown(f"<span style='display: block; color: #5c3934;text-align: center;font-weight: normal;font-size: 1rem;'>{datetime.now().strftime('%d/%m/%Y')}</span>", unsafe_allow_html=True)
    selected = option_menu(menu_title="MENU PRINCIPAL",
            options= ['Página Inicial', 'Insights Gerados', 'Resultados de Negócio'],
            icons=['house','bar-chart', 'calendar2-check'],
            menu_icon='cast',
            default_index = 0,
            orientation='vertical',
            styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "#087888", "font-size": "18px"},
                    "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px",
                                    "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#5c3934"},
                    "menu-title": {"text-align": "center", "color": "#5c3934"}})

def display_home_page(data):
    if selected == 'Página Inicial':
        st.write('Mostrando a Página 1')
    
    return None
        

def display_insights_page(data):
    if selected == 'Insights Gerados':
        st.write('Mostrando a Página 2')

    return None

def display_results_page(data):
    if selected == 'Resultados de Negócio':
        st.write('Mostrando a Página 3')

    return None

def main():
    # Extract


    # Transform


    # Load


    # Criando Páginas do Dashboard
    display_home_page('awe')
    display_insights_page('ewa')
    display_results_page('ew')

if __name__ == "__main__":
    main()