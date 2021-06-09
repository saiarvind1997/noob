#This intial code does not work, since its out of bounds
# This also has a lot of redundancies.
# read about all the libiraries like urllib.parse.
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
    lib_end="https://api.spotify.com/v1/me/tracks?limit={}&offset={}".format(50,0)
    lib_end_req=requests.get(lib_end, params=token_data)
    lib_end_json=lib_end_req.json()
    lib_end_next=lib_end_json["next"]
    lib_limit=int(lib_end_json["limit"])
    print (lib_limit)
    print (lib_end_next)
    track_total=int(lib_end_json["total"])
    print (track_total)
    
    with open(file_name,'w+') as f:
        saved_dict={}
        track_list=[]
        total_track_num=0
        while lib_end_next!="null":
            track_counter=0
            tmp_list=[]
            while track_counter<lib_limit and total_track_num<=track_total:
                #since  while loop is looping by index, the last 9-10 songs will be counted as None as the index goes all the way to 50.
                # for is more effiecent to read from start to end
                # index is used for positional insert or delete.
                lib_end_name=lib_end_json["items"][track_counter]["track"]["name"]
                lib_end_id=lib_end_json["items"][track_counter]["track"]["id"]
                lib_end_uri=lib_end_json["items"][track_counter]["track"]["uri"]
                
                t_dict={"name":lib_end_name,
                    "id":lib_end_id,
                    "uri":lib_end_uri}

                print (t_dict)
                tmp_list.append(t_dict)
                track_counter+=1
                total_track_num+=1
                print (total_track_num)

            #t_track_str=json.dumps(tmp_list)
            #f.write(t_track_str)
            track_list=track_list+tmp_list

            lib_end2=lib_end_next
            lib_end_req=requests.get(lib_end2, params=token_data)
            lib_end_json=lib_end_req.json()
            lib_end_next=lib_end_json["next"]
            print(lib_end_next)
        
        saved_dict["Saved"]=track_list
        t_track_str=json.dumps(saved_dict)
        print (len(track_list))
        f.write(t_track_str)   

            
    f.close()          
    return lib_end_json
if __name__ == '__main__':
    app.run()

        
        #return lib_end_json

    
  
 
    '''
    
    while lib_end_next!="null":
        track_counter=0

        while track_counter<lib_limit:
            lib_end_name=lib_end_json["items"][track_counter]["track"]["name"]
            print (track_counter)
            print (lib_end_name)
            track_counter+=1
     
        lib_end2=lib_end_next
        lib_end_req=requests.get(lib_end2, params=token_data)
        lib_end_json=lib_end_req.json()
        lib_end_next=lib_end_json["next"]
        print(lib_end_next)
    '''

    
    
    '''
       api_endpoint="https://api.spotify.com/v1/me/playlists?limit={}&offset={}".format(50,0)

    end_rp=requests.get(api_endpoint, params=token_data)
    end_rp_json=end_rp.json() 




    lib_end2=lib_end_next
    lib_end_req2=requests.get(lib_end2, params=token_data)
    lib_end_json2=lib_end_req2.json()
    lib_end_next2=lib_end_json2["next"]
    lib_end_id2=lib_end_json2["items"][1]["track"]["name"]
    print(lib_end_id2)

    {"saved":[{"id":"1RnbXVoyt0yYFPfJqNiyMG","uri":"spotify:track:1RnbXVoyt0yYFPfJqNiyMG"}]}
    '''