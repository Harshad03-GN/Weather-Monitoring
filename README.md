# 🌦️ Real-Time Weather Monitoring Dashboard with Alerts

A Flask-based weather monitoring web application that fetches real-time weather data using the OpenWeatherMap API, displays it via a user-friendly interface, stores history in Azure Blob Storage, and enables users to view past weather records. Deployed and monitored via Azure Cloud.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![Azure](https://img.shields.io/badge/Microsoft_Azure-Cloud-blue?logo=microsoftazure)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## Preview

> ✅ Enter city → Get current weather info  
> ✅ Weather info is saved as JSON in Azure Blob Storage  
> ✅ View full weather history on dashboard  

---

## Features

- 🌐 Search weather data for any city
- 📤 Automatically upload weather JSON data to Azure Blob Storage
- 📖 View stored weather history (city-wise)
- ☁️ Hosted on Azure VM with monitoring via Azure Monitor
- 🔐 API secrets securely managed using `.env` files

---

## Tech Stack

### Backend
- **Python**
- **Flask**

### Frontend
- **HTML**
- **Jinja2 Templates**
- **Bootstrap** (optional for styling)

### APIs & Data
- **OpenWeatherMap API** for real-time weather data

### Azure Cloud Services
- **Azure Virtual Machine (VM)** – hosting the Flask app
- **Azure Blob Storage** – storing `.json` files with weather data
- **Azure Monitor** – real-time monitoring, performance insights, and alerting

### Security
- **.env File** – stores all sensitive keys (API key, Azure connection string)
- **python-dotenv** – to load environment variables safely
- `.gitignore` – ensures `.env` and `__pycache__` are not pushed to GitHub

---

## Project Structure

```bash
weather-monitoring/
│
├── app/
│   ├── templates/
│   │   ├── index.html
│   │   └── history.html
│   └── __init__.py
│
├── azure_blob.py          # Handles blob uploads
├── main.py                # Main Flask application
├── .env                   # Secrets file (ignored in Git)
├── requirements.txt       # Python dependencies
└── README.md              # Project info
