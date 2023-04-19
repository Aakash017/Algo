import requests
import json
import random
url = "https://controlpanel-testing.pasarpolis.io/api/partner/policy-attributes/?product_code=personal-accident&partner_code=megafinance"
for i in range(2):
    payload = json.dumps({
      "dob": "2000-01-01",
      "email": "aakash.sharma@pasarpolis.com",
      "gender": "M",
      "ktp": "4975393901996495",
      "name": "Aakash",
      "package_id": "personal_accident_option2",
      "phone_no": "6299898989",
      "reference_id": f"ref600011{i}",
        "product_price":"1000000"
    })
    headers = {
      'authority': 'controlpanel-testing.pasarpolis.io',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'authorization': 'jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMTAsInVzZXJuYW1lIjoiYWFrYXNoLnNoYXJtYUBwYXNhcnBvbGlzLmNvLmlkIiwiZXhwIjoxNjc4MzU4MjA1LCJlbWFpbCI6ImFha2FzaC5zaGFybWFAcGFzYXJwb2xpcy5jby5pZCJ9.HTYJ54cb1Ue4SXEprc3Kq22PuY2in5Ik3vmyRpxjTbw',
      'content-type': 'application/json',
      'cookie': 'pasarpolis-_zldp=TgP47VGApuEIuDKb2hD4lOj3YYdzLJ6SEz4kL7TIhjdKjMKaRfV5TOCNqlE1W1BwlfjNUTqTZOU%3D; _hjSessionUser_2626307=eyJpZCI6IjY4OWM2ZTlhLWY3YWYtNTY5Ni04N2E0LTVmN2ZjMjQ5ZjdlNiIsImNyZWF0ZWQiOjE2NTI3OTI1MTAyMjIsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.2.913181920.1648019398; _ga_WNCMKTES14=GS1.1.1668760297.2.0.1668760297.0.0.0; ph_phc_1IUXCfSnBKiTOX4rsKNcHGAQ2B2IvDb3bffNmXvA1H8_posthog=%7B%22distinct_id%22%3A%22184836235f194f-0b8695e86d9c17-18525635-13c680-184836235f2e4c%22%2C%22%24device_id%22%3A%22184836235f194f-0b8695e86d9c17-18525635-13c680-184836235f2e4c%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22%24referrer%22%3A%22%24direct%22%2C%22%24referring_domain%22%3A%22%24direct%22%2C%22%24sesid%22%3A%5B1668760297426%2C%2218489dd5fd21222-03548d6a19d915-18525635-13c680-18489dd5fd3174b%22%5D%2C%22%24session_recording_enabled%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%7D; _hjSessionUser_2119773=eyJpZCI6ImIzNDFhYzc0LWNkZTItNWViOC1iMWRmLTkwNGE0ODg3OWNlZSIsImNyZWF0ZWQiOjE2NzUwNzg3NDQ1MzcsImV4aXN0aW5nIjp0cnVlfQ==; id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMTAsInVzZXJuYW1lIjoiYWFrYXNoLnNoYXJtYUBwYXNhcnBvbGlzLmNvLmlkIiwiZXhwIjoxNjc4MzU4MjA1LCJlbWFpbCI6ImFha2FzaC5zaGFybWFAcGFzYXJwb2xpcy5jby5pZCJ9.HTYJ54cb1Ue4SXEprc3Kq22PuY2in5Ik3vmyRpxjTbw; userProfile=%7B%22id%22%3A110%2C%22email%22%3A%22aakash.sharma%40pasarpolis.co.id%22%2C%22name%22%3A%22aakash%20sharma%22%2C%22phone%22%3Anull%2C%22user_language%22%3A%22en%22%2C%22user_timezone%22%3A%22Asia%2FJakarta%22%2C%22isAgentInsuranceProvider%22%3Afalse%7D; _gid=GA1.2.1880320617.1678363033; menu=partner',
      'origin': 'https://controlpanel-testing.pasarpolis.io',
      'referer': 'https://controlpanel-testing.pasarpolis.io/partner/test-create-policy/megafinance/personal-accident',
      'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)