# # request对象的属性
#
# request.scheme
#
# 代表请求的方案, http或者https
#
# request.path
#
# 请求的路径, 比如请求127.0.0.1/org/list, 那这个值就是/org/list
#
# request.method
#
# 表示请求使用的http方法, GET或者POST请求
#
# request.encoding
#
# 表示提交数据的编码方式
#
# request.GET
#
# 获取GET请求
#
# request.POST
#
# 获取post的请求, 比如前端提交的用户密码, 可以通过request.POST.get()
# 来获取
#
# 另外：如果使用
# POST
# 上传文件的话，文件信息将包含在
# FILES
# 属性中
#
# request.COOKIES
#
# 包含所有的cookie
#
# request.META
#
# 一个标准的Python
# 字典，包含所有的HTTP
# 首部。具体的头部信息取决于客户端和服务器，下面是一些示例：
#
# CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
# CONTENT_TYPE —— 请求的正文的MIME
# 类型。
# HTTP_ACCEPT —— 响应可接收的Content - Type。
# HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
# HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
# HTTP_HOST —— 客服端发送的HTTP
# Host
# 头部。
# HTTP_REFERER —— Referring
# 页面。
# HTTP_USER_AGENT —— 客户端的user - agent
# 字符串。
# QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
# REMOTE_ADDR —— 客户端的IP
# 地址。
# REMOTE_HOST —— 客户端的主机名。
# REMOTE_USER —— 服务器认证后的用户。
# REQUEST_METHOD —— 一个字符串，例如
# "GET"
# 或
# "POST"。
# SERVER_NAME —— 服务器的主机名。
# SERVER_PORT —— 服务器的端口（是一个字符串）
# request.user
#
# 一个
# AUTH_USER_MODEL
# 类型的对象，表示当前登录的用户。
#
# 如果用户当前没有登录，user
# 将设置为
# django.contrib.auth.models.AnonymousUser
# 的一个实例。你可以通过
# is_authenticated()
# 区分它们
#
# 把request传给前端的时候, 前端可以通过
# { % if request.user.is_authenticated %}判断用户时候登录
#
# request.session
