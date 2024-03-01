# World GDP per Capita Visualization

## Project Overview
This project visualizes the GDP per capita of different countries on a world map. The data is fetched from the World Bank API, and the visualization is created using the Folium library in Python.

## Steps Taken

### 1. Fetching GDP Data
- GDP per capita data is fetched from the World Bank API using the `fetch_gdp_data` function.
- The API endpoint used is: `http://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?format=json`.
- A GET request is made to the API, and the response is checked for a successful status code (200).
- If the response is successful, the data is extracted from the response JSON and stored in a list of dictionaries.
- Each dictionary contains the country name and its GDP per capita value.

### 2. Geocoding Countries
- Geocoding is the process of converting country names to geographical coordinates (latitude and longitude).
- The `get_coordinates` function is used to obtain latitude and longitude coordinates for each country.
- Nominatim's open API is used for geocoding, which is accessed via a GET request.
- The API endpoint used is: `https://nominatim.openstreetmap.org/search?format=json&q={country}`.
- For each country, a GET request is made to the API with the country name, and the response JSON is parsed to extract latitude and longitude coordinates.
- The latitude and longitude coordinates are then stored in separate lists.

### 3. Data Visualization
- The GDP data and corresponding latitude-longitude coordinates are combined into a DataFrame.
- A world map is initialized using Folium with an initial zoom level and center coordinates.
- For each country in the DataFrame, a marker is added to the map at its latitude-longitude coordinates.
- The marker popup displays the country name and its GDP per capita value.
- The generated map is saved as an HTML file (`world_gdp_map.html`), and it is opened in the default web browser for visualization using the `webbrowser.open` function.

## Dependencies
- Python 3.x
- Requests
- Pandas
- Folium
- Webbrowser
- Nominatim (from the Geopy library)

## Usage
1. Ensure all dependencies are installed.
2. Run the script `world_gdp_visualization.py`.
3. The script will fetch GDP per capita data, geocode countries, visualize the data on a world map, and open the map in the default web browser for visualization.

## Conclusion
This project demonstrates the process of fetching data from an API, performing geocoding, and visualizing the data on a map using Python libraries. The resulting visualization provides insights into the distribution of GDP per capita across different countries.
