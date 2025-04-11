# 📊 Sales Visualizer with Performance Levels

This is a simple Streamlit web app that lets users input sales data for multiple products and visualizes them with performance levels (High, Medium, Low) using a color-coded bar chart.

##  Features

- Enter custom product names and sales figures.
- Automatically categorize performance:
  - 🟢 High (>= 1000)
  - 🟠 Medium (>= 500)
  - 🔴 Low (< 500)
- Visual summary and interactive bar chart.

## 🧰 Tech Stack

- Python 🐍
- [Streamlit](https://streamlit.io/) – for building the UI
- [Matplotlib](https://matplotlib.org/) – for plotting the bar chart

## 📦 Installation (Local)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/sales-visualizer.git
cd sales-visualizer

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
