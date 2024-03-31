import requests


url_head = r'https://morebukv.ru/mask/'

vowels = 'аиеёоуюя'
used = set('пирог').union('макет')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

for letter in vowels:
    if letter not in used:
        for i in range(5):
            word = ['-'] * 5
            word[i] = letter
            full_url = url_head + ''.join(word)
            print(full_url)
            data = requests.get(url_head + ''.join(word), headers=headers)
            if data:
                print(data.text)
            else:
                print(data.status_code)
