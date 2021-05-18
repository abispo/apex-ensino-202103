import requests

API_URL = 'https://api.postmon.com.br/v1/cep/{}'
API_WEATHER_URL = 'https://goweather.herokuapp.com/weather/{}'

if __name__ == '__main__':
    cep = input("Digite o CEP: ")
    # timestamp inicio
    response = requests.get(API_URL.format(cep))
    # timestamp fim
    cep_info = response.json()

    response = requests.get(API_WEATHER_URL.format(cep_info.get('cidade')))
    clima_info = response.json()

    print(f"Endereço: {cep_info.get('logradouro')}")
    print(f"Cidade: {cep_info.get('cidade')}")
    print(f"Estado: {cep_info.get('estado')}")
    print(f"Temperatura: {clima_info.get('temperature')}")
