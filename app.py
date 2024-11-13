from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/map")
def map():
    m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

    # Convert the map to an HTML string
    map_html = m.get_root().render()
    return map_html

if __name__=="__main__":
    app.run(debug=True)

