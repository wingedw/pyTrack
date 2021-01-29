from issue import Issue


class IssuesRepository(object):
    def __init__(self, conn):
        self.conn = conn

    def to_values(self, i):
        values = '"' + i.subject + '", "' + i.description + '", "' + i.issue_type + '", "' + i.priority + '", "' + i.category +\
                 '", "' + i.status + '", "' + i.project + '", "' + i.assignee + '", "' + i.version + '", "' +\
                 i.time_estimate + '", "' + i.due_date + '", "' + i.created_date + '"'
        return values

    def get_issues(self):
        sql = """SELECT *
                 FROM issues"""
        for row in self.conn.execute(sql):
            issue = Issue(*row[1:])
            issue.rowid = row[0]
            yield issue

    def get_issue_by_id(self, _id):
        sql = """SELECT Id, Subject, Description, Issue_Type, Priority,
        Category, Status, Project, Assignee, Version, Time_Estimate,
        Due_Date, Created_Date FROM Issues WHERE Id = '""" + _id + "'"

        for row in self.conn.execute(sql):
            issue = Issue(*row[1:])
        #    issue.id = row[0]
            return issue

    def get_by_project(self, project):
        sql = """SELECT Id, Subject, Description, Issue_Type, Priority,
                Category, Status, Project, Assignee, Version, Time_Estimate,
                Due_Date, Created_Date
                FROM Issues WHERE Project = '""" + project + "'"
        for row in self.conn.execute(sql):
            issues = Issue(*row[1:])
            yield issues

    def create_issue(self, issue):
        _error = 'Issue successfully added.'
        try:
            sql = "INSERT INTO Issues (\
                Subject, \
                Description, \
                Issue_Type, \
                Priority, \
                Category, \
                Status, \
                Project, \
                Assignee, \
                Version, \
                Time_Estimate, \
                Due_Date, \
                Created_date) \
                VALUES ("\
                + "'" + issue.subject  \
                + "', '" + issue.description  \
                + "', '" + issue.issue_type  \
                + "', '" + issue.priority  \
                + "', '" + issue.category  \
                + "', '" + issue.status \
                + "', '" + issue.project  \
                + "', '" + issue.assignee \
                + "', '" + str(issue.version) \
                + "', '" + str(issue.time_estimate)  \
                + "', '" + str(issue.due_date)  \
                + "', '" + str(issue.created_date) + "')"

            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(sql)
                issue.id = cursor.lastrowid
                self.conn.commit()
        except Exception as e:
            _error = e
        return _error

    def update_issue(self, issue):
        sql = """ UPDATE Issues
        SET Subject = ?, Description = ?, Issue_Type = ?, Priority = ?,
        Category = ?, Status = ?, Project = ?, Assignee = ?, Version = ?,
        Time_Estimate = ?, Due_Date, Created_Date = ? WHERE Id= ?"""

        with self.conn:
            self.conn.execute(sql, self.to_values(issue) + issue.id)
        return issue

    def delete_issue(self, issue):
        sql = "DELETE FROM Issues WHERE id = ?"
        with self.conn:
            self.conn.execute(sql, (issue.id,))
