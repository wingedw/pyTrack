import sqlite3

from issues_repository import IssuesRepository
from root_view import Root
from issues_controller import IssuesController


def main():
    with sqlite3.connect("pytrack.db") as conn:
        repo = IssuesRepository(conn)
        view = Root()
        ctrl = IssuesController(repo, view)

    #   view.set_ctrl(ctrl)
        ctrl.start()


if __name__ == "__main__":
    main()
