@echo off
echo Use: run_client.bat 02_Caesar_Cipher
if "%~1"=="" goto end
py "%~1\client.py"
:end
pause
