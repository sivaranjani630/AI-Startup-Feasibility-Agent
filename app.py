import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Startup Feasibility Agent", layout="wide")

st.title("🚀 Autonomous AI Startup Feasibility & Risk Intelligence Agent")

st.header("Startup Input Parameters")

idea = st.text_input("Startup Idea")
market_clarity = st.selectbox("Market Clarity", ["Low", "Medium", "High"])
budget = st.number_input("Available Budget (₹)", min_value=0)
team_size = st.number_input("Team Size", min_value=1)
timeline = st.number_input("Development Timeline (Months)", min_value=1)
competitors = st.number_input("Number of Competitors", min_value=0)

revenue_model = st.selectbox(
    "Revenue Model",
    ["Subscription", "One-time Purchase", "Ads", "Freemium", "Marketplace"]
)

if st.button("Run Feasibility Analysis"):

    market_score = {"Low": 40, "Medium": 65, "High": 85}[market_clarity]

    tech_score = min(100, team_size * 18)

    financial_score = 85 if budget > 500000 else 65 if budget > 200000 else 45

    comp_score = 85 if competitors <= 2 else 65 if competitors <= 6 else 40

    feasibility_score = int((market_score + tech_score + financial_score + comp_score) / 4)

    risk_level = "Low" if feasibility_score > 75 else "Medium" if feasibility_score > 55 else "High"

    stability_index = max(0, feasibility_score - competitors * 3)

    st.subheader("📊 Multi-Dimensional Scores")
    st.write(f"Market Score: {market_score}")
    st.write(f"Technical Score: {tech_score}")
    st.write(f"Financial Score: {financial_score}")
    st.write(f"Competition Score: {comp_score}")
    st.write(f"Overall Feasibility Score: {feasibility_score}/100")
    st.write(f"Startup Stability Index: {stability_index}/100")
    st.write(f"Risk Level: {risk_level}")
    monthly_burn = budget / timeline
    
    st.subheader("💰 Financial Burn Analysis")
    st.write(f"Estimated Monthly Burn Rate: ₹{int(monthly_burn)}")
    st.write(f"Estimated Runway: {timeline} months")
    st.subheader("🔍 SWOT Analysis")
    st.write("Strengths: Clear idea and structured revenue model")
    st.write("Weaknesses:", "Small team size" if team_size < 3 else "Moderate team capacity")
    st.write("Opportunities: Market expansion and scaling potential")
    st.write("Threats:", "High competitive pressure" if competitors > 5 else "Manageable competition")
    st.subheader("🔄 Strategic Recommendations")
    if risk_level == "High":
        st.write("- Narrow target market")
        st.write("- Reduce MVP scope")
        st.write("- Seek early funding")
    elif risk_level == "Medium":
        st.write("- Improve differentiation")
        st.write("- Optimize cost structure")
    else:
        st.write("- Scale marketing efforts")
        st.write("- Focus on product expansion")
    st.subheader("📅 6-Month Forecast")
    failure_prob = 70 if risk_level == "High" else 40 if risk_level == "Medium" else 15
    st.write(f"Estimated Failure Probability: {failure_prob}%")
    st.subheader("🔥 Risk Heat Map")
    data = pd.DataFrame({
        "Market": [market_score],
        "Technical": [tech_score],
        "Financial": [financial_score],
        "Competition": [comp_score]
    })

    fig, ax = plt.subplots()
    sns.heatmap(data, annot=True, cmap="Reds", ax=ax)
    st.pyplot(fig)