import requests

class IBGE:
  def __init__(self):
      self.url = 'https://servicodados.ibge.gov.br/api/v1/pesquisas'

  def get_pesquisas(self):
      try:
          response = requests.get(self.url)
          if response.status_code == 200:
              return response.json()
          else:
              raise Exception(f"Erro na requisição: {response.status_code}")
      except requests.RequestException as e:
          raise Exception(f"Erro na requisição: {str(e)}")