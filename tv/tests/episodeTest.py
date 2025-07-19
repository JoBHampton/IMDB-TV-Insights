import pandas as pd

id = 'tt0319931'
episode_data = pd.read_csv('title.episode.tsv', sep='\t')
rating_data = pd.read_csv('title.ratings.tsv',sep='\t')
name_data = pd.read_csv('title.basics.tsv',sep='\t',dtype={'isAdult':str})



tvshow = name_data[name_data["tconst"] == id]
tvshowName = tvshow[["primaryTitle"]].iloc[0]['primaryTitle']
print(tvshowName)

# episode_data.columns = episode_data.columns.str.strip()
# print(episode_data.columns)
mask = episode_data["parentTconst"] == id
episode_list = episode_data.loc[mask, "tconst"]
episode_list = episode_list.tolist()
# print(episode_list)
if(episode_list):
        top_rating = 0.0
        top_id = ''
        top_votes = 0
        rating = ''
        votes = ''
        for episode in episode_list:
            row = rating_data[rating_data["tconst"] == episode]

            result = row[["averageRating","numVotes"]]
            if not result.empty:
                rating = result.iloc[0]['averageRating']
                votes = result.iloc[0]['numVotes']
                # print(f"{episode} {rating} {votes}")

            # print(f"episode: {episode} rating: {rating} votes: {votes}")

                if rating > top_rating:
                    top_rating = rating
                    top_votes = votes
                    top_id = episode
                    # print(f"current top rated episode: {episode}  with a ranking of  {rating}")
                elif rating == top_rating:
                    if votes > top_votes:
                        top_rating = rating
                        top_votes = votes
                        top_id = episode
                        # print(f"current top rated episode: {episode}  with a ranking of  {rating}")


        name = name_data[name_data["tconst"] == top_id]
        name = name[["primaryTitle"]].iloc[0]['primaryTitle']
        row = episode_data[episode_data["tconst"] == top_id]
        result = row[["seasonNumber","episodeNumber"]]
        season = result.iloc[0]["seasonNumber"]
        episode = result.iloc[0]["episodeNumber"]
        print(f"{tvshowName} - (S{season}.E{episode}) - {name}   - {top_rating}/10")
else:
    print(f"oops wrong tconst + {tvshowName}")