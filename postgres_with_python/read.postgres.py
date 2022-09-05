#importing the dependencies
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:Immacula8te@localhost:5432/data.db", pool_recycle=-1)

db_engine = engine.connect()

print("engine created successfully")

# Load Csv file into postgresql from python using the to_sql() function
def query_db(query: str, db_conn: sqlalchemy.engine.base.Connection ) -> pd.DataFrame:
    df = pd.read_sql(query)
    print(df)
    return df

query_db("SELECT * FROM fashion")
df = pd.read_csv("designers.csv")

df.to_sql('fashion', con=engine, if_exists='append', index=False)

print("Done")