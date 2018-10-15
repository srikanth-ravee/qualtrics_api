import pandas as pd
from sqlalchemy import create_engine

engine_gear = create_engine('postgresql://imentor:7yh8uj9ik0ol@10.12.21.17/imentor_production')

connection = engine_gear.connect()

df = pd.read_sql_query('select iu.id as user_id,iue.name from iuser_user as iu left join iuser_employer as iue on iue.id = iu.employer_id left join iuser_persona as ip on iu.id = ip.user_id left join iuser_assignedusertype as iuat on iuat.id = ip.assigned_usertype_id where iuat.usertype_id = 4', con=engine_gear)
#result = connection.execute("select id from iuser_user order by id desc limit 10")



#df["name2"] = [x.strip().replace(' ', '').replace('.', '') for x in df['name'].str.lower()]


df["name2"] = df['name'].astype(str)

#print(df)
#print(df.dtypes)
#print(df["name2"])
df["name3"] = [x.strip().replace(' ', '').replace('.', '').replace("'", '').replace('-', '').replace(';', '').replace(':', '').replace(',', '').replace('&', '') for x in df['name2'].str.lower()]
print(df["name3"])
