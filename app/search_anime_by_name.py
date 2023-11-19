import requests
import json

def search_anime(anime_name):
    url = 'https://graphql.anilist.co'
    query = '''
    query ($name: String) {
      Media (search: $name, type: ANIME) {
        id
        title {
          english
          native
        }
        description
        coverImage {
          extraLarge
          large
          medium
          color
        }
        startDate {
          year
          month
          day
        }
        endDate {
          year
          month
          day
        }
        season
        seasonYear
        episodes
        duration
        format
      }
    }
    '''
    variables = {
        'name': anime_name
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    return response.json()

anime_name = "Naruto"  # replace this with user's search
result = search_anime(anime_name)
print(json.dumps(result, indent=4)) # print the result