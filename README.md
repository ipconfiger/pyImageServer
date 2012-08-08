pyImageServer
=============

An Image Server based on flask,can be deployed on many Paas instance

Install
----------------------------------------
1.从github获取代码
    $git clone https://github.com/ipconfiger/pyImageServer.git

2.把py代码copy到Paas实例中去
  
  假设你使用的新浪SAE:
    $vim settings.py
 
  将设置项 HOLDER 设置为 "saestore"

  SAEDOMAIN 设置为 "img1"

  "img1"这个值是你在新浪SAE的控制面板里Storage那里设置的，添加一个域，这个值和你添的一致就行了

    $vim index.wsgi
    
  删除所有内容后，添加下内容保存:
    import sae
    import serv
    application = sae.create_wsgi_app(serv.app)

  提交svn后就能使用了。通过url http://domain/ping 可以看到是否正常启动了

  
也可以不用部署在SAE这类PAAS上，Linode也行，VPS类的话，就设置HOLDER为"",然后需要设置配置项UPFILE_ROOT 这个项用来配置上传文件存储的目录

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









 

