from flask import Flask,redirect,request
import requests
from urllib.parse import quote#
import requests
import base64
import json
app = Flask(__name__)
client_id = "077ad5e5a8f7477481dce043012c064d"
client_secret = "9f02e50cc0024659b555449921354fb7"
scopes = "user-read-private user-read-email user-library-read playlist-read-private"
auth_url = "https://accounts.spotify.com/authorize"
redirect_uri = "http://localhost:5000/connect"
state = "s123"

@app.route('/')
def hello_world():

    url = "https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope={}&state={}".format(client_id,quote(redirect_uri),quote(scopes),state)
    
    return redirect(url, code=307)

@app.route('/connect')
def auth():

    # here we want to get the value of code (i.e. ?code=some-value)
    code = request.args.get('code')#read about this.
    print("code is = " + code)

     # send this code to /api/token

    client_cred= "{}:{}".format(client_id,client_secret) #convetiing it to base64 with the specified format
    client_cred_64=base64.b64encode(client_cred.encode())

    token_param={
    "grant_type" : "authorization_code",
    "code" : code,
    "redirect_uri" : redirect_uri
    }
    token_header={
    "Authorization" : "Basic {}".format(client_cred_64.decode()),
    "Content-Type": "application/x-www-form-urlencoded"
    }

    token_url="https://accounts.spotify.com/api/token/"
    rtoken=requests.post(token_url,headers=token_header,data=token_param)
    token_data=rtoken.json()
    print (token_data)

    access_token=token_data["access_token"]

    end_headers={
        "Authorization":access_token
    }
    end_parameters={
        "limit":50,
        "offset":0
    }
    #["items"]["external_uri"]["spotify"][0]
    api_endpoint="https://api.spotify.com/v1/me/playlists?limit={}&offset={}".format(50,0)
    end_rp=requests.get(api_endpoint, params=token_data)
    json_obj=json.dumps(end_rp.json())
    print (type(json_obj))
    return end_rp.json()

if __name__ == '__main__':
    app.run()
