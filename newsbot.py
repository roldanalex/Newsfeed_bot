### Load Libraries ####
from email.mime import audio
# import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import requests
from sys import argv

#### Load Tokens ####
from api_tokens import news_api
from api_tokens import news_url

#### Main Logic ####
def get_artciles_by_category(category, country_code_1):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": country_code_1,
        "apiKey": news_api
    }
    return _get_articles(query_parameters)

# def get_artciles_by_query(query, country_code_2):
#     query_parameters = {
#         "q": query,
#         "sortBy": "top",
#         "country": country_code_2,
#         "apiKey": news_api
#     }
#     return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(news_url, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for i in range(5):
        print(results[i]['title'])
        print(results[i]['url'])
        print('')
        news_talk(results[i]['title'])

    # for result in results:
    #     print(result['title'])
    #     print(result['url'])
    #     print('')

## Convert Txt to Speech (English)
def news_talk(text):
    # creates an audio file to store talk
    file_raw = 'audio_raw.mp3'

    tts = gTTS(text = text, lang = 'en')
    tts.save(file_raw)

    playsound.playsound(file_raw)
    os.remove(file_raw)


if __name__ == "__main__":
    print(f"Fetching top 5 news for {argv[1]}...\n")
    news_talk('Fetching top 5 ' + argv[1] + 'headlines')
    get_artciles_by_category(argv[1], argv[2])
    print(f"Successfully retrieved top {argv[1]} headlines for {argv[2]}")
    # get_artciles_by_query(argv[1], argv[2])
    #print_sources_by_category("technology")