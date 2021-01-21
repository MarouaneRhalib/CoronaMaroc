import folium
import pandas as pd
df=pd.read_csv('corona.csv')
print(df)
latlng = [df['LAT'].mean(), df['LNG'].mean()]
map = folium.Map(location=latlng)
for CITY, LAT,LNG, Number in zip(df['CITY'],df['LAT'],df['LNG'],df['Number']):
    if Number in range(0,10):
        color = 'green'
    elif Number in range(10,100):
        color = 'orange'
    else :
        color = 'red'
    folium.Marker(location=[LAT, LNG], popup=CITY+' : '+str(Number), icon=folium.Icon(color=color)).add_to(map)
    folium.CircleMarker(location=[LAT, LNG], radius=Number/10, fill=True, color=color).add_to(map)
map.save('index.html')