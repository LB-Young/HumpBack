import streamlit as st
import requests

def login_page():
    st.title("登录")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(
            """
            <div style="background-color: lightblue; padding: 20px; text-align: center;">
                <h1 style="font-family: 'Arial', sans-serif; color: #333;">
                    Agent Humpback based on Orca language
                </h1>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        username = st.text_input("用户名")
        password = st.text_input("密码", type="password")
        
        if st.button("登录"):
            response = requests.post(
                "http://localhost:8000/token",
                data={"username": username, "password": password}
            )
            
            if response.status_code == 200:
                st.session_state.authenticated = True
                st.session_state.token = response.json()["access_token"]
                st.experimental_rerun()
            else:
                st.error("登录失败,请检查用户名和密码")
