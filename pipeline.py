import pandas as pd
from luigi import Task, LocalTarget
import requests
from bs4 import BeautifulSoup as BS
import datetime

# setting the year
year = datetime.date.today().year

# creating a script to run post draft to update information
def get_rec_data(year):
    """Creating a function to scrape receiving data"""
    pd.set_option('display.max_columns', None)
    # setting the url
    URL = f'https://www.sports-reference.com/cfb/years/{year}-receiving.html'
    # saving the url as a variable
    res = requests.get(URL)
    # creating a beautifulSoup object
    soup = BS(res.content, 'html.parser')
    # locate table of interest
    table = soup.find(class_="sortable stats_table", id='receiving')
    # read data into a datafrae
    df_rec = pd.read_html(str(table))[0]
    # rename columns
    df_rec.columns = ['Rk', 'Player', 'School', 'Conf', 'G', 'Rec', 'RecYds', 'RecAvg', 'RecTD', 'RushAtt', 'RushYds', 'RushAvg', 'RushTD', 'Plays', 'TotalYds', 'YardsPerPlay', 'TotalTDs']
    # remove blank rows
    df_rec = df_rec.loc[df_rec['Conf']!='Conf']
    # remove the * that's next to several player names
    df_rec['Player'] = df_rec['Player'].apply(lambda x: x.split('*')[0].strip())
    # save data to csv
    df_rec.to_csv(f'receiving/{year}.csv', index=False)
    return "Data successfully saved"

def get_passing_data(year):
    """Creating a function to scrape passing data"""
    pd.set_option('display.max_columns', None)
    # setting the url
    URL = f'https://www.sports-reference.com/cfb/years/{year}-passing.html'
    # saving the url as a variable
    res = requests.get(URL)
    # creating a beautifulSoup object
    soup = BS(res.content, 'html.parser')
    # locate table of interest
    table = soup.find(class_="sortable stats_table", id='passing')
    # read data into a datafrae
    df_pass = pd.read_html(str(table))[0]
    # rename columns
    df_pass.columns = ['Rk', 'Player', 'School', 'Conf', 'G', 'Completions', 'Attempts', 'CompletionPCT', 'PassYds', 'YardsPerAttempt',
                  'AdjustedYardsPerAttempt', 'PassingTDs', 'Int', 'EfficiencyRtg', 'RushAtt', 'RushYds', 'RushAvg', 'RushTD']
    # remove blank rows
    df_pass = df_pass.loc[df_pass['Conf']!='Conf']
    # remove the * that's next to several player names
    df_pass['Player'] = df_pass['Player'].apply(lambda x: x.split('*')[0].strip())
    # save data to csv
    df_pass.to_csv(f'passing/{year}.csv', index=False)
    return "Data successfully saved"

def get_rush_data(year):
    """Creating a function to scrape receiving data"""
    pd.set_option('display.max_columns', None)
    # setting the url
    URL = f'https://www.sports-reference.com/cfb/years/{year}-rushing.html'
    # saving the url as a variable
    res = requests.get(URL)
    # creating a beautifulSoup object
    soup = BS(res.content, 'html.parser')
    # locate table of interest
    table = soup.find(class_="sortable stats_table", id='rushing')
    # read data into a datafrae
    df_rush = pd.read_html(str(table))[0]
    # rename columns
    df_rush.columns = ['Rk', 'Player', 'School', 'Conf', 'G', 'RushAtt', 'RushYds', 'RushAvg', 'RushTD', 'Rec', 'RecYds', 'RecAvg', 'RecTD', 'Plays', 'TotalYds', 'YardsPerPlay', 'TotalTDs']
    # remove blank rows
    df_rush = df_rush.loc[df['Conf']!='Conf']
    # remove the * that's next to several player names
    df_rush['Player'] = df_rush['Player'].apply(lambda x: x.split('*')[0].strip())
    # save data to csv
    df_rush.to_csv(f'rushing/{year}.csv', index=False)
    return "Data successfully saved"

def get_draft_data(year):
    """Takes in year and returns draft data"""
    pd.set_option('display.max_columns', None)
    # setting the url
    URL = f'https://www.pro-football-reference.com/years/{year}/draft.htm'
    # saving the url as a variable
    res = requests.get(URL)
    # creating a beautifulSoup object
    soup = BS(res.content, 'html.parser')
    # locate table of interest
    table = soup.find(class_="sortable stats_table", id='drafts')
    # read data into a datafrae
    df_draft = pd.read_html(str(table))[0]
    # rename columns
    df_draft.columns = ['Round', 'Pick', 'Team', 'Player', 'Position', 'Age', 'To', 'AP1', 'PB', 'St', 'wAV', 'DrAV','G', 'Cmp', 'PassAtt',
                'PassYds', 'PassTD', 'Int', 'RushAtt', 'RushYds', 'RushTD', 'Rec', 'RecYds', 'RecTD', 'Solo', 'Int', 'Sk', 'School', 'Unnamed: 28_level_1']

    # remove blank rows
    df_draft = df_draft.loc[df_draft['Player']!='Player']
    # filtering to only positions of interest
    # df1 = df1[(df1['Player']=='QB') or (df1['Player']=='WR') or (df1['Player']=='RB') or (df1['Player']=='TE')].copy() 
    # select only relevant columns
    df_draft = df_draft[['Round', 'Pick', 'Team', 'Player', 'Position', 'Age', 'School']].copy()
    # remove the * that's next to several player names
    df_draft['Player'] = df_draft['Player'].apply(lambda x: x.split('*')[0].strip())
        # save data to csv
    df_draft.to_csv(f'draft_data/{year}.csv', index=False)
    print('success')

def get_combine_data(year):
    """Takes in year and returns combine data"""
    pd.set_option('display.max_columns', None)
    # setting the url
    URL = f'https://www.pro-football-reference.com/draft/{year}-combine.htm'
    # saving the url as a variable
    res = requests.get(URL)
    # creating a beautifulSoup object
    soup = BS(res.content, 'html.parser')
    # locate table of interest
    table = soup.find(class_="sortable stats_table", id='combine')
    # read data into a datafrae
    df_combine = pd.read_html(str(table))[0]
    # rename columns
    df_combine.columns = ['Player', 'Position', 'School', 'College', 'Height', 'Weight', '40 Time', 'Vertical Jump', 'Bench', 'Broad Jump', '3 Cone', 'Shuttle', 'Drafted']
    # remove blank rows
    df_combine = df_combine.loc[df_combine['Player']!='Player']
    # filtering to only positions of interest
    # df1 = df1[(df1['Player']=='QB') or (df1['Player']=='WR') or (df1['Player']=='RB') or (df1['Player']=='TE')].copy() 
    # select only relevant columns
    df_combine = df_combine[df_combine['Drafted'].notnull()].copy()
    # remove the * that's next to several player names
    df_combine['Player'] = df_combine['Player'].apply(lambda x: x.split('*')[0].strip())
    # save data to csv
    df_combine.to_csv(f'combine_data/{year}.csv', index=False)
    print('success')

# reading in the draft data
draft_data = pd.read_csv(f'draft_data/{year}.csv')
draft_data['Year'] = year

# reading in the combine data
combine_data = pd.read_csv(f'combine_data/{year}.csv')
combine_data['Year'] = year

# reading in receiving, rushing, and passing data
receiving_data = pd.read_csv(f'receiving/{year}')
rushing_data = pd.read_csv(f'rushing/{year}')
passing_data = pd.read_csv(f'passing/{year}')

# setting the year column
receiving_data['Year'] = year
rushing_data['Year'] = year
passing_data['Year'] = year

def clean_combine(combine_full, position):
    """Function for cleaning scraped combine data"""
    combine_full = combine_full[combine_full['Position']==f'{position}']
    combine_full = combine_full[combine_full['Year'].notna()].copy()
    combine_full = combine_full.reset_index(drop=True)
    combine_full['Year'] = combine_full['Year'].astype(int)
    combine_full['Year'] = combine_full['Year'].astype(str)
    combine_full['Player'] = combine_full['Player'].str.lower()
    combine_full['Drafted'] = combine_full['Drafted'].str.split("/")
    combine_full['Round'] = combine_full['Drafted'].str[1]
    combine_full['Pick'] = combine_full['Drafted'].str[2]
    combine_full['Pick'] = combine_full['Pick'].str.replace("th pick","")
    combine_full['Pick'] = combine_full['Pick'].str.replace("rd pick","")
    combine_full['Pick'] = combine_full['Pick'].str.replace("nd pick","")
    combine_full['Pick'] = combine_full['Pick'].str.replace("st pick","")

    combine_full['Round'] = combine_full['Round'].str.replace("th","")
    combine_full['Round'] = combine_full['Round'].str.replace("rd","")
    combine_full['Round'] = combine_full['Round'].str.replace("nd","")
    combine_full['Round'] = combine_full['Round'].str.replace("st","")

    combine_full['Pick'] = combine_full['Pick'].astype('int32')
    combine_full['Round'] = combine_full['Round'].astype('int32')
    # converting height to inches
    combine_full = combine_full[combine_full['Height'].notnull()]
    combine_full['Height'] = combine_full['Height'].str.split("-")
    combine_full['Feet'] = combine_full['Height'].str[0]
    combine_full['Inches'] = combine_full['Height'].str[1]
    combine_full['Feet'] = combine_full['Feet'].astype('int')
    combine_full['Inches'] = combine_full['Inches'].astype('int')
    combine_full['Height (in)'] = combine_full['Feet']*12 + combine_full['Inches']

    combine_full = combine_full.drop(columns=['College', 'Height', 'Bench', 'Broad Jump', 'Drafted', 'Feet', 'Inches'])
    
    return combine_full

wr_combine = clean_combine(combine_data, 'WR')
rb_combine = clean_combine(combine_data, 'RB')
qb_combine = clean_combine(combine_data, 'QB')

def combine_draft_and_combine(df1, df2):
    """Function for combining the draft order and combine data df1 refers to the draft dataframe, df2 is combine"""
    df1 = df1[df1['Position']=='WR']
    a = df1.merge(df2, how='left', on='Pick')
    a = a.drop(columns=['Player_y', 'Position_y','School_y','Year_y', 'Round_y'])
    a.columns = ['Round', 'Pick', 'Team', 'Player', 'Position', 'Age', 'School', 'Year', 'Weight', '40 Time', 'Vertical Jump', '3 Cone', 'Shuttle', 'Height (in)']
    a['Year'] = a['Year'].astype(str)
    a['PK'] = a['Player'] + "+" + a['Year']
    a['PK'] = a['PK'].str.lower()
    return a

wrpt1 = combine_draft_and_combine(draft_data, wr_combine)
rbpt1 = combine_draft_and_combine(draft_data, rb_combine)
qbpt1 = combine_draft_and_combine(draft_data, qb_combine)



def get_final_df(df1, df2):
    """function for getting the final dataframe. df1 refers to combine and draft, df2 is stats"""
    a = df1.merge(df2[['G', 'Rec', 'RecYds', 'RecAvg', 'RecTD', 'RushAtt', 'RushYds', 'RushAvg', 'RushTD', 'Plays', 'TotalYds', 'YardsPerPlay', 'TotalTDs', 'YPG', 'Conf',"PK"]], on='PK', how='left')
    return a

wr_final = get_final_df(wrpt1, receiving_data)
rb_final = get_final_df(rbpt1, rushing_data)
qb_final = get_final_df(qbpt1, receiving_data)