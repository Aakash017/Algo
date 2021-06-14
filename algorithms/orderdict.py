from collections import OrderedDict
request={
    "OldData": [
        {
            "RegistrationNumber4": "1234",
            "RegistrationNumber3": "A",
            "RegistrationNumber1": "MH",
            "RegistrationNumber": "MH-06-A-1234",
            "RegistrationNumber2": "06"
        }
    ],
    "DocumnetData": [
        {
            "DocumnetName": "PanCard",
            "DocumnetType": "PNG",
            "DocumentByte": {
                "document_bytes": "8HhIyoluJvvUYAAAAASUVORK5CYII="
            }
        }
    ],
    "commonfield": [
        {
            "AgentCode": "PBZ001",
            "IMDCode": "200932735046",
            "PolicyNo": "2312100101715700000",
            "CheckSumData": "F11FBB6B66412044A826A41111AC7E72",
            "AgentName": "Policy Bazar",
            "UserIP": "86.123.127.8",
            "SourceDate": "2019/08/02",
            "EndorsementName": "Correction In Registration Number",
            "Guid": "GUID1234"
        }
    ],
    "NewData": [
        {
            "RegistrationNumber4": "1255",
            "RegistrationNumber3": "A",
            "RegistrationNumber1": "MH",
            "RegistrationNumber": "MH-06-A-1255",
            "RegistrationNumber2": "06"
        }
    ]
}

r= OrderedDict()
r["commonfield"]=[request["commonfield"]]
r["OldData"]=[request["OldData"]]
r["NewData"]=[request["NewData"]]
r["DocumnetData"]=[request["DocumnetData"]]
# r = dict(r)
# print(r)
import json
print(json.dumps(r))


