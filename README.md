# E_trade V1.06
## 功能更新：
- 增加coupon功能
- 升级myAccount模块

# E_trade V1.05
## 功能更新：
- 启用forms.py，设置forms.Form
- 账户有效性前端JS验证、后端forms.Form.is_valid()验证
- 用户注册、登录成功后，显示用户名，不再显示邮箱

# E_trade V1.04
## 功能更新：
- 用户注册、登录；设置session会话，登出删除会话；设置登录时长，暂定36000秒=10小时
- 后端验证账户是否存在
- 自动生成随机8位数user_id
- 用户注册、登录成功；管理员编辑index、listing成功，共用done.html模板

# E_trade V1.03
## 功能更新：
- 管理员账户
- 管理员后台操作界面
- 创建Listing

# E_trade V1.02
## 功能更新：
- 同步 asininfo | listing | productdescription | productinfo 表中的asin数量
- 新增 edit 编辑 listing 功能，编辑完成后，数据提交到 listing | productdescription | productinfo 三张表中，
- 成功页面提示成功或失败，并提供 view | again | go back to listing 链接去对应的页面

# E_trade V1.01
## 功能更新：
- 模板：index/about/products/detail/login/signUp/cart/myAccount/order
- 读取：panda读取csv数据，保存到mysql
- 添加asin包（包括：csv、image-products-asin-7、970、300、show），自动处理数据，并在products模板中显示

