import streamlit as st
import pandas as pd
import pickle

# Pandas code to get lists of players
wr_df = pd.read_csv("wr_final.csv")

# Stramlit code
st.header('Welcome to Quantitative GM!')

st.header('Enter relevant information on the left to get started')


year = st.sidebar.number_input('Please enter year drafted')

position = st.sidebar.selectbox(
    "Select a position", ("WR", 'RB')
)

# filtering df to only contain relevant columns
wr_df = wr_df[wr_df['Year']==year].copy()


# TODO change this to an if else statement based on position
player_list = wr_df['Player']

player = st.sidebar.selectbox(
    "Select a player of interest", player_list 
)

filtered_df = wr_df[wr_df['Player']==player]
filtered_df = filtered_df.drop(columns=['Unnamed: 0', 'Player', '3 Cone', 'Shuttle', 'Vertical Jump', 'Position', 'PK', 'Year', 'RushAvg'])

wr_pkl = pickle.load(open('wr_pickled_initial.pkl', 'rb'))
# round_drafted = st.sidebar.number_input("Round Drafted",1,7)

# pick_drafted = st.sidebar.number_input("Round Drafted",1)

# team = st.sidebar.selectbox(
#     'Drafting team', ('ARI', 'ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE', 'DAL', 'DEN', 'DET', )
# )