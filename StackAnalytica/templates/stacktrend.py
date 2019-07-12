import requests
import time
from datetime import datetime
import statistics
import operator
from stackapi import StackAPI
import json

data = {}
data['key'] = 'value'
json_data = json.dumps(data)

date_format = "%m-%d-%Y %H:%M:%S"

SITE = StackAPI('stackoverflow')
pythonUsers = {}
javaUsers = {}
jsUsers = {}
goUsers = {}
globalUsers = {}
language = ['python']

# --------users language-wise--------------

for i in language:
    resp = requests.get('https://api.stackexchange.com/2.2/tags/' + i + '/top-answerers/month?site=stackoverflow')
    gh = resp.json()
    for user in gh['items']:
        # globalUsers.update({user['user']['user_id']:user['score']})
        if i == 'python':
            pythonUsers.update({user['user']['user_id']: user['score']})
        # elif i == 'java':
        #     javaUsers.update({user['user']['user_id']: user['score']})
        # elif i == 'javascript':
        #     jsUsers.update({user['user']['user_id']: user['score']})
        # elif i == 'golang':
        #     goUsers.update({user['user']['user_id']: user['score']})

pythonUsers = sorted(pythonUsers.items(), key=operator.itemgetter(1), reverse=True)
pythonUsers = dict(pythonUsers)

# --------- Profile Score by StackOverFlow ---------

sd = statistics.stdev(list(pythonUsers.values()))
avg_resp = statistics.mean(list(pythonUsers.values()))
for key in pythonUsers:
    pythonUsers.update({key: ((pythonUsers.get(key) - avg_resp) / sd)})

# ---------Last Seen of The user-------------
profile_name = {}
profile_link = {}
activityScore = {}
activityScore_min = {}
for key in pythonUsers:
    resp = requests.get('https://api.stackexchange.com/2.2/users/' + str(key) +
                        '?order=desc&sort=reputation&site=stackoverflow')
    gh = resp.json()
    for user in gh['items']:
        profile_name.update({key: user['display_name']})
        profile_link.update({key: user['link']})

        last_seen = time.strftime('%m-%d-%Y %H:%M:%S', time.localtime(user['last_access_date']))
        time1 = datetime.strptime(last_seen, date_format)
        cur = datetime.now()
        activityScore.update({key: (cur - time1).seconds})
        activityScore_min.update({key: (cur - time1).seconds//60})

sd = statistics.stdev(list(activityScore.values()))
avg_resp = statistics.mean(list(activityScore.values()))

for key in activityScore:
    activityScore.update({key: ((activityScore.get(key) - avg_resp) / sd)})

# ----------- Approved Answer's Score and Average Response to the question ---------

approved_score = 0
approved_score_total = {}

response_time = 0
count = 0
response_score = {}
upvotes_analysis = 0
upvote_score = {}

for key in pythonUsers:
    resp = requests.get('https://api.stackexchange.com/2.2/users/' + str(key) +
                        '/tags/python/top-answers?order=desc&sort=activity&site=stackoverflow')
    gh = resp.json()
    for user in gh['items']:

        upvotes_analysis += user['score']

        if user['is_accepted']:
            approved_score += 10
        else:
            approved_score -= 15
        if 'last_edit_date' in user:
            last_seen = time.strftime('%m-%d-%Y %H:%M:%S', time.localtime(user['last_edit_date']))
            time1 = datetime.strptime(last_seen, date_format)
            last_seen = time.strftime('%m-%d-%Y %H:%M:%S', time.localtime(user['creation_date']))
            time2 = datetime.strptime(last_seen, date_format)
            response_time += (time1 - time2).seconds
        count += 1

    response_score.update({key: response_time / count})
    approved_score_total.update({key: approved_score})
    upvote_score.update({key: upvotes_analysis})
    upvotes_analysis = 0
    approved_score = 0
    response_time = 0
    count = 0

sd = statistics.stdev(list(response_score.values()))
avg_resp = statistics.mean(list(response_score.values()))
for key in response_score:
    response_score.update({key: ((response_score.get(key) - avg_resp) / sd)})

sd = statistics.stdev(list(approved_score_total.values()))
avg_resp = statistics.mean(list(approved_score_total.values()))
for key in approved_score_total:
    approved_score_total.update({key: ((approved_score_total.get(key) - avg_resp) / sd)})

sd = statistics.stdev(list(upvote_score.values()))
avg_resp = statistics.mean(list(upvote_score.values()))
for key in upvote_score:
    upvote_score.update({key: ((upvote_score.get(key) - avg_resp) / sd)})

# -------------Normalized_Score---------------

# normalized_score = list(pythonUsers.values()) + list(activityScore.values()) + list(response_score.values())
normalized_score = [x + (2 * y) + (3 * z) + (4 * w) + (3.5 * u) for x, y, z, w, u in
                    zip(list(pythonUsers.values()), list(activityScore.values()),
                        list(response_score.values()), list(approved_score_total.values()),
                        list(upvote_score.values()))]
# ---------Overall Profile evaluation--------
normalized_final_score = {}
for key, score in zip(profile_name.keys(), normalized_score):
    normalized_final_score.update({key: score})

print(pythonUsers)
print(activityScore)
print(approved_score_total)
print(response_score)
print(upvote_score)
print(normalized_final_score)
print(profile_name)
print(profile_link)
print(activityScore_min)

# data = {}
# data['Top_Users'] = []
# for profile_id, display_name, link, Score, Response_Time, Popularity, last_active in zip(profile_name.keys(), profile_name.values(),
#                                                                     profile_link.values(),
#                                                                     normalized_final_score.values(),
#                                                                     response_score.values(),
#                                                                     approved_score_total.values(),activityScore_min.values()):
#     data['Top_Users'].append({
#         'Profile_ID': profile_id,
#         'display_name': display_name,
#         'link': link,
#         'Score': Score,
#         'Response_Time': Response_Time,
#         'Popularity': Popularity,
#         'last_activity': last_active
#     })
#
# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)