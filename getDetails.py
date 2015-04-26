#/usr/bin/python
import gspread
import re
import sys
import requests
import getpass
from pprint import pprint
from collections import defaultdict
from bs4 import BeautifulSoup

fossMemberRealName = ''
fossMemberUserName = ''
fossMemberPassword = ''

gmailUsername = ''
gmailPassword = ''

contributionDbName = ''
totalRowsInDb = 264

def getuserdetails():
    global fossMemberRealName, fossMemberPassword, fossMemberUserName, gmailUsername, gmailPassword, contributionDbName

    if not fossMemberPassword and not fossMemberUserName and not fossMemberRealName and not gmailPassword and not gmailUsername:
        fossMemberRealName = raw_input("Enter Your Real Name (as in contribution DB): ")
        fossMemberUserName = raw_input("Enter Your FOSS Username: ")
        fossMemberPassword = getpass.getpass("Enter your FOSS Password: ")
        gmailUsername = raw_input("Enter your gmail Email-id: ")
        gmailPassword = getpass.getpass("Enter your gmail password: ")
        contributionDbName = raw_input("Enter the name of your copy of Contribution DB: ")
    return


def getspreadsheet():
    gc = gspread.login(gmailUsername,gmailPassword )
    sh = gc.open(contributionDbName)
    if sh:
        print "SpreadSheet opened"
    return sh.get_worksheet(0)


def posttofosswebsite(client,form_data):
    url = "http://foss.amrita.ac.in/register/login"
    contributionUrl = "http://foss.amrita.ac.in/achievement/new/contribution"
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])

    print ("Bug ID : ", form_data.get('bug_id'), "Bug Org : ", form_data.get('org_name'),
           "Bug URL :", form_data.get('bug_url'), "Bug Desc:", form_data.get('bug_description'))
    choice = raw_input("Do You want to submit this (y/n)").lower()
    if choice in yes:
        post = client.post(contributionUrl, data=form_data, headers=dict(Referer=url))
        if post:
            print "Updated contribution! " + str(form_data.get('bug_id'))
    elif choice in no:
        print "Cancelled"
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")
    return


def insertintofosswebsite(contribution_field_dict) :
    global fossMemberRealName, fossMemberPassword, fossMemberUserName
    url = "http://foss.amrita.ac.in/register/login"
    client = requests.session()

    client.get(url)
    csrftoken = client.cookies['csrftoken']
    login_data = dict(username=fossMemberUserName, password=fossMemberPassword, csrfmiddlewaretoken=csrftoken, next='/')
    r = client.post(url, data=login_data, headers=dict(Referer=url))

    contributionUrl = "http://foss.amrita.ac.in/achievement/new/contribution"

    headers = {'User-Agent': 'Mozilla/5.0'}
    client.post(contributionUrl, headers=headers )

    for k in range(0,len(contribution_field_dict)):
        bug_id = contribution_field_dict.get(k).get('bug_id')
        bug_org = contribution_field_dict.get(k).get('bug_org')
        bug_url = contribution_field_dict.get(k).get('bug_url')
        bug_description = contribution_field_dict.get(k).get('bug_summary')

        form_data = {
            'bug_id': bug_id,
            'org_name': bug_org,
            'bug_url': bug_url,
            'bug_description': bug_description,
            'submit': 'submitted',
            'username': fossMemberUserName,
            'password': fossMemberPassword,
            'csrfmiddlewaretoken': csrftoken,
            'next': '/'
        }
        posttofosswebsite(client,form_data)
    return


def main():
    global totalRowsInDb
    getuserdetails()
    worksheet = getspreadsheet()
    print "Please wait as I scan through the Contribution Db"
    id = 100
    counter = 0
    contribution_field_dict = {}

    for i in range(1, totalRowsInDb ):
        if worksheet.cell(i, 8).value == fossMemberRealName:
            contribution_field_dict[counter] = {
                'bug_id': id,
                'bug_org': worksheet.cell(i, 2).value,
                'bug_url': worksheet.cell(i, 7).value,
                'bug_summary': worksheet.cell(i, 6).value
            }
            counter += 1
            print "Found new contribution!, Total: " + str(counter)
            id += 1

    print "Found all contributions! Please proceed to Update the FOSS website"
    insertintofosswebsite(contribution_field_dict)



if __name__ == "__main__":
    main()


