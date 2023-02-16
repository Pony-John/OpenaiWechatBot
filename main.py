from servercli.server import *
from httpcli.output import *
from servercli.server import *
import configparser
from multiprocessing import Process
from pyfiglet import Figlet


# 读取本地的配置文件
current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, "./config/config.ini")
config = configparser.ConfigParser()  # 类实例化
config.read(config_path, encoding="utf-8")
admin_id = config.get("server", "admin_id")


def main():
    output("WechatBot Run ....")
    # 获取本账号微信信息并打印
    get_personal_info()
    # 机器人进程
    bot()


if __name__ == "__main__":
    f = Figlet(font="slant", width=2000)
    cprint(f.renderText("WechatBot"), "green")
    cprint("\t\t\t\t\t\t--------By Pony")
    main()
