#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/17    15:11
# @Author    :Young.liu
# tips       :
import os
from dotenv import load_dotenv
from Orca.Orca import OrcaExecutor

load_dotenv()
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

content = """
            step 1:
            query：{query}
            你是一位情报领域的专家，擅长处理各种情报数据。请使用72B的qwen2.5模型生成3条化学品价格相关的情报数据，每条数据字数在50-100字, 结果以list格式返回。
            (bp)

            step 2:
                遍历{1}:
                    使用gemma-2-27b模型对内容进行分类，分类规则如下：   
                    `价格`: 情报主要内容为价格的变化、涨跌情况;
                    `供应`: 情报主要内容是生产、库存以及供应量的变化情况；
                    请将情报数据归纳到对应的分类中，只返回情报所属的类别名。

            step 3:
                tool_call('send_email', texts={1}通过我的邮箱发送给客户，主题为化学品调研。我的邮箱为“lby15356@gmail.com”，密码为“seulby356..”，客户邮箱为“Young.liu@aishu.cn。使用llama3-8b-8192模型。”)

            """

variables = {
    "query": "AI 撰写"
}
tool = {
    "web_search": "websearch"
}

init_params = {
    "config": config,
    "memories": [],
    "debug_infos": [],
    "variables": variables,
    "tools": tool,
}
async def main():
    executor = OrcaExecutor()
    executor.init_executor(init_parmas=init_params)
    res = await executor.execute(prompt=content)
    print(res.keys())
    while "breakpoint_infos" in res.keys():
        mode = input("请输入运行模式：")
        executor.init_executor(init_parmas=res['breakpoint_infos'])
        res = await executor.execute(content, breakpoint_infos=res["breakpoint_infos"], mode=mode)
    print(res)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
