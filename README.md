<h2>contributionExtractor</h2>
Python script to extract contributions from FOSS contribution database and post to FOSS website ( foss.amrita.ac.in)

<h4>Usgae instructions</h4>
1. Create a local copy of the original ''Contribution Database - FOSS@Amrita'' in your Google Drive <br/>
2. Download the getDetails.py script and run it using  python getDetails.py<br/>

3. Authentication<br/>
Give all required details as asked for. Please note to give your full gmail Email-id when asked for. The 'name of your copy of Contribution DB' is the name of the new spreadsheet you just created.
If everything match, you will get a message  "SpreadSheet opened".<br/>

4. The program will do a linear scan, and list the contributions which it will come across
POSTing to FOSS Website<br/>

5. Once the program collects all info, it wil show contributions one by one so that you can select which one to be posted. You can confirm by entering ( Y/y )  in your keyboard<br/>
6. If the POST was success, it will show a message Updated contribution ($bug_id)<br/>

7. Confirm the entry with the FOSS Website<br/>
<h4>Report Bugs</h4>
If you find some bugs, please do report at https://github.com/amfoss/contributionExtractor/issues<br/>
<h4>Improve performance<h4>

You can improve the linear search time, by sorting your spreadsheet with Your Name and deleting all others. Please make sure that you do that on your local copy of the same<br/>
<h4>Contact</h4>

You can ping tonythomas on #amfoss on freenode IRC
