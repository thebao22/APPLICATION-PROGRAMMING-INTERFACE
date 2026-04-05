from transformers import pipeline
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
sequence_to_classify = "I just passed my exam with a 10"
candidate_labels = [
    "stressed",
    "sad",
    "angry",
    "tired",
    "unfocused",
    "happy"
]
output = classifier(sequence_to_classify, candidate_labels)
print(output['labels'][0])