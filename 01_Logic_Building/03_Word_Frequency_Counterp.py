user_text = "The bridge is strong, and the bridge is wide."

user_text = user_text.lower()
user_text = user_text.replace(","," ")
user_text = user_text.replace("."," ")
words = user_text.split()

word_count = {}

for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

top_word = max(word_count, value=word_count.get)

print("--- Word Frequency Report ---")

for word, count in word_count.items():
    print(f"'{word}': appears {count} times")


print(f"Most Common Word: {top_word}")
