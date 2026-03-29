# Model Card: Mood Machine

This model card covers two versions of a mood classifier built in this project:

1. A rule-based model in `mood_analyzer.py`
2. A machine learning model in `ml_experiments.py` using scikit-learn

Both were built and compared.

---

## 1. Model Overview

**Model type:** Rule-based classifier and ML classifier (logistic regression). Both were used and compared.

**Intended purpose:** Classify short text posts as `positive`, `negative`, `neutral`, or `mixed`. The target input is informal, social-media-style text: short sentences, slang, emojis, and mixed tone.

**How it works:**

Rule-based version:
- Tokenizes the input by lowercasing, separating emojis, and stripping punctuation.
- Checks each token against a list of positive and negative words.
- Adds +1 for a positive word match, -1 for a negative match.
- Handles negation: if a negation word (not, never, don't) appears before a sentiment word, the score contribution is flipped.
- Maps the net score to a label. Score 0 with both positive and negative signals returns `mixed`. Score 0 with no signals returns `neutral`.

ML version:
- Converts all posts to word-count vectors using `CountVectorizer`.
- Trains a logistic regression classifier on those vectors and the human-assigned labels.
- Predicts the label for new text by transforming it into the same vector space.

---

## 2. Data

**Dataset:** 20 labeled posts in `SAMPLE_POSTS` and `TRUE_LABELS` in `dataset.py`. The starter had 6 posts. 14 new posts were added.

**Labeling process:** Each post was labeled by hand. Labels reflect the intended tone, not just surface words. Sarcastic posts were labeled by their real meaning. For example, "I absolutely love sitting in traffic for two hours" is labeled `negative` even though "love" is a positive word.

Some posts were genuinely hard to label. "my dog ran away but we found her" could be `mixed` or `negative` depending on whether you weight the fear or the relief. "this is fine" could be `neutral` or dry sarcasm.

**Dataset characteristics:**
- Includes slang: lowkey, no cap, fr fr, rn, meh, kinda
- Includes emojis: used in varied and sometimes ironic ways
- Includes sarcasm: multiple posts use positive words to describe negative situations
- Includes mixed-feeling posts: tired but hopeful, stressed but proud
- Some posts have no sentiment words at all and rely entirely on context

**Possible issues:**
- Only 20 examples. This is not enough to train a reliable ML model.
- The dataset reflects one person's language habits and tone. Formal language, other dialects, or non-English slang are not represented.
- Labels for ambiguous posts are subjective. A different annotator would likely disagree on 3 to 4 of them.

---

## 3. How the Rule-Based Model Works

**Scoring rules:**
- Each token is checked against `POSITIVE_WORDS` and `NEGATIVE_WORDS` in `dataset.py`.
- Positive match: score += 1. Negative match: score -= 1.
- Negation words (not, never, no, don't, doesn't, didn't, isn't, wasn't, can't, won't) set a flag that flips the modifier for the next sentiment word only.
- Score > 0: positive. Score < 0: negative. Score == 0 with both signal types: mixed. Score == 0 with no signals: neutral.

**Word list additions:**
The starter word lists were too narrow. Five positive words were added based on words that appear in the dataset but were not matched: `proud`, `hopeful`, `best`, `vibes`, `immaculate`. One negative word was added: `worst`.

**Strengths:**
- Transparent and inspectable. You can trace exactly why any prediction was made.
- Consistent. The same input always returns the same output.
- Works immediately, no training required.
- Negation handling correctly flips "not happy" to negative.

**Weaknesses:**
- Cannot detect sarcasm. "love" always scores +1, even in "love sitting in traffic."
- Single-word negation only. "not at all happy" is not correctly handled because the negation resets before reaching "happy."
- Vocabulary coverage is a constant problem. Words not in the list have zero effect.
- "incredible", "bittersweet", "awful" (if not in the list) produce neutral predictions regardless of how strong the actual tone is.

---

## 4. How the ML Model Works

**Features:** Bag-of-words representation using `CountVectorizer`. Each post becomes a vector of word counts.

**Training data:** All 20 entries in `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:** The model is evaluated on the same data it was trained on. This means the reported accuracy of 1.00 is training accuracy, not generalization accuracy. It reflects memorization, not learning.

When two sarcasm posts were added (labeled `negative` but containing the words "amazing" and "love"), the model's internal weights for those words shifted. "amazing how I can study all night and still fail" changed from `positive` to `negative` after those posts were added. This shows how directly the model's predictions depend on the specific labels in the dataset.

**Strengths:**
- Captures word co-occurrence patterns automatically without hand-written rules.
- Updates its predictions when the dataset changes, with no code changes needed.

**Weaknesses:**
- Evaluated only on training data. True accuracy on new text is unknown.
- With 20 examples, the model memorizes rather than generalizes.
- Sensitive to label noise. One mislabeled example shifts predictions in hard-to-predict ways.

---

## 5. Evaluation

**Rule-based accuracy on 20 posts:** 0.70 (14 of 20 correct)

**ML model training accuracy on 20 posts:** 1.00 (not a meaningful generalization score)

**What the rule-based model got right:**

- "I am not happy about this" -> negative. Negation handling worked: "not" flipped "happy" from +1 to -1.
- "so tired of everything rn but at least the coffee is good" -> mixed. "tired" scored -1, "good" scored +1, net score of 0 with both signals, so the model returned mixed.
- "this is simultaneously the best and worst day of my life lol" -> mixed. "best" scored +1, "worst" scored -1, same result.

**What the rule-based model got wrong:**

- "I absolutely love sitting in traffic for two hours" -> predicted positive, true negative. The word "love" scored +1. The model has no mechanism to detect irony. This is the clearest example of the sarcasm failure.
- "I am absolutely not stressed about this presentation at all" -> predicted positive, true negative. Negation handling flipped "stressed" from -1 to +1. The model treated "not stressed" as genuinely positive. This is accurate literal logic applied to a sarcastic sentence.
- "finally got some rest and I feel incredible" -> predicted neutral, true positive. "incredible" is not in the positive word list, so no score was produced despite strong positive tone.

---

## 6. Limitations

**Sarcasm is not detectable.** A sentence like "I absolutely love sitting in traffic" shares the same surface features as "I love this class so much." The rule-based model cannot distinguish them. The ML model only handles sarcasm correctly if it has seen similar examples labeled as negative during training.

**The dataset is too small for the ML model.** 20 examples cannot produce a generalizable classifier. "today was an immaculate day" was predicted as negative by the ML model because "today was" and "day" co-occurred with the negative training example "today was a terrible day." The model overfitted to the pattern rather than understanding the word "immaculate."

**Negation only covers the next word.** "not at all happy" will still score as positive because "at" resets the negation flag before "happy" is reached.

**The vocabulary is narrow and English-only.** Words outside the list have zero effect. The model reflects one style of informal English. Users who write in other dialects, other languages, or with non-standard spelling will consistently get neutral predictions.

**Labels are subjective.** Several posts in the dataset could be labeled differently by another person. The ML model reflects this person's labeling choices directly.

---

## 7. Ethical Considerations

**Misclassifying distress as positive or neutral.** A message like "I'm totally fine, everything is great" could be genuine or a sign someone is struggling. Both models would predict positive. Using this system to monitor emotional states in real settings would produce false negatives on masked distress.

**Language bias.** The dataset contains one style of informal English with specific slang. Formal writing, other dialects, non-English speakers writing in English, and other communities are not represented. The model will produce worse results for anyone whose patterns differ from the training data.

**Transparency.** The rule-based model is fully inspectable. The ML model is a black box in the sense that its weights are not readable as rules. If the ML model is deployed, users cannot easily understand why a given prediction was made.

**Scope.** This system was built as a learning exercise on 20 examples. It is not appropriate for any real application without significant additional data, testing, and review.

---

## 8. Ideas for Improvement

- Add 500+ diverse labeled examples from multiple authors and writing styles.
- Use TF-IDF instead of raw word counts to reduce the weight of common words.
- Add a real held-out test set so accuracy scores reflect generalization, not memorization.
- Build a small emoji sentiment map so emojis like 🙃 and 😭 contribute to scoring directly.
- Improve negation to carry across multiple words, not just the next token.
- Use a pre-trained transformer model fine-tuned on sentiment data for sarcasm and subtlety.
- Add inter-annotator agreement checks so label quality is measurable.
