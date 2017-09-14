# Enable Flask's debugging features. Should be False in production

class MainConfig:
    DEBUG = True
    CLIENTSECRETS_LOCATION = '/Users/sanand/Documents/workspace-main/virtualenvs/flask-demo/config/client_secret.json'
    REDIRECT_URI = 'http://localhost:5000/ns-gmail/access_token'
    SCOPES = [
        'https://www.googleapis.com/auth/gmail.readonly',
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile'
    ]

    SERVICE_ACCOUNT_LOCATION = '/Users/sanand/Documents/workspace-main/virtualenvs/flask-demo/config/service_account/ns-gmail-158af621105c.json'
    SERVICE_ACCOUNT_SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']
