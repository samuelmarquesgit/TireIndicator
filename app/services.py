import requests
from typing import List, Dict

# Usando uma API pública da FIPE para dados reais
# Documentação sugerida: https://deividfortuna.github.io/fipe/
BASE_URL_FIPE = "https://parallelum.com.br/fipe/api/v1/carros"

class FipeService:
    @staticmethod
    def get_marcas() -> List[Dict]:
        try:
            response = requests.get(f"{BASE_URL_FIPE}/marcas")
            response.raise_for_status()
            return response.json()
        except:
            return []

    @staticmethod
    def get_modelos(marca_id: str) -> List[Dict]:
        try:
            response = requests.get(f"{BASE_URL_FIPE}/marcas/{marca_id}/modelos")
            response.raise_for_status()
            return response.json().get("modelos", [])
        except:
            return []

    @staticmethod
    def get_anos(marca_id: str, modelo_id: str) -> List[Dict]:
        try:
            response = requests.get(f"{BASE_URL_FIPE}/marcas/{marca_id}/modelos/{modelo_id}/anos")
            response.raise_for_status()
            return response.json()
        except:
            return []

class RecommendationEngine:
    @staticmethod
    def recommend_tires(veiculo_info: Dict) -> List[Dict]:
        # Lógica simplificada de recomendação baseada no modelo/categoria
        # Em um sistema real, isso consultaria uma base técnica de compatibilidade
        
        # Exemplo de base técnica "embutida" para demonstração
        tech_base = {
            "sedan": {"largura": 205, "perfil": 55, "aro": "R16"},
            "suv": {"largura": 225, "perfil": 65, "aro": "R17"},
            "hatch": {"largura": 175, "perfil": 70, "aro": "R13"},
            "pick-up": {"largura": 265, "perfil": 70, "aro": "R16"}
        }
        
        categoria = veiculo_info.get("categoria", "sedan").lower()
        specs = tech_base.get(categoria, tech_base["sedan"])
        
        # Simula retorno de pneus compatíveis
        return [
            {
                "marca": "Michelin",
                "modelo": "Primacy 4",
                "largura": specs["largura"],
                "perfil": specs["perfil"],
                "aro": specs["aro"],
                "indice_carga": 91,
                "velocidade": "V",
                "preco_estimado": 550.00
            },
            {
                "marca": "Pirelli",
                "modelo": "Cinturato P7",
                "largura": specs["largura"],
                "perfil": specs["perfil"],
                "aro": specs["aro"],
                "indice_carga": 91,
                "velocidade": "W",
                "preco_estimado": 480.00
            }
        ]
