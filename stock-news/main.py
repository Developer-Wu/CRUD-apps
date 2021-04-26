import requests
import datetime as dt
from twilio.rest import Client



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = 'STOCK_API_KEY'
news_api_key = 'NEWS_API_KEY'
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {'function': 'TIME_SERIES_DAILY',
              'symbol':STOCK,
              'apikey': stock_api_key}
response = requests.get('https://www.alphavantage.co/query', params=parameters)
response.raise_for_status()
stock_prices = response.json()['Time Series (Daily)']
today_weekday = (dt.datetime.now()).weekday()

if today_weekday == 6:
    day_before = 2
    day_before_yesterday = 3
elif today_weekday == 0:
    day_before = 3
    day_before_yesterday = 4
elif today_weekday == 1:
    day_before = 1
    day_before_yesterday = 4
else:
    day_before = 1
    day_before_yesterday = 2

last_stock_date = str((dt.datetime.now() - dt.timedelta(day_before)).date())
day_before_stock_date = str((dt.datetime.now() - dt.timedelta(day_before_yesterday)).date())


yesterday_stock_price = float(stock_prices[last_stock_date]['4. close'])
day_before_yesterday_stock_price=float(stock_prices[day_before_stock_date]['4. close'])

news_parameters = {
    'apiKey': news_api_key,
    'keyword': 'Tesla',
    'includeArticleTitle': True,
    'includeArticleBasicInfo': True,
    'articlesCount': 3,
    'lang':'eng',

    'includeArticleEventUri': False,
    'articlesSortBy': 'sourceImportance',
}
percentage_change = ((yesterday_stock_price - day_before_yesterday_stock_price)) / day_before_yesterday_stock_price *100


if abs(percentage_change) > 5:
    news_response = requests.get('http://eventregistry.org/api/v1/article/getArticles', params=news_parameters)
    news_response.raise_for_status()
    news = news_response.json()['articles']['results']
    news_dict = {f'article_{title}':[news[title]['title'],news[title]['url'],news[title]['body']] for title in range(0,3)}

    if percentage_change > 0:
        change_direction = '🔺'
    elif percentage_change < 0:
        change_direction = '🔻'

    message = f'{STOCK}: {change_direction}{abs(round(percentage_change))}%\n'

    for article in range(0, 3):
        title = f"Headline: {news_dict[f'article_{article}'][0]}\n"
        url = f"url: {news_dict[f'article_{article}'][1]}\n"
        summary = news_dict[f'article_{article}'][2].split('\n')[0]
        brief = f"Brief:{summary}\n\n"

        message += title
        message += url
        message += brief

    account_sid = 'ACCOUNT SID'
    auth_token = 'AUTH_CODE'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body= message,
        from_='+15612207867',
        to='RECEPIENT NUMBER'
    )

    print(message.status)








## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


## STEP 4 Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

