import configparser
import os
import openai

from httpcli.output import *

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, "../config/config.ini")
config = configparser.ConfigParser()  # 类实例化
config.read(config_path, encoding="utf-8")
openai_key = config.get("apiService", "openai_key")
openai.api_key = openai_key

# DALL·E·2 接口
def DALLE2_Server(img_description,img_size):
    output(f"正在请求DALL·E·2:{img_description}")
    try:
        response = openai.Image.create(
            prompt = img_description,
            n = 1,
            size = img_size,
        )
        res_DALLE2 = response['data'][0]['url']
        return res_DALLE2
    except Exception as e:
        output(f"OpenAI_ERROR：{e}")
        res_DALLE2 = f'\n❌请求DALL·E·2失败！\n════════════\n✉️消息：“{img_description}”\n════════════\n🚫错误：From<openai.com>:{str(e)}'
        return res_DALLE2

# GPT接口
def OpenaiServer(msg=None):
    original_msg = msg #记录提问内容
    output(f"正在请求ChatGPT:{original_msg}")
    try:
        if msg is None:
            output(f'ERROR：msg is None')
        else:
            start_time = time.time()
            print("正在请求openai.com……")
            print(str(msg))
            response = openai.Completion.create(
                model="text-davinci-003",#发生连续错误时，可以更换一下模型请求
                # model="text-ada-001",
                prompt=str(msg),
                temperature=0.6,
                max_tokens=3600,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            end_time = time.time()
            msg = response.choices[0].text  #ChatGPT的原始回复
            msg += '('+str(int(end_time-start_time+2))+"s"+')'.replace("\n\n", "")  #添加耗时戳，删除连续换行
            if msg.startswith("！"):    #删除异常出现的叹号和问号
                msg = msg.replace("！", "")
            elif msg.startswith("？"): 
                msg = msg.replace("？", "")
            return msg
    except Exception as e:
        output(f"OpenAI_ERROR：{e}")
        msg = f'\n❌请求DALL·E·2失败！\n🕗请稍后重试。\n════════════\n✉️消息：“{original_msg}”\n════════════\n🚫错误：From<openai.com>:{str(e)}'
        return msg