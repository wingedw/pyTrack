from issues_view import  NewIssue


class IssuesController(object):
    def __init__ (self, repo, view):
        self.repo = repo
        self.view = view
        self.selection = None
        self.issues = list(repo.get_issues())

    def create_issue(self):
        new_issue = NewIssue(self.view).show()
        if new_issue:
            issue = self.repo.add_issue(new_issue)
            self.issues.append(issue)
            self.view.add_issue(issue)

    def select_issue(self, index):
        self.selection = index
        issue = self.issues[index]
        self.view.load_details(issue)

    def update_issue(self):
        if not self.selection:
            return
        rowid = self.issues[self.selection].rowid
        update_issue = self.view.get_details()
        update_issue.rowid = rowid

        issue = self.repo.update_issue(update_issue)
        self.issues[self.selection] = issue
        self.view.update_issue(issue, self.selection)

    def delete_issue(self):
        if not self.selection:
            return
        issue = self.issues[self.selection]
        self.repo.delete_issue(issue)
        self.view.remove_issue(self.selection)

    def start(self):
        for i in self.issues:
            self.view.add_issue(i)
        self.view.mainloop()
