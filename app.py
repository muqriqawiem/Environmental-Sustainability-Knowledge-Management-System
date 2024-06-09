import random
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
        
        current_practices_options = [
            "Energy-efficient Lighting", "Renewable Energy Usage", "Recycling Program", 
            "Waste Reduction Initiatives", "Water Conservation Measures", "Sustainable Transportation Initiatives",
            "Biodiversity Conservation Efforts", "Carbon Offsetting Programs", "Sustainable Supply Chain Management",
            "Employee Engagement Programs"
        ]
        current_practices = []
        for option in current_practices_options:
            if st.checkbox(option):
                current_practices.append(option)
    
    with tabs[2]:
        st.header("🎯 Sustainability Goals")
        st.write("Select your organization's sustainability goals.")
        
        sustainability_goals_options = [
            "Reduce Carbon Emissions", "Achieve Zero Waste", "Promote Renewable Energy",
            "Implement Sustainable Procurement", "Enhance Corporate Social Responsibility", "Increase Energy Efficiency",
            "Sustainable Packaging", "Water Stewardship", "Environmental Education & Training",
            "Circular Economy Adoption", "Sustainable Agriculture and Foor Systems"
        ]
        goals = []
        for option in sustainability_goals_options:
            if st.checkbox(option):
                goals.append(option)
    
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
            },
            {
                "name": "Green Supply Chain Management",
                "description": "Develop a green supply chain strategy to ensure that suppliers follow sustainable practices and reduce environmental impact.",
                "implementation_time": " 6-12 months"
            },
            {
                "name": "Sustainable Product Design",
                "description": "Design products with sustainability in mind, using eco-friendly materials and processes to minimize environmental impact.",
                "implementation_time": " 8-12 months"
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
            },
            {
                "name": "E-Waste Recycling Program",
                "description": "Implement an e-waste recycling program to safely dispose of electronic waste and reduce landfill impact.",
                "implementation_time": "2-4 months"
            },
            {
                "name": "Sustainable Software Development",
                "description": "Develop software solutions that help optimize energy usage and reduce the carbon footprint of digital services.",
                "implementation_time": "6-9 months"
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
            },
            {
                "name": "Green Building Upgrades",
                "description": "Upgrade office buildings with energy-efficient lighting, HVAC systems, and water-saving fixtures.",
                "implementation_time": "4-8 months"
            },
            {
                "name": "Employee Sustainability Training",
                "description": " Provide training programs for employees to promote sustainable practices within the organization.",
                "implementation_time": "3-6 months"
            }
        ],
        "Healthcare": [
            {
                "name": "Green Building Certification",
                "description": "Pursue green building certification (such as LEED or BREEAM) for healthcare facilities to enhance energy efficiency, reduce water usage, and improve indoor air quality.",
                "implementation_time": "12-24 months"
            },
            {
                "name": "Sustainable Medical Waste Management",
                "description": "Implement a sustainable medical waste management program to reduce the environmental impact of hazardous and non-hazardous medical waste through proper segregation, recycling, and disposal.",
                "implementation_time": "6-12 months"
            },
            {
                "name": "Energy-efficient Medical Equipment",
                "description": "Invest in energy-efficient medical equipment that reduces energy consumption and operating costs.",
                "implementation_time": "3-6 months"
            },
            {
                "name": "Water Conservation Measurest",
                "description": "Implement water conservation measures, such as low-flow fixtures and water recycling systems, to reduce water usage in healthcare facilities.",
                "implementation_time": "4-6 months"
            }
        ],
        "Retail": [
            {
                "name": "Sustainable Packaging Initiative",
                "description": "Develop a sustainable packaging initiative to reduce plastic use and promote recyclable or biodegradable packaging materials for products.",
                "implementation_time": "3-6 months"
            },
            {
                "name": "Energy-efficient Store Operations",
                "description": "Upgrade store operations to be more energy-efficient by installing LED lighting, energy-efficient HVAC systems, and smart energy management systems.",
                "implementation_time": "6-12 months"
            },
            {
                "name": "Eco-friendly Product Line",
                "description": "Launch an eco-friendly product line that emphasizes sustainable materials and ethical sourcing.",
                "implementation_time": "6-9 months"
            },
            {
                "name": "Customer Awareness Campaigns",
                "description": "Run campaigns to educate customers on sustainability issues and promote eco-friendly products and practices.",
                "implementation_time": "2-4 months"
            }
        ],
        "Education": [
            {
                "name": "Campus Sustainability Plan",
                "description": "Develop and implement a comprehensive campus sustainability plan that includes energy conservation, waste reduction, water conservation, and sustainable transportation initiatives.",
                "implementation_time": "12-24 months"
            },
            {
                "name": "Green Curriculum Development",
                "description": "Integrate sustainability into the curriculum by developing courses and programs focused on environmental science, renewable energy, and sustainable practices.",
                "implementation_time": "6-12 months"
            },
            {
                "name": "Sustainable Campus Infrastructure",
                "description": "Invest in sustainable infrastructure projects, such as green buildings, solar panels, and rainwater harvesting systems.",
                "implementation_time": "12-18 months"
            },
            {
                "name": "Student-led Sustainability Projects",
                "description": "Encourage student-led sustainability projects that address environmental issues on campus and in the community.",
                "implementation_time": "3-6 months"
            }
        ],
        "Other": [
            {
                "name": "Community-based Environmental Programs",
                "description": "Launch community-based environmental programs that encourage local engagement in sustainability efforts such as tree planting, community clean-ups, and local recycling drives.",
                "implementation_time": "3-6 months"
            },
            {
                "name": "Carbon Offset Projects",
                "description": "Invest in carbon offset projects such as reforestation, renewable energy projects, and methane capture initiatives to neutralize the organization's carbon footprint.",
                "implementation_time": "6-12 months"
            },
            {
                "name": "Sustainable Event Planning",
                "description": "Plan and execute events in a sustainable manner by reducing waste, promoting recycling, and using eco-friendly materials.",
                "implementation_time": "2-4 months"
            },
            {
                "name": "Green Procurement Policies",
                "description": "Establish green procurement policies that prioritize purchasing eco-friendly products and services from sustainable suppliers.",
                "implementation_time": "3-6 months"
            }
        ]
    }
    
    # Filter recommendations based on industry and goals
    selected_recommendations = random.choice(recommendations_data[industry])
    
    return [selected_recommendations]

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

    st.write("")
    
    st.subheader("🌱 Sustainability Profile")
    st.write(f"**Current Sustainable Practices**: {', '.join(current_practices)}")

    st.write("")
    
    st.subheader("🎯 Sustainability Goals")
    st.write(f"**Goals**: {', '.join(goals)}")

    st.write("")
    
    st.subheader("💡 Recommendations")
    for rec in recommendations:
        st.write(f"#### {rec['name']}")
        st.write(f"**Description**: {rec['description']}")
        st.write(f"**Implementation Time**: {rec['implementation_time']}")

if __name__ == "__main__":
    main()