import streamlit as st
import folium
from streamlit_folium import folium_static

def create_map():
    # Coordinates for the bounds of the image (latitude and longitude of the image corners)
    bounds = [[7.3, 97.51], [36.43, 68.1]]  # Update with your image's lat/lon bounds

    # Initialize Folium map
    m = folium.Map(location=[(7.3+36.43)/2, (68.1+97.51)/2], zoom_start=4.3)

    # Overlay the Kriging image
    folium.raster_layers.ImageOverlay(
        image='output-bg.png',  # Path to your kriging image
        bounds=bounds,
        opacity=0.6,  # Adjust opacity for better visibility
        name='Kriging Overlay'
    ).add_to(m)

    # Add LayerControl to toggle layers
    folium.LayerControl().add_to(m)

    # Add click event to get coordinates
    m.add_child(folium.LatLngPopup())

    return m

def main():
    st.title('Kriging Map Overlay with Coordinate Popup')

    # Create the map
    m = create_map()

    # Display the map using streamlit-folium
    folium_static(m)

    # Additional instructions
    st.info('Click anywhere on the map to see the latitude and longitude.')

if __name__ == '__main__':
    main()