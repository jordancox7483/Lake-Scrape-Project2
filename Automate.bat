@echo off
REM Activate the virtual environment
CALL "C:\Users\jcox\Documents\Lake Scrape Project\.venv\Scripts\activate.bat"

REM Run the Python script
"C:\Users\jcox\Documents\Lake Scrape Project\.venv\Scripts\python.exe" "C:\Users\jcox\Documents\Lake Scrape Project\Lake_Level_Automate.py"

REM Run the Python script
"C:\Users\jcox\Documents\Lake Scrape Project\.venv\Scripts\python.exe" "C:\Users\jcox\Documents\Lake Scrape Project\WriteToGithub.py"

pause