import spacy

class Context:
    """
    class used to obtain the context for different cases throughout Athena
    """
    def __init__(self):
        self.nlp = spacy.load("en_core_web_md")
        self.number_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "twenty-one": 21, "twenty-two": 22, "twenty-three": 23, "twenty-four": 24}

    def get_reminders_context(self, sentence: str) -> dict:
        #TODO: fix for sentences that use compound clauses
        # e.g. do x next friday night, only gets friday but not "next"
        """Gets the context for the reminders

        Args:
            sentence (str): the sentence to get context from

        Returns:
            dict: a dictionary containing keys for time, date, frequency, and task
        """
        doc = self.nlp(sentence)
        extracted_info = {"time": None, "date": None, "frequency": None, "task": None}

        for token in doc:
            task = self.check_task(token)
            if task:
                extracted_info["task"] = task

            time = self.check_time(token)
            if time:
                extracted_info["time"] = time



            if token.ent_type_ == "DATE":
                children = [c for c in token.children]
                if len(children) > 0:
                    if children[0].dep_ == "det":
                        extracted_info["frequency"] = f"{children[0].lower_} {token.lower_}"
                    else:
                        extracted_info["date"] = f"{children[0].lower_} {token.lower_}"
                else:
                    extracted_info["date"] = token.text



            if token.dep_ == "compound":
                children = [c for c in token.head.children]
                if len(children) == 0:
                    continue
                extracted_info["date"] = f"{children[0].lower_} {children[1].lower_}"

        return extracted_info

    def check_task(self, token) -> str:
        """checks if the current token is the task and returns it

        Args:
            token (Spacy.Token): token to check

        Returns:
            str: the task to be done
        """
        task = None

        if token.pos_ == "VERB":
            children = [c for c in token.children]
            for child in children:
                if child.dep_ == "dobj":
                    task = f"{token.text} {child.text}"

        return task

    def check_time(self, token) -> str:
        """checks if the current token is the time and returns it

        Args:
            token (Spacy.Token): token to check

        Returns:
            str: the time to be done
        """
        time = None

        if token.ent_type_ == "TIME":
            if token.lower_ in ['am', 'pm']:
                return None

            if token.head.dep_ == "pobj":
                if token.text.isdigit():
                    time = f"{token.lower_} {token.head.lower_}"
                else:
                    time = f"{self.number_dict[token.lower_]} {token.head.lower_}"

            else:
                time = token.lower_

        return time
