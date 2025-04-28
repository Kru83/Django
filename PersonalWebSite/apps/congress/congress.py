import requests
import os
from dotenv import load_dotenv
load_dotenv()

def congressMemberByState(state):
    state = state
    url = F"https://api.congress.gov/v3/member/{state}"
    key = os.getenv('CONGRESS_API_KEY')

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

    member_list = []

    for member in congressMemberData["members"]:
        member_info = {
            "name": member["name"],
            "partyName": member["partyName"],
            "district": member.get("district", "N/A"),
            "state": member["state"],
            "chamber": member["terms"]["item"][0]["chamber"],
            "startYear": member["terms"]["item"][0]["startYear"],
            "imageUrl": member["depiction"]["imageUrl"],
        }
        member_list.append(member_info)
    return member_list

#congressMemberByState = congressMemberByState("FL")
#congressMemberListByState = congressMemberListByState(congressMemberByState)
#print(congressMemberListByState)