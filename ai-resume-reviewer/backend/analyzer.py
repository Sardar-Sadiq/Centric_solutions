class ResumeReviewer:
    def __init__(self, text):
        self.text = text.lower()

    def get_score(self, keywords):
        """Categorize and check for keywords."""
        found = [word for word in keywords if word.lower() in self.text]
        missing = [word for word in keywords if word.lower() not in self.text]
        score = (len(found) / len(keywords)) * 100 if keywords else 0
        
        return {
            "score": int(score),
            "found": found,
            "missing": missing
        }