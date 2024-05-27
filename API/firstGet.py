from randomuser import RandomUser
import pandas as pd
import requests
import json

r = RandomUser()
data = requests.get("https://fruityvice.com/api/fruit/all")

print("====================================")
print("generate random user")
some_list = r.generate_users(10)
for user in some_list:
    print(user)
print("====================================")
for user in some_list:
    print(f"Name {user.get_full_name()}, Email {user.get_email()}")
print("====================================")
def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({"Name" : user.get_full_name(), "Gender":user.get_gender(), "City":user.get_city(), "State":user.get_state(),"Email":user.get_email()})

    return pd.DataFrame(users)

print(get_users())
print("====================================")
result = json.loads(data.text)
print(pd.DataFrame(result))
print("====================================")
df2 = pd.json_normalize(result)
print(df2)
print("====================================")
cal_banana = df2.loc[df2["name"] == "Banana"]
cal_banana.iloc[0]["nutritions.calories"]
print(cal_banana)
print("====================================")
