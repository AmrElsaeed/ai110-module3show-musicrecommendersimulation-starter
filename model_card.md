# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**

---

## 2. Intended Use  

VibeMatch suggests songs from a small catalog. It picks songs that match a user's taste.

- It gives a top 5 list with a reason for each song.
- It assumes the user can describe their taste. They give a favorite mood, a favorite genre, and a target energy level.
- It assumes taste stays the same. It does not change with time of day or activity.
- It is for classroom learning. It is not for real users.

---

## 3. How the Model Works  

The model compares each song to what the user likes. Closer songs get higher scores.

Each song has these traits:

- Genre, like pop or lofi
- Mood, like chill or happy
- Energy, from calm to intense
- Valence, which is how positive the song sounds
- Acousticness, which is how organic the song sounds

The user gives a target for each trait. They can skip any trait.

The score works like this:

- For energy, valence, and acousticness, closer is better. A song far from the target loses points. This works in both directions. A calm fan does not get a high-energy song just because it has "more" energy.
- For mood and genre, a match earns a bonus. No match earns nothing.
- Each trait has a weight. Energy counts most. Mood is next. Genre counts least.

The model scores every song and sorts them. It shows the top few. Each song comes with the reasons for its score.

Changes from the starter:

- I filled in the empty starter code.
- I wrote a scoring rule that rewards closeness.
- I made the score explain itself.

---

## 4. Data  

- The catalog has 19 songs in `songs.csv`.
- The starter file had 10 songs. I added 9 more.
- Genres include pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip hop, classical, country, metal, r&b, reggae, edm, blues, and folk.
- Moods include happy, chill, intense, relaxed, moody, focused, confident, melancholic, nostalgic, angry, romantic, laid-back, euphoric, gritty, and hopeful.
- Most genres have only one song.
- Missing parts of taste: lyrics, language, artist fame, decade, and many world genres. There is no data on how people actually listen.

---

## 5. Strengths  

- It works well when the user's tastes agree. A "rock, intense, high energy" user gets Storm Runner, Gym Hero, and Iron Requiem. That feels right.
- A "lofi, chill, calm" user gets Library Rain, Midnight Coding, and Spacewalk Thoughts. That also feels right.
- It keeps calm songs away from intense fans, and the other way around.
- The reasons are easy to read. You can see why a song ranked high.
- It adds up simple parts. That makes it easy to debug and tune.

---

## 6. Limitations and Bias 

- The catalog is tiny. Most songs have no close neighbor. The top results can be "closest available" and not a true match.
- Mood must match exactly. "Sad" does not match "melancholic". A "sad, quiet" user got a lower score than they should have.
- Genre has a tiny weight. A pop fan can get lofi songs at the top.
- Energy counts most. This can hide other tastes.
- A user with mixed tastes gets odd results. For example, "pop" and "chill" at energy 0.6 does not fit any real song. The top picks were all lofi and ambient. Pop was ignored.
- Genres with one song only have one real match. Fans of those genres have fewer good options than pop or lofi fans.
- It ignores tempo, danceability, lyrics, and artist.
- The weights are my guesses. They are not learned from data.
- It only learns from what the user types. It does not learn from skips or plays.

---

## 7. Evaluation  

I ran five user profiles and read the top three songs.

| Profile | Top results |
|---|---|
| Pop, happy, energy 0.8 | Sunrise City, Rooftop Lights, Gym Hero |
| Rock, intense, energy 0.9 | Storm Runner, Gym Hero, Iron Requiem |
| Lofi, chill, energy 0.4 | Library Rain, Midnight Coding, Spacewalk Thoughts |
| Pop, chill, energy 0.6 | Midnight Coding, Library Rain, Spacewalk Thoughts |
| Classical, sad, quiet | Winter Etude, Spacewalk Thoughts, Library Rain |

What I looked for:

- Do the results match my gut feeling?
- Do very different users get very different lists?
- Do the reasons make sense?

What surprised me:

- The pop and chill profile never showed a pop song. Mood beat genre every time.
- The "sad" profile missed its mood match. The word "sad" is not in the data.
- Gym Hero shows up for both pop and rock fans. It is high energy, and it is also pop.

Simple tests:

- I scored Library Rain and Gym Hero for a calm lofi fan. Library Rain scored about 0.98. Gym Hero scored about 0.36.
- I read the reasons for each result to check that the points added up.

---

## 8. Future Work  

- Allow more than one favorite mood or genre.
- Give partial credit to close moods, like chill and relaxed.
- Use tempo and danceability in the score.
- Add a bigger and more balanced catalog.
- Avoid a top list full of the same artist or genre.
- Warn the user when their tastes conflict.
- Learn the weights from real listening data.
- Use skips and replays to update the profile.
- Tell users in plain words why a song was picked.

---

## 9. Personal Reflection  

I learned that a recommender is mostly a scoring rule plus a sort. The hard part is choosing what counts.

The biggest surprise was how much one weight can change things. Giving genre a small weight meant a pop fan rarely saw pop. The data also matters. With only 19 songs, many results were just "closest available."

I also learned that closeness works better than "bigger is better." A calm listener should not get the most intense song.

This makes me look at music apps differently. Real apps use huge amounts of data and many signals. My version is simple, but it shows the basic idea.
