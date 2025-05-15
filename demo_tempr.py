from tkinter import *
from tkinter import ttk
import requests


def detect_location():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return data['city']
    except:
        return None


def show_weather():
    city = city_name.get()
    try:
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=576f22db8017c1d0fe7d897efedd3524").json()

        climate_value.config(text=data["weather"][0]["main"])
        desc_value.config(text=data["weather"][0]["description"])
        temp_value.config(text=f"{int(data['main']['temp'] - 273.15)}°C")
        temp_min_value.config(text=f"{int(data['main']['temp_min'] - 273.15)}°C")
        temp_max_value.config(text=f"{int(data['main']['temp_max'] - 273.15)}°C")
        pressure_value.config(text=f"{data['main']['pressure']} hPa")
        wind_value.config(text=f"{data['wind']['speed']} m/s")
    except:
        climate_value.config(text="Error")
        desc_value.config(text="--")
        temp_value.config(text="--")
        temp_min_value.config(text="--")
        temp_max_value.config(text="--")
        pressure_value.config(text="--")
        wind_value.config(text="--")


def set_detected_city():
    city = detect_location()
    if city:
        city_name.set(city)
    else:
        city_name.set("Location not found")



win = Tk()
win.title("SkyTrack")
win.geometry("500x500")
win.config(bg="#a3d2ca")  # Soothing blue-green background


title_label = Label(
    win, text=" SkyTrack ", font=("Verdana", 22, "bold"),
    bg="#f7fff7", fg="#05668d", bd=3, relief=GROOVE
)
title_label.place(x=40, y=30, width=420, height=60)


city_label = Label(win, text="Select Region:", font=("Verdana", 14), bg="#a3d2ca", fg="#023047")
city_label.place(x=50, y=100)

city_list = [
    # Indian Cities
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune", "Jaipur", "Surat",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Bhopal", "Patna", "Vadodara", "Ludhiana", "Agra", "Nashik",
    "Faridabad", "Meerut", "Rajkot", "Varanasi", "Srinagar", "Ranchi", "Amritsar", "Guwahati", "Chandigarh", "Noida",
    # Global Cities
    "New York", "London", "Tokyo", "Paris", "Berlin", "Singapore", "Dubai", "Bangkok", "Rome", "Toronto",
    "Barcelona", "Los Angeles", "Chicago", "Moscow", "Beijing", "Seoul", "Istanbul", "Melbourne", "Sydney", "Cape Town",
    "Kuala Lumpur", "Jakarta", "San Francisco", "Mexico City", "Doha", "Madrid", "Vienna", "Amsterdam", "Stockholm", "Zurich"
]

city_name = StringVar()
city_combo = ttk.Combobox(win, values=city_list, font=("Verdana", 13), textvariable=city_name)
city_combo.place(x=50, y=130, width=400, height=35)

# Auto-set detected city at start
detected_city = detect_location()
if detected_city and detected_city in city_list:
    city_name.set(detected_city)


Button(win, text="📍 Use My Location", font=("Verdana", 10),
       bg="#05668d", fg="white", bd=0, command=set_detected_city).place(x=340, y=100)


frame = Frame(win, bg="#f7fff7", bd=3, relief=GROOVE)
frame.place(x=30, y=240, width=440, height=230)

info_style = {"font": ("Verdana", 12, "bold"), "bg": "#f7fff7", "anchor": "w"}
value_style = {"font": ("Verdana", 12), "bg": "#f7fff7", "fg": "#0077b6", "anchor": "w"}

Label(frame, text="🌦️ Climate        :", **info_style).place(x=20, y=10, width=160)
climate_value = Label(frame, text="--", **value_style)
climate_value.place(x=190, y=10, width=220)

Label(frame, text="📝 Description :", **info_style).place(x=20, y=40, width=160)
desc_value = Label(frame, text="--", **value_style)
desc_value.place(x=190, y=40, width=220)

Label(frame, text="🌡Temperature :", **info_style).place(x=20, y=70, width=160)
temp_value = Label(frame, text="--", **value_style)
temp_value.place(x=190, y=70, width=220)

Label(frame, text="🔻 Min Temp     :", **info_style).place(x=20, y=100, width=160)
temp_min_value = Label(frame, text="--", **value_style)
temp_min_value.place(x=190, y=100, width=220)

Label(frame, text="🔺 Max Temp    :", **info_style).place(x=20, y=130, width=160)
temp_max_value = Label(frame, text="--", **value_style)
temp_max_value.place(x=190, y=130, width=220)

Label(frame, text="🎈 Pressure       :", **info_style).place(x=20, y=160, width=160)
pressure_value = Label(frame, text="--", **value_style)
pressure_value.place(x=190, y=160, width=220)

Label(frame, text="💨 Wind Speed :", **info_style).place(x=20, y=190, width=160)
wind_value = Label(frame, text="--", **value_style)
wind_value.place(x=190, y=190, width=220)


done_btn = Button(
    win, text="🔍 Get Weather", font=("Verdana", 12, "bold"),
    bg="#05668d", fg="white", activebackground="#028090",
    cursor="hand2", bd=0, command=show_weather
)
done_btn.place(x=170, y=180, width=160, height=40)

win.mainloop()
