# --- STEP 1: DATA PREPARATION ---
user_text = str(input("Enter The Paragraph : "))

# Normalize text: lower case and remove punctuation to avoid duplicate keys like "Bridge" vs "bridge"
user_text = user_text.lower().replace(",", " ").replace(".", " ")
words = user_text.split()

# --- STEP 2: FREQUENCY MAPPING ---
word_count = {}

for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

# --- STEP 3: LOGIC FOR TIES (The "Winner" Algorithm) ---
# We calculate max_val once here to save CPU cycles (O(n) efficiency)
max_val = max(word_count.values())

winner = []
for word, count in word_count.items():
    if count == max_val:
        winner.append(word)

# --- STEP 4: OUTPUT REPORTING ---
print("--- Word Frequency Report ---")
for word, count in word_count.items():
    print(f"'{word}': appears {count} times")

print("\n--- Winner Report ---")
for i in winner:
    print(f"{i} is winner with {max_val} times appearance")