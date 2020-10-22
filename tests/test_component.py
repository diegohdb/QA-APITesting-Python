import unittest

import pytest

from Requests.requests import Requests
from Resources import utils as Utils


class User(unittest.TestCase):

    def setUp(self):
        self.request = Requests()
        self.data = Utils.load_json_file("data.json")
        self.token = self.data['token']
        self.component_new = self.data['component_new']
        self.product_id = self.data['product_id']
        self.component_id = self.data['component_id']

    @pytest.mark.run(order=1)
    def test_add_component(self):
        response = self.request.add_component(self.token, self.product_id, self.component_new)

        if response.status_code == 201:
            response_dict = response.json()
            message = response_dict['message']
            data = response_dict['data']
            component_name = data['componentenome']
            component_quantity = data['componentequantidade']

            if data:
                self.component_id = data['componenteid']

            assert message == 'Componente de produto adicionado com sucesso', 'Failed on message'
            # assert message == 'Sucesso ao criar o componente de produto', 'Failed on message'
            assert component_name == self.component_new['componentenome'], 'Component name failed'
            assert component_quantity == self.component_new['componentequantidade'], 'Component quantity failed'
        else:
            assert False

    @pytest.mark.run(order=2)
    def test_get_all_components(self):
        response = self.request.get_all_components(self.token, self.product_id)

        if response.status_code == 200:
            response_dict = response.json()
            message = response_dict['message']
            data = response_dict['data']
            assert message == 'Listagem de componentes de produto realizada com sucesso', 'Failed on message'
            # assert message == 'Sucesso ao buscar os componentes de produtos', 'Failed on message'

            if data:
                self.component_id = data[-1]['componenteid']

        else:
            assert False

    @pytest.mark.run(order=3)
    def test_get_component(self):
        response = self.request.get_component(self.token, self.product_id, self.component_id)

        if response.status_code == 200:
            response_dict = response.json()
            message = response_dict['message']
            component_id = response_dict['data']['componenteid']
            component_name = response_dict['data']['componentenome']
            component_quantity = response_dict['data']['componentequantidade']

            assert message == 'Detalhando dados do componente de produto'
            # assert message == 'Sucesso ao buscar o componente de produto', 'Failed on message'
            assert self.component_id == component_id, 'Failed to get components'
            assert self.component_new['componentenome'] == component_name, 'Failed to get component name'
            assert self.component_new['componentequantidade'] == component_quantity, 'Failed to get component name'
        else:
            assert False

    @pytest.mark.run(order=4)
    def test_edit_component(self):
        response = self.request.edit_component(self.token, self.product_id, self.component_id,
                                               self.component_new['componentenome'], 300)

        if response.status_code == 200:
            response_dict = response.json()
            message = response_dict['message']
            data = response_dict['data']
            component_quantity = data['componentequantidade']

            assert message == 'Componente de produto alterado com sucesso', 'Failed on message'
            # assert message == 'Sucesso ao alterar o componente de produto', 'Failed on message'
            assert component_quantity == 300
        else:
            assert False

    @pytest.mark.run(order=5)
    def test_delete_component(self):
        response = self.request.delete_component(self.token, self.product_id, self.component_id)

        if response.status_code == 204:
            self.component_id = {}
            assert True
        else:
            assert False

    def tearDown(self):
        # Update the component id and refresh component id in data.json
        self.data["component_id"] = self.component_id
        Utils.update_json_file("data.json", self.data)
