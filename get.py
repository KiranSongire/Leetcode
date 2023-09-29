import requests
# payload={"Name":"Harry","location":"USA"}
# r=requests.get("http://www.google.com", params=payload)
# print(r.content)

# payload={'title': "john",
#   'body': "John is an engineer",
#   'id': 101}
# res2=requests.post('https://httpbin.org/post',data=payload)
# print(res2.text)

jar=requests.cookies.RequestsCookieJar()
jar.set('location','India',domain='httpbin.org',path='/cookies')
jar.set('Name','Harry',domain='httpbin.org',path='/profile')
r=requests.get('https://httpbin.org/cookies',cookies=jar)
print(r.text)
{
"cookies": {
"location": "India"
}
}