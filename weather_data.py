import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your actual API key
API_KEY = "37375f0dbba45058f49cdf8b89e5d8fa"
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
response = requests.get(URL)
data = response.json()

# DEBUG: Print the response to see what's returned
print("API response:", data)

# ✅ Error check before accessing 'list'
if 'list' not in data:
    print("❌ Error fetching weather data!")
    print("Message from API:", data.get("message", "No message"))
    exit()  # stop the program safely

# Extract temperature and date/time
dates = []
temperatures = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temperatures.append(entry['main']['temp'])

# Visualization
plt.figure(figsize=(10, 5))
sns.lineplot(x=dates, y=temperatures)
plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date/Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
