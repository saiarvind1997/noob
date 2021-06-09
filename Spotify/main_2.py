#Modified to get the right output.
# Refer to this code for the full project.
from flask import Flask, redirect, request
import requests
from urllib.parse import quote
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
    url = "https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope={}&state={}".format(
        client_id, quote(redirect_uri), quote(scopes), state)

    return redirect(url, code=307)


@app.route('/connect')
def auth():

    # here we want to get the value of code (i.e. ?code=some-value)
    code = request.args.get('code')  # read about this.
    print("code is = " + code)

    # send this code to /api/token

    # convetiing it to base64 with the specified format
    client_cred = "{}:{}".format(client_id, client_secret)
    client_cred_64 = base64.b64encode(client_cred.encode())

    token_param = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri
    }

    token_header = {
        "Authorization": "Basic {}".format(client_cred_64.decode()),
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_url = "https://accounts.spotify.com/api/token/"
    rtoken = requests.post(token_url, headers=token_header, data=token_param)
    token_data = rtoken.json()
    print(token_data)

    # we got the access token
    access_token = token_data["access_token"]

    user_info = "https://api.spotify.com/v1/me/"
    user_info_req = requests.get(user_info, params=token_data)

    user_info_json = user_info_req.json()

    user_info_id = user_info_json["id"]

    output_file_name = "{}.json".format(user_info_id)
    print(output_file_name)

    with open(output_file_name, 'w+') as file:

        lib_url = "https://api.spotify.com/v1/me/tracks?limit={}&offset={}".format(
            50, 0)

        track_list = []

        while lib_url is not None:

            print("Getting tracks")

            lib_request = requests.get(lib_url, params=token_data)
            library_json = lib_request.json()

            # print(json.dumps(library_json))

            lib_next_url = library_json["next"]

            # set lib_url as next_url
            lib_url = lib_next_url

            lib_limit = int(library_json["limit"])

            print("lib_limit " + str(lib_limit))
            print("lib_next_url " + str(lib_next_url))

            track_total = int(library_json["total"])

            print("track_total " + str(track_total))

            # loop items
            for item in library_json["items"]:
                lib_end_name = item["track"]["name"]
                lib_end_id = item["track"]["id"]
                lib_end_uri = item["track"]["uri"]

                t_dict = {
                    "name": lib_end_name,
                    "id": lib_end_id,
                    "uri": lib_end_uri
                }

                print(t_dict)

                track_list.append(t_dict)

        saved_dict = {}
        saved_dict["saved"] = track_list

        t_track_str = json.dumps(saved_dict)

        print("Writing... " + str(len(track_list)))

        file.write(t_track_str)

        # while lib_next_url != "null":
        #     track_counter = 0
        #     tmp_list = []

        #     while track_counter < lib_limit and total_track_num <= track_total:

        #         lib_end_name = library_json["items"][track_counter]["track"]["name"]
        #         lib_end_id = library_json["items"][track_counter]["track"]["id"]
        #         lib_end_uri = library_json["items"][track_counter]["track"]["uri"]

        #         t_dict = {
        #             "name": lib_end_name,
        #             "id": lib_end_id,
        #             "uri": lib_end_uri
        #         }

        #         print(t_dict)

        #         tmp_list.append(t_dict)
        #         track_counter += 1
        #         total_track_num += 1

        #         print(total_track_num)

        #     # t_track_str=json.dumps(tmp_list)
        #     # f.write(t_track_str)
        #     track_list = track_list+tmp_list

        #     lib_url = lib_next_url
        #     lib_request = requests.get(lib_url, params=token_data)
        #     library_json = lib_request.json()
        #     lib_next_url = library_json["next"]

        #     print(lib_next_url)

    file.close()
    return t_track_str


if __name__ == '__main__':
    app.run()
