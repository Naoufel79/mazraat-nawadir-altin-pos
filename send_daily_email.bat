@echo off
REM Daily Product List Email Script
REM This script runs the Django management command to send product list email

cd /d "%~dp0"
python manage.py send_daily_product_list

REM Log the execution
echo %date% %time% - Email sent >> email_log.txt
