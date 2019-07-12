import requests
import time
from datetime import datetime
import statistics
import operator
import json

# --------- python's dictionary tag extracting is done here ---------------------
# for internal use only
def extract_popularity(json):
    try:
        return int(json['Top_Users']['Score'])
    except KeyError:
        return 0

# ------------- overall analysis, fetching of dynamic data from stakoverflow is done here------------------
def stack_data(language):

    # Defining date in a proper format which is used to compute response time for the answers by user
    date_format = "%m-%d-%Y %H:%M:%S"
    i = language

# -----------------------------users language-wise----------------------------------------------

    stackUsers = {}
    resp = requests.get('https://api.stackexchange.com/2.2/tags/' + i + '/top-answerers/month?site=stackoverflow')
    gh = resp.json()
    for user in gh['items']:
        # globalUsers.update({user['user']['user_id']:user['score']})
        stackUsers.update({user['user']['user_id']: user['score']})

    stackUsers = sorted(stackUsers.items(), key=operator.itemgetter(1), reverse=True)
    stackUsers = dict(stackUsers)
    print("\n"+i)

# --------- Profile Score by StackOverFlow ---------

    sd = statistics.stdev(list(stackUsers.values()))
    avg_resp = statistics.mean(list(stackUsers.values()))
    for key in stackUsers:
        stackUsers.update({key: ((stackUsers.get(key) - avg_resp) / sd)})

# ---------Last Seen of The user-------------
    profile_name = {}
    profile_link = {}
    activityScore = {}
    activityScore_min = {}
    for key in stackUsers:
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
            # measuring user's last activity on stackoverflow in hours
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
    raw_response_score = {}
    upvotes_analysis = 0
    upvote_score = {}

    for key in stackUsers:
        resp = requests.get('https://api.stackexchange.com/2.2/users/' + str(key) +
                            '/tags/'+i+'/top-answers?order=desc&sort=activity&site=stackoverflow')
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
        final_hours = response_time/count//60
        raw_response_score.update({key: final_hours})

        # score to represent the number of approved answers for a speicific language
        approved_score_total.update({key: approved_score})

        # score to represent user's average of total upvotes for a specific quetions & answers
        upvote_score.update({key: upvotes_analysis})

        upvotes_analysis = 0
        approved_score = 0
        response_time = 0
        count = 0

    # user's response score to the specific question in the language is computed here
    sd = statistics.stdev(list(response_score.values()))
    avg_resp = statistics.mean(list(response_score.values()))
    for key in response_score:
        response_score.update({key: ((response_score.get(key) - avg_resp) / sd)})

    # user's approval score is normalized here
    sd = statistics.stdev(list(approved_score_total.values()))
    avg_resp = statistics.mean(list(approved_score_total.values()))
    for key in approved_score_total:
        approved_score_total.update({key: ((approved_score_total.get(key) - avg_resp) / sd)})

    # user's upvote score is normalized here to make it comparable in charts
    sd = statistics.stdev(list(upvote_score.values()))
    avg_resp = statistics.mean(list(upvote_score.values()))
    for key in upvote_score:
        upvote_score.update({key: ((upvote_score.get(key) - avg_resp) / sd)})

    # -------------Normalized_Score---------------

    # normalized_score = list(stackUsers.values()) + list(activityScore.values()) + list(response_score.values())
    # Here Weights of each scores are multiplied
    # User's profile score has the mqximum weight followed by their approval score
    normalized_score = [5*x + (2 * y) + (3 * z) + (4 * w) + (3.5 * u) for x, y, z, w, u in
                        zip(list(stackUsers.values()), list(activityScore.values()),
                            list(response_score.values()), list(approved_score_total.values()),
                            list(upvote_score.values()))]

    # ---------Overall Profile evaluation--------
    normalized_final_score = {}
    for key, score in zip(profile_name.keys(), normalized_score):
        normalized_final_score.update({key: score})

    data = {}
    data['Top_Users'] = []
    for profile_id, display_name, link, Score, Response_Time, Popularity, last_active in zip(profile_name.keys(), profile_name.values(),
                                                                        profile_link.values(),
                                                                        normalized_final_score.values(),
                                                                        raw_response_score.values(),
                                                                        approved_score_total.values(),activityScore_min.values()):
        data['Top_Users'].append({
            'Profile_ID': profile_id,
            'display_name': display_name,
            'link': link,
            'Score': Score,
            'Response_Time': Response_Time,
            'Popularity': Popularity,
            'last_activity': last_active
        })
    print(raw_response_score)
    stack_data = json.dumps(data)
    with open(i+'_users.json', 'w') as outfile:
        json.dump(data, outfile)
    return stack_data