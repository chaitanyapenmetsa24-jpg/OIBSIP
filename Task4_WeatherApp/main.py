import tkinter as tk
from tkinter import messagebox
import requests

# Your OpenWeather API Key
API_KEY = "0d7d4d33f7e03dc59d06d116c475cf68"


def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning("Warning", "Please enter a city name!")
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            messagebox.showerror(
                "Error",
                data.get("message", "Unable to fetch weather.")
            )
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        weather = data["weather"][0]["description"].title()

        result = (
            f"📍 City: {city_name}, {country}\n\n"
            f"🌡 Temperature: {temp} °C\n"
            f"🤗 Feels Like: {feels_like} °C\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌬 Wind Speed: {wind} m/s\n"
            f"☁ Weather: {weather}"
        )

        result_label.config(text=result)

    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Error",
            "Unable to connect to OpenWeather.\nCheck your internet connection."
        )


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Weather App")
root.geometry("500x500")
root.configure(bg="#0F172A")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🌤 Weather App",
    font=("Arial", 22, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
)
title.pack(pady=20)

tk.Label(
    root,
    text="Enter City Name",
    font=("Arial", 12),
    bg="#0F172A",
    fg="white"
).pack()

city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30,
    justify="center"
)
city_entry.pack(pady=10)

tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    command=get_weather
).pack(pady=10)

result_label = tk.Label(
    root,
    text="Weather details will appear here",
    font=("Arial", 12),
    bg="#0F172A",
    fg="white",
    justify="left"
)
result_label.pack(pady=20)

root.mainloop()