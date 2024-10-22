import streamlit as st
from chat import chat_page
import asyncio

async def main():
    st.set_page_config(layout="wide")
    await chat_page()

if __name__ == "__main__":
    asyncio.run(main())
