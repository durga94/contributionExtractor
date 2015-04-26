# contributionExtractor
Python script to extract contributions from FOSS contribution database and post to FOSS website ( foss.amrita.ac.in)

# Usgae instructions
1. Create a local copy of the original <code>Contribution Database - FOSS@Amrita</code> in your Google Drive <br/>. Find more https://support.google.com/docs/answer/180897?hl=en
2. Download required module - <code> gspread </code> by <code> sudo pip install gspread </code>
2. Download the <code>getDetails.py</code> script and run it using  <code>$ python getDetails.py</code>

## Authentication
1. Give all required details as asked for. Please note to give your full gmail Email-id when asked for. The 'name of your copy of Contribution DB' is the name of the new spreadsheet you just created.
If everything match, you will get a message <code>"SpreadSheet opened"</code>

2. The program will do a linear scan, and list the contributions which it will come across
POSTing to FOSS Website<br/>

5. Once the program collects all info, it wil show contributions one by one so that you can select which one to be posted. You can confirm by entering <code>( Y/y )</code>  in your keyboard<br/>
6. If the POST was success, it will show a message <code>Updated contribution ($bug_id)</code>

7. Confirm the entry with the FOSS Website<br/>

##Report Bugs
If you find some bugs, please do report at <code>https://github.com/amfoss/contributionExtractor/issues</code>
##Improve performance

You can improve the linear search time, by sorting your spreadsheet with Your Name and deleting all others. Please make sure that you do that on your local copy of the same<br/>
##Contact

You can ping <code>tonythomas</code> on <code>#amfoss</code> on freenode IRC
