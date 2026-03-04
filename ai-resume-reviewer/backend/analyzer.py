import re
from pdfminer.high_level import extract_text

class ResumeAnalyzer:
    #the analysis engine. uses classes to store state and functions to process data.abs
    def __init__(self, file_path):
        self.file_path = file_path
        self.raw_text = ""
        self.processed_data = {
            "score": 0,
            "found_keywords": [],
            "missing_keywords": [],
            "sections": {}
        }
        # file handling: safely open and read the pdf.
        def extract_content(self):
            try:
                self.raw_text = extract_text(self.file_path).lower()
                return True
            except Exception as e:
                print(f"error reading file: {e}")
                return False
        # control strucctures: loop through keywords and categorize. 
        def analyze(self, job_keywords):
            if not self.raw_text:
                return self.processed_data


            # simple scoring logic
            for word in job_keywords:
                if re.search(rf"\b{word.lower()}\b", self.raw_text):
                    self.processed_data["found_keywords"].append(word)
                else:
                    self.processed_data["missing_keywords"].append(word)


            #calculate score
            total = len(job_keywords)
            found = len(self.processed_data["found_keywords"])
            self.processed_data["score"] = int((found / total)*100) if total > 0 else 0

            return self.processed_data