class Subject:
    """Объект наблюдения"""
    def __init__(self):
        self.observers = []

    def notify(self):
        for observer in self.observers:
            observer.update(self)


class Observer:
    """Наблюдатель"""
    def update(self, subject: Subject):
        pass


class SmsNotifier(Observer):
    def update(self, subject: Subject):
        print('SMS: присоединился', subject.students[-1].fullname)


class EmailNotifier(Observer):
    def update(self, subject: Subject):
        print('Email: присоединился', subject.students[-1].fullname)
