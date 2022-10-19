# RemindMe

RemindMe is a web application that helps students keep track of their assignments and deadlines directly from the Canvas LMS application.

## How it Works

RemindMe works by allowing the user to sign into Canvas using their Canvas details. The Canvas API documentation uses an OAuth2 workflow for this authentication. After the user has been successfully authenticated, their assignment details are pulled from the assignment tab for their respective Canvas profile and are synced with a calender of their choice (either Google Calendar and Outlook Calendar for now).

I intend to add a feature that would display the assignments first and allow the user to select which assignments to sync to their calendar.

## Usefulness

While Canvas notifies students when assignments are posted, it is still up to them to continually check the platform for their assignment due dates. Some students opt to continually update their calenders with their assignment due dates manually, but this can quicly become tedious. RemindMe saves students the manual work by automatically syncing all available assignments with their calendars. They only have to go through the workflow of signing in and synchronizing the assignments once a week (or as often as they choose).


This is the Python version of the application implemented with Flask. I intend to create another implementation with Go.
