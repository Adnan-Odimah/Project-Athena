import spacy

class Context:
    """
    class used to obtain the context for different cases throughout Athena
    """
    def __init__(self):
        self.nlp = spacy.load("en_core_web_md")
        self.number_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "twenty-one": 21, "twenty-two": 22, "twenty-three": 23, "twenty-four": 24}
    def get_reminders_context(self, sentence: str) -> dict:
        """Gets the context for the reminders

        Args:
            sentence (str): the sentence to get context from

        Returns:
            dict: a dictionary containing keys for time, date, frequency, and task
        """
        doc = self.nlp(sentence)
        time = None
        date = None
        frequency = None
        task = None

        for token in doc:
            if token.like_num and "pm" in token.text.lower():
                time = token.text
            elif token.lower_ in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                date = token.text
            elif token.lower_ == "week":
                frequency = "weekly"
            elif token.lower_ in ["call", "remind"]:
                task = " ".join([t.text for t in token.subtree])

        return {"time": time, "date": date, "frequency": frequency, "task": task}