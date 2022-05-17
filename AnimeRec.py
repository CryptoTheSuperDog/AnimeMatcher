from AnilistPython import Anilist
from pprint import pprint

if __name__ == "__main__":

    user_selection = input("What range of episodes are you looking for?: \na) 1-13, \nb) 14-50, \nc) 50-100, \nd) 100+,")
    print(type(user_selection))
    anilist = Anilist()
    animes = anilist.search_anime(score=range(0, 95))

    genres = [
        {'relaxing': ['Comedy', 'Slice of Life']}, 
        {'serious': ['Drama', 'Horror', 'Mecha', 'Mystery', 'Psychological', 'Thriller']},
        {'other': ['Action', 'Adventure', 'Ecchi', 'Fantasy', 'Mahou Shoujo', 'Music', 'Romance', 'Sci-Fi', 'Supernatural', 'Sports']}
    ]

    ranges = {"a": range(1, 14), "b": range(14, 50), "c": range(50, 100), "d": range(100, 9000)}
    results = []

    for elem in animes:
        if(elem['airing_episodes'] != None):
            if(elem['airing_episodes'] in ranges[user_selection]):
                results.append(elem)
                
    # print("SORTED LIST OF ANIMES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sorted_results = sorted(results, key=lambda x: int(x['airing_episodes']))
    # pprint(sorted_results)
