import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import joblib

def classification():
    
    model = joblib.load("models/logistic_regression_model.pkl")  # Update path if necessary
    
    # Full name dictionaries for feature mapping (as provided earlier)
    cap_shape_full_names = {"b": "Bell", "c": "Conical", "f": "Flat", "k": "Knobbed", "s": "Sunken", "x": "Convex"}
    cap_surface_full_names = {"f": "Fibrous", "g": "Grooves", "s": "Smooth", "y": "Scaly"}
    cap_color_full_names = {"n": "Brown", "b": "Buff", "c": "Cinnamon", "g": "Gray", "r": "Green", "p": "Pink", "u": "Purple", "e": "Red", "w": "White", "y": "Yellow"}
    bruises_full_names = {"t": "Bruises", "f": "No Bruises"}
    odor_full_names = {"a": "Almond", "l": "Anise", "c": "Creosote", "y": "Fishy", "f": "Foul", "m": "Musty", "n": "None", "p": "Pungent", "s": "Spicy"}
    gill_attachment_full_names = {"a": "Attached", "d": "Descending", "f": "Free", "n": "Notched"}
    gill_spacing_full_names = {"c": "Close", "w": "Crowded", "d": "Distant"}
    gill_size_full_names = {"b": "Broad", "n": "Narrow"}
    gill_color_full_names = {"k": "Black", "n": "Brown", "b": "Buff", "h": "Chocolate", "g": "Gray", "r": "Green", "o": "Orange", "p": "Pink", "u": "Purple", "e": "Red", "w": "White", "y": "Yellow"}
    stalk_shape_full_names = {"e": "Enlarging", "t": "Tapering"}
    stalk_root_full_names = {"b": "Bulbous", "c": "Club", "u": "Cup", "e": "Equal", "z": "Rhizomorphs", "r": "Rooted", "?": "Missing"}
    stalk_surface_above_ring_full_names = {"f": "Fibrous", "y": "Scaly", "k": "Silky", "s": "Smooth"}
    stalk_surface_below_ring_full_names = {"f": "Fibrous", "y": "Scaly", "k": "Silky", "s": "Smooth"}
    stalk_color_above_ring_full_names = {"n": "Brown", "b": "Buff", "c": "Cinnamon", "g": "Gray", "o": "Orange", "p": "Pink", "e": "Red", "w": "White", "y": "Yellow"}
    stalk_color_below_ring_full_names = {"n": "Brown", "b": "Buff", "c": "Cinnamon", "g": "Gray", "o": "Orange", "p": "Pink", "e": "Red", "w": "White", "y": "Yellow"}
    ring_number_full_names = {"n": "None", "o": "One", "t": "Two"}
    ring_type_full_names = {"c": "Cobwebby", "e": "Evanescent", "f": "Flaring", "l": "Large", "n": "None", "p": "Pendant", "s": "Sheathing", "z": "Zone"}
    spore_print_color_full_names = {"k": "Black", "n": "Brown", "b": "Buff", "h": "Chocolate", "r": "Green", "o": "Orange", "u": "Purple", "w": "White", "y": "Yellow"}
    population_full_names = {"a": "Abundant", "c": "Clustered", "n": "Numerous", "s": "Scattered", "v": "Several", "y": "Solitary"}
    habitat_full_names = {"g": "Grasses", "l": "Leaves", "m": "Meadows", "p": "Paths", "u": "Urban", "w": "Waste", "d": "Woods"}

    # Define the PCA transformation function
    def apply_pca(df):
        # Columns to be encoded and transformed
        cap_columns = ['cap-shape', 'cap-surface', 'cap-color']
        gill_columns = ['gill-attachment', 'gill-spacing', 'gill-size', 'gill-color']
        stalk_columns = ['stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring']

        # Encode categorical features using factorize
        for col in [cap_columns, gill_columns, stalk_columns]:
            for feature in col:
                df[feature] = pd.factorize(df[feature])[0]
        
        # Scale the features before applying PCA
        scaler = StandardScaler()
        df[cap_columns + gill_columns + stalk_columns] = scaler.fit_transform(df[cap_columns + gill_columns + stalk_columns])
        
        # Apply PCA transformation to the features
        pca = PCA(n_components=1)
        df['cap'] = pca.fit_transform(df[cap_columns])
        df['gill'] = pca.fit_transform(df[gill_columns])
        df['stalk'] = pca.fit_transform(df[stalk_columns])

        # Drop the original columns after PCA
        df = df.drop(columns=cap_columns + gill_columns + stalk_columns)
        return df

st.markdown(
    """
    <style>
        .main {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        .footer {
            margin-top: 50px;
            font-size: 14px;
            color: #888;
            text-align: center;
        }
        h1, h2 {
            color: #4CAF50;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def classify_mushroom(odor, bruises, gill_color, cap_shape, cap_surface, cap_color):
    match (odor, bruises, gill_color, cap_shape, cap_surface, cap_color):
        case ("f" | "y" | "c" | "m" | "p" | "s", _, _, _, _, _):
            return "Poisonous"
        case ("n", "t", _, _, _, "w" | "g" | "n"):
            return "Edible"
        case ("n", _, "b" | "p" | "u", _, _, _):
            return "Edible"
        case ("a", _, "b" | "p" | "u", _, _, _):
            return "Edible"
        case ("n", _, _, "x" | "f", "s", _):
            return "Edible"
        case (_, "f", _, "b" | "c", "y" | "f", _):
            return "Poisonous"
        case _:
            return "Poisonous"

# Streamlit app
def app():

    def set_bg_hack_url():
        st.markdown(
            f"""
            <style>
                .stApp {{
                    background: url("https://avi-chavan-96.sirv.com/Mushroom/mushroom-7235034_1280.jpg");
                    background-size: 100% 100%;
                    background-position: center;
                    min-height: 100vh; /* Minimum height to cover the full viewport */
                    height: auto; /* Adjust height based on content */
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

    set_bg_hack_url()


    st.title("🍄 Edibility Checker")
    st.subheader("👀 Not sure if it’s edible? Check with the Edibility Checker!")

    with st.container():
        # Create 2 columns for better layout
        col1, col2 = st.columns(2)

        with col1:
            odor = st.selectbox("Odor", ["Almond", "Anise", "Creosote", "Fishy", "Foul", "Musty", "None", "Pungent", "Spicy"])
            bruises = st.selectbox("Bruises", ["Yes", "No"])
            gill_color = st.selectbox("Gill Color", ["Black", "Brown", "Buff", "Chocolate", "Gray", "Green", "Orange", "Pink", "Purple", "Red", "White", "Yellow"])

        with col2:
            cap_shape = st.selectbox("Cap Shape", ["Bell", "Conical", "Flat", "Knobbed", "Sunken", "Convex"])
            cap_surface = st.selectbox("Cap Surface", ["Fibrous", "Grooves", "Smooth", "Scaly"])
            cap_color = st.selectbox("Cap Color", ["Brown", "Buff", "Cinnamon", "Gray", "Green", "Pink", "Purple", "Red", "White", "Yellow"])

    # Mapping for classification
    odor_map = {"Almond": "a", "Anise": "l", "Creosote": "c", "Fishy": "y", "Foul": "f", "Musty": "m", "None": "n", "Pungent": "p", "Spicy": "s"}
    bruises_map = {"Yes": "t", "No": "f"}
    gill_color_map = {"Black": "k", "Brown": "n", "Buff": "b", "Chocolate": "h", "Gray": "g", "Green": "r", "Orange": "o", "Pink": "p", "Purple": "u", "Red": "e", "White": "w", "Yellow": "y"}
    cap_shape_map = {"Bell": "b", "Conical": "c", "Flat": "f", "Knobbed": "k", "Sunken": "s", "Convex": "x"}
    cap_surface_map = {"Fibrous": "f", "Grooves": "g", "Smooth": "s", "Scaly": "y"}
    cap_color_map = {"Brown": "n", "Buff": "b", "Cinnamon": "c", "Gray": "g", "Green": "r", "Pink": "p", "Purple": "u", "Red": "e", "White": "w", "Yellow": "y"}

    # Convert selections to codes
    odor_code = odor_map[odor]
    bruises_code = bruises_map[bruises]
    gill_color_code = gill_color_map[gill_color]
    cap_shape_code = cap_shape_map[cap_shape]
    cap_surface_code = cap_surface_map[cap_surface]
    cap_color_code = cap_color_map[cap_color]

    # Classify on button click
    if st.button("🍄 Classify Mushroom"):
        classification = classify_mushroom(odor_code, bruises_code, gill_color_code, cap_shape_code, cap_surface_code, cap_color_code)
        if classification == "Edible":
            st.success(f"✅ The Mushroom is **{classification}**! 🍄")
        else:
            st.error(f"⚠️ The Mushroom is **{classification}**! 🍄")

    # Footer
    st.markdown('<div class="footer">Created with ❤️ by Strategic Synergists</div>', unsafe_allow_html=True)