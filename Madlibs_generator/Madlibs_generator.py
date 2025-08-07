with open("story.txt", "r") as r:
    story = r.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    # يعطينا كل حرف وموقعه داخل النص
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        star_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + " :")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
