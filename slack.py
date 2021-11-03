# slack token
import requests
f = open('slackToken.txt','r')
myToken = f.read()
print(myToken)

def post_message(token,channel,text):
    """send Slack message"""
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization":"Bearer "+token},
                             data={"channel":channel,"text":text}
                             )
    print(response)