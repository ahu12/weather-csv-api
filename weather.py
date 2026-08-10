import csv,os,requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.csv"
API_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(zip_code):
    # Get current weather informatin for a Zip code

    params = {
        "key": API_KEY,
        "q": zip_code,
        "aqi": "no"
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            return {
                "zip": zip_code,
                "city": data["location"]["name"],
                "temperature": data["current"]["temp_f"],
                "feels_like": data["current"]["feelslike_f"],
                "humidity": data["current"]["humidity"],
                "condition": data["current"]["condition"]["text"]                
            }

        print(f"API request failed for {zip_code}.")
        print(f"Status code: {response.status_code}")
        return None

    except requests.RequestException as error:
        print(f"Could not connect to weather API for {zip_code}.")
        print(f"Error: {error}")
        return None

def main():
    # Read ZIP codes, get weather, and output results to a CSV

    results = []

    with open(INPUT_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            zip_code = row["zip"]
            weather = get_weather(zip_code)

            if weather:
                results.append(weather)

    fieldnames = [
        "zip",
        "city",
        "temperature",
        "feels_like",
        "humidity",
        "condition"
    ]

    with open(OUTPUT_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    main()