import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, data):
        if isinstance(data, list):
            self.data = pd.DataFrame(data)
        else:
            self.data = data

    def clean_data(self):
        # Remove duplicates
        self.data = self.data.drop_duplicates()
        # Fill missing values (using newer pandas syntax)
        self.data = self.data.ffill()
        return self.data

    def analyze_demand(self):
        # Handle case where 'route' or 'price' columns might not exist
        if 'route' in self.data.columns and 'price' in self.data.columns:
            # Convert price to numeric if it's string
            self.data['price'] = pd.to_numeric(self.data['price'].str.replace('$', '').str.replace(',', ''), errors='coerce')
            avg_price = self.data.groupby('route')['price'].mean().reset_index()
            avg_price.columns = ['route', 'average_price']
            return avg_price
        else:
            return pd.DataFrame()

    def identify_peak_periods(self):
        if 'date' in self.data.columns:
            self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')
            demand_by_month = self.data.groupby(self.data['date'].dt.to_period('M')).size()
            peak_months = demand_by_month[demand_by_month > demand_by_month.mean()]
            return [str(period) for period in peak_months.index.tolist()]
        else:
            return []