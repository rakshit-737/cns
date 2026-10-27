@echo off
echo Use: run_server.bat 02_Caesar_Cipher
if "%~1"=="" goto end
py "%~1\server.py"
:end
pause
