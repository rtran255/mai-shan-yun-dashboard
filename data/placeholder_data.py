import pandas as pd


def get_placeholder_data():
  months = pd.date_range('2024-01-01', periods=12, freq='M')
  data = {
  'Month': months,
  'Inventory Level': [500 + i*20 for i in range(12)]
  }
  return pd.DataFrame(data)
