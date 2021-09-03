from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
import plotly

url = BeautifulSoup('https://www.sharesansar.com/today-share-price','html.parser')

response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'lxml')
soup = soup.table
tag = soup.find_all('tr')

a = []
for i in tag:
    x = i.get_text()
    a.append(x)

output = []
for i in a:
   x = i.split('\n')[1:-1]
   output.append(x)


with open('compare.csv','w') as f:

    write = csv.writer(f)
    for i in output:
        write.writerow(i)


df = pd.read_csv('compare.csv')
titles = list(df.columns)
titles[0],titles[1]=titles[1],titles[0]
df = df[titles]
df.drop('Symbol',axis=1,inplace=True)
df.rename(columns={'S.No':'Symbol'},inplace=True, errors='raise')
print(df)



#Plotly Diagram

fig = go.Figure(data=[go.Candlestick(
                            x=df['Symbol'].iloc[0:10],
                            open=df['Open'],
                            high=df['High'],
                            low=df['Low'],
                            close=df['Close'],
                            increasing_line_color = 'green',
                            decreasing_line_color = 'red'

                            )])
                            
fig.show()
# // Black Background and no gridlines
# fig.update_layout(plot_bgcolor='rgb(0,0,0)',
#                     xaxis =  {'showgrid': False},
#                     yaxis =  {'showgrid': False})

# Export Candlestick to HTML
#plotly.offline.plot(fig, filename='Candlestick.html')

# animals=df['Symbol'].iloc[0:10]
# fig = go.Figure(data=[
#     go.Bar(name='Open', x=animals, y=df['Open'].iloc[0:10]),
#     go.Bar(name='Close', x=animals, y=df['Close'].iloc[0:10])
    
   
# ])
# # Change the bar mode
# fig.update_layout(barmode='group')
# fig.show()

# a=df[df['Symbol'=='ADBL']]
# fig = go.Figure([go.Scatter(name='52 Weeks High', x=a, y=df['52 Weeks High'])])
# #fig = go.Figure([go.Scatter(x=a, y=df['Low'].iloc)])
# fig.show()

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# fig = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
# fig.show()

