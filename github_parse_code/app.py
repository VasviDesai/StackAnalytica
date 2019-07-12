from flask import Flask, render_template
import github_parse as git_script
# import stacktrends as stack_script
import json

app = Flask(__name__)

language_selected = None


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/java')
def java():
    custom_data = git_script.getTrendingRepo('java', 'daily')
    json_object = json.dumps(custom_data)
    print("Trending repositories rendered on web-portal")
    print(json_object)
    return render_template('Analytics.html', language='Java', custom_data=json_object)


@app.route('/javascript')
def javascript():
    custom_data = git_script.getTrendingRepo('javascript', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='Javascript', custom_data=json_object)


@app.route('/python')
def python():
    custom_data = git_script.getTrendingRepo('python', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='Python', custom_data=json_object)


@app.route('/EmailSubscription')
def submit():
    # language_selected = request.form['language2']
    print(language_selected, 'okk')
    stack_data = stack_script.stack_data('python')
    return render_template('EmailSubscription.html')


if __name__ == '__main__':
    app.run()
