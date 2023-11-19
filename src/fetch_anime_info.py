import requests

def fetch_anime_info(anime_name):
    url = "https://graphql.anilist.co"
    query = """
    query ($name: String) {
      Media (type: ANIME, search: $name) {
        id
        title {
          romaji
          english
          native
        }
        description
        startDate {
          year
          month
          day
        }
        genres
        averageScore
        episodes
        nextAiringEpisode {
          airingAt
          timeUntilAiring
          episode
        }
      }
    }
    """
    variables = {
        'name': anime_name
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    response.raise_for_status()

    return response.json()