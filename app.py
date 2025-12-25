import streamlit as st
import pandas as pd
from os import *
from datetime import *
from pathlib import *
from scraper import scrape_and_save


# Page configuration
st.set_page_config(
    page_title="E-Commerce Web Scraper",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== HELPER FUNCTIONS =====

def get_scraped_files():
    """Get list of all scraped data files with their details"""
    scraped_dir = Path('scraped_data')
    if not scraped_dir.exists():
        return []
    
    files = []
    for file in scraped_dir.glob('products_*.csv'):
        file_size = file.stat().st_size / 1024  # KB
        mod_time = datetime.fromtimestamp(file.stat().st_mtime)
        files.append({
            'filename': file.name,
            'size_kb': round(file_size, 2),
            'modified': mod_time.strftime("%Y-%m-%d %H:%M:%S"),
            'path': str(file)
        })
    
    # Sort by modified time (newest first)
    files.sort(key=lambda x: x['modified'], reverse=True)
    return files


def load_csv_file(filepath):
    """Load CSV file safely"""
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None


def format_file_size(size_kb):
    """Format file size nicely"""
    if size_kb > 1024:
        return f"{size_kb / 1024:.2f} MB"
    return f"{size_kb:.2f} KB"


# Custom CSS for e-commerce theme
st.markdown("""
<style>
    .main-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .main-title h1 {
        margin: 0;
        font-size: 2.5rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
    }
    .success-box {
        background-color: #d1e7dd;
        border: 1px solid #badbcc;
        padding: 1rem;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Header with gradient background
st.markdown("""
<div class="main-title">
    <h1>🛒 E-Commerce Web Scraper</h1>
    <p>Extract product data from e-commerce websites with ease</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR: Configuration ---
# --- SIDEBAR: Configuration & Info ---
with st.sidebar:
    st.header("⚙️ Scraper Configuration")
    
    st.markdown("---")
    
    # Tabs: Manual Scraping vs Automation Info
    config_tab, auto_tab, history_tab = st.tabs(["Manual Run", "Automation", "History"])
    
    with config_tab:
        # Input: URL
        url = st.text_input(
            "🔗 E-Commerce URL",
            value="https://www.web-scraping.dev/products",
            help="Enter the full URL of the e-commerce category/products page"
        )
        
        st.markdown("---")
        
        # Input: Output filename (now optional - auto-generated if empty)
        custom_filename = st.text_input(
            "💾 Custom Filename (Optional)",
            value="",
            placeholder="Leave empty for auto-generated: products_yyyyMMdd.csv",
            help="Leave empty to use auto-generated filename with today's date"
        )
        
        st.markdown("---")
        
        # Info box
        st.info(
            "**How it works:**\n"
            "1. Enter an e-commerce site URL\n"
            "2. (Optional) Enter custom filename\n"
            "3. Click 'Start Scraping'\n"
            "4. Download the CSV/Excel with product data"
        )
    
    with auto_tab:
        st.markdown("### 🤖 Automation Setup")
        st.markdown("""
        **Run scheduler for automated scraping:**
        
        ```
        python scheduler.py
        ```
        
        **What happens:**
        - Runs scraper at scheduled times
        - Auto-generates filenames with dates
        - Saves to `scraped_data/` folder
        - No manual intervention needed
        """)
        
        st.success(
            "✅ **Automation Features:**\n"
            "• Daily scheduled runs\n"
            "• Auto-dated filenames\n"
            "• Excel + CSV export\n"
            "• Background processing"
        )
        
        st.warning(
            "⚠️ **Note:**\n"
            "Keep scheduler.py running to enable automation. "
            "You can minimize it or run on a server."
        )
    
    with history_tab:
        st.markdown("### 📂 Scraped Data Files")
        
        files = get_scraped_files()
        
        if files:
            st.markdown(f"**Total files: {len(files)}**")
            
            for file in files[:10]:  # Show last 10 files
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"""
                    📄 **{file['filename']}**
                    - Size: {format_file_size(file['size_kb'])}
                    - Modified: {file['modified']}
                    """)
                
                with col2:
                    if st.button("📂 View", key=file['filename']):
                        st.session_state.selected_file = file['path']
        else:
            st.info("📭 No scraped files yet. Run scraper to generate data.")


# --- MAIN CONTENT ---
st.markdown("""
<style>
    .about-box {
        background: linear-gradient(135deg, #668eea 0%, #768ba2 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        margin-bottom: 2rem;
    }
    .about-box h3 {
        margin-top: 0;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .about-box p {
        font-size: 1.05rem;
        line-height: 1.8;
        margin: 0;
    }
</style>


<div class="about-box">
    <h3>📊 About This Scraper</h3>
    <p>This tool extracts product information (name, price, availability, URL, etc) from e-commerce websites.
    It automatically detects product elements and exports them to CSV/Excel for analysis.</p>
</div>
""", unsafe_allow_html=True)


# Status Overview
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🖥️ Manual Mode",
        "Ready",
        "Click to run"
    )

with col2:
    st.metric(
        "🤖 Scheduler",
        "Check status",
        "Run scheduler.py"
    )

with col3:
    files = get_scraped_files()
    st.metric(
        "📂 Saved Files",
        len(files),
        "in scraped_data/"
    )

with col4:
    st.metric(
        "⏰ Auto-Filename",
        "Enabled",
        "yyyyMMdd format"
    )


# Colored stats
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background-color: #e7f3ff; padding: 1rem; border-radius: 8px; border-left: 4px solid #0066cc;">
        <h4 style="margin-top: 0; color: #0066cc;">✨ Features</h4>
        <ul style="margin-bottom: 0; color: #333;">
            <li>Automatic product detection</li>
            <li>CSV & Excel export</li>
            <li>Multi-site support</li>
            <li>Polite scraping</li>
            <li>Date-based filenames</li>
            <li>Scheduled automation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color: #f0e7ff; padding: 1rem; border-radius: 8px; border-left: 4px solid #7c3aed;">
        <h4 style="margin-top: 0; color: #7c3aed;">🚀 Quick Start</h4>
        <ol style="margin-bottom: 0; color: #333;">
            <li>Paste your e-commerce URL</li>
            <li>(Optional) Enter custom filename</li>
            <li>Click Start Scraping</li>
            <li>Download your data</li>
            <li>Or run scheduler.py for automation</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")


# Columns for better layout
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("🚀 Manual Scraping")
    st.write("Configure your settings in the sidebar and click the button below to start.")

with col2:
    st.metric("Status", "Ready" if url else "⚠️ Enter URL")

st.markdown("---")

# Button to start scraping
if st.button("🚀 Start Scraping", width='stretch', type="primary"):
    
    if not url:
        st.error("❌ Please enter a valid e-commerce URL.")
    else:
        # Call the scraper function
        with st.spinner("⏳ Scraping products... Please wait."):
            # Pass custom filename (or None for auto-generation)
            success, message, df, product_count = scrape_and_save(
                url, 
                custom_csv_filename=custom_filename if custom_filename else None
            )

        st.markdown("---")

        # Display results
        if success:
            st.markdown(f"""
            <div class="success-box">
                <h3>✅ Scraping Successful!</h3>
                <p><strong>{message}</strong></p>
            </div>
            """, unsafe_allow_html=True)

            # Statistics in columns
            st.subheader("📈 Scraping Summary")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Products Found", product_count)
            with col2:
                st.metric("Columns", len(df.columns))
            with col3:
                csv_size = len(df.to_csv(index=False).encode()) / 1024
                st.metric("File Size", f"{csv_size:.2f} KB")
            with col4:
                st.metric("Status", "✅ Complete")

            st.markdown("---")

            # Data preview
            st.subheader("🔍 Product Data Preview")
            
            # Tabs for different views
            tab1, tab2, tab3 = st.tabs(["First 10 Products", "Full Data", "Column Info"])
            
            with tab1:
                st.dataframe(
                    df.head(10),
                    width='stretch',
                    height=400
                )
            
            with tab2:
                st.dataframe(
                    df,
                    width='stretch',
                    height=600
                )
            
            with tab3:
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Columns in Dataset:**")
                    for col in df.columns:
                        st.write(f"• {col}")
                with col2:
                    st.write("**Data Types:**")
                    for col, dtype in df.dtypes.items():
                        st.write(f"• {col}: `{dtype}`")

            st.markdown("---")

            # Download section
            st.subheader("💾 Download Data")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # CSV download
                csv_bytes = df.to_csv(index=False, encoding="utf-8").encode()
                st.download_button(
                    label="📥 Download as CSV",
                    data=csv_bytes,
                    file_name=custom_filename if custom_filename else f"products_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv",
                    width='stretch',
                    type="primary"
                )
            
            with col2:
                # Excel download
                try:
                    import io
                    buffer = io.BytesIO()
                    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False, sheet_name='Products')
                    excel_data = buffer.getvalue()
                    
                    excel_filename = (custom_filename.replace('.csv', '.xlsx') 
                                     if custom_filename else 
                                     f"products_{datetime.now().strftime('%Y%m%d')}.xlsx")
                    
                    st.download_button(
                        label="📊 Download as Excel",
                        data=excel_data,
                        file_name=excel_filename,
                        width='stretch',
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                except Exception as e:
                    st.warning(f"⚠️ Excel export unavailable: {str(e)}")

        else:
            st.error(f"❌ Scraping Failed\n\n{message}")
            st.info("💡 **Troubleshooting Tips:**\n"
                   "• Check if the URL is correct and accessible\n"
                   "• Verify the website isn't blocking automated requests\n"
                   "• Try a different e-commerce site")


# Footer
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem; margin-top: 3rem;">
    <p>🛒 E-Commerce Web Scraper | Powered by Streamlit</p>
    <p>Use responsibly and respect website terms of service</p>
</div>
""", unsafe_allow_html=True)
