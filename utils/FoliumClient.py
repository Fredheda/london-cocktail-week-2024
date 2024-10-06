import folium

def init_map(map_center, zoom_start=12):
    map = folium.Map(location=map_center, zoom_start=zoom_start)
    return map 

def add_bar_to_map(map, bar_row, popup, filtered_drinks):
    folium.Marker(
        location=[bar_row['Latitude'], bar_row['Longitude']], 
        popup=popup,
        icon=folium.DivIcon(
            html=f"""
            <div style="
                font-size: 12px; 
                color: white; 
                background-color: {'navy' if bar_row['Preference'] == True else 'green'}; 
                border-radius: 50%; 
                width: 35px; 
                height: 25px;
                text-align: center;
                line-height: 25px;">
                {",".join([str(int(i)) for i in filtered_drinks.Score.tolist()])}
            </div>
            """
        )
    ).add_to(map)
    return map