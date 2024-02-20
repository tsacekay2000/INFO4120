import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart_stats = pd.read_csv('streamlit_template/data/kart_stats.csv')

# st.write(df_kart)

# st.dataframe(df_kart_stats)

df_kart = df_kart_stats[['Body', 'Weight', 'Acceleration', 'Ground Speed', 'Water Speed', 'Air Speed']]

st.dataframe(df_kart.style
            .highlight_max(color='Lightgreen', axis=0, subset=['Weight', 'Acceleration', 'Ground Speed', 'Water Speed', 'Air Speed'])
            .highlight_min(color='Red', axis=0, subset=['Weight', 'Acceleration', 'Ground Speed', 'Water Speed', 'Air Speed'])             
)

st.header("Acceleration by Speed Types")
st.line_chart(df_kart, x='Acceleration', y=['Ground Speed', 'Water Speed', 'Air Speed'])

st.header("Data by Body Types")
st.scatter_chart(df_kart, x='Body', y=['Weight', 'Acceleration', 'Ground Speed', 'Water Speed', 'Air Speed'])

st.header("Single Kart Data")
chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['Category', 'row number']).reset_index().drop(columns='row number').rename({0:'Strenght'}, axis=1)
st.bar_chart(df_unp_kart, x='Category', y='Strenght')