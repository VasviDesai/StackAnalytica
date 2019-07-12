import json
import requests


def getTrendingRepo(language, since):
    parameters = {"language": language, "since": since}
    response = requests.get("https://github-trending-api.now.sh/repositories", params=parameters)

    # Get the response data as a python object.  Verify that it's a dictionary.
    data = response.json()
    # print(data)
    custom_data = []
    for i in range(0, 5):
        custom_data.append({
            'author': data[i]['author'],
            'name': data[i]['name'],
            'description': data[i]['description'],
            'url': data[i]['url']
        })
    return custom_data
    # with open("templates/"+language + '_' + 'git' + '.json', 'w', encoding='utf-8') as outfile:
    #     json.dump(custom_data, outfile, ensure_ascii=False)


# getTrendingRepo('javascript', 'daily')

# getTrendingRepo('python','daily')
# getTrendingRepo('java','daily')
