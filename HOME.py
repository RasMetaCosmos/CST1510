import streamlit as st


from appmod.user_conn import add_user, get_user
from hash import hash_password,check_password
from appmod.dataB import check_connection

conn = check_connection()

st.set_page_config(
    page_title="Home",
    page_icon="downloadhome.png",
    layout="wide"
)

st.title("Welcome to the Home Page")

session_state = st.session_state
if "logged_in" not in session_state:
    session_state["logged_in"] = False  


if not st.session_state["logged_in"]:
    #st.warning("Please log in to access the dashboard.")
    pass
else:
    st.success("You are logged in!")
    st.stop()



tab_login, tab_register = st.tabs(["Login", "Register"])

with tab_login:
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input(
        "Password", type="password", key="login_password")

    if st.button("Log In"):
        username, password_hash = get_user(conn, login_username)
        if username == login_username and check_password(login_password, password_hash):
            st.session_state["logged_in"] = True
            st.success("Login successful! Welcome, " + username + "!")
            st.switch_page("Pages/DASH_B.py")
        else:
            st.session_state["logged_in"] = False
            st.error("Invalid username or password. Please try again.")


with tab_register:
    register_username = st.text_input("New Username")
    register_password = st.text_input("New Password", type="password")
    
    if st.button("Register"):
        if register_username and register_password:
            h_password = hash_password(register_password)
            add_user(conn, register_username, h_password)
            st.session_state["logged_in"] = True
            st.success("Registration successful!Redirecting to dashboard...")
            st.switch_page("Pages/DASH_B.py")
        else:
            st.error("Please enter both username and password to register.")