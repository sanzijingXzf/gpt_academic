# --- GPT-Academic 本地部署私有配置文件 ---

# [备注] 1. API Key 配置
# 填入你在代理网站获取的 API Key
API_KEY = "hellotheworld"

# [备注] 2. 模型选择
# 核心备注：必须加上 "one-api-" 前缀！
# 只有加了前缀，程序才会强制走 OpenAI 协议，从而让你下方的 API_URL_REDIRECT 生效。
# 如果直接写 "gemini-"，程序会尝试直连 Google 官方服务器，导致重定向失效。
LLM_MODEL = "one-api-gemini-2.5-flash"

# [备注] 3. 可选模型列表
# 在界面下拉菜单中显示的候选模型
AVAIL_LLM_MODELS = ["one-api-gemini-2.5-flash", "gpt-4"]

# [备注] 4. API 重定向 (代理网关)
# 将官方 OpenAI 接口地址重定向到你的 ClawCloud 代理地址
API_URL_REDIRECT = {
    "https://api.openai.com/v1/chat/completions": "自定义ip/v1/chat/completions"
}

# [备注] 5. 网络代理设置
# 既然你已经使用了 API_URL_REDIRECT 重定向到国内可直连的代理地址，
# 那么 USE_PROXY 必须设置为 False，否则会产生冲突。
USE_PROXY = False

# [备注] 6. 本地端口配置
# 本地运行建议使用默认的 22303，或者你喜欢的任何未占用端口
WEB_PORT = 22303

# [备注] 7. 监听 IP
# 如果只在自己电脑用，写 "127.0.0.1"
# 如果希望同局域网的其他设备也能访问，写 "0.0.0.0"
LISTEN_IP = "0.0.0.0"

# [备注] 8. 启动稳定性优化
# 跳过启动时的 API 连通性预热测试，防止因为网络波动导致程序启动卡死
AUTH_SKIP_WARMUP = True

# [备注] 9. 附加功能
# 是否在右下角显示看板娘
ADD_WAIFU = True
