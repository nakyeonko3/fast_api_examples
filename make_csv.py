
import pandas as pd
import time
from datetime import datetime

save_data = {
    "temp":'https://i.waifu.pics/HjkIsP1.png',
}

df = pd.DataFrame([], columns=['Date', 'Url'])

def make_csvfile(url, file_name = 'urls.csv'):
    global df
    new_line = pd.DataFrame({
            'Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
            'Url': [url]
            })
    df = pd.concat([df, new_line], ignore_index=True)
    df.to_csv(file_name, index=False)


def read_csvfile_last_value(file_name="urls.csv"):
    try:
        df = pd.read_csv(file_name)
        last_value = df['Url'].values[-1]
        save_data["temp"] = last_value
        return last_value
    except:
        return save_data["temp"]

# 이 코드 제대로 이해 한 것이 아닌듯,
# csv 작성 오류가 있다. 따로 db 만들기는 해야 될듯