# Environmental Sustainability Recommender System

## System Background

An environmental sustainability recommender system is a resource use management system that provides suggestions for users to optimize their resource usage, which is helpful for both efficiency and environmental sustainability. With this recommender system, users can get advice on reducing waste, saving energy, and using resources more effectively. This can help contribute to environmental sustainability by minimizing unnecessary resource consumption, promoting green practices, saving energy, and reducing waste.

## Objective

1. **Develop a Functional Knowledge Management System**: Analyze existing resource usage data and provide actionable recommendations to users to improve the efficiency of resource utilization.
2. **Empower Users for Informed Decisions**: Provide recommendations considering both environmental impact and resource efficiency to help users make informed decisions regarding resource allocation.
3. **Promote Sustainable Resource Management**: Enable users to discover resource-efficient practices that directly contribute to achieving their chosen sustainability goals.

## Target Users

- **Organizational Leaders**: Executives and managers looking to enhance their organization’s resource efficiency and sustainability practices.
- **Environmental and Sustainability Professionals**: Experts focused on promoting and implementing sustainable practices within organizations and communities.
- **Knowledge Management Practitioners**: Professionals involved in managing and optimizing the flow of information and resources within organizations to improve efficiency and sustainability.

## Scope and Limitations

The system aims to offer a comprehensive resource use management solution that provides users with actionable recommendations to enhance resource efficiency and sustainability. However, the system’s scope may be influenced by several factors:

- **Data Quality and Availability**: Inaccurate data may lead to ineffective optimization suggestions.
- **System Performance**: Handling large amounts of data may affect system performance.
- **Diversity of User Needs**: Users may have varying levels of knowledge and expertise in resource management. Tailoring the system to accommodate these diversities is important for ensuring its relevance and usability.

## Key Features

- **User-Friendly Interface**: Offers a user-friendly interface designed to gather organization details and sustainability preferences efficiently.
- **Sustainability Profile**: Allows users to provide details about their organization's current sustainable practices by selecting from a list of options presented in checkboxes.
- **Sustainability Goals**: Users can select their organization's sustainability goals from a list of predefined options, facilitating the articulation of their environmental objectives.
- **Personalized Recommendations**: Generates personalized sustainability recommendations based on the organization's industry and selected goals.

## Ontology

The ontology of the Environmental Sustainability Knowledge Management System outlines the structured framework for organizing information and relationships within the domain:

![Ontology Diagram](https://i.imgur.com/RYhLioZ.png)

- **User**: Represents the users interacting with the system.
- **SustainablePractice**: Denotes various practices aimed at promoting sustainability.
- **SustainabilityGoal**: Defines the goals related to sustainability that users aim to achieve.
- **Advisor**: Refers to the system or entity providing recommendations and advice.
- **EnvironmentalProfile**: Contains information about the environmental aspects related to the user or organization.

![Ontology Diagram](https://i.imgur.com/3JAWhGc.png)

- **Primary Classes**: Represented by yellow-colored circles.
  - **User**: Represents individuals interacting with the system, e.g., 'Mike'.
    - **SustainabilityGoals**: Specifies goals such as reducing carbon footprint or achieving zero waste.
  - **SustainablePractice**: Recommendations made by the **Advisor** class.
  - **Advisor**: Provides recommendations to users; can be entities like 'Jane' or systems like 'Environmental Sustainability Recommender System'.
  - **EnvironmentalProfile**: Contains information about environmental aspects related to users or organizations, facilitating personalized recommendations.

Each primary class may have individual instances represented by purple-colored diamonds, highlighting specific entities or systems within the ontology. For instance, users like 'Mike' may have associated sustainability goals, while practices such as water conservation and renewable energy are recommended based on these goals.

## Accessing the Streamlit App

You can access the Environmental Sustainability Knowledge Management System through our Streamlit application [here](https://environmental-sustainability-recommendation-system.streamlit.app/).
