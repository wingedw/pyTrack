# pyTrack
***
***
### Description
pyTrack is a desktop app to track issues.
It will be implemented with MVC design pattern
to ease the ability to change out database platform
 so it can be configured as a
multi-user issue tracker.

This a personal project that I am developing in my spare time
to track my development work and projects around the house.
It is free for you to use and if you have any comments
or suggestions for changes or improvements drop me a line at dale@wingedw.com.

---
### Setup
1. Clone the repository
2. Install tkCalendar from the IDE terminal

   ```pip install tkcalendar```
3. SQLite is a self-contained, file-based SQL 
database. SQLite comes bundled with Python no
additional installation is required. To created 
the database for pyTrack run create_db.py in
the db_init folder and a SQLite database named
pytrack.db will be created in the root directory.

### Tools
1. pyCharm 2020.3.x
2. Python 3.8.x
3. SQLite 3.x
4. tkCalendar 1.6.x

---

### Development Path
* Version 3.0 - **Project Settings**
* Version 2.0 - **Dashboard**
* Version 1.0 - **Add, view and edit issues**
   - [] 0.4 Refactor to MVC design pattern 
   - [] 0.3 Edit issues
   - [] 0.2 View issues
   - [x] 0.1 Persist issue to database 

### Versions

#### 0.11
1. Add Issue Tab
   * Clear form if insert is successful
#### 0.1
1. Add Issue Tab
   * Clear Form button functional
   * Display error or success when adding issue
   * Added date picker for due date
   * Set issue created date to today 
#### 0.02
1. General
    * Began moving to MVC design pattern
    * Do insert into issues table
#### 0.01
1. General
    * Created tab layout for GUI
    * Create repository
