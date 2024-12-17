import pandas as pd

def load_csv_data(file_path, delimiter=',', encoding='utf-8'):
    """Loads CSV data from the given file path."""
    try:
        df = pd.read_csv(file_path, delimiter=delimiter, encoding=encoding)
        return df
    except FileNotFoundError:
      raise FileNotFoundError(f"File not found at {file_path}")
    except Exception as e:
      raise Exception(f"An error occured loading csv data: {e}")