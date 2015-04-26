contributionExtractor
Python script to extract contributions from FOSS contribution database and post to FOSS website ( foss.amrita.ac.in)

Usgae instructions
Create a local copy of the original ''Contribution Database - FOSS@Amrita'' in your Google Drive
Download the getDetails.py script and run it using  python getDetails.py
Authentication

Give all required details as asked for. Please note to give your full gmail Email-id when asked for. The 'name of your copy of Contribution DB' is the name of the new spreadsheet you just created
If everything match, you will get a message  SpreadSheet opened"
The program will do a linear scan, and list the contributions which it will come across
POSTing to FOSS Website

Once the program collects all info, it wil show contributions one by one so that you can select which one to be posted. You can confirm by entering ( Y/y )  in your keyborad
If the POST was success, it will show a message Updated contribution ($bug_id)
Confirm the entry with the FOSS Website
Report Bugs

If you find some bugs, please do report at https://github.com/amfoss/contributionExtractor/issues
Improve performance:

You can improve the linear search time, by sorting your spreadsheet with Your Name and deleting all others. Please make sure that you do that on your local copy of the same

Contact

You can ping tonythomas on #amfoss on freenode IRC
