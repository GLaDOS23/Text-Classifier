import requests


txt = "Элементарный заряд. Закон сохранения электрического заряда. Точечный заряд. Закон Кулона. Система единиц. Рационализированная запись формул."

text = "Составь из этого текста вопрос для теста и один ответ на него (без дополнительной информации): " + txt

prompt = {
    "modelUri": "gpt://b1g1o9j4lup4tvhfe5u6/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "8000"
    },
    "messages": [
        {
            "role": "user",
            "text": text
        }
    ]
    
}


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVN36QRntV3Gys6tAvWaL1nEZeEYkCkW2hsYdqV"
}


response = requests.post(url, headers=headers, json=prompt)

result = response.text
#print(result)
result = result.replace('{"result":{"alternatives":[{"message":{"role":"assistant","text":"','')
result = result[:-156]

#print(result)
def split_and_print_string(string):
    lines = string.split("\n")
    for line in lines:
        print(line)
split_and_print_string(result)

#////////////////////////////
print(" ")
text2 = "Составь из этого текста вопрос для теста и варианты ответов (без дополнительной информации): " + txt
prompt = {
    "modelUri": "gpt://b1g1o9j4lup4tvhfe5u6/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "user",
            "text": text2
        }
    ]
    
}


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVN36QRntV3Gys6tAvWaL1nEZeEYkCkW2hsYdqV"
}


response = requests.post(url, headers=headers, json=prompt)

result = response.text
#print(result)
result = result.replace('{"result":{"alternatives":[{"message":{"role":"assistant","text":"','')
result = result[:-156]

print(result)









'''
        {
            "role": "system",
            "text": "Ты ассистент дроид, способный помочь в галактических приключениях."
        },
        {
            "role": "user",
            "text": "Привет, Дроид! Мне нужна твоя помощь, чтобы узнать больше о Силе. Как я могу научиться ее использовать?"
        },
        {
            "role": "assistant",
            "text": "Привет! Чтобы овладеть Силой, тебе нужно понять ее природу. Сила находится вокруг нас и соединяет всю галактику. Начнем с основ медитации."
        },
        {
            "role": "user",
            "text": "Хорошо, а как насчет строения светового меча? Это важная часть тренировки джедая. Как мне создать его?"
        }
'''
