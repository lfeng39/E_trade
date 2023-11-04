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


# For more options and information see
# http://rpf.io/configtxt
# Some settings may impact device functionality. See link above for details

# uncomment if you get no picture on HDMI for a default "safe" mode
#hdmi_safe=1

# uncomment the following to adjust overscan. Use positive numbers if console
# goes off screen, and negative if there is too much border
#overscan_left=16
#overscan_right=16
#overscan_top=16
#overscan_bottom=16

# uncomment to force a console size. By default it will be display's size minus
# overscan.
#framebuffer_width=1280
#framebuffer_height=720

# uncomment if hdmi display is not detected and composite is being output
#hdmi_force_hotplug=1

# uncomment to force a specific HDMI mode (this will force VGA)
#hdmi_group=1
#hdmi_mode=1

# uncomment to force a HDMI mode rather than DVI. This can make audio work in
# DMT (computer monitor) modes
#hdmi_drive=2

# uncomment to increase signal to HDMI, if you have interference, blanking, or
# no display
#config_hdmi_boost=4

# uncomment for composite PAL
#sdtv_mode=2

#uncomment to overclock the arm. 700 MHz is the default.
#arm_freq=800

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Uncomment this to enable infrared communication.
#dtoverlay=gpio-ir,gpio_pin=17
#dtoverlay=gpio-ir-tx,gpio_pin=18

# Additional overlays and parameters are documented /boot/overlays/README

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

# Automatically load overlays for detected cameras
camera_auto_detect=1

# Automatically load overlays for detected DSI displays
display_auto_detect=1

# Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d
max_framebuffers=2

# Disable compensation for displays with overscan
disable_overscan=1

[cm4]
# Enable host mode on the 2711 built-in XHCI USB controller.
# This line should be removed if the legacy DWC2 controller is required
# (e.g. for USB device mode) or if USB support is not required.
otg_mode=1

[all]

[pi4]
# Run as fast as firmware / board allows
arm_boost=1

[all]
