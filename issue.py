import re
import utilities


class Issue(object):
    def __init__(self, subject,
                 description,
                 issue_type,
                 priority,
                 category,
                 status,
                 project,
                 assignee,
                 version,
                 time_estimate,
                 due_date,
                 created_date):
        self.subject = subject
        self.description = description
        self.issue_type = issue_type
        self.priority = priority
        self.category = category
        self.status = status
        self.project = project
        self.assignee = assignee
        self.version = version
        self.time_estimate = time_estimate
        self.due_date = due_date
        self.created_date = created_date

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = utilities.required(value, 'Subject is required')

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = utilities.required(value, 'Description is required.')

    @property
    def issue_type(self):
        return self._issue_type

    @issue_type.setter
    def issue_type(self, value):
        self._issue_type = value

    @property
    def priority(self):
        return self.priority

    @priority.setter
    def priority(self, value):
        self._priority = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, value):
        self._project = value

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        self._assignee = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def time_estimate(self):
        return self._time_estimate

    @time_estimate.setter
    def time_estimate(self, value):
        self._time_estimate = value

    @property
    def due_date(self):
        return self.due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value

    @property
    def created_date(self):
        return self._created_date

    @created_date.setter
    def created_date(self, value):
        self._created_date = value

