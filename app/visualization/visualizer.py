import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime
import numpy as np

def plot_demand_trends(data):
    plt.figure(figsize=(12, 6))
    
    # Handle different data structures
    if isinstance(data, pd.DataFrame):
        df = data
    else:
        df = pd.DataFrame(data)
    
    # Create sample data if no date/demand columns exist
    if 'date' not in df.columns or 'demand' not in df.columns:
        # Create sample trend based on available data
        dates = pd.date_range(start='2024-01-01', periods=len(df) if len(df) > 0 else 30, freq='D')
        demands = np.random.randint(50, 200, len(dates)) if len(df) == 0 else range(len(df))
        
        plt.plot(dates, demands, marker='o', linewidth=2, markersize=4)
        plt.title('Airline Booking Demand Trends (Sample Data)')
    else:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])
        
        plt.plot(df['date'], df['demand'], marker='o', linewidth=2, markersize=4)
        plt.title('Airline Booking Demand Trends')
    
    plt.xlabel('Date')
    plt.ylabel('Demand')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Ensure static directory exists
    static_dir = 'static'
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    image_path = os.path.join(static_dir, f'demand_trends_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png')
    plt.savefig(image_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return image_path