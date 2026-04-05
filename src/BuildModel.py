import torch
from omegaconf import OmegaConf
from transformers import pipeline, DistilBertTokenizer, DistilBertForSequenceClassification


class MoodClassification:
    def __init__(self, config_path=None):
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
        self.labels = [
            "stressed",
            "sad",
            "angry",
            "tired",
            "unfocused",
            "happy"
        ]

    def __call__(self, text):
        result = self.classifier(text, self.labels)
        return result['labels'][0]