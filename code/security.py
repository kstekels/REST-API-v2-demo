from user import User
import hmac

users = [
    User(1, 'karlis', 'qwerty')
]

username_mapping = { user.username: user for user in users}

userid_mapping = { user.id: user for user in users }

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and hmac.compare_digest(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)