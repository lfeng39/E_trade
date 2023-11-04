# E_trade V1.00
## 功能模块：
  新品、折扣、活动展示；--index.html
  货架展示；--products.html
  产品详细展示；--detail.html
  品牌及故事展示；--about.html
## 功能详细：
### 首页
  新品展示，点击进入该产品的详细展示页；
  折扣展示，点击进入该产品的详细展示页；--增加折扣显示模块
  活动展示，点击进入该产品的详细展示页；--增加活动说明模块
### 货架
        显示全部SKU
        仅显示在售SKU
### 详细
        主图，其他图片
        标题
        价格显示、折扣显示、活动显示
        购买按钮
        五点
        描述
        A+图片
### 品牌
        简单介绍
* PC端 移动端

# E_trade V1.01
### 功能详细：
        1）注册：email, passwrod, country, ctiy, address, code, first_name, last_name
        2）登录：email, passwrod
        3）注册验证
        4）登录验证

# E_trade V1.02
### 功能更新：
        1）同步 asininfo | listing | productdescription | productinfo 表中的asin数量
        2）新增 edit 编辑 listing 功能，编辑完成后，数据提交到 listing | productdescription | productinfo 三张表中，
        3）成功页面提示成功或失败，并提供 view | again | go back to listing 链接去对应的页面

# E_trade V1.03
### 功能详细：
        1）管理员账户
        2）管理员后台操作界面
        3）创建Listing


# JS control Login SignUp input
        默认分别显示Email、Password字符串；
        Email input获取光标时，Email字符串消失；
        Password input获取光标时，Password字符串消失；
        失去光标，且无任何输入时，恢复字符串；

        Email、Password任一输入为空时，在该输入框下提示错误；

        检查Email输入字符串，不包含’@‘字符串时，提示格式错误；
        检查Password输入字符串，长度小于8个字符时，提示错误；

