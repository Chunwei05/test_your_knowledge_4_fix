class Calculator:
    def __init__(self):
        self.answer = 0
    
    def get_answer(self):
        return self.answer

    def reset(self):
        self.answer = 0
        return self
