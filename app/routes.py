from flask import render_template, request, jsonify
import pandas as pd
import traceback

# Import from subfolders - adjust for your structure
from .api.api_client import APIClient
from .processing.processor import DataProcessor  
from .scraper.scraper import scrape_airline_data
from .visualization.visualizer import plot_demand_trends

def register_routes(app):
    """Register all routes with the Flask app"""
    
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/test-data")
    def test_data():
        """Test endpoint with sample data"""
        sample_data = [
            {"route": "NYC-LAX", "price": "$299", "date": "2024-08-15", "airline": "TestAir"},
            {"route": "NYC-LAX", "price": "$319", "date": "2024-08-16", "airline": "SkyTest"},
            {"route": "LAX-NYC", "price": "$289", "date": "2024-08-15", "airline": "TestAir"},
            {"route": "NYC-MIA", "price": "$259", "date": "2024-08-17", "airline": "AirTest"},
        ]
        return jsonify({
            "message": "Test data endpoint working!",
            "data": sample_data
        })

    @app.route("/scrape", methods=["POST"])
    def scrape():
        try:
            data = request.get_json()
            url = data.get("url", "")
            
            if not url:
                return jsonify({"error": "URL is required"}), 400
                
            scraped_data = scrape_airline_data(url)
            return jsonify(scraped_data.to_dict(orient="records"))
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/api-data", methods=["GET"])
    def api_data():
        try:
            client = APIClient()
            origin = request.args.get("origin")
            destination = request.args.get("destination")
            
            if not origin or not destination:
                return jsonify({"error": "Origin and destination are required"}), 400
                
            data = client.get_route_data(origin, destination)
            return jsonify(data or {})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/process", methods=["POST"])
    def process():
        try:
            request_data = request.get_json()
            raw_data = request_data.get("data", [])
            
            if not raw_data:
                return jsonify({"error": "No data provided"}), 400
                
            processor = DataProcessor(raw_data)
            cleaned = processor.clean_data()
            insights = processor.analyze_demand()
            peak_periods = processor.identify_peak_periods()
            
            return jsonify({
                "insights": insights.to_dict(orient="records") if not insights.empty else [],
                "peak_periods": peak_periods
            })
        except Exception as e:
            return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

    @app.route("/visualize", methods=["POST"])
    def visualize():
        try:
            request_data = request.get_json()
            processed_data = request_data.get("data", [])
            
            if not processed_data:
                return jsonify({"error": "No data provided"}), 400
            
            df = pd.DataFrame(processed_data)
            image_path = plot_demand_trends(df)
            
            return jsonify({"image_path": image_path})
        except Exception as e:
            return jsonify({"error": str(e)}), 500