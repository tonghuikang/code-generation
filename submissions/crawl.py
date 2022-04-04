import urllib.request
import json

def download_codeforces_user_submissions_id(user_handle):

    user_submissions_api = """
    https://codeforces.com/api/user.status?handle={}
    """.strip()

    with urllib.request.urlopen(user_submissions_api.format(user_handle)) as url:
        data = json.loads(url.read().decode())

    with open('codeforces/{}.json'.format(user_handle), "w") as f:
        json.dump(data, f, indent=4)
