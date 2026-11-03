#Loading the dataset using pandas libarary
import pandas as pd;
df=pd.read_csv('customer_shopping_behavior (1).csv')

# print(df.head())

# df.info()

#summary statics using.describe()

# print(df.describe(include='all'))

# print(df.isnull().sum())
# df['review_rating'] = df.groupby('category')['review_rating'].transform(
#     lambda x: x.fillna(x.median())
# )
# # print(df.isnull().sum())
# print(df.describe(include='all'))

# df.columns=df.columns.str.lower()
# df.columns=df.columns.str.replace('','_')
# # df.columns=df.rename( columns={'purchase_amount(usd)':'purchase_amount'})
# print(df.columns)

# labels=['Young_Adult','Adult','Middle_age','Senior']
# df['age_group']=pd.qcut(df['age'], q=4, labels=labels)
# print(df[['age','age_group']].head(10))
# print(df.head())

#create new column purchase frequency _days
# frequency_maping ={
#     'Fortnightly':14,
#     'Weekly':7,
#     'Monthly':30,
#     'Quarterly':90,
#     'Bi_Weekly':14,
#     'Annually':365,
#     'Every 3 Months':90
# } 
# df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_maping)
# print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))
# print(df.head())

# print(df[['discount_applied','promo_code_used']].head(10))
# print(df.head())
# # print(df.columns)
# print(df.isnull().sum())

from sqlalchemy import create_engine

# engine = create_engine(
#     "postgresql+psycopg2://postgres:NewPassword123@localhost:5432/postgres"
# )
engine = create_engine(
    "postgresql+psycopg2://postgres:NewPassword123@localhost:5432/dataanalysis"
)

try:
    with engine.connect() as connection:
        print("SQLAlchemy connected successfully!")

except Exception as e:
    print("Connection failed:", e)

table_name='customer'
df.to_sql(table_name,engine,if_exists="replace",index=False)
print(f"Data succesfully load into Table 'customer' indatabse 'dataanalysis")