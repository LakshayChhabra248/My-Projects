import streamlit as st
import pandas as pd
import time
import random
from utils import data_manager
from utils.whatsapp_driver import WhatsAppDriver

st.set_page_config(page_title="PyPigeon - WhatsApp Automator", page_icon="🐦", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* Main Background - Dark Deep Space */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        background-attachment: fixed;
    }

    /* Text Color */
    .stMarkdown, .stDataFrame, .stAlert, h1, h2, h3, h4, h5, h6, p, label {
        color: #e0e0e0 !important;
    }

    /* Sidebar Glass - Darker */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Input Fields - Dark Glass */
    .stTextInput > div > div > input, .stNumberInput > div > div > input {
        background-color: rgba(0, 0, 0, 0.3);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 8px;
    }
    
    /* Buttons - Dark Glass */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
        backdrop-filter: blur(5px);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.3);
        transform: translateY(-2px);
    }

    /* Dataframe styling */
    [data-testid="stDataFrame"] {
        background: rgba(0, 0, 0, 0.3);
        padding: 10px;
        border-radius: 10px;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Success/Error/Info Messages */
    .stSuccess, .stError, .stInfo, .stWarning {
        background-color: rgba(0, 0, 0, 0.4) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #e0e0e0 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🐦 PyPigeon")
st.markdown("### Automated WhatsApp Messaging for Finance Updates")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("This tool uses Selenium to automate WhatsApp Web. You will need to scan the QR code.")
    
    st.subheader("Test Data")
    if st.button("Generate Sample Excel"):
        df_sample = data_manager.generate_test_data(10)
        # Convert to bytes for download
        output = pd.ExcelWriter('sample_data.xlsx', engine='openpyxl')
        df_sample.to_excel(output, index=False)
        output.close() # Important: close the writer
        
        # Re-read to get bytes (or use BytesIO)
        with open('sample_data.xlsx', 'rb') as f:
            st.download_button(
                label="Download Sample .xlsx",
                data=f,
                file_name="pypigeon_sample.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        st.success("Sample data generated! Click download.")

# Main Content
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("1. Upload Data")
    uploaded_file = st.file_uploader("Upload Excel File", type=['xlsx', 'xls'])

if uploaded_file:
    try:
        df = data_manager.load_data(uploaded_file)
        is_valid, error_msg = data_manager.validate_data(df)
        
        if not is_valid:
            st.error(f"Invalid Data: {error_msg}")
        else:
            with col2:
                st.subheader("2. Data Preview")
                st.dataframe(df, use_container_width=True)
                st.caption(f"Total Records: {len(df)}")

            st.divider()
            st.subheader("3. Automation")
            
            min_delay = st.slider("Min Delay (seconds)", 5, 20, 8)
            max_delay = st.slider("Max Delay (seconds)", 10, 30, 15)
            
            if st.button("🚀 Start Sending Messages", type="primary"):
                progress_bar = st.progress(0)
                status_text = st.empty()
                log_container = st.container()
                
                driver = WhatsAppDriver()
                
                try:
                    status_text.info("Initializing Browser... Please wait.")
                    driver.initialize_driver()
                    
                    status_text.warning("⚠️ Please Scan the QR Code on the opened browser window!")
                    if driver.wait_for_login():
                        status_text.success("Login Detected! Starting messaging...")
                        time.sleep(2)
                        
                        total_messages = len(df)
                        success_count = 0
                        fail_count = 0
                        
                        for index, row in df.iterrows():
                            # Update Status
                            progress = (index + 1) / total_messages
                            progress_bar.progress(progress)
                            status_text.info(f"Processing {index + 1}/{total_messages}: {row['Name']}")
                            
                            # Construct Message
                            message = f"Hello {row['Name']},\n\nYour account summary:\nTotal Purchase: {row['Total Purchase Amount']}\nPayment Received: {row['Payment Done']}\n----------------\nOutstanding Balance: {row['Outstanding Balance']}\n\nPlease clear your dues at the earliest."
                            
                            # Send
                            success, error = driver.send_message(row['Mobile Number'], message)
                            
                            if success:
                                success_count += 1
                                log_container.markdown(f"✅ **{row['Name']}**: Sent")
                            else:
                                fail_count += 1
                                log_container.markdown(f"❌ **{row['Name']}**: Failed ({error})")
                            
                            # Random Delay
                            delay = random.uniform(min_delay, max_delay)
                            time.sleep(delay)
                        
                        st.success(f"Completed! Success: {success_count}, Failed: {fail_count}")
                        
                    else:
                        st.error("Login Timeout. Please try again and scan the QR code faster.")
                        
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                finally:
                    status_text.info("Closing browser...")
                    time.sleep(3)
                    driver.close()

    except Exception as e:
        st.error(f"Error loading file: {e}")

else:
    with col2:
        st.info("👋 Welcome to PyPigeon! Upload an Excel file to get started.")
        st.markdown("""
        **Required Columns:**
        - `Name`
        - `Mobile Number`
        - `Total Purchase Amount`
        - `Payment Done`
        - `Outstanding Balance`
        """)
