# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.
My recommender is content-based. It compares each song's attributes to what a user says they like, and doesn't use other users' behavior. It works in two steps: it scores every song, then ranks the scores to pick the top few.

Some prompts to answer:

- What features does each `Song` use in your system

 I chose energy, mood and valence as the main features. Energy splits the 10-song catalog into calm songs and intense songs. Mood groups songs by feel across genres. Valence adds a second dimension that energy doesn't capture, such as telling a moody high-energy song from a happy one.
- What information does your `UserProfile` store

The profile holds the user's target values for the same features:

target_energy, for example 0.40
target_valence, for example 0.60
target_acousticness, for example 0.80
preferred_mood, for example "chill"
preferred_genre, for example "lofi"
It describes the song the user would love, and the recommender looks for songs close to it.
- How does your `Recommender` compute a score for each song

Each song gets a score from 0 to 1 as a weighted sum:

Numeric features (energy, valence, acousticness) are rewarded for being close to the user's target, not for being high or low: closeness = 1 − |song value − target|. A user who wants calm songs (energy 0.4) therefore doesn't get "Gym Hero" (energy 0.93) just because it has more energy.
Categorical features (mood, genre) score 1 if they match the user's preference and 0 if not.
- How do you choose which songs to recommend

A separate ranking step works on the whole list of scores:

Score every song in the catalog against the user profile.
Sort the songs from highest to lowest score.
Break ties with a fixed rule, such as the better energy match first.
Return the top k (for example, 5) songs, and optionally drop any below a minimum score.
I keep scoring and ranking separate because scoring judges one song at a time, while choosing and ordering a shortlist needs all the scores together. This also means I can change one without breaking the other.

You can include a simple diagram or bullet list if helpful.

UserProfile ──┐
              ├─► score each song ──► sort by score ──► top-k list
songs.csv ────┘   (per song)          (whole list)      (recommendations)


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



