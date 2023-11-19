import fetch_anime_info
import notify

# List your favourite anime here
favourite_anime = ["One Piece", "Attack on Titan", "Naruto"]

for anime in favourite_anime:
    info = fetch_anime_info.fetch_anime_info(anime)

    try:
        next_episode = info['data']['Media']['nextAiringEpisode']

        # If the next episode airs within the next 24 hours (86400 seconds)
        if next_episode and next_episode['timeUntilAiring'] < 86400:
            subject = f"The next episode of {anime} airs soon!"
            body = f"The next episode of {anime} airs in {next_episode['timeUntilAiring']} seconds!"
            notify.send_email(subject, body, "rollins49@gmail.com")
    except TypeError:
        print(f"It seems that {anime} has finished airing or doesn't exist in AniList!")