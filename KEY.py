import requests

url = "https://hh.ru/oauth/authorize"
params = {"response_type": "code", "client_id": "SUR3TEM6GAPICF6I8CSDKIAEDLOF906MHTUV96K7PITHL1BAT8J19CB739T1UM3R"}
# https://hh.ru/oauth/authorize?response_type=code&client_id=SUR3TEM6GAPICF6I8CSDKIAEDLOF906MHTUV96K7PITHL1BAT8J19CB739T1UM3R

# url = "https://api.hh.ru/token"
headers = {"User-Agent": "Console application of suitable vacancies/1.0 (andrianov_maksim@outlook.com)"}
# params = {
#     "client_id" : "SUR3TEM6GAPICF6I8CSDKIAEDLOF906MHTUV96K7PITHL1BAT8J19CB739T1UM3R",
#     "client_secret" : "J5TM5P8P0QNEH39CUB53FT2KR96MU4BCK7Q379D8Q4FC5IPM7PV8BKK89LJBUOIC",
#     "code" : 58028617,
#     "grant_type" : "authorization_code",
#     "redirect_uri" : "https://github.com/MaksoN12340987/Coursework_OOP_Andrianov_M_S"
# }
response = requests.get(url, headers=headers, params=params)
print(response)

vacancies = response.text
with open("return.py", "w") as file:
    file.write(f"OUTPUT DATA:\n{str(vacancies)}\n")

print(vacancies)
