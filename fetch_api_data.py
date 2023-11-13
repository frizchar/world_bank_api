import requests
import json
import pandas as pd


def bring_data(url: str):
    # get status code of the API below and raise exception in case of HTTP errors
    try:
        response_API = requests.get(url)
        response_API.raise_for_status()
        print("status_code: ", response_API.status_code, "\n")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    # generate json object obj
    data = response_API.text
    obj = json.loads(data)

    # print element 0 of json object 0 to inspect json structure
    y = json.dumps(obj[1][0], indent=4)
    if __name__ == "__main__":
        print("example :\n", y, "\n")

    # generate lists year_list, population_list parsing the json object obj
    year_list = [obj[1][i]["date"] for i in reversed(range(len(obj[1][:])))]
    y_list = [obj[1][i]["value"] for i in reversed(range(len(obj[1][:])))]

    # calling DataFrame constructor after zipping both lists
    df = pd.DataFrame(list(zip(year_list, y_list)))
    return df
