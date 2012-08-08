pyImageServer
=============

An Image Server based on flask,can be deployed on many Paas instance

Install
----------------------------------------
1.Clone source code from github with command
    $git clone https://github.com/ipconfiger/pyImageServer.git

2.Copy all .py file into your Paas Instance

  SAE for example:
    $vim settings.py
 
  change the option HOLDER = "saestore" and SAEDOMAIN = "img1"
  the value of SAEDOMAIN is what you created in the App control panel

    $vim index.wsgi
    
  delete all lines,and add lines after:
    import sae
    import serv
    application = sae.create_wsgi_app(serv.app)

使用者被假设具备一定web开发的技能，本货也可以被部署到多个实例上组成图片服务的群集来使用。想测试功能可以自行制作一个静态页面，或者使用restfull console

API
---------------------------------------------
1. 上传图片
  path: /
  method: POST

  参数:
  thefile ->  图片文件，唯一必须的参数 
  sizes   ->  指定缩略图参数，格式为json对象{"small": "50x50","large": "100x100"}
              必须用双引号，value格式为宽x高，如果宽、高设为0则自适应宽、高
  on_success-> 自定义成功返回内容 不是必填参数
  on_error  -> 自定义出错后返回内容 不是必填参数
  
  占位符【on_success和on_error中使用】：
  $status  -> 上传的状态
  $info    -> 返回的信息（一般来说是出错信息）
  $filename-> 返回上传后文件名

2. 浏览图片

得到上传后的文件名后，假设得到的文件名是 xmdkfg03.jpg
http://domain/xmdkfg03.jpg 就能访问到该图片

如果通过sizes参数指定了缩略图的话
假设 {"small": "50x50"}

那么http://domain/xmdkfg03_small.jpg 就能访问到这张缩略图_









 

