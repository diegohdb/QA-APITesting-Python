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
        self.product1 = self.data['product1']
        self.value1 = self.data['value1']
        self.colors_many = self.data['colors_many']
        self.colors_one = self.data['colors_one']
        self.component_one = self.data['components_one']
        self.component_many = self.data['components_many']
        self.product_id = self.data['product_id']

    def test_add_product(self):
        response = self.request.add_product(self.token, self.product1, self.value1, self.colors_one,
                                            self.component_one)
        if response.status_code == 201:
            response_dict = response.json()
            message = response_dict['message']
            assert message == 'Produto adicionado com sucesso', 'Failed on message'
            assert True
        else:
            assert False

    def test_get_products(self):
        response = self.request.get_products(self.token)

        if response.status_code == 200:
            response_dict = response.json()
            message = response_dict['message']
            data = response_dict['data']
            assert message == 'Listagem de produtos realizada com sucesso', 'Failed on message'
            # assert message == 'Sucesso ao buscar os produtos', 'Failed on message'
            if data:
                self.product_id = data[0]['produtoid']
        else:
            assert False

    def test_get_one_product(self):
        response = self.request.get_one_product(self.token, self.product_id)

        if response.status_code == 200:
            response_dict = response.json()
            message = response_dict['message']
            data = response_dict['data']
            product_id = data['produtoid']

            assert message == 'Detalhando dados do produto', 'Failed on message'
            assert product_id == self.product_id, 'Failed to get the product'
            # assert message == 'Sucesso ao buscar o produto', 'Failed on message'
        else:
            assert False

    def test_edit_product(self):
        response = self.request.edit_one_product(self.token, self.product_id, self.product1, 3000, self.colors_many,
                                                 self.component_one)

        if response.status_code == 200:
            response_dict = response.json()
            message = response_dict['message']
            data = response_dict['data']
            product_value = data['produtovalor']

            assert message == 'Produto alterado com sucesso', 'Failed on message'
            # assert message == 'Sucesso ao alterar o produto', 'Failed on message'
            assert product_value == 3000
        else:
            assert False

    def test_delete_product(self):
        response = self.request.delete_product(self.token, self.product_id)

        assert response.status_code == 204, 'Failed to delete product'

    def tearDown(self):
        # Update the product id and refresh product id in data.json
        self.data["product_id"] = self.product_id
        Utils.update_json_file("data.json", self.data)
