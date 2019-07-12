from flask import Flask, render_template
import github_parse as git_script
import stacktrends as stack_script
import json

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('HomePage.html')


@app.route('/java')
def java():
    stack_data = stack_script.stack_data('java')
    custom_data = git_script.getTrendingRepo('java', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='java', custom_data=json_object, stack_data=stack_data)


@app.route('/javascript')
def javascript():
    stack_data = stack_script.stack_data('javascript')
    custom_data = git_script.getTrendingRepo('javascript', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='javascript', custom_data=json_object, stack_data=stack_data)


@app.route('/python')
def python():
    stack_data = stack_script.stack_data('python')
    custom_data = git_script.getTrendingRepo('python', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='python', custom_data=json_object, stack_data=stack_data)

@app.route('/swift')
def swift():
    stack_data = stack_script.stack_data('swift')
    custom_data = git_script.getTrendingRepo('swift', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='swift', custom_data=json_object, stack_data=stack_data)

@app.route('/ruby')
def ruby():
    stack_data = stack_script.stack_data('ruby')
    custom_data = git_script.getTrendingRepo('ruby', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='ruby', custom_data=json_object, stack_data=stack_data)

@app.route('/golang')
def golang():
    stack_data = stack_script.stack_data('golang')
    custom_data = git_script.getTrendingRepo('golang', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='golang', custom_data=json_object, stack_data=stack_data)

@app.route('/cplus')
def cplus():
    stack_data = stack_script.stack_data('c++')
    custom_data = git_script.getTrendingRepo('c++', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='c++', custom_data=json_object, stack_data=stack_data)
@app.route('/csharp')
def csharp():
    stack_data = stack_script.stack_data('c++')
    custom_data = git_script.getTrendingRepo('c++', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='c++', custom_data=json_object, stack_data=stack_data)

@app.route('/r')
def r():
    stack_data = stack_script.stack_data('r')
    custom_data = git_script.getTrendingRepo('r', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='r', custom_data=json_object, stack_data=stack_data)

@app.route('/php')
def php():
    stack_data = stack_script.stack_data('php')
    custom_data = git_script.getTrendingRepo('php', 'daily')
    json_object = json.dumps(custom_data)
    print(json_object)
    return render_template('Analytics.html', language='php', custom_data=json_object, stack_data=stack_data)


@app.route('/emailsubscribe')
def emailsubscribe():
    return render_template('EmailSubscription.html')


if __name__ == '__main__':
    app.run()
