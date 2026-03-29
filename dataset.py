"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    # Added: words that appear in SAMPLE_POSTS but were unrecognized
    "proud",       # "kinda proud of myself"
    "hopeful",     # "kind of hopeful"
    "best",        # "simultaneously the best and worst day"
    "vibes",       # "vibes are immaculate"
    "immaculate",  # "vibes are immaculate"
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    # Added: words that appear in SAMPLE_POSTS but were unrecognized
    "worst",       # "simultaneously the best and worst day"
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    # --- New posts ---
    "Lowkey stressed but no cap kinda proud of myself 😅",
    "I absolutely love sitting in traffic for two hours 🙃",
    "just got the job offer!!!! I'm literally crying happy tears 😭🎉",
    "meh. another monday. whatever",
    "this is simultaneously the best and worst day of my life lol",
    "so tired of everything rn but at least the coffee is good ☕",
    "my dog ran away but we found her 💀 my heart cannot take this",
    "vibes are immaculate today no complaints fr fr 🔥",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    # --- New labels ---
    "mixed",     # stressed but proud — classic mixed
    "negative",  # sarcasm: traffic is clearly bad
    "positive",  # job offer + happy crying
    "neutral",   # flat "meh" vibe, no strong signal
    "mixed",     # explicitly best AND worst
    "mixed",     # tired (negative) + coffee (small positive)
    "mixed",     # scary dog situation but resolved happily
    "positive",  # "immaculate vibes", no complaints
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
