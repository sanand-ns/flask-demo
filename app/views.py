from flask import render_template
from flask import redirect
from flask import request
from flask import jsonify
import httplib2
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from apiclient.discovery import build

from app import flask_app
from src import test

store = {}


@flask_app.route('/')
def home():
    print("---- Starting in the / endpoint ---- ")
    test.test_02()
    return render_template('index.html')


@flask_app.route('/about')
def about():
    """Shows the about page of the application.
    """
    return render_template('about.html')


@flask_app.route('/login')
def login():
    """Retrieve the authorization URL.
    Returns:
            Redirects to the Authorization URL
    """
    flow = flow_from_clientsecrets(
        flask_app.config["CLIENTSECRETS_LOCATION"], ' '.join(flask_app.config["SCOPES"]))
    flow.params['access_type'] = 'offline'
    flow.params['approval_prompt'] = 'force'
    print(flow.step1_get_authorize_url(flask_app.config["REDIRECT_URI"]))
    return redirect(flow.step1_get_authorize_url(flask_app.config["REDIRECT_URI"]), code=302)


@flask_app.route('/ns-gmail/access_token')
def get_authorization_code():
    """Retrieve the authorization code from the token that comes in the oAuth Redirect URI.
    Returns:
            The authorization code received after the successful authorization
    """
    print("------ Getting Authz code ---------- ")
    print(request.args.get('code'))
    authz_code = request.args.get('code')
    return render_template('index.html', response="No API has been fired yet!", authz_code=authz_code)


@flask_app.route('/user_info')
def get_user_information():
    """Send a request to the UserInfo API to retrieve the user's information.
Args:
credentials: authorization_code from the initial API call
Returns:
User information as a dict.
"""
    print("-------------- Getting the user Information from the API call --------------")

    authz_code = request.args.get('authz_code')

    print("Authz code(in user_info) is:")
    print(authz_code)

    if not authz_code:
        return jsonify({
            'status': 400,
            'message': 'Invalid Authz Code Supplied'
        })

    flow = flow_from_clientsecrets(
        flask_app.config["CLIENTSECRETS_LOCATION"], ' '.join(flask_app.config["SCOPES"]))
    flow.redirect_uri = flask_app.config["REDIRECT_URI"]
    credentials = flow.step2_exchange(authz_code)

    if not credentials:
        return jsonify({
            'status': 400,
            'message': 'Authentication could not be retrieved'
        })

    user_info_service = build(
        serviceName='oauth2', version='v2',
        http=credentials.authorize(httplib2.Http()))
    user_info = None
    user_info = user_info_service.userinfo().get().execute()
    print("---------- Priting User Info ----------")
    print(user_info)

    # storing the credentials with the UserID
    user_id = user_info.get('id')

    store[user_id] = credentials

    print(credentials.access_token)

    return jsonify({
        'status': 200,
        'message': 'Success',
		'user': {
			'user_id': user_info.get('id'),
			'access_token': credentials.access_token
		}
    })


@flask_app.route('/user_labels')
def get_user_labels():

    user_id = request.args.get('user_id')
    access_token = request.args.get('access_token')

    print("Access Token is:")
    print(access_token)

    print("------------------------- Store retriving --------------- ")
    print(store.get(user_id))

    if not user_id or not access_token:
        return jsonify({
            'status': 400,
            'message': "Invalid UserID/Authz Code Supplied"
        })

    # credentials = flow.step2_exchange(authz_code)
    # http = credentials.authorize(httplib2.Http())
    # service = discovery.build('gmail', 'v1', http=http)
    # results = service.users().labels().list(userId=user_id).execute()
    # labels = results.get('labels', [])
    # print("------- Printing Labels ---------")
    # print(labels)

    print(user_id, access_token)

    return jsonify({
        'status': 400,
        'message': "labels are correct"
    })