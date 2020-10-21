import requests


class Requests:

    def __init__(self):
        self.base_url = 'http://165.227.93.41/lojinha'

    def register_user(self, user, login, password):
        # headers = {'Content-type': 'application/json'}
        url = f'{self.base_url}/usuario'

        body = {
            "usuarionome": user,
            "usuariologin": login,
            "usuariosenha": password
        }

        return requests.post(url=url, data=body)

    def login(self, login, password):
        url = f'{self.base_url}/login'

        body = {
            "usuariologin": login,
            "usuariosenha": password
        }

        return requests.post(url=url, data=body)

    def delete_user(self, token):
        url = f'{self.base_url}/dados'
        # headers = token
        headers = {'token': token}
        return requests.delete(url=url, headers=headers)
