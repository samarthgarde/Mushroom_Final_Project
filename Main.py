import streamlit as st
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from streamlit_option_menu import option_menu


# ----------------------------- Background Styling -----------------------------
def set_bg_hack_url():
    st.markdown(
        """
        <style>
            .stApp {
                background: url("https://avi-chavan-96.sirv.com/Mushroom/parasol-4549617_1280.jpg");
                background-size: cover;
                background-position: center;
                min-height: 100vh;

            .stButton > button {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 16px;
            }
            .stButton > button:hover {
                background-color: #45a049;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_hack_url()

# ----------------------------- Database Initialization -----------------------------
def init_db():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()

# ----------------------------- User Authentication -----------------------------
def add_user(username, password):
    hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
    try:
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def authenticate_user(username, password):
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result:
            return check_password_hash(result[0], password)
    return False

init_db()

# ----------------------------- Session State Initialization -----------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None

# ----------------------------- Login Function -----------------------------
def login():
    st.markdown("## 🔒 Login", unsafe_allow_html=True)
    with st.form("Login Form", clear_on_submit=True):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        submit = st.form_submit_button("Login")

    if submit:
        if username and password:
            if authenticate_user(username, password):
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.query_params["authenticated"] = True
                st.query_params["username"] = username
                st.success(f"✅ Welcome back, **{username}**!")
            else:
                st.error("❌ Invalid username or password!")
        else:
            st.warning("⚠️ Please fill out both fields!")

# ----------------------------- Signup Function -----------------------------
def signup():
    st.markdown("## 📝 Sign Up", unsafe_allow_html=True)
    with st.form("Signup Form", clear_on_submit=True):
        new_username = st.text_input("Choose a Username", placeholder="Create a username")
        new_password = st.text_input("Choose a Password", type="password", placeholder="Create a password")
        submit = st.form_submit_button("Sign Up")

    if submit:
        if new_username and new_password:
            if add_user(new_username, new_password):
                st.success("✅ Account created successfully! Please log in.")
            else:
                st.error("❌ Username already exists!")
        else:
            st.warning("⚠️ Please fill out all fields!")

# ----------------------------- Main Application -----------------------------
def Main_app():
    st.title(f"👋 Welcome, {st.session_state.current_user}!")
    st.write("---")

    # Sidebar navigation
    with st.sidebar:
        selected = option_menu(
            menu_title="🍄 Mushroom Classifier",
            options=["Home", "Edibility Checker", "Mushroom ML Lab", "Mushroom Wisdom", "Gallery"],
            icons=["house", "search", "cpu", "info-circle", "image"],
            menu_icon="mushroom",
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#00172B"},
                "icon": {"color": "white", "font-size": "22px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#4CAF50",
                },
                "nav-link-selected": {"background-color": "#4CAF50", "color": "white"},
            }
        )

    # Load pages dynamically
    if selected == "Home":
        from views.Home import app
        app()
    elif selected == "Edibility Checker":
        from views.EdibilityChecker import app
        app()
    elif selected == "Mushroom ML Lab":
        from views.MushroomMlLab import app
        app()
    elif selected == "Mushroom Wisdom":
        from views.MushroomWisdom import app
        app()
    elif selected == "Gallery":
        from views.Gallery import app
        app()

    # Logout Button
    if st.sidebar.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.session_state.current_user = None
        st.query_params.clear()
        st.experimental_rerun()

# ----------------------------- Main Logic -----------------------------
try:
    authenticated = st.query_params.get("authenticated", False)
    username = st.query_params.get("username", None)
    
    if authenticated and username:
        st.session_state.authenticated = True
        st.session_state.current_user = username
        Main_app()
    else:
        raise ValueError("Invalid state")
except Exception:
    st.sidebar.title("🍄 Mushroom Classifier")
    page = st.sidebar.radio("🔐 Authentication", ["🔒 Login", "📝 Sign Up"])
    if page == "🔒 Login":
        login()
    elif page == "📝 Sign Up":
        signup()
