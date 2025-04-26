@echo off
setlocal

:: Gereklilikleri yükle
pip install -r requirements.txt

:: Python betiğini çalıştır
python totp_secret_extractor.py

:: PowerShell'i açık tut
pause