import json
#import yaml

user_model = {
    "email": 'user_email',
    "password": 'user_password',
    "remember": False
}
with open('sample_users_with_id.json') as jsonfile:
    json_users_data = json.load(jsonfile)

