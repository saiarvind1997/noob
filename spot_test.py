import requests
import base64
client_id="077ad5e5a8f7477481dce043012c064d"
client_secret="9f02e50cc0024659b555449921354fb7"
scope="user-read-private%20user-read-email%20user-library-read"
redirect_uri= "http://localhost:5000/"   #"http://127.0.0.1:5000/"  
state="s123"
url='https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope={}&state={}'.format(client_id,redirect_uri,scope,state)

r=requests.get(url,allow_redirects=True)
print(r.url)
print(r.json)
print("\n\n")

client_cred= "{}:{}".format(client_id,client_secret)
client_cred_64=base64.b64encode(client_cred.encode())

token_param={
"grant_type":"authorization_code",
"code": "authorization_code",
"redirect_uri" : redirect_uri
}
token_header={
"Authorization" : "Basic {}".format(client_cred_64.decode())
}
print (token_header) 
token_url="https://accounts.spotify.com/api/token/"
rtoken=requests.post(token_url,params=token_param,headers=token_header)




'''get_param={
  "client_id":client_id,
  "redirect_uri":redirect_uri,
  "scope":scope,
  "state":state
}
url1='https://accounts.spotify.com/authorize?'
r=requests.get(url1,params=get_param, allow_redirects=True)
'''


'''
app.get('/login', function(req, res) {
var scopes = 'user-read-private user-read-email';
res.redirect('https://accounts.spotify.com/authorize' +
  '?response_type=code' +
  '&client_id=' + my_client_id +
  (scopes ? '&scope=' + encodeURIComponent(scopes) : '') +
  '&redirect_uri=' + encodeURIComponent(redirect_uri));
});'''


'''
url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=a1878c5853a94b97b1bb68c37673b039"
r=requests.get(url)
js=r.json
print(js)
print (r.text)
'''

'''
#print (r.text)
js_title=js["articles"][0]["title"].values()
print (js_title)
'''