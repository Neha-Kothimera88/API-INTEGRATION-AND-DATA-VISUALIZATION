# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KOTHIMERA NEHA

*INTERN ID*: CT06DL1449

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

*TASK DESCRIPTION*: 
In this project, I developed a Python-based application to fetch real-time weather forecast data for a specific city using the OpenWeatherMap API, and then visualized this data using 
matplotlib.

The task aimed to build an end-to-end data pipeline that retrieves weather data, processes it, and produces a visual plot showing temperature trends over time.

This kind of project helps you understand how real-world APIs work, how to handle JSON data in Python, and how to visualize time-series data, which are key skills for any data analyst, 

developer, or IoT application designer.

Tools and Technologies Used:

Programming Language:

Python 3.13

Python is used for its simplicity and powerful libraries. In this task, Python helped us fetch data from the web, process it, and visualize it effectively.

API:

OpenWeatherMap API
This public API provides weather forecast data in JSON format. We used the 5-day / 3-hour forecast endpoint to get weather data at 3-hour intervals for the next 5 days.

Python Libraries:

requests: To send HTTP GET requests to the OpenWeatherMap API and fetch weather data.

matplotlib: To plot temperature vs. date-time and visualize weather patterns.

datetime: To parse and manipulate date-time objects from the API data.

json: To parse and work with JSON data received from the API.

Development Environment:

Visual Studio Code (VS Code)
VS Code was used as the primary code editor for writing and running Python scripts. It is lightweight, customizable, and provides excellent support for Python with extensions like

Pylance and Python extension pack.

Operating System:

Windows 10
The development and execution of the project were carried out on a Windows 10 machine.

Steps Involved in the Project:

API Key Generation:

We first created an account on OpenWeatherMap.org and generated a unique API key, which is required for authentication to access weather data.

Data Fetching:

A Python script was written to send a GET request to the forecast API URL with the city name (e.g., Mumbai) and API key as parameters.

Data Processing:

The JSON response was parsed.

We extracted the relevant fields like dt_txt (date and time) and main['temp'] (temperature).

The temperature values were converted to Celsius if needed using the metric parameter.

Data Visualization:

Using matplotlib, we plotted the temperature data on the y-axis against the forecast time on the x-axis.

The graph displayed a clean and informative line chart labeled with titles, axes labels, and tilted x-axis ticks for readability.

Real-World Applications:

Weather Dashboards: This task is a miniature version of weather dashboard applications used in smartphones, websites, or smart home displays.

IoT Projects: Weather data is critical in many IoT systems like smart irrigation, air quality monitoring, and disaster prediction.

Data Analytics: Understanding time-series data and visualizing it is essential for analytics jobs in domains like meteorology, environment, energy, and transportation.

Learning API Integration: This project provides a practical foundation in consuming RESTful APIs, a must-have skill in modern software development.

*OUTPUT*: 

![Image](https://github.com/user-attachments/assets/e714f9f5-a08e-4922-8ed0-d9e0e245450f)


Outcome:
The final output was a graph titled "Temperature Forecast for Mumbai", showing temperature fluctuations across several days at regular intervals. The plot successfully gave insights into

the upcoming weather patterns, demonstrating our ability to transform raw JSON data from an API into meaningful visual analytics.


