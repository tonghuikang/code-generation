import urllib.request
import json

from bs4 import BeautifulSoup


def download_codeforces_user_submissions_id(user_handle):
    # download_codeforces_user_submissions_id("huikang")

    user_submissions_api = f"""
    https://codeforces.com/api/user.status?handle={user_handle}
    """.strip()

    with urllib.request.urlopen(user_submissions_api) as url:
        data = json.loads(url.read().decode())

    with open('codeforces/{}.json'.format(user_handle), "w") as f:
        json.dump(data, f, indent=4)

    return data


def download_codeforces_code_given_submission_id(contest_id, submission_id):
    # print(download_codeforces_code_given_submission_id(1656, 151467849))
    
    submission_url = f"""
    http://codeforces.com/contest/{contest_id}/submission/{submission_id}'
    """

    submission_html = urllib.request.urlopen(submission_url).read().decode()
    code = BeautifulSoup(submission_html).find('pre').text
    return code
