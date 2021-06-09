#Refer to main_3.py for all the mistakes and drafts.
#This code works after cleaning and changing a few loops.
from flask import Flask,redirect,request
import requests
from urllib.parse import quote#
import requests
import base64
import json
app = Flask(__name__)
app.config['TESTING'] = True
client_id = "077ad5e5a8f7477481dce043012c064d"
client_secret = "9f02e50cc0024659b555449921354fb7"
scopes = "user-read-private user-read-email user-library-read playlist-read-private playlist-read-collaborative"
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

    user_info="https://api.spotify.com/v1/me/"
    user_info_req=requests.get(user_info, params=token_data)
    user_info_json=user_info_req.json()
    user_info_id=user_info_json["id"]
    file_name="{}.json".format(user_info_id)

    
    
 
    
    with open(file_name,'w+') as f:
        lib_end="https://api.spotify.com/v1/me/tracks?limit={}&offset={}".format(50,0)
        saved_dict={}
        track_list=[]
        while lib_end is not None:

            lib_end_req=requests.get(lib_end, params=token_data)
            lib_end_json=lib_end_req.json()
            lib_end_next=lib_end_json["next"]

            lib_limit=int(lib_end_json["limit"])
            print (lib_limit)
            track_total=int(lib_end_json["total"])
            print (track_total)

            for items in lib_end_json["items"]:
                lib_end_name=items["track"]["name"]
                lib_end_id=items["track"]["id"]
                lib_end_uri=items["track"]["uri"]
                
                t_dict={"name":lib_end_name,
                    "id":lib_end_id,
                    "uri":lib_end_uri}

                print (t_dict)
                track_list.append(t_dict)
            
            lib_end=lib_end_next
            print(lib_end)

            #t_track_str=json.dumps(tmp_list)
            #f.write(t_track_str)

        
        saved_dict["Saved"]=track_list
        t_track_str=json.dumps(saved_dict)
        print (len(track_list))
        f.write(t_track_str)   

            
    f.close()          
    return lib_end_json
if __name__ == '__main__':
    app.run()

