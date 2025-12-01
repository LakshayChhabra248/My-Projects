import pandas as pd
import random
from faker import Faker
import io

fake = Faker('en_IN')  # Use Indian locale for realistic phone numbers

REQUIRED_COLUMNS = ['Name', 'Mobile Number', 'Total Purchase Amount', 'Payment Done', 'Outstanding Balance']

def generate_test_data(num_records=5):
    """Generates a DataFrame with random test data."""
    data = []
    for _ in range(num_records):
        purchase = round(random.uniform(1000, 50000), 2)
        payment = round(random.uniform(0, purchase), 2)
        balance = round(purchase - payment, 2)
        
        # Generate a random Indian mobile number
        # Format: +91 followed by 10 digits
        mobile = f"+91{random.randint(6000000000, 9999999999)}"
        
        data.append({
            'Name': fake.name(),
            'Mobile Number': mobile,
            'Total Purchase Amount': purchase,
            'Payment Done': payment,
            'Outstanding Balance': balance
        })
    
    return pd.DataFrame(data)

def validate_data(df):
    """
    Validates if the DataFrame has the required columns.
    Returns (True, None) if valid, else (False, error_message).
    """
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        return False, f"Missing columns: {', '.join(missing_cols)}"
    return True, None

def load_data(uploaded_file):
    """Loads data from a Streamlit uploaded file object."""
    try:
        df = pd.read_excel(uploaded_file)
        # Clean mobile numbers: ensure they are strings
        if 'Mobile Number' in df.columns:
            df['Mobile Number'] = df['Mobile Number'].astype(str)
            # Basic cleanup: remove .0 if it was read as float
            df['Mobile Number'] = df['Mobile Number'].apply(lambda x: x.replace('.0', '') if x.endswith('.0') else x)
        return df
    except Exception as e:
        raise ValueError(f"Error reading file: {str(e)}")
