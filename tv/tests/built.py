import pandas as pd

ref = pd.read_csv('tvshows.tsv',sep='\t')
wrong = pd.read_csv('wrongTV.tsv',sep='\t')

tsv_filename = 'tvshows.tsv'

data = {'title': [],
        'tconst': [],
        'startYear': []}


# res = []
# res = ref["title"]

num = 1

for name in ref["title"]:
    correctYear = ref.loc[ref['title'] == name, 'startYear'].iloc[0]
    print(correctYear)
    # print(name)
    data['title'].append(name)
    data['startYear'].append(correctYear)
print(data)