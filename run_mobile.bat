@echo off
title Khaata Mobile App Server
echo ========================================================
echo       Starting Khaata Standalone Mobile App...
echo ========================================================
echo.
start http://127.0.0.1:8080
python -m http.server 8080
pause
