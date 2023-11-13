# source : https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures

import fetch_api_data as fad
import api_url_composer as auc


api_dict = {
  "gdp": "NY.GDP.MKTP.CD",
  "population": "SP.POP.TOTL",
  "employment_rate": "SL.UEM.TOTL.ZS"
}

api_urls_keys = api_dict.keys()
api_urls_values = [auc.composer(x) for x in api_dict.values()]
api_urls = {k: v for k, v in zip(api_urls_keys,api_urls_values)}

# Iterate over key/value pairs in dict api_urls and print them
for key, value in api_urls.items():
    print(key, ' : ', value)

for z in range(len(api_urls)):
    df = fad.bring_data(list(api_urls.values())[z])
    df.columns = ["year", list(api_urls.keys())[z]]
    print("data: ", "\n", df.tail(), "\n")
