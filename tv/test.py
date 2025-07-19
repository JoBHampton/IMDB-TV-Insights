import pandas as pd

df = pd.read_csv('title.basics.tsv',sep='\t',dtype={'isAdult':str}, na_values=r"\N", low_memory=False)


name = 'Succession'
res = []

filtered = df[((df["originalTitle"] == name) | (df["primaryTitle"] == name)) &
            (df["endYear"].notna())]

if not filtered.empty:
    tconst_value = filtered["tconst"].iloc[0]
else:
    tconst_value = None

print(f"{name}: {tconst_value}")





# row = df[df["originalTitle"] == name]
# notOG = df[df["primaryTitle"] == name]

# endyear = df[df["endYear"].notna()]
# print(endyear)
# df.loc[(row & row[["endYear"] != "\\N"])]
# print(f"{row[["endYear"]]} and {row[["tconst"]].iloc[0]['tconst']}")
# print(row[["titleType"]].iloc[0]['titleType'])
# print(row[["tconst"]])

# if (row[["titleType"]].iloc[0]['titleType'] == "tvSeries") or (row[["titleType"]].iloc[0]['titleType'] == "tvMiniSeries"):
#     result = row[["tconst"]].iloc[0]['tconst']
#     res.append(result)
# print(res)
# if(row[["endYear"]] != "\\N") or (notOG[["endYear"]] != "\\N"):
#     result = row[["tconst"]].iloc[0]['tconst']

# if (row[["titleType"]].iloc[0]['titleType'] == "tvSeries") or (row[["titleType"]].iloc[0]['titleType'] == "tvMiniSeries"):
#     result = row[["tconst"]].iloc[0]['tconst']
#     res.append(result)
# elif (notOG[["titleType"]].iloc[0]['titleType'] == "tvSeries") or (notOG[["titleType"]].iloc[0]['titleType'] == "tvMiniSeries"):
#     result = notOG[["tconst"]].iloc[0]['tconst']
#     res.append(result)
# else:
#     print(f"whoops")
   

print(res)