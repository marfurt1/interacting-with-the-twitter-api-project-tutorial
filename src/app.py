
# librerias
import os
from dotenv import load_dotenv
import tweepy
import requests
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

# cargo .env
load_dotenv()                    

# cargo datos de acceso desde archivo .env
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

print(f'{consumer_key},{consumer_secret},{access_token},{access_token_secret},{bearer_token}' )



# Creando cliente de Twitter
client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

# Definiendo la query para Twitter

query = '#100daysofcode (pandas OR python) -is:retweet'     

# traigo 100 tweets más recientes
tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id','created_at','lang'],
                                     max_results=100)

# creo diccionario
tweets_dict = tweets.json()

# extraigo "data" del diccionario
tweets_data = tweets_dict['data'] 

# creo data frame usando pandas
df = pd.json_normalize(tweets_data)
print(df.head())

# guardo data frame en csv
df.to_csv("coding-tweets.csv")

# funcion para saber si un texto está dentro de un tweet
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

### busco cuantas veces figura las palabras "pandas" y "python" en los tweets

# inicializo lista
[pandas, python] = [0, 0]

# itero filas del df
for index, row in df.iterrows():
    pandas += word_in_text('pandas', row['text'])
    python += word_in_text('python', row['text'])

# imprimo resultados
print(f'la palabra pandas aparece en {pandas} tweets mientras que python aparece en {python} tweets')

# grafico resultados

# estilo de colores en seaborn
sns.set(color_codes = True)

# etiquetas
cd = ['pandas', 'python']

# gráfico de barras
ax = sns.barplot(x = cd, y = [pandas, python])
ax.set(ylabel="count")
plt.show()
