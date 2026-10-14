class Counter:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1

    def decrease(self):
        self.value -= 1

    def show(self):
        print("Счётчик:", self.value)


counter = Counter()

counter.increase()
counter.increase()
counter.increase()
counter.show()

counter.decrease()
counter.show()