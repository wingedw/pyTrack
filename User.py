import utilities


class User(object):
    def __init__(self, id, first_name, last_name, status, level):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.level = level

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
