import streamlit as st
import aiohttp

async def chat_page():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2 style="font-family: 'Arial', sans-serif; color: #333;">
                Agent Humpback based on Orca language
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # 上方输入区域
        input_text = st.text_area("输入消息", height=150, key="input_area")
        if st.button("发送"):
            async with aiohttp.ClientSession() as session:
                async with session.post("http://localhost:8000/chat", json={"message": input_text}) as response:
                    if response.status == 200:
                        return_content = await response.json()
                        st.session_state.chat_response = return_content
                        st.success("消息已发送并处理")
                    else:
                        st.error(f"请求失败: {await response.text()}")
        
        if "chat_response" in st.session_state:
            operation_steps = st.text_area("请编辑操作步骤", value=st.session_state.chat_response, height=300, key="operation_steps")
        else:
            operation_steps = st.text_area("请输入操作步骤", height=300, key="operation_steps")
        
        if st.button("执行"):
            await execute_code(operation_steps, "c")
    
    with col2:
        st.subheader("执行结果")
        if "execution_results" not in st.session_state:
            st.session_state.execution_results = []
        
        for result in st.session_state.execution_results:
            st.write(result.get("result", "No result"))
        
        if st.session_state.execution_results and "breakpoint_infos" in st.session_state.execution_results[-1]:
            col1, col2 = st.columns(2)
            with col1:
                if st.button("继续执行"):
                    await execute_code(operation_steps, "c")
            with col2:
                if st.button("单步执行"):
                    await execute_code(operation_steps, "n")

async def execute_code(code, mode):
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8000/execute", json={"code": code, "mode": mode}) as response:
            if response.status == 200:
                result = await response.json()
                if "execution_results" not in st.session_state:
                    st.session_state.execution_results = []
                st.session_state.execution_results.append(result)
                st.success("代码已执行")
            else:
                st.error(f"执行失败: {await response.text()}")
    st.rerun()  # 使用 st.rerun() 替代 st.experimental_rerun()
