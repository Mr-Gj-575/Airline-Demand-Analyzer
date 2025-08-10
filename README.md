# 🛩️ Airline Demand Analyzer

A Flask-based web application for analyzing airline booking market demand data through web scraping and API integration.

## Features

- **Data Scraping**: Extract airline booking data from websites
- **API Integration**: Fetch data from aviation APIs
- **Data Processing**: Clean and analyze demand trends
- **Visualization**: Generate charts showing demand patterns
- **Web Interface**: User-friendly dashboard for data analysis

## Screenshots

![Airline Demand Analyzer Interface](screenshot.png)

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Quick Start

1. **Clone the repository:**
   git clone https://github.com/yourusername/airline-demand-analyzer.git
   cd airline-demand-analyzer
2. **Create a virtual environment:**
   python -m venv airline_env
   # On Windows:
   airline_env\Scripts\activate
   # On macOS/Linux:
   source airline_env/bin/activate
3. **Install dependencies:**
   pip install -r requirements.txt
4. **Run the application:**
   python run.py
5.**Open your browser:**
Navigate to http://localhost:5000

Usage
Scraping Data

Enter a website URL in the "Scrape Data" section
Click "Scrape Data" to extract flight information
View processed insights and visualizations

API Data

Enter origin and destination airports (e.g., NYC, LAX)
Click "Get API Data" to fetch route information
Analyze demand trends and pricing patterns