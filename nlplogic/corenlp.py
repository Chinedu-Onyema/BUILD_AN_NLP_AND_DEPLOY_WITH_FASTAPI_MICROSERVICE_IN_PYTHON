import wikipedia
from textblob import TextBlob


def search_wikipedia(name):
    """Search Wikipedia for a name."""
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize a Wikipedia page."""
    print(f"Finding Wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Get a TextBlob object from text."""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find Wikipedia summary for a name and extract noun phrases."""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
