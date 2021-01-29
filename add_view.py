import tkinter as tk
from tkinter import Button
import datetime
import tkcalendar as tkcal

class Add_Issue(tk.Frame):
    def __init__(self,  master, **kwargs):
        super().__init__(master)

        # <editor-fold desc="Variables -make dynamic in future version">
        #
        issue_types = [
            'Task',
            'Bug',
            'Feature'
        ]

        priority_types = [
            'Critical',
            'High',
            'Normal',
            'Low'
        ]

        category_types = [
            'Interface',
            'Business',
            'Database'
        ]

        status_types = [
            'Open',
            'In Progress',
            'Resolved',
            'Test',
            'Closed',
            'Back Log',
            'Shelved'
        ]

        projects = [
            'pyTrack',
            'House'
        ]

        assignees = [
            'Dale Woodard',
            'Dad',
            'Husband'
        ]

        versions = [
            1,
            2,
            3,
            4
        ]

        issue_type = tk.StringVar()
        priority_type = tk.StringVar()
        category_type = tk.StringVar()
        status_type = tk.StringVar()
        project = tk.StringVar()
        assignee = tk.StringVar()
        version = tk.IntVar()
        # </editor-fold>

        # Methods
        def date():
            date_entry.set(str(self.cal.get_date()))

        def clear_form():
            issue_type.set(issue_types[0])
            priority_type.set(priority_types[2])
            category_type.set(category_types[0])
            status_type.set(status_types[0])
            project.set(projects[0])
            assignee.set(assignees[0])
            version.set(versions[0])
            date_entry.set(str(datetime.date.today()))
            self.cal.selection_set(datetime.date.today())
            subject_tb.delete(0, tk.END)
            description_tb.delete(1.0, tk.END)
            time_tb.delete(0, tk.END)
            error_message.config(text='')

        def add_issue():
            return

        tk.Label(self, text='Issue Type').grid(column=0, row=0, padx=(10, 2), pady=(5, 0))
        issue_type.set(issue_types[0])
        issue_type_dd = tk.OptionMenu(self, issue_type, *issue_types)
        issue_type_dd.grid(column=0, row=1, padx=(10, 2), pady=(2, 5))
        issue_type_dd.config(width=12)

        tk.Label(self, text='Priority').grid(column=1, row=0, padx=2, pady=(5, 0))
        priority_type.set(priority_types[2])
        priority_type_dd = tk.OptionMenu(self, priority_type, *priority_types)
        priority_type_dd.grid(column=1, row=1, padx=2, pady=(2, 5))
        priority_type_dd.config(width=12)

        tk.Label(self, text='Category').grid(column=2, row=0, padx=2, pady=(5, 0))
        category_type.set(category_types[0])
        category_type_dd = tk.OptionMenu(self, category_type, *category_types)
        category_type_dd.grid(column=2, row=1, padx=2, pady=(2, 5))
        category_type_dd.config(width=9)

        tk.Label(self, text='Status').grid(column=3, row=0, padx=2, pady=(5, 0))
        status_type.set(status_types[0])
        status_type_dd = tk.OptionMenu(self, status_type, *status_types)
        status_type_dd.grid(column=3, row=1, padx=2, pady=(2, 5))
        status_type_dd.config(width=9)

        tk.Label(self, text='Project').grid(column=4, row=0, padx=2, pady=(5, 0))
        project.set(projects[0])
        project_type_dd = tk.OptionMenu(self, project, *projects)
        project_type_dd.grid(column=4, row=1, padx=2, pady=(2, 5))
        project_type_dd.config(width=9)

        tk.Label(self, text='Assignee').grid(column=5, row=0, padx=2, pady=(5, 0))
        assignee.set(assignees[0])
        assignee_dd = tk.OptionMenu(self, assignee, *assignees)
        assignee_dd.grid(column=5, row=1, padx=2, pady=(2, 5))
        assignee_dd.config(width=15)

        tk.Label(self, text='Version').grid(column=6, row=0, padx=2, pady=(5, 0))
        version.set(versions[0])
        version_dd = tk.OptionMenu(self, version, *versions)
        version_dd.grid(column=6, row=1, padx=2, pady=(2, 5))
        version_dd.config(width=5)

        tk.Label(self, text='Due Date').grid(column=7, row=0, padx=2, pady=(5, 0))
        date_entry = tk.StringVar()
        date_entry.set(str(datetime.date.today()))
        due_date_tb = tk.Entry(self, text=date_entry, width=12)
        due_date_tb.grid(column=7, row=1, padx=2, pady=(5, 0))
        due_date_tb.get()

        self.cal = tkcal.Calendar(master, selectmode="day", date_pattern='y-mm-dd')
        self.cal.place(x=700, y=85)
        self.select_btn = tk.Button(master, text="Select Date", command=date)
        self.select_btn.place(x=785, y=280)

        self.Label = tk.Label(master, text='Subject').place(x=15, y=80)
        subject_tb = tk.Entry(master, width=112)
        subject_tb.place(x=10, y=100)
        subject_tb.get()

        self.Label = tk.Label(master, text='Issue Description').place(x=15, y=120)
        description_tb = tk.Text(master, width=84, height=20)
        description_tb.place(x=10, y=140)
        description_tb.get(1.0, tk.END)

        error_message = tk.Label(self, text='')
        error_message.place(x=10, y=500)

        button_frame = tk.LabelFrame(master)
        button_frame.place(x=690, y=500)

        self.Label = tk.Label(button_frame, text='Time Estimate: ').grid(column=0, row=0)
        time_tb = tk.Entry(button_frame, width=4)
        time_tb.grid(column=1, row=0, padx=2)

        clear_btn = Button(button_frame, text='Clear Form', command=clear_form)
        clear_btn.grid(column=2, row=0, padx=(15, 2))

        add_btn = Button(button_frame, text='Add Issue', command=add_issue)
        add_btn.grid(column=3, row=0, padx=2)
