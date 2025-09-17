class Calculator:
    def __init__(self):
        self.answer = 0
    
    def get_answer(self):
        return self.answer

    def reset(self):
        self.answer = 0
        return self

    def add(self, num):
        self.answer += num
        return self

    def subtract(self, num):
        self.answer -= num
        return self

    def multiply(self, num):
        self.answer *= num
        return self

    def power(self, num):
        self.answer **= num
        return self
