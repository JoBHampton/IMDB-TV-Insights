import pandas as pd

# namesList = ['24' ,'30 Rock' ,'60 Minutes' ,'Alfred Hitchcock Presents' ,'Alias' ,'All in the Family' ,'American Idol' ,'The Americans' ,'The Andy Griffith Show' ,'Arrested Development' ,'Atlanta' ,'Band of Brothers' ,'Barry' ,'Battlestar Galactica' ,'Beavis and Butt-Head' ,'Better Call Saul' ,'Boardwalk Empire' ,'The Bob Newhart Show' ,'BoJack Horseman' ,'Breaking Bad' ,'Buffy the Vampire Slayer' ,'The Carol Burnett Show' ,'Chappelle\'s Show' ,'Cheers' ,'Chernobyl' ,'The Colbert Report' ,'Columbo' ,'Community' 
#              ,'The Cosby Show' ,'Curb Your Enthusiasm' ,'The Daily Show' ,'Dallas' ,'Deadwood' ,'Dexter' ,'The Dick Van Dyke Show' ,'Doctor Who','Downton Abbey' ,'The Ed Sullivan Show' ,'ER' ,'Everybody Loves Raymond' ,'Fargo' ,'Fawlty Towers' ,'Firefly' ,'Fleabag' ,'Frasier' ,'Freaks and Geeks' ,'Friday Night Lights' ,'Friends' ,'The Fugitive' ,'Game of Thrones' ,'Gilmore Girls' ,'Girls' ,'The Golden Girls' ,'The Good Place' ,'Good Times' ,'The Good Wife' ,'Grey\'s Anatomy' ,'Gunsmoke' 
#              ,'Hannibal' ,'Happy Days' ,'Hill Street Blues' ,'Homeland' ,'Homicide: Life on the Street' ,'The Honeymooners' ,'I Love Lucy' ,'I May Destroy You' ,'I, Claudius' ,'In Living Color' ,'It\'s Always Sunny in Philadelphia' ,'The Jeffersons' ,'Jeopardy!' ,'Justified' ,'The Larry Sanders Show' ,'Late Night with David Letterman' ,'Law & Order' ,'The Leftovers' ,'Lost' ,'Louie' ,'M*A*S*H' ,'Mad Men' ,'Mary Tyler Moore' ,'Modern Family' ,'Monty Python\'s Flying Circus' ,'Mr. Show with Bob and David' 
#              ,'The Muppet Show' ,'My So-Called Life' ,'Mystery Science Theater 3000' ,'NYPD Blue' ,'The Odd Couple' ,'The Office' ,'The Office' ,'The Oprah Winfrey Show' ,'Oz' ,'Parks and Recreation' ,'Playhouse 90' ,'Prime Suspect' ,'The Prisoner' ,'The Real World' ,'Rick and Morty' ,'The Rockford Files' ,'Roots' ,'Roseanne' ,'Sanford and Son' ,'Saturday Night Live' ,'Seinfeld' ,'Sesame Street' ,'Sex and the City' ,'The Shield' ,'The Simpsons' ,'Six Feet Under' ,'Soap' ,'The Sopranos' ,'South Park' 
#              ,'St. Elsewhere' ,'Star Trek: The Next Generation' ,'Star Trek' ,'Stranger Things' ,'Succession' ,'Survivor' ,'Taxi' ,'Thirtysomething' ,'The Tonight Show Starring Johnny Carson' ,'The Twilight Zone' ,'Twin Peaks' ,'Veep' ,'Watchmen' ,'The West Wing' ,'Will & Grace' ,'The Wire' ,'The Wonder Years' ,'The X-Files' ,'Your Show of Shows']

df = pd.read_csv('title.basics.tsv',sep='\t',dtype={'isAdult':str}, na_values=r"\N", low_memory=False)
ref = pd.read_csv('tvshows.tsv',sep='\t')

tsv_filename = 'listTV.tsv'

data = {'title': [],
        'tconst': [],
        'startYear': []}


# res = []
num = 1

for name in ref["title"]:
    # print(name)
    

    correctYear = ref.loc[ref['title'] == name, 'startYear'].iloc[0]
    
    filtered = df[((df["originalTitle"] == name) | (df["primaryTitle"] == name)) &
            (df["endYear"].notna()) &
            (df["startYear"] == correctYear)]
    
    noEnd =df[((df["originalTitle"] == name) | (df["primaryTitle"] == name)) & 
              ((df["titleType"] == "tvSeries") | (df["titleType"] == "tvMiniSeries"))&
            (df["startYear"] == correctYear)]
    
    if not filtered.empty:
        yearRes = filtered[["startYear"]].iloc[0]['startYear']
        conRes = filtered[["tconst"]].iloc[0]['tconst']
        # res.append(result)
        data["title"].append(name)
        data["tconst"].append(conRes)
        data["startYear"].append(yearRes)
        print(f"{num}: {name} ✅ ")
        num = num + 1
    elif not noEnd.empty:
        yearRes = noEnd[["startYear"]].iloc[0]['startYear']
        conRes = noEnd[["tconst"]].iloc[0]['tconst']
        # res.append(result)
        data["title"].append(name)
        data["tconst"].append(conRes)
        data["startYear"].append(yearRes)
        print(f"{num}: {name} ✅ ")
        num = num + 1
    else:
        print(f"{num}: {name} ❌ ")
        num = num + 1

res = pd.DataFrame(data)
res.to_csv(tsv_filename,sep='\t',index=False)
# print(res)