import pandas
import pandas as pd
from operator import itemgetter

poles_num = input("How many poles (2 or 4): ")
poles_num = int(poles_num)

while poles_num not in (2, 4):
    poles_num = input("Invalid entry. How many poles (2 or 4): ")
    poles_num = int(poles_num)

if poles_num == 2:
    poleA = ['poleA']
    poleB = ['poleB']
    poles = [poleA, poleB]
else:
    poleA = ['poleA']
    poleB = ['poleB']
    poleC = ['poleC']
    poleD = ['poleD']
    poles = [poleA, poleB, poleC, poleD]

i = 0
for x in poles:
    sta = input("Enter a station for POLE " + poles[i][0] + " ")
    off = input("Enter a offset for POLE " + poles[i][0] + " ")
    x.append(sta)
    x.append(off)
    i += 1

# TESTING VARIABLES
# poles_num = 4
# poleA = ['poleA', 30, 20]
# poleB = ['poleB', 45, 25]
# poleC = ['poleC', 25, 15]
# poleD = ['poleD', 50, 20]
# poles = [poleA, poleB, poleC, poleD]

# FIND THE LOWEST STATION
print(poles)
poles.sort(key=itemgetter(1))
print(poles)

if poles[0][2] < poles[1][2]:
    set_pole = poles[0]
elif poles[1][2] < poles[0][2]:
    set_pole = poles[1]

try:
    print("the set pole is " + set_pole[0])
except:
    print("Cannot find set pole")

# FIND ORIGIN
origin = ['origin']

# EXPORT TO DATAFRAME
# df = pd.DataFrame.from_dict(nodes, orient='index').reset_index()
# df = df.iloc[:, 1:4]
# df.columns = ['x', 'y', 'z']
# print(df)
# filename = "nodes.csv"
# df.to_csv(filename, index=False)
