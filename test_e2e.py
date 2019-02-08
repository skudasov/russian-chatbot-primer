import requests
HOST = 'http://localhost:5005/'
RECEPIENT = 'default'

def test_path_no_addons():
    print(requests.post('%sconversations/%s/respond' % (HOST, RECEPIENT), json={"query":"хочу заказать большую пиццу"}).text)
    print(requests.post('%sconversations/%s/respond' % (HOST, RECEPIENT), json={"query":"с ветчиной"}).text)
