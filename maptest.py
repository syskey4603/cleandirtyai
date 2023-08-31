import folium
import webbrowser
import os


loc1 = [12.904344402235987, 77.67183784831207]
loc2 = [12.971599325363028, 77.71471588196061]
coordlist = []
coordlist.append(loc1)
coordlist.append(loc2)

def genmap(coordlist):
  
  m = folium.Map(coordlist[0], zoom_start=13)

  tooltip = "Click me!"

  for coords in coordlist:

    folium.Marker(
        coords, 
        popup="<i>Mt. Hood Meadows</i>", 
        tooltip=tooltip, 
        icon=folium.Icon(color="red", icon="trash"),
    ).add_to(m)

  m.save("index.html")  

  filename = 'file:///'+os.getcwd()+'/' + 'index.html'
  webbrowser.open_new_tab(filename)

genmap(coordlist)