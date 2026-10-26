LEXICON = {
    "delicious": 3, "great": 3, "tasty": 2, "kind": 2, "fresh": 2, "good": 2,
    "cold": -1, "slow": -1, "bad": -2, "rude": -2, "burnt": -2, "awful": -3,
}
NEGATIONS = {"not", "never", "no"}
PUNCTUATION = ".,!?:;\"'()"

TEST_COMMENTS = [
    ("The pasta was delicious and the staff were kind", "HAPPY"),
    ("The queue was slow and the juice was awful", "UNHAPPY"),
    ("Not good, the rice was cold", "UNHAPPY"),
    ("Not bad at all, I will come again", "HAPPY"),
    ("Lunch is at 1 pm on Fridays", "OK"),
    ("Great, they ran out of food again", "UNHAPPY"),
]
def clean_words(comment):
    return []
print("PART 1: Clean words")
print(clean_words("Not GOOD, the rice was cold!"))
def comment_score(comment):
    return 0
print("\nPART 2: Score")
print(comment_score("Not good, the rice was cold"))
def mood(comment):
    return "OK"
print("\nPART 3: Mood")
print(mood("The pasta was delicious and the staff were kind"))
print("\nPART 4: Test all comments")
mistakes = 0