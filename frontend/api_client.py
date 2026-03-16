import requests

BASE_URL = "http://127.0.0.1:8080"

class ApiClient:
    @staticmethod
    def get_clientes():
        try:
            return requests.get(f"{BASE_URL}/clientes/").json()
        except:
            return []

    @staticmethod
    def create_cliente(nome, email):
        payload = {"nome": nome, "email": email, "is_active": True}
        return requests.post(f"{BASE_URL}/clientes/", json=payload).json()

    @staticmethod
    def get_marcas():
        return requests.get(f"{BASE_URL}/fipe/marcas").json()

    @staticmethod
    def get_modelos(marca_id):
        return requests.get(f"{BASE_URL}/fipe/marcas/{marca_id}/modelos").json()

    @staticmethod
    def get_anos(marca_id, modelo_id):
        return requests.get(f"{BASE_URL}/fipe/marcas/{marca_id}/modelos/{modelo_id}/anos").json()

    @staticmethod
    def create_veiculo(cliente_id, marca, modelo, ano, motorizacao, categoria):
        payload = {
            "cliente_id": cliente_id,
            "marca": marca,
            "modelo": modelo,
            "ano": int(ano) if ano else 0,
            "motorizacao": motorizacao,
            "categoria": categoria
        }
        return requests.post(f"{BASE_URL}/veiculos/", json=payload).json()

    @staticmethod
    def get_veiculos(cliente_id):
        return requests.get(f"{BASE_URL}/clientes/{cliente_id}/veiculos").json()

    @staticmethod
    def get_recomendacao(veiculo_id):
        return requests.get(f"{BASE_URL}/recomendação/{veiculo_id}").json()
