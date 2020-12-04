# Neworld_SignIn

1、此系统为自动签到新界翻墙的脚本工具

2、具体操作fork项目到自己仓库，然后在仓库的‘settings’的Secrets添加自己的登录邮箱和密码，就可以每天自动签到了

## 图解步骤

#### 1、找到项目之后需要先Frok到自己的仓库

![Fork图片](https://cdn.jsdelivr.net/gh/chenkuangAmber/Neworld_SignIn_Doc@main/imgs/fork.png)

#### 2、fork完成后找到自己的仓库


![Fork图片](https://cdn.jsdelivr.net/gh/chenkuangAmber/Neworld_SignIn_Doc@main/imgs/forked.png)

### 3、添加Secrets
| Secret Name  | Secret Value     |
| -----------  | ---------------- |
| USERNAME     | 登录账号 |
| PASSWORD     | 密码 |


![Fork图片](https://cdn.jsdelivr.net/gh/chenkuangAmber/Neworld_SignIn_Doc@main/imgs/add-Secrets01.png)
![Fork图片](https://cdn.jsdelivr.net/gh/chenkuangAmber/Neworld_SignIn_Doc@main/imgs/add-Secrets02.png)
![Fork图片](https://cdn.jsdelivr.net/gh/chenkuangAmber/Neworld_SignIn_Doc@main/imgs/add-Secrets03.png)


### 4、创建完成后，到action中查看是否存在工作流



![Fork图片](https://cdn.jsdelivr.net/gh/chenkuangAmber/Neworld_SignIn_Doc@main/imgs/action1.png)


### 5、编写工作流文件
* 工作流文件在./github/workflows/xxx.yml文件中 github会自动识别yml文件，会自动加载到工作流中
* 触发方式默认为上午九点触发，可以修改cron表达式，更改触发事件，北京时间对应UTC时间需要减去8个小时，
* 例如 想要在每天的下午四点运行 需要16-8 = 8，定义的时间就是- cron: '0 8 * * *' 
* 注意：cron定义到分钟的时间点会有10-15分钟的误差  //未知原因
* 如果想要开启手动执行，需要解开注释  `# workflow_dispatch: # 手动触发`


![Fork图片](https://cdn.jsdelivr.net/gh/chenkuangAmber/Neworld_SignIn_Doc@main/imgs/time.png)

### 6、上述工作都完成后，项目就可以在设定的时间内运行了，运行成功后会在actions中看到成功的记录


![Fork图片](https://cdn.jsdelivr.net/gh/chenkuangAmber/Neworld_SignIn_Doc@main/imgs/scuuess.png)


### 7、执行成功后登录新界，可以看到签到按钮已经变成'已签到'了


![Fork图片](https://cdn.jsdelivr.net/gh/chenkuangAmber/Neworld_SignIn_Doc@main/imgs/ok.png)
