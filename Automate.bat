@echo off
REM Define the log file path
set LOGFILE="C:\Users\jcox\Documents\Lake Scrape Project\batlog.txt"

REM Activate the virtual environment and redirect output to log file
CALL "C:\Users\jcox\Documents\Lake Scrape Project\.venv\Scripts\activate.bat" >> %LOGFILE% 2>&1

REM Run the first Python script and redirect output to log file
"C:\Users\jcox\Documents\Lake Scrape Project\.venv\Scripts\python.exe" "C:\Users\jcox\Documents\Lake Scrape Project\Lake_Level_Automate.py" >> %LOGFILE% 2>&1

REM Run the second Python script and redirect output to log file
"C:\Users\jcox\Documents\Lake Scrape Project\.venv\Scripts\python.exe" "C:\Users\jcox\Documents\Lake Scrape Project\WriteToGithub.py" >> %LOGFILE% 2>&1

REM Deactivate the virtual environment if needed
REM deactivate.bat
