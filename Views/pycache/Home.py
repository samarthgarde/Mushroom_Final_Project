import streamlit as st
import base64
import pandas as pd
import plotly.express as px


def app():

    # # Load images and set the background dynamically
    
    def set_bg_hack_url():

        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url("https://avi-chavan-96.sirv.com/Mushroom/mushroom1.jpg");
                background-size: 100% 100%;
                background-position: center;
                min-height: 100vh; /* Minimum height to cover the full viewport */
                height: auto; /* Adjust height based on content */
            }}
            </style>
            """,
            unsafe_allow_html=True)
    set_bg_hack_url()

    # Header Section
    st.title(" Mushroom Trio Classifier 🍄")
    st.write(
        """
        Welcome to the **Mushroom Classification Project**! This advanced system uses machine learning models to help classify mushrooms as either **edible** or **poisonous** based on their physical features.
        
        The goal of this project is to provide an easy-to-use platform for mushroom enthusiasts, researchers, and foragers to identify mushrooms quickly and safely.

        In this project, we have developed two models:
        - **Model 1**: 🍄  Input the characteristics of a mushroom to predict if it's edible or poisonous.
        - **Model 2**:  📊 Upload a mushroom dataset and classify multiple mushrooms automatically.
        """
    )

    data = {
        "Mushroom Type": ["Edible", "Poisonous", "Edible", "Poisonous", "Edible", "Poisonous", "Edible", "Poisonous"],
        "Frequency": [200, 150, 180, 210, 240, 190, 220, 160],
    }
    df = pd.DataFrame(data)

    # Create a bar chart
    fig = px.bar(df, x="Mushroom Type", y="Frequency", title="Mushroom Type Distribution", color="Mushroom Type")
    st.plotly_chart(fig, use_container_width=True)

    # Mushroom Classification Overview
    st.header("🌟 How It Works")
    st.write(
        """
        Our project uses a **pattern-matching classification model** to identify mushroom edibility based on specific mushroom features.  
        The system takes user input for mushroom characteristics, encodes them into shorthand codes, and applies a structured pattern-matching algorithm to classify mushrooms.

        ---

        ## 🍄 **1. Feature-Based Classification**  
        The model takes the following mushroom attributes as input:  

        - **Odor** – Scent of the mushroom (e.g., Almond, Fishy, Foul).  
            ➡️ Odor is one of the strongest indicators of mushroom edibility. Certain toxic mushrooms have distinct foul or pungent odors.  
        - **Bruises** – Whether the mushroom bruises easily (Yes/No).  
            ➡️ Bruising behavior often correlates with the presence of toxic compounds.  
        - **Gill Color** – The color of the gills under the mushroom cap (e.g., White, Brown, Yellow).  
            ➡️ Some poisonous mushrooms have specific gill color patterns.  
        - **Cap Shape** – Shape of the mushroom cap (e.g., Bell, Flat, Convex).  
            ➡️ Shape is used to identify the mushroom species and predict toxicity.  
        - **Cap Surface** – Surface texture of the mushroom cap (e.g., Smooth, Scaly).  
            ➡️ Toxic mushrooms often have irregular or rough cap surfaces.  
        - **Cap Color** – Color of the mushroom cap (e.g., Red, White, Yellow).  
            ➡️ Some bright or unusual colors can indicate toxicity.  

        ---

        ## 📊 **2. Prediction Workflow**  
        **Step-by-Step Process:**  
        1. User selects mushroom features through the interface.  
        2. Features are encoded into shorthand codes.  
        3. Encoded values are evaluated using a ML algorithm.  
        4. If the pattern matches a known toxic or edible combination, the result is shown instantly.  
        5. If uncertain, the model defaults to **poisonous** for safety.  

        ---

        ## 🚀 **3. Key Features:**  
        ✅ **Fast and accurate predictions** using pattern matching.  
        ✅ **User-friendly interface** for quick input and feedback.  
        ✅ **Structured encoding** of mushroom attributes for accuracy.  
        ✅ **Immediate classification** — results in real-time.  
        ✅ **Handles ambiguous patterns** by prioritizing safety.  
        ✅ **Scalable** — capable of handling multiple inputs and datasets.  
        ✅ **High reliability** — model trained on real-world data patterns.  

        ---

        ## ⚠️ **4. Important Safety Notice:**  
        - Even though the model is highly accurate, **do not rely solely on AI predictions** for mushroom consumption.  
        - Always consult an expert or reference trusted sources before consuming any wild mushrooms.  
        - Toxic mushrooms can have subtle variations — visual confirmation is not always sufficient.  
        - When in doubt, **do not consume**!  

        ---
        """
    )
    # Footer with social links
    st.markdown('<div class="footer">Created with ❤️ by Strategic Synergists</div>', unsafe_allow_html=True)
