# 🎯 Day Thirty Five: Keys, Authentication & Environment Variables: Send SMS

Today was all about working with third-party APIs in Python! We focused on two powerful APIs—OpenWeatherMap for fetching real-time weather data and Twilio for sending SMS messages programmatically.

### What We Covered:

✅ **OpenWeatherMap API** – We learned how to make HTTP requests to retrieve weather data based on location (latitude & longitude). We explored how to parse JSON responses and extract useful information like temperature, humidity, and weather conditions.  
✅ **Twilio API for SMS** – Using Twilio’s Python library (twilio.rest.Client), we learned how to send text messages directly from our Python scripts. We also explored Twilio’s limitations for trial accounts, verified numbers, and how to troubleshoot common errors.  
✅ **Environment Variables & API Security** – Since APIs require secret keys, we learned the importance of keeping credentials safe by storing them in environment variables instead of hardcoding them in our scripts. We practiced using ```os.environ.get()``` to access these variables securely.

### Hands-On Practice:

🔹 Made GET requests to OpenWeather’s API and displayed weather information in a user-friendly format.  
🔹 Sent SMS messages via Twilio, handling authentication and response errors.  
🔹 Used .env files and Python’s os module to protect sensitive API keys.

By the end of the session, we had a solid understanding of how to integrate external APIs into Python projects, process JSON data, and securely manage API keys. 🚀 Looking forward to building more projects with these skills!