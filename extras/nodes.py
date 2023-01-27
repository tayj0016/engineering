import pandas
import pandas as pd
from operator import itemgetter

# SET CONSTANTS
c1 = 8.5
c2 = 6.99

# poles_num = input("How many poles (2 or 4):")
#
# while poles_num not in (2, 4):
#     poles_num = input("Invalid entry. How many poles (2 or 4): ")
#     poles_num = int(poles_num)
#
# if poles_num == 2:
#     poles = {
#         'poleA': [],
#         'poleB': [],
#     }
# else:
#     poles = {
#         'poleA': [],
#         'poleB': [],
#         'poleC': [],
#         'poleD': [],
#     }

poles = {
    'poleA': [10, 20],
    'poleB': [5, 15],
    'poleC': [4, 30],
    'poleD': [12, 50],
}


# for x in poles:
#     station = input("Input " + x + " station:")
#     station = int(station)
#     poles[x].append(station)
#     offset = input("Input " + x + " offset:")
#     offset = int(offset)
#     poles[x].append(offset)

# FIND LOWEST STATION
low1 = None
low2 = None

# minval = min(poles.values())
# print(minval)
#
# N = 2
# res = sorted(poles.items())
# print(res)
# res = dict(sorted(test_dict.items(), key = itemgetter(1), reverse = True)
# print(res)

i = len(poles)
for x in range(0, len(poles)):
    print(poles[x+1][0])


    # print(poles[x])


# FIND HIGHEST OFFSET

# SET UP NODES WITH [X, Y]
# nodes = {
#     'n1': [1, 2],
#     'n2': [5, 7],
#     'n3': [6, 8],
#     'n4': [2, 4],
#     'n5': [8, 9]
# }

# CALCULATE AND ADD Z TO NODES
# for el in nodes:
#     nodes[el].insert(3, nodes[el][1] * c1)
#
# df = pd.DataFrame.from_dict(nodes, orient='index').reset_index()
# df = df.iloc[:, 1:4]
# df.columns = ['x', 'y', 'z']
# print(df)
# filename = "nodes.csv"
# df.to_csv(filename, index=False)
