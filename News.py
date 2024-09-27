import requests
import Speak as s
def News():   
    query_params = {
        "source": "the-times-of-india",
        "sortBy": "top",
        "apiKey": "8cd1ad008dfa44bdb9044b8ff92118f7"
        }
    main_url = " https://newsapi.org/v1/articles"
     
    # fetching data in json format
    toi_page = requests.get(main_url, params=query_params).json()
    # getting all articles in a string article
    article = toi_page["articles"]
    # empty list which will  contain all trending news
    results = []
    for each_title in article:
        results.append(each_title["title"])
             
    for i in range(len(results)): 
        # printing all trending news
        s.speak(str(i + 1)+" "+results[i])

if __name__=="__main__":
    s.speak("todays news is :")
    News()
    s.speak("News Over...")

        