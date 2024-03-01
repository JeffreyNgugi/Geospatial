import requests
import pandas as pd
import folium
import webbrowser

def fetch_gdp_data():
    url = "http://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[1]  # Extract data from the response
        gdp_data = []
        for entry in data:
            country_name = entry['country']['value']
            gdp_value = entry['value']
            if gdp_value is None:
                continue
            gdp_data.append({
                'Country': country_name,
                'GDP per Capita (USD)': gdp_value
            })
        return gdp_data
    else:
        print("Failed to fetch data from the World Bank API.")
        return None

def get_coordinates(country):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={country}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return latitude, longitude
    return None, None

def visualize_on_map(gdp_data):
    world_map = folium.Map(location=[30, 0], zoom_start=2)
    for index, row in gdp_data.iterrows():
        latitude, longitude = get_coordinates(row['Country'])
        if latitude is not None and longitude is not None:
            folium.Marker(location=[latitude, longitude],
                          popup=f"{row['Country']}: ${row['GDP per Capita (USD)']:,}").add_to(world_map)
    world_map.save('world_gdp_map.html')
    webbrowser.open('world_gdp_map.html')

def main():
    gdp_data = fetch_gdp_data()
    if gdp_data:
        gdp_df = pd.DataFrame(gdp_data)

        visualize_on_map(gdp_df)
    else:
        print("No data available. Exiting...")

if __name__ == "__main__":
    main()
