from catboost import CatBoostClassifier, Pool
import streamlit as st
import pandas as pd
import pickle

# Pandas code to get lists of players
wr_df = pd.read_csv("wr_final.csv")
rb_df = pd.read_csv("rb_final1.csv")
# TODO fix qb df to include year column
qb_df = pd.read_csv("qb_final1.csv")

# Stramlit code
st.header('Welcome to Quantitative GM!')

st.header('Enter relevant information on the left to get started')


year = st.sidebar.number_input('Please enter year drafted', min_value=1993,max_value=2022, value=2022,step=1)

position = st.sidebar.selectbox(
    "Select a position", ("WR", 'RB', 'QB')
)

# filtering dfs to only contain relevant columns and remove missing values
wr_df = wr_df[(wr_df['Year']==year)&(wr_df['Rec'].notna())].copy()
rb_df = rb_df[(rb_df['Year']==year)&(rb_df['RushYds'].notna())].copy()
qb_df = qb_df[(qb_df['Year']==year)&(qb_df['PassYds'].notna())].copy()

# setting player list 
if position == 'WR':
    player_list = wr_df['Player']
elif position == 'RB':
    player_list = rb_df['Player']
elif position == 'QB':
    player_list = qb_df['Player']

player = st.sidebar.selectbox(
    "Select a player of interest", player_list 
)

# loading data and model
if position == 'WR':
    filtered_df = wr_df[wr_df['Player']==player]
    filtered_df = filtered_df.drop(columns=['Unnamed: 0', 'Player', '3 Cone', 'Shuttle', 'Vertical Jump', 'Position', 'PK', 'Year', 'RushAvg'])
    model = pickle.load(open('wr_pickled_initial.pkl', 'rb'))
elif position == 'RB':
    filtered_df = rb_df[rb_df['Player']==player]
    filtered_df = filtered_df.drop(columns=['Unnamed: 0', 'Player', '3 Cone', 'Shuttle', 'Vertical Jump', 'Position', 'PK', 'Year'])    
    model = pickle.load(open('rb_pickled_initial.pkl', 'rb'))
else:
    filtered_df = qb_df[qb_df['Player']==player]
    filtered_df = filtered_df.drop(columns=['Player', 'Unnamed: 0', '3 Cone', 'Shuttle', 'Vertical Jump', 'Position', 'PK', 'PK1', 'Year', 'Year_y', 'Last_Year', 'year_drafted', 'AdjustedYds'])
    model = pickle.load(open('qb_pickled_initial.pkl', 'rb'))

# loading pkl model
# wr_pkl = pickle.load(open('wr_pickled_initial.pkl', 'rb'))
# rb_pkl = pickle.load(open('rb_pickled_initial.pkl', 'rb'))

cbpool = Pool(filtered_df, cat_features=['Team', 'School', 'Conf'])

if st.button("Predict"):
    data = model.predict_proba(cbpool)
    result = model.predict(cbpool)
    if result[0]==1:
        st.write('This player should become a superstar')
    elif result[0] == 2:
        st.write('This player should become an above average starter')
    elif result[0] == 3:
        st.write('This player should become a low level starter or backup')
    else:
        st.write('This player will probably become a low level backup or not play')
    # st.write(result[0])
    st.write(pd.DataFrame({
        "Chance of being a superstar": [data[0][0]],
        "Chance of being a star": [data[0][1]],
        "Chance of starting": [data[0][2]],
        "Chance of being a dud": [data[0][3]]
    }))
    st.write("Player Info")
    st.write(filtered_df.drop(columns='response'))