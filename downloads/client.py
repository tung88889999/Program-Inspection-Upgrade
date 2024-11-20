import requests

url = 'http://127.0.0.1:5000/translate_page'
payload = {
    'text': '最终你会明白，金钱不能替代爱。扔给你的金钱，那不是爱，那是扔给乞丐的怜悯。',
    'target_language': 'la'
}
response = requests.post(url, json=payload)

print(response.json())