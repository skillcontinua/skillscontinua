@echo off
echo ===========================================
echo   SkillsContinua - Django Shell
echo ===========================================
cd /d C:\skillscontinua
echo Activating virtual environment...
call venv\Scripts\activate
echo.
echo Running Django shell...
python manage.py shell
pause