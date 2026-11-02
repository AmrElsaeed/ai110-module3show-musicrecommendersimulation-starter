"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


WIDTH = 60


def print_recommendations(user_prefs: dict, recommendations: list) -> None:
    """Print each recommendation as a card: title, score, then one line per reason."""
    profile = ", ".join(f"{key}={value}" for key, value in user_prefs.items())

    print()
    print("=" * WIDTH)
    print("TOP RECOMMENDATIONS".center(WIDTH))
    print(f"Profile: {profile}".center(WIDTH))
    print("=" * WIDTH)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        bar = "#" * round(score * 20)
        print(f"\n#{rank}  {song['title']} - {song['artist']}")
        print(f"    Score: {score:.2f} / 1.00  [{bar:<20}]")
        print("    Reasons:")
        for reason in explanation.split("; "):
            print(f"      * {reason}")
        print("-" * WIDTH)
    print()


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print_recommendations(user_prefs, recommendations)


if __name__ == "__main__":
    main()
