📊 Netflix Watch History BI Dashboard
📌 Project Overview

This project analyzes Netflix watch-history data to uncover user engagement patterns and support data-driven business decisions.
The analysis is developed in Python and deployed as an interactive Streamlit BI dashboard.

The dashboard focuses on engagement, viewing behavior, and subscription performance, similar to real-world analytics use cases at streaming platforms.

🎯 Objectives

Identify key engagement metrics Netflix should track

Analyze watch behavior across subscription types and devices

Understand user viewing frequency and content interaction

Build an interactive dashboard for business stakeholders

🛠️ Tech Stack

Python 3.10

Pandas – data manipulation and aggregation

Matplotlib – analytical visualizations

Streamlit – interactive BI dashboard

VS Code – local development

📂 Project Structure

Netflix_Watch_History_Analysis/
│── app.py
│── requirements.txt
│── netflix_watch_history.csv
│── README.md

📈 Key Metrics & Visualizations
1️⃣ Total Watch Time by Subscription Type

Purpose:
Identifies which subscription tier drives the highest engagement.

Business Insight:
Higher watch time indicates higher customer lifetime value.

2️⃣ Average Watch Time by Device

Purpose:
Analyzes user behavior across devices such as Mobile, TV, Tablet, and Desktop.

Business Insight:
Helps prioritize UI/UX and streaming performance improvements by device.

3️⃣ Viewing Frequency per User

Purpose:
Measures how often users return to the platform.

Business Insight:
High-frequency users indicate strong retention; low-frequency users signal churn risk.

🚀 How to Run the Project Locally
1️⃣ Clone or Download the Repository
git clone https://github.com/yourusername/netflix-watch-history-dashboard.git
cd netflix-watch-history-dashboard

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py


The dashboard will open automatically at:

http://localhost:8501

📊 Dataset

Source: Provided as part of a BI/Analytics assessment

Format: CSV

Key fields include:

user_id

duration_watched(minutes)

subscription_type

device_used

date_watched

🧠 Business Use Cases

Pricing Strategy: Identify high-value subscription plans

Product Optimization: Improve device-specific viewing experience

Retention Analysis: Detect engagement patterns early

Content Strategy: Understand user behavior trends

🔮 Future Enhancements

Add filters (device, location, subscription)

Introduce KPI cards (DAU, Avg Session Length)

Include retention and churn indicators

Deploy publicly on Streamlit Cloud

Integrate Power BI or Tableau dashboards

👤 Author

Utkrisht Agrawal
Aspiring Data / BI Analyst
📧 Contact: (add if required)

📄 License

This project is for educational and portfolio purposes only.