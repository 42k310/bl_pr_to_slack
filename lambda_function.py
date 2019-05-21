import json
import requests
import slackweb
import const_module
from datetime import datetime, date, timedelta
from pull_request import PullRequest

# FIXME: Lambdaに上げるときは、メソッドを定義する
# def lambda_handler(event, context):
work_arrs = []
work_arrs_yesterday = []
params = {
    'apiKey': const_module.BACKLOG_API_KEY,
    'assigneeId[]': [const_module.BACKLOG_USER_ID],
    'statusId[]': [const_module.PR_OPEN]
}

# common
common_prs = PullRequest(const_module.EP_COMMON_PR, params)
work_arrs.append(common_prs.get_prs(const_module.URL_COMMON_PR))
work_arrs_yesterday.append(
    common_prs.get_prs_yesterday(const_module.URL_COMMON_PR))
# sapi
sapi_prs = PullRequest(const_module.EP_SAPI_PR, params)
work_arrs.append(sapi_prs.get_prs(const_module.URL_SAPI_PR))
work_arrs_yesterday.append(sapi_prs.get_prs_yesterday(
    const_module.URL_SAPI_PR))
# rapi
rapi_prs = PullRequest(const_module.EP_RAPI_PR, params)
work_arrs.append(rapi_prs.get_prs(const_module.URL_RAPI_PR))
work_arrs_yesterday.append(rapi_prs.get_prs_yesterday(
    const_module.URL_RAPI_PR))
# smdl
smdl_prs = PullRequest(const_module.EP_SMDL_PR, params)
work_arrs.append(smdl_prs.get_prs(const_module.URL_SMDL_PR))
work_arrs_yesterday.append(smdl_prs.get_prs_yesterday(
    const_module.URL_SMDL_PR))
# mpwb
mpwb_prs = PullRequest(const_module.EP_MPWB_PR, params)
work_arrs.append(mpwb_prs.get_prs(const_module.URL_MPWB_PR))
work_arrs_yesterday.append(mpwb_prs.get_prs_yesterday(
    const_module.URL_MPWB_PR))
# nptl
nptl_prs = PullRequest(const_module.EP_NPTL_PR, params)
work_arrs.append(nptl_prs.get_prs(const_module.URL_NPTL_PR))
work_arrs_yesterday.append(nptl_prs.get_prs_yesterday(
    const_module.URL_NPTL_PR))
# sptl
sptl_prs = PullRequest(const_module.EP_SPTL_PR, params)
work_arrs.append(sptl_prs.get_prs(const_module.URL_SPTL_PR))
work_arrs_yesterday.append(sptl_prs.get_prs_yesterday(
    const_module.URL_SPTL_PR))
# async
async_prs = PullRequest(const_module.EP_ASYNC_PR, params)
work_arrs.append(async_prs.get_prs(const_module.URL_ASYNC_PR))
work_arrs_yesterday.append(
    async_prs.get_prs_yesterday(const_module.URL_ASYNC_PR))
# batch
batch_prs = PullRequest(const_module.EP_BATCH_PR, params)
work_arrs.append(batch_prs.get_prs(const_module.URL_BATCH_PR))
work_arrs_yesterday.append(
    batch_prs.get_prs_yesterday(const_module.URL_BATCH_PR))
# admin
admin_prs = PullRequest(const_module.EP_ADMIN_PR, params)
work_arrs.append(admin_prs.get_prs(const_module.URL_ADMIN_PR))
work_arrs_yesterday.append(
    admin_prs.get_prs_yesterday(const_module.URL_ADMIN_PR))

today = datetime.today()
today_str = today.strftime('%Y-%m-%d')

slack = slackweb.Slack(url=const_module.EP_SLACK)
work_arrs = filter(None, work_arrs)
work_arrs_yesterday = filter(None, work_arrs_yesterday)
post_arr = []
post_arr_yesterday = []
for work_arr_yes in work_arrs_yesterday:
    for tgt_yes in work_arr_yes:
        post_arr_yesterday.append(tgt_yes)
for work_arr in work_arrs:
    for tgt in work_arr:
        post_arr.append(tgt)
post_text = today_str + '\n' + '```🎯昨日、新しく追加されたプルリクエスト：' + str(
    len(post_arr_yesterday)) + '件' + '\n'.join(
        post_arr_yesterday) + '```' + '\n' + '```📝累積プルリクエスト：' + str(
            len(post_arr)) + '件' + '\n'.join(post_arr) + '```'
slack.notify(text=post_text)
