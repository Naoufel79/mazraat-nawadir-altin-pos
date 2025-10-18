# Daily Product List Email Setup Instructions

This guide will help you set up automatic daily emails containing your product list and quantities to kharroubi.naoufel@gmail.com at 03:00 AM every day.

## Step 1: Configure Gmail App Password

To send emails from your Gmail account, you need to create an App Password:

1. Go to your Google Account: https://myaccount.google.com/
2. Select **Security** from the left menu
3. Enable **2-Step Verification** if not already enabled
4. Once 2-Step Verification is enabled, go back to Security
5. Under "How you sign in to Google", select **App passwords**
6. Select app: **Mail**
7. Select device: **Windows Computer**
8. Click **Generate**
9. Copy the 16-character password (it will look like: xxxx xxxx xxxx xxxx)

## Step 2: Update Email Settings

1. Open the file: `Point_De_Vente/Point_De_Vente/settings.py`
2. Find the email settings section at the bottom
3. Replace the following values:
   ```python
   EMAIL_HOST_USER = 'kharroubi.naoufel@gmail.com'  # Replace with your actual Gmail address
   EMAIL_HOST_PASSWORD = 'Aa@191079'  # Replace with the 16-character app password
   DEFAULT_FROM_EMAIL = 'kharroubi.naoufel@gmail.com'  # Replace with your actual Gmail address
   ```

## Step 3: Test the Email Manually

Before setting up the automatic schedule, test the email command:

1. Open Command Prompt
2. Navigate to the Point_De_Vente directory:
   ```
   cd "c:\Users\knaou\OneDrive\Commandes Figs\web_site\Point_De_Vente"
   ```
3. Run the command:
   ```
   python manage.py send_daily_product_list
   ```
4. Check kharroubi.naoufel@gmail.com inbox for the email
5. If successful, you'll see: "Successfully sent product list to kharroubi.naoufel@gmail.com"

## Step 4: Set Up Windows Task Scheduler

Now configure Windows to run the email automatically at 03:00 AM every day:

### Option A: Using Task Scheduler GUI

1. Press `Win + R`, type `taskschd.msc`, press Enter
2. Click **Create Basic Task** in the right panel
3. Name: "Daily Product Email"
4. Description: "Send daily product list to kharroubi.naoufel@gmail.com"
5. Click **Next**
6. Trigger: Select **Daily**, click **Next**
7. Start date: Today's date
8. Start time: **03:00:00** (3:00 AM)
9. Recur every: **1 days**
10. Click **Next**
11. Action: Select **Start a program**, click **Next**
12. Program/script: Browse to `send_daily_email.bat` file:
    ```
    c:\Users\knaou\OneDrive\Commandes Figs\web_site\Point_De_Vente\send_daily_email.bat
    ```
13. Start in: Enter the directory:
    ```
    c:\Users\knaou\OneDrive\Commandes Figs\web_site\Point_De_Vente
    ```
14. Click **Next**, then **Finish**

### Option B: Using PowerShell Command

Open PowerShell as Administrator and run:

```powershell
$action = New-ScheduledTaskAction -Execute "c:\Users\knaou\OneDrive\Commandes Figs\web_site\Point_De_Vente\send_daily_email.bat" -WorkingDirectory "c:\Users\knaou\OneDrive\Commandes Figs\web_site\Point_De_Vente"
$trigger = New-ScheduledTaskTrigger -Daily -At 03:00AM
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType Interactive
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
Register-ScheduledTask -TaskName "Daily Product Email" -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description "Send daily product list to kharroubi.naoufel@gmail.com"
```

## Step 5: Verify Task Scheduler Setup

1. Open Task Scheduler (`Win + R`, type `taskschd.msc`)
2. Find "Daily Product Email" in the task list
3. Right-click and select **Run** to test immediately
4. Check the email inbox to verify it works
5. Check the log file: `Point_De_Vente/email_log.txt` for execution history

## Troubleshooting

### Email not sending?

1. **Check Gmail settings**: Ensure 2-Step Verification is enabled and App Password is correct
2. **Check credentials**: Verify EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in settings.py
3. **Test manually**: Run `python manage.py send_daily_product_list` from command prompt
4. **Check error messages**: Look at the output for specific error details

### Task not running at scheduled time?

1. Ensure computer is turned on at 03:00 AM (or change time if needed)
2. Check Task Scheduler History tab for execution logs
3. Verify the batch file path is correct
4. Make sure Python is in system PATH

### Python command not found?

1. Find Python installation path: `where python` in command prompt
2. Update `send_daily_email.bat` to use full Python path:
   ```batch
   "C:\Path\To\Python\python.exe" manage.py send_daily_product_list
   ```

## Email Format

The email will contain:
- Subject: "Daily Product List - YYYY-MM-DD"
- Product name and quantity for each product
- Total number of products
- Total quantity across all products

## Changing the Schedule Time

To change from 03:00 AM to a different time:

1. Open Task Scheduler
2. Find "Daily Product Email" task
3. Right-click and select **Properties**
4. Go to **Triggers** tab
5. Edit the trigger and change the time
6. Click **OK** to save

## Notes

- The email will only be sent if there are products in the database
- A log file (`email_log.txt`) tracks each email execution
- Make sure your computer is on at the scheduled time for the email to be sent
- The email uses Gmail's SMTP server (smtp.gmail.com)
