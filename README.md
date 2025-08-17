# weather-app
Python app that fetches and displays weather data from an API.
📄 README.md

Weather App (PyQt5 + OpenWeatherMap)

A clean desktop weather app built with Python and PyQt5 that fetches real‑time weather from OpenWeatherMap. 

✨ Features

Search weather by city (metric °C)

Clear emoji for conditions (☀️, 🌧️, ⛈️, ❄️, 🌫️, ☁️)

Robust error messages for bad input/network/API issues

Keyboard: press Enter to search

🧰 Tech Stack

- Python 3.10+

- PyQt5 (UI)

- requests (HTTP)

python-dotenv (config)

pytest + GitHub Actions (tests/CI)


🚀 Quickstart
# 1) Clone
git clone https://github.com/<your-username>/weather-app.git
cd weather-app

# 2) Create venv
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3) Install deps
pip install -r requirements.txt

# 4) Configure API key
cp .env.example .env
# edit .env and paste your OpenWeather API key

# 5) Run
python app.py



🔑 Configuration

Create a .env file:
OPENWEATHER_API_KEY=your_key_here
Get a free key at https://openweathermap.org/ 

Tests
pip install -r requirements-dev.txt
pytest -q



🗂 Project Structure
weather-app/
├─ app.py
├─ README.md
├─ requirements.txt
├─ requirements-dev.txt
├─ .env.example
├─ .gitignore
├─ tests/
│  └─ test_emoji.py
├─ .github/
│  └─ workflows/
│     └─ ci.yml
└─ screenshots/
   └─ app.png


📚 What I Learned

- Building stateful PyQt5 UIs

- Handling HTTP errors & timeouts

- Secure API key management via .env


🪪 License

MIT — see LICENSE.

🤝 Acknowledgments

- Weather data by OpenWeatherMap










