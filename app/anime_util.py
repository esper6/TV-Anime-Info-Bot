import requests

def fetch_anime_info(anime_name, page=1, per_page=20):
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
        coverImage {
                large
                color
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
        "name": anime_name,
        "page": page,
        "perPage": per_page,
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    response.raise_for_status()

    print(response.request.body)  # Print the request body (GraphQL query and variables)
    print(response.json())  # Print the API response

    return response.json()
