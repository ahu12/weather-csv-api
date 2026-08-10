<<<<<<< HEAD
# weather-csv-api
Python program that retrieves weather data for ZIP codes using WeatherAPI.com and exports the results to CSV.
=======
# Weather CSV API

Python program that takes a list of ZIP codes from a CSV file, gets the current weather for each location using WeatherAPI.com, and saves the results to another CSV file.

## What it Does

* Reads ZIP codes from `input.csv`
* Gets current weather data from WeatherAPI.com
* Records the city, temperature, feels-like temperature, humidity, and conditions
* Saves the results to `output.csv`
* Uses a `.env` file to keep the API key out of the source code
* Continues processing if an individual API request fails

## Requirements

* Python 3
* A [WeatherAPI.com](https://www.weatherapi.com/) API key

## Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd weather-csv-api
```

### 2. Create a Virtual Environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Add Your API Key

Create a `.env` file in the project folder:

```text
WEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your WeatherAPI.com API key.

The `.env` file is included in `.gitignore` so the API key is not uploaded to GitHub.

## Input

The program reads ZIP codes from `input.csv`.

The file should have a `zip` column:

```csv
zip
95112
94105
94040
95014
94305
```

## Running the Program

With the virtual environment activated, run:

```powershell
python weather.py
```

The program reads each ZIP code, makes a request to WeatherAPI.com, and writes the results to `output.csv`.

## Output

The program creates an `output.csv` file with the following columns:

* `zip`
* `city`
* `temperature`
* `feels_like`
* `humidity`
* `condition`

Example:

```csv
zip,city,temperature,feels_like,humidity,condition
95112,San Jose,72.5,71.8,64,Sunny
94105,San Francisco,63.2,62.7,78,Cloudy
94040,Mountain View,71.4,70.9,60,Sunny
95014,Cupertino,70.8,70.1,59,Sunny
94305,Stanford,69.9,69.3,62,Sunny
```

The weather values will change depending on current conditions.

## Error Handling

The program checks for:

* Missing API credentials
* Failed API requests
* Connection errors
* Non-successful API responses

If a request fails for one ZIP code, the program reports the error and continues with the remaining ZIP codes.

## Project Structure

```text
weather-csv-api/
├── .gitignore
├── input.csv
├── README.md
├── requirements.txt
└── weather.py
```

The following files are kept out of version control:

```text
.env
.venv/
__pycache__/
output.csv
```

The `.env` file contains the API key, while `.venv`, `__pycache__`, and `output.csv` are local or generated files.

## Dependencies

* `requests` - Used to make requests to WeatherAPI.com
* `python-dotenv` - Used to load the API key from `.env`

Install them with:

```powershell
pip install -r requirements.txt
```

## API

This project uses the [WeatherAPI.com Current Weather API](https://www.weatherapi.com/docs/).
