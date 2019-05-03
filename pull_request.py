import requests
import json
from datetime import datetime, date, timedelta


class PullRequest:
    def __init__(self, end_point, params):
        res = requests.get(end_point, params=params)
        self.prs = json.loads(res.text)

    def get_prs(self, pr_url):
        arr = []
        if len(self.prs) > 0:
            for pr in self.prs:
                text = '\n' + str(pr['summary']) + '\n' + pr_url + str(
                    pr['number'])
                arr.append(text)
        return arr

    def get_prs_yesterday(self, pr_url):
        today = datetime.today()
        yesterday_datetime = today - timedelta(days=1)
        arr = []
        if len(self.prs) > 0:
            for pr in self.prs:
                created = datetime.strptime(pr['created'][0:10], '%Y-%m-%d')
                if created.date() == yesterday_datetime.date():
                    text = '\n' + str(pr['summary']) + '\n' + pr_url + str(
                        pr['number'])
                    arr.append(text)
                return arr
