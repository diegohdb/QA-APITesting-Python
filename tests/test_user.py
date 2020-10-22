import unittest
from Requests.requests import Requests
from Resources import utils as Utils


class User(unittest.TestCase):

    def setUp(self):
        self.request = Requests()
        self.data = Utils.load_json_file("data.json")
        self.user = self.data['user']
        self.login = self.data['login']
        self.password = self.data['password']
        self.token = self.data['token']

    def test_register_user(self):
        response = self.request.register_user(self.user, self.login, self.password)
        print(response.status_code)
        if response.status_code == 201:
            response_dict = response.json()
            message = response_dict['message']
            username = response_dict['data']['usuarionome']
            userlogin = response_dict['data']['usuariologin']

            assert message == 'Usuário adicionado com sucesso' and username == self.user and userlogin == self.login
        else:
            assert False

    def test_login(self):
        response = self.request.login(self.login, self.password)

        if response.status_code == 200:
            response_dict = response.json()
            message = response_dict['message']
            data = response_dict['data']
            token = data['token']

            assert message == 'Sucesso ao realizar o login', 'Failed on message'
            # assert message == 'Sucesso ao fazer login', 'Failed on message'
            assert token == self.token

        else:
            assert False

    def test_delete_user(self):
        response = self.request.delete_user(self.token)
        assert response.status_code == 204
