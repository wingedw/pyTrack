from tkinter import *
from tkinter import ttk
from tkcalendar import *
import sqlite3
from issues_repository import IssuesRepository
import issue
import datetime

root = Tk()
root.title('pyTrack Issue Tracker')
root.geometry('972x600')
root.resizable(False, False)

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Dashboard')
tabControl.add(tab2, text='Add Issue')
tabControl.add(tab3, text='Issues Details')
tabControl.add(tab4, text='Project Settings')

tabControl.pack(expand=1, fill="both")

# <editor-fold desc="Tab 1 Dashboard">
ttk.Label(tab1,
          text="Welcome to Your Dashboard").grid(column=0,
                                                 row=0,
                                                 padx=30,
                                                 pady=30)
ttk.Label(tab1, text='Dashboard to implemented in Version 2').grid(column=0, row=1, padx=2, pady=(5, 0))
quit_btn = Button(tab1, text="Exit pyTrack", command=root.quit)
quit_btn.place(x=870, y=5)
# </editor-fold>

# <editor-fold desc="Tab 2 Enter an Issue">
# Variables
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

issue_type = StringVar()
priority_type = StringVar()
category_type = StringVar()
status_type = StringVar()
project = StringVar()
assignee = StringVar()
version = IntVar()


# due_date = StringVar()

# Methods
def date():
    date_entry.set(str(cal.get_date()))


def clear_form():
    issue_type.set(issue_types[0])
    priority_type.set(priority_types[2])
    category_type.set(category_types[0])
    status_type.set(status_types[0])
    project.set(projects[0])
    assignee.set(assignees[0])
    version.set(versions[0])
    date_entry.set(str(datetime.date.today()))
    cal.selection_set(datetime.date.today())
    subject_tb.delete(0, END)
    description_tb.delete(1.0, END)
    time_tb.delete(0, END)
    error_message.config(text='')


def add_issue():
    i = issue.Issue
    i.subject = subject_tb.get()
    i.description = description_tb.get(1.0, END)
    i.issue_type = issue_type.get()
    i.priority = priority_type.get()
    i.category = category_type.get()
    i.status = status_type.get()
    i.project = project.get()
    i.assignee = assignee.get()
    i.version = version.get()
    i.time_estimate = time_tb.get()
    i.due_date = due_date_tb.get()
    i.created_date = datetime.date.today()

    conn = sqlite3.connect('pytrack.db')
    ir = IssuesRepository(conn)
    _error = ir.create_issue(i)
    if _error == 'Issue successfully added.':
        clear_form()
    error_message.config(text=_error)
    return


# Form
ttk.Label(tab2, text='Issue Type').grid(column=0, row=0, padx=(10, 2), pady=(5, 0))
issue_type.set(issue_types[0])
issue_type_dd = OptionMenu(tab2, issue_type, *issue_types)
issue_type_dd.grid(column=0, row=1, padx=(10, 2), pady=(2, 5))
issue_type_dd.config(width=12)

ttk.Label(tab2, text='Priority').grid(column=1, row=0, padx=2, pady=(5, 0))
priority_type.set(priority_types[2])
priority_type_dd = OptionMenu(tab2, priority_type, *priority_types)
priority_type_dd.grid(column=1, row=1, padx=2, pady=(2, 5))
priority_type_dd.config(width=12)

ttk.Label(tab2, text='Category').grid(column=2, row=0, padx=2, pady=(5, 0))
category_type.set(category_types[0])
category_type_dd = OptionMenu(tab2, category_type, *category_types)
category_type_dd.grid(column=2, row=1, padx=2, pady=(2, 5))
category_type_dd.config(width=9)

ttk.Label(tab2, text='Status').grid(column=3, row=0, padx=2, pady=(5, 0))
status_type.set(status_types[0])
status_type_dd = OptionMenu(tab2, status_type, *status_types)
status_type_dd.grid(column=3, row=1, padx=2, pady=(2, 5))
status_type_dd.config(width=9)

ttk.Label(tab2, text='Project').grid(column=4, row=0, padx=2, pady=(5, 0))
project.set(projects[0])
project_type_dd = OptionMenu(tab2, project, *projects)
project_type_dd.grid(column=4, row=1, padx=2, pady=(2, 5))
project_type_dd.config(width=9)

ttk.Label(tab2, text='Assignee').grid(column=5, row=0, padx=2, pady=(5, 0))
assignee.set(assignees[0])
assignee_dd = OptionMenu(tab2, assignee, *assignees)
assignee_dd.grid(column=5, row=1, padx=2, pady=(2, 5))
assignee_dd.config(width=15)

ttk.Label(tab2, text='Version').grid(column=6, row=0, padx=2, pady=(5, 0))
version.set(versions[0])
version_dd = OptionMenu(tab2, version, *versions)
version_dd.grid(column=6, row=1, padx=2, pady=(2, 5))
version_dd.config(width=5)

ttk.Label(tab2, text='Due Date').grid(column=7, row=0, padx=2, pady=(5, 0))
date_entry = StringVar()
date_entry.set(str(datetime.date.today()))
due_date_tb = Entry(tab2, text=date_entry, width=12)
due_date_tb.grid(column=7, row=1, padx=2, pady=(5, 0))
due_date_tb.get()

cal = Calendar(tab2, selectmode="day", date_pattern='y-mm-dd')
cal.place(x=700, y=85)
select_btn = Button(tab2, text="Select Date", command=date)
select_btn.place(x=785, y=280)

ttk.Label(tab2, text='Subject').place(x=15, y=80)
subject_tb = Entry(tab2, width=112)
subject_tb.place(x=10, y=100)
subject_tb.get()

ttk.Label(tab2, text='Issue Description').place(x=15, y=120)
description_tb = Text(tab2, width=84, height=20)
description_tb.place(x=10, y=140)
description_tb.get(1.0, END)

error_message = ttk.Label(tab2, text='')
error_message.place(x=10, y=500)

button_frame = LabelFrame(tab2)
button_frame.place(x=690, y=500)

ttk.Label(button_frame, text='Time Estimate: ').grid(column=0, row=0)
time_tb = Entry(button_frame, width=4)
time_tb.grid(column=1, row=0, padx=2)

clear_btn = Button(button_frame, text='Clear Form', command=clear_form)
clear_btn.grid(column=2, row=0, padx=(15, 2))

add_btn = Button(button_frame, text='Add Issue', command=add_issue)
add_btn.grid(column=3, row=0, padx=2)
#</editor-fold>

# <editor-fold desc="Tab 3 Issue Details an Issue">
left_frame = LabelFrame(tab3)
left_frame.place(x=5, y=5, width=390, height=260)
ttk.Label(left_frame, text='Search Conditions').grid(column=0, row=0)

ttk.Label(left_frame, text='Project').grid(column=0, row=1, padx=2, pady=(5, 0))
project.set(projects[0])
projects_dd = OptionMenu(left_frame, project, *projects)
projects_dd.grid(column=1, row=1, padx=2, pady=(2, 5))
projects_dd.config(width=9)
project.get()

left_frame_lower = LabelFrame(tab3)
left_frame_lower.place(x=5, y=270, width=390, height=301)
ttk.Label(left_frame_lower, text='Issues').grid(column=0, row=0)

issues_lb = Listbox(left_frame_lower)
i = 0
while i < len(projects):
    issues_lb.insert(i, projects[i])
    i += 1

issues_lb.grid(column=0, row=1)

right_frame = LabelFrame(tab3)
right_frame.place(x=400, y=5, width=566, height=566)
ttk.Label(right_frame, text='Issue Details').grid(column=0, row=0)
ttk.Label(right_frame, text='Due: 01/20/2021').grid(column=4, row=0)

ttk.Label(right_frame, text='Issue: pyTrack').grid(column=0, row=1)
ttk.Label(right_frame, text='Version: 1').grid(column=4, row=1)

ttk.Label(right_frame, text='Type: Task').grid(column=0, row=2)
ttk.Label(right_frame, text='Priority: Normal').grid(column=1, row=2)
ttk.Label(right_frame, text='Category: Interface').grid(column=2, row=2)
ttk.Label(right_frame, text='Status: Open').grid(column=3, row=2)
ttk.Label(right_frame, text='Assignee: Dale Woodard').grid(column=4, row=2)

ttk.Label(right_frame, text='Issue Description').place(x=15, y=80)
details = Text(right_frame, width=67, height=20)
details.place(x=5, y=100)
# </editor-fold">

# <editor-fold desc="Tab 4 Project Settings an Issue">

ttk.Label(tab4, text="Welcome to Your Project Settings").grid(column=0, row=0, padx=30, pady=30)

ttk.Label(tab4, text='Project Settings to implemented in Version 2 and 3').grid(column=0, row=1, padx=2, pady=(5, 0))
# </editor-fold>

root.mainloop()
