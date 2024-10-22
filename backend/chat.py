import os
from dotenv import load_dotenv
from Orca.Orca import OrcaExecutor
from backend.cache import orcacache
load_dotenv()

async def init_orca_executor(content):
    default_api_key = os.getenv("DEFAULT_MODEL_API_KEY")
    default_base_url = os.getenv("DEFAULT_MODEL_BASE_URL")
    default_llm_model_name = os.getenv("DEFAULT_LLM_MODEL_NAME")
    deepseek_api_key = os.getenv("DEEPSEEK_CHAT_MODEL_API_KEY")
    deepseek_model_base_url = os.getenv("DEEPSEEK_CHAT_MODEL_BASE_URL")
    deepseek_llm_model_name = os.getenv("DEEPSEEK_CHAT_LLM_MODEL_NAME")

    groq_api_key = os.getenv("Groq_API_KEY")
    groq_llm_model_name = os.getenv("Groq_LLM_MODEL_NAME")

    together_api_key = os.getenv("Together_API_KEY")
    together_llm_model_name = os.getenv("Together_LLM_MODEL_NAME")
    config = {
        "default_model_api_key": default_api_key,
        "default_model_base_url": default_base_url,
        "default_llm_model_name": default_llm_model_name,
        "deepseek_chat_model_api_key": deepseek_api_key,
        "deepseek_chat_model_base_url": deepseek_model_base_url,
        "deepseek_chat_llm_model_name": deepseek_llm_model_name,
        "groq_api_key": groq_api_key,
        "groq_llm_model_name": groq_llm_model_name,
        "together_api_key": together_api_key,
        "together_llm_model_name": together_llm_model_name
    }
    variables = {
        "query": "AI 撰写"
    }

    tool = {
        "web_search": "websearch"
    }
    breakpoint_infos = None
    global orcacache
    cache_content = orcacache.get(content)
    if cache_content:
        init_params = cache_content['breakpoint_infos']
        breakpoint_infos = cache_content['breakpoint_infos']
    else:
        init_params = {
            "config": config,
            "memories": [],
            "debug_infos": [],
            "variables": variables,
            "tools": tool,
        }
    executor = OrcaExecutor()
    executor.init_executor(init_parmas=init_params)
    return executor, breakpoint_infos


async def chat(message: str):
    # 实现聊天逻辑
    return message

async def execute(code: str, mode: str = None):
    # 实现代码执行逻辑
    executor, breakpoint_infos = await init_orca_executor(code)
    res = await executor.execute(code, breakpoint_infos=breakpoint_infos, mode=mode)
    print("res:", res.keys())
    
    if "breakpoint_infos" in res:
        orcacache.set(code, res)
        step_name = "#### step " + str(res['breakpoint_infos']['memories'][-1]['name']) + " output:\n"
        result = step_name + str(res['output'])
        return {"result": result, "breakpoint_infos": "debug mode"}
    else:
        orcacache.set(code, res)
        return {"result": "#### final result: \n  " + str(res['output'])}