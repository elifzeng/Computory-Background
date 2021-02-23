### escape day
```python
cd group_meeting/mail_alarm/
code exceptDays
# modify this file, add escape day in the form of del+the date
python schedule_generator.py
#update schedule
mv scheduleDATE.txt ../
mv scheduleDATE.txt latestSchedule.txt
#okk
        cd mail_alarm
        # generating MAIL_CONFIG: python mail_alarm.py -f ../latestSchedule.txt
        echo $MAIL_CONFIG > ~/.mail_config.json
        
        # without -run, only send mail to admin
        python3 mail_alarm.py -f ../latestSchedule.txt -sender nibs
