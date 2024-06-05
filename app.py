import streamlit as st
import time

def main():
    st.set_page_config(page_title="Organizational Sustainability Recommender System", layout="wide")
    
    st.title("🏢 Environmental Sustainability Recommender System")
    st.subheader("This is an environmental sustainability recommender system focusing for organizations. Please provide your organization's details and preferences to receive personalized sustainability recommendations.")
    
    tabs = st.tabs(["Organization Information", "Sustainability Profile", "Sustainability Goals", "Recommendations"])
    
    with tabs[0]:
        st.header("🏢 Organization Information")
        st.write("Please provide your organization's details.")
        
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            name = st.text_input("Organization Name", placeholder="Enter organization name")
            industry = st.selectbox("Industry", ["Manufacturing", "Technology", "Finance", "Healthcare", "Retail", "Education", "Other"])
        with col2:
            size = st.selectbox("Organization Size", ["Small (1-50 employees)", "Medium (51-500 employees)", "Large (501+ employees)"])
            location = st.text_input("Location", placeholder="Enter organization location")
        with col3:
            contact_person = st.text_input("Contact Person", placeholder="Enter contact person's name")
    
    with tabs[1]:
        st.header("🌱 Sustainability Profile")
        st.write("Provide information about your organization's current sustainability practices.")
        
        current_practices = st.multiselect(
            "Current Sustainable Practices",
            ["Energy-efficient Lighting", "Renewable Energy Usage", "Recycling Program", "Waste Reduction Initiatives", "Water Conservation Measures"]
        )
    
    with tabs[2]:
        st.header("🎯 Sustainability Goals")
        st.write("Select your organization's sustainability goals.")
        
        goals = st.multiselect(
            "Select your sustainability goals",
            ["Reduce Carbon Emissions", "Achieve Zero Waste", "Promote Renewable Energy", "Implement Sustainable Procurement", "Enhance Corporate Social Responsibility"]
        )
    
    with tabs[3]:
        st.header("💡 Recommendations")
        st.write("Click the button below to generate recommendations based on your organization's profile and goals.")
        
        if st.button("Generate Recommendations"):
            with st.spinner("Generating recommendations..."):
                time.sleep(3)
                recommendations = generate_recommendations(name, industry, size, contact_person, current_practices, goals)
                display_recommendations(name, industry, size, contact_person, current_practices, goals, recommendations)

def generate_recommendations(name, industry, size, contact_person, current_practices, goals):
    # Mock data for demonstration purposes
    recommendations_data = {
        "Manufacturing": [
            {
                "name": "Energy Efficiency Audit",
                "description": "Conduct an energy efficiency audit to identify areas for improvement and cost-saving opportunities.",
                "implementation_time": "2-3 months"
            },
            {
                "name": "Waste Reduction Program",
                "description": "Implement a waste reduction program to minimize waste generation and promote recycling.",
                "implementation_time": "4-6 months"
            }
        ],
        "Technology": [
            {
                "name": "Renewable Energy Adoption",
                "description": "Invest in renewable energy sources such as solar panels or wind turbines to power operations.",
                "implementation_time": "6-12 months"
            },
            {
                "name": "Green IT Practices",
                "description": "Adopt green IT practices to reduce energy consumption and promote sustainable computing.",
                "implementation_time": "3-6 months"
            }
        ],
        "Finance": [
            {
                "name": "Carbon Footprint Assessment",
                "description": "Conduct a carbon footprint assessment to quantify emissions and identify reduction opportunities.",
                "implementation_time": "2-4 months"
            },
            {
                "name": "Sustainable Investment Portfolio",
                "description": "Develop a sustainable investment portfolio that aligns with environmental and social criteria.",
                "implementation_time": "6-12 months"
            }
        ]
        # Add recommendations for other industries as needed
    }
    
    # Filter recommendations based on industry and goals
    selected_recommendations = []
    for rec in recommendations_data[industry]:
        selected_recommendations.append(rec)
    
    return selected_recommendations

def display_recommendations(name, industry, size, contact_person, current_practices, goals, recommendations):
    # Add space between sections
    st.write("")
    st.subheader("🏢 Organization Information")
    col1, col2, col3 = st.columns([1, 1, 1.5])
    with col1:
        st.write(f"**Organization Name**: {name}")
        st.write(f"**Industry**: {industry}")
    with col2:
        st.write(f"**Size**: {size}")
    with col3:
        st.write(f"**Contact Person**: {contact_person}")

    # Add space between sections
    st.write("")
    
    st.subheader("🌱 Sustainability Profile")
    st.write(f"**Current Sustainable Practices**: {', '.join(current_practices)}")

    # Add space between sections
    st.write("")
    
    st.subheader("🎯 Sustainability Goals")
    st.write(f"**Goals**: {', '.join(goals)}")

    # Add space between sections
    st.write("")
    
    
    st.subheader("💡 Recommendations")
    st.write("---")
    for rec in recommendations:
        st.write(f"#### {rec['name']}")
        st.write(f"**Description**: {rec['description']}")
        st.write(f"**Implementation Time**: {rec['implementation_time']}")

if __name__ == "__main__":
    main()
