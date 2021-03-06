import folium
import gpxpy
from os import listdir


# Generates a list of coordinates from a gpx file
def open_gpx(file):
    gpx_file = open(file, "r")
    gpx = gpxpy.parse(gpx_file)
    coordinates = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                coordinates.append(tuple([point.latitude, point.longitude]))

    return coordinates


# prints all gpx files in the 2021-21 directory. The "year" variable can be changed to any year directory
def main():
    ski_map = folium.Map()
    year = "2020-21"
    for file in listdir("gpx_files/" + year):
        coordinates = open_gpx("gpx_files/" + year + "/" + file)
        folium.PolyLine(coordinates, color="red", weight=2.5, opacity=1).add_to(ski_map)

    ski_map.save("maps/ski_tracks_" + year + ".html")


# prints all gpx files in gpx_file directory
def print_all():
    increment = color_increment()
    color_count = increment

    ski_map = folium.Map()
    for directory in listdir("gpx_files"):
        for file in listdir("gpx_files/" + directory):
            coordinates = open_gpx("gpx_files/" + directory + "/" + file)
            hex_color = hex(color_count)
            print(hex_color[2:len(hex_color)])
            # folium.Marker(coordinates[0], popup=directory + ": " + file, icon=folium.Icon(color="red")).add_to(ski_map)

            folium.PolyLine(coordinates, color="#" + hex_color[2:len(hex_color)], weight=2, opacity=1).add_to(ski_map)
            color_count += increment
    ski_map.save("maps/ski_tracks_all_blue_no_markers.html")


# Determines color shift depending on the number of gpx files
def color_increment():
    count = 2
    for directory in listdir("gpx_files"):
        for file in listdir("gpx_files/" + directory):
            count += 1

    print(count)
    max_hex = 16777215
    increment = max_hex / count

    return int(increment)







# print_all()

if __name__ == "__main__":
    main()
