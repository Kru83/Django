from django.test import TestCase
import requests
import os
from dotenv import load_dotenv
load_dotenv()
# Create your tests here.

def congressMemberByState(state):
    state = state
    url = F"https://api.congress.gov/v3/member/{state}"
    key = os.getenv('CONGRESS_API_KEY')
    state = state

    headers = {
        "X-API-KEY": key,
    }

    response = requests.get(url, headers=headers)
    statusCode = response.status_code
    if statusCode == 200:
        congressMemberByState = response.json()
        return congressMemberByState
    else:
        print(F"Error {statusCode}")

def congressMemberListByState(congressMemberList):
    congressMemberData = congressMemberList

    congressMemberListByState = []

    for member in congressMemberData["members"]:
        member_info = {
            "name": member["name"],
            "partyName": member["partyName"],
            "district": member["district"],
            "state": member["state"],
            "chamber": member["terms"]["item"][0]["chamber"],
            "startYear": member["terms"]["item"][0]["startYear"],
            "imageUrl": member["depiction"]["imageUrl"],
        }
        congressMemberListByState.append(member_info)
    return congressMemberListByState

#congressMemberByState = congressMemberByState("FL")
#congressMemberListByState = congressMemberListByState(congressMemberByState)
#print(congressMemberListByState)

'''
for member in congressMemberData["members"]:
    name = member["name"]
    partyName = member["partyName"]
    district = member["district"]
    state = member["state"]
    chamber = member["terms"]["item"][0]["chamber"]
    startYear = member["terms"]["item"][0]["startYear"]
    imageUrl = member["depiction"]["imageUrl"]
    print(name, partyName, district, state, chamber, startYear, imageUrl)
'''
congressMemberData = congressMemberByState("AL")
print(congressMemberData)

name = congressMemberData["members"][0]["name"]
partyName = congressMemberData["members"][0]["partyName"]
district = congressMemberData["members"][0]["district"]
state = congressMemberData["members"][0]["state"]
chamber = congressMemberData["members"][0]["terms"]["item"][0]["chamber"]
startYear = congressMemberData["members"][0]["terms"]["item"][0]["startYear"]
imageUrl = congressMemberData["members"][0]["depiction"]["imageUrl"]
print(name, partyName, district, state, chamber, startYear, imageUrl)