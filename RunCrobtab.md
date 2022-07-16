
Add a new cron tab in Mac OS:

crontab -e

Then add item:

eg.
55 5 * * * osascript /Users/bangnguyen/Documents/autoLoadWebsite.scpt

Note:
+ Use https://crontab.guru/ to edit your schedule
+ First time of running, it may request some permissions, such as allow "cron" access Documents, "System Events"... So run it at least 1 time to make sure you grant all permissions and everything works