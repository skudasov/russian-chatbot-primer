import requests
HOST = 'http://localhost:5005/'
RECEPIENT = 'default2'

def test_path_skipped():
    print(requests.post('%sconversations/%s/respond' % (HOST, RECEPIENT), json={"query":"вези большую пиццу"}).text)
    print(requests.post('%sconversations/%s/respond' % (HOST, RECEPIENT), json={"query":"что еще ты можешь сделать для меня"}).text)

def test_path_no_addons():
    print(requests.post('%sconversations/%s/respond' % (HOST, RECEPIENT), json={"query":"вези большую пиццу"}).text)
    print(requests.post('%sconversations/%s/respond' % (HOST, RECEPIENT), json={"query":"с ветчиной"}).text)
