class FeedBackData:
    name = ""
    email = ""
    age = ""
    rating = ""
    suggestion = ""
    question1 = ""
    question2 = ""
    question3 = ""
    question4 = ""
    question5 = ""

    def clear(self):
        self.name = ""
        self.rating = ""
        self.age = ""
        self.email = ""
        self.suggestion = ""
        self.question1 = ""
        self.question2 = ""
        self.question3 = ""
        self.question4 = ""
        self.question5 = ""

    def __str__(self) -> str:
        return f"(name={self.name},rating={self.rating},age={self.rating},email={self.email},suggestion={self.suggestion},question1={self.question1},question2={self.question2},question3={self.question3},question4={self.question4},question5={self.question5})"
