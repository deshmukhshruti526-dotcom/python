# Text moderation filter

feedback = input("Enter your feedback: ")

# Words to be masked
target_words = ["badword", "stupid", "idiot"]

# Replace target words with ****
for word in target_words:
    feedback = feedback.replace(word, "****")

print("Moderated Feedback:", feedback)
