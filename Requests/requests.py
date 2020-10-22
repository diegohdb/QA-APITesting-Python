import requests


class Requests:

    def __init__(self):
        self.base_url = 'http://165.227.93.41/lojinha'

    # Usuario Requests
    def register_user(self, user, login, password):
        url = f'{self.base_url}/usuario'

        body = {
            "usuarionome": user,
            "usuariologin": login,
            "usuariosenha": password
        }

        return requests.post(url=url, json=body)

    def login(self, login, password):
        url = f'{self.base_url}/login'

        body = {
            "usuariologin": login,
            "usuariosenha": password
        }

        return requests.post(url=url, json=body)

    def delete_user(self, token):
        url = f'{self.base_url}/dados'
        headers = {'token': token}
        return requests.delete(url=url, headers=headers)

    # Produtos Requests
    def add_product(self, token, product, product_value, product_colors_list, component_dicts):
        url = f'{self.base_url}/produto'
        body = {
            'produtonome': product,
            'produtovalor': product_value,
            'produtocores': product_colors_list,
            'componentes': component_dicts
        }
        headers = {'token': token}

        return requests.post(url=url, headers=headers, json=body)

    def get_products(self, token):
        url = f'{self.base_url}/produto'
        headers = {'token': token}
        return requests.get(url=url, headers=headers)

    def get_one_product(self, token, product_id):
        url = f'{self.base_url}/produto/{product_id}'
        headers = {'token': token}
        return requests.get(url=url, headers=headers)

    def edit_one_product(self, token, product_id, product, product_value, product_colors_list, component_dicts):
        url = f'{self.base_url}/produto/{product_id}'
        headers = {'token': token}
        body = {
            'produtonome': product,
            'produtovalor': product_value,
            'produtocores': product_colors_list,
            'componentes': component_dicts
        }
        return requests.put(url=url, headers=headers, json=body)

    def delete_product(self, token, product_id):
        url = f'{self.base_url}/produto/{product_id}'
        headers = {'token': token}
        return requests.delete(url=url, headers=headers)

    # Componente Requests
    def add_component(self, token, product_id, component_dict):
        url = f'{self.base_url}/produto/{product_id}/componente'
        body = component_dict
        headers = {'token': token}

        return requests.post(url=url, headers=headers, json=body)

    def get_all_components(self, token, product_id):
        url = f'{self.base_url}/produto/{product_id}/componente'
        headers = {'token': token}

        return requests.get(url=url, headers=headers)

    def get_component(self, token, product_id, component_id):
        url = f'{self.base_url}/produto/{product_id}/componente/{component_id}'
        headers = {'token': token}

        return requests.get(url=url, headers=headers)

    def edit_component(self, token, product_id, component_id, component_name, component_quantity):
        url = f'{self.base_url}/produto/{product_id}/componente/{component_id}'
        headers = {'token': token}
        body = {
            "componentenome": component_name,
            "componentequantidade": component_quantity
        }

        return requests.put(url=url, headers=headers, json=body)

    def delete_component(self, token, product_id, component_id):
        url = f'{self.base_url}/produto/{product_id}/componente/{component_id}'
        headers = {'token': token}

        return requests.delete(url=url, headers=headers)
