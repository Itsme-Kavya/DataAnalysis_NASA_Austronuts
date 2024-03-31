
import pandas as pd

df = pd.read_csv("/Users/kavya/Desktop/MyGit/DataAnalysis/nasa.csv")
df.head(5)
#Counting Null Values
df.isnull().sum()
#Data Cleaning and Filtering Operations.
df.dropna(subset=['Alma_Mater'], how='all', inplace=True)
filtering = df[(df['Death_Mission'].isnull()) & (~df['Death_Date'].isnull())].index
df.drop(filtering, inplace=True)
#datetime format with day-first parsing separately.
df['Birth_Date'] = pd.to_datetime(df['Birth_Date'], dayfirst=True)
df['Death_Date'] = pd.to_datetime(df['Death_Date'], dayfirst=True)
df
#exporting datframe
df.to_csv('astronauts.csv',index= False)
#%load_ext sql

# --- Load your mysql db using credentials from the "DB" area ---
#%sql mysql+pymysql://b003c3f8:Cab#22se@localhost/b003c3f8
