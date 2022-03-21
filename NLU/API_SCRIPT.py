import pandas as pd
import requests
import ast
import time
import json


url = 'http://173.254.242.195/api/nlutext' 
df_twitter = pd.read_csv('./Twitter_Data/tweets_2019.csv')
df_twitter.dropna(subset=['full_text'], inplace=True)


# First we need to remove special caracters from text
df_twitter.full_text = df_twitter.full_text.apply(lambda x: x.replace('"', '').replace('\t', ' ').replace('\n', ' ').replace('\r', ''))

t0 = time.time()

# use a list to append each dictionary
nlp_list = []
counter = 1
for message in df_twitter.full_text.head(5000):
    response = requests.post(url, json={"text": message})    
    nlp_list.append(response.text)
    print(counter)
    counter += 1

    
print((time.time() - t0) / 3600)

nlp_list = list(map(ast.literal_eval, nlp_list))

with open('output.json', 'w') as f:
    json.dump(nlp_list, f)