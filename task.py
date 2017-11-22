import datetime


class Task:
    def __init__(self, name='default', date_done=datetime.datetime.now(),
                 time_spent=0, notes='none'):
        self.name = name
        self.date_done = date_done
        self.time_spent = time_spent
        self.notes = notes

    def edit_name(self, name):
        self.name = name
        return self.name

    def edit_date_done(self, date_done):
        self.date_done = date_done
        return self.date_done

    def edit_time_spent(self, time_spent):
        self.time_spent = time_spent
        return self.time_spent

    def edit_notes(self, notes):
        self.notes = notes
        return self.notes
