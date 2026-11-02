import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into dicts, converting numeric columns to int/float."""
    print(f"Loading songs from {csv_path}...")

    int_fields = ("id", "tempo_bpm")
    float_fields = ("energy", "valence", "danceability", "acousticness")

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            song = dict(row)
            for field in int_fields:
                song[field] = int(row[field])
            for field in float_fields:
                song[field] = float(row[field])
            songs.append(song)

    print(f"Loaded {len(songs)} songs.")
    return songs

# Weights sum to 1, so a perfect match on every feature scores 1.0.
WEIGHTS = {
    "energy": 0.35,
    "mood": 0.30,
    "valence": 0.20,
    "acousticness": 0.10,
    "genre": 0.05,
}

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences; return (score, list of reasons)."""
    score = 0.0
    reasons: List[str] = []

    # Categorical features: full weight for an exact match, nothing otherwise.
    for feature in ("mood", "genre"):
        target = user_prefs.get(feature)
        if target is None:
            continue
        if song[feature] == target:
            points = WEIGHTS[feature]
            score += points
            reasons.append(f"{feature} match: {target} (+{points:.2f})")

    # Numeric features: reward closeness to the target, not a higher/lower value.
    for feature in ("energy", "valence", "acousticness"):
        target = user_prefs.get(feature)
        if target is None:
            continue
        closeness = 1 - abs(song[feature] - target)
        points = WEIGHTS[feature] * closeness
        score += points
        reasons.append(
            f"{feature} {song[feature]:.2f} vs target {target:.2f} (+{points:.2f})"
        )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k (song, score, explanation) tuples, best score first."""
    scored = (
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    )
    return sorted(scored, key=lambda rec: rec[1], reverse=True)[:k]
