## Docker基础
### 1. Docker介绍
Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从 Apache2.0 协议开源。

Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

Docker 从 17.03 版本之后分为 CE（Community Edition: 社区版） 和 EE（Enterprise Edition: 企业版），我们用社区版就可以了。

#### Docker的应用场景
- Web 应用的自动化打包和发布。
- 自动化测试和持续集成、发布。
- 在服务型环境中部署和调整数据库或其他的后台应用。
- 从头编译或者扩展现有的 OpenShift 或 Cloud Foundry 平台来搭建自己的 PaaS 环境。

#### 相关链接
Docker 官网：[https://www.docker.com](https://www.docker.com)

Github Docker 源码：[https://github.com/docker/docker-ce](https://github.com/docker/docker-ce)

### 2. Docker 架构
Docker 包括三个基本概念:

- 镜像（Image）：Docker 镜像（Image），就相当于是一个 root 文件系统。比如官方镜像 ubuntu:16.04 就包含了完整的一套 Ubuntu16.04 最小系统的 root 文件系统。
- 容器（Container）：镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的类和实例一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。
- 仓库（Repository）：仓库可看成一个代码控制中心，用来保存镜像。

Docker 使用客户端-服务器 (C/S) 架构模式，使用远程API来管理和创建Docker容器。

Docker 容器通过 Docker 镜像来创建。

容器与镜像的关系类似于面向对象编程中的对象与类。

![](https://www.runoob.com/wp-content/uploads/2016/04/576507-docker1.png)

概念 |	说明
---|---
Docker 镜像(Images)|Docker 镜像是用于创建 Docker 容器的模板，比如 Ubuntu 系统。
Docker 容器(Container)|容器是独立运行的一个或一组应用，是镜像运行时的实体。
Docker 客户端(Client)|Docker 客户端通过命令行或者其他工具使用 Docker SDK (https://docs.docker.com/develop/sdk/) 与 Docker 的守护进程通信。
Docker 主机(Host)|一个物理或者虚拟的机器用于执行 Docker 守护进程和容器。
Docker Registry|Docker 仓库用来保存镜像，可以理解为代码控制中的代码仓库。<br/>Docker Hub(https://hub.docker.com) 提供了庞大的镜像集合供使用。<br/>一个 Docker Registry 中可以包含多个仓库（Repository）；每个仓库可以包含多个标签（Tag）；每个标签对应一个镜像。<br/>通常，一个仓库会包含同一个软件不同版本的镜像，而标签就常用于对应该软件的各个版本。我们可以通过 <仓库名>:<标签> 的格式来指定具体是这个软件哪个版本的镜像。如果不给出标签，将以 latest 作为默认标签。
Docker Machine|Docker Machine是一个简化Docker安装的命令行工具，通过一个简单的命令行即可在相应的平台上安装Docker，比如VirtualBox、 Digital Ocean、Microsoft Azure。

### 3. 安装
> Ubuntu 20.04

- 卸载旧版本
> Older versions of Docker were called docker, docker.io, or docker-engine. If these are installed, uninstall them:
```shell script
sudo apt-get remove docker docker-engine docker.io containerd runc
```
- 使用官方安装脚本自动安装
安装命令如下：
```shell script
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

- 使用国内 daocloud 一键安装命令：
```shell script
curl -sSL https://get.daocloud.io/docker | sh
```

### 4. Hello World
#### 简单示例
```shell script
docker run ubuntu:20.04 /bin/echo "Hello world"
```
- docker: Docker 的二进制执行文件。
- run: 与前面的 docker 组合来运行一个容器。
- ubuntu:20.04 指定要运行的镜像，Docker 首先从本地主机上查找镜像是否存在，如果不存在，Docker 就会从镜像仓库 Docker Hub 下载公共镜像。
    > 可通过 `lsb_release -a` 查看当前ubuntu的版本号。
- /bin/echo "Hello world": 在启动的容器里执行的命令

#### 运行交互式的容器
```shell script
docker run -i -t ubuntu:15.10 /bin/bash
```
- t: 在新容器内指定一个伪终端或终端。
- i: 允许你对容器内的标准输入 (STDIN) 进行交互。

#### 查看运行中的容器
```shell script
docker ps
```
CONTAINER ID        |IMAGE              | COMMAND           |  CREATED        |     STATUS         |     PORTS         |      NAMES
---|---|---|---|---|---|---
f61fe54b59ef       |ubuntu:20.04        |"/bin/bash"         |2 hours ago         |Up 2 hours         |                  |   vigilant_albattani

- CONTAINER ID: 容器 ID。
- IMAGE: 使用的镜像。
- COMMAND: 启动容器时运行的命令。
- CREATED: 容器的创建时间。
- STATUS: 容器状态。

状态有7种：

created（已创建）
restarting（重启中）
running（运行中）
removing（迁移中）
paused（暂停）
exited（停止）
dead（死亡）
- PORTS: 容器的端口信息和使用的连接类型（tcp\udp）。

- NAMES: 自动分配的容器名称。

#### 停止容器
```shell script
docker stop xxxxxx
```
或者
```shell script
docker stop amazing_cori
```

### 5. 替换docker镜像源
> 国内访问国外Docker镜像源通常是非常慢的，最好是替换成国内的资源

几个可用的国内镜像源
```text
Docker 官方中国区：       https://registry.docker-cn.com
网易：                   http://hub-mirror.c.163.com
中国科技大学：            https://docker.mirrors.ustc.edu.cn
阿里云：                 https://y0qd3iq.mirror.aliyuncs.com
```
增加Docker的镜像源配置文件 /etc/docker/daemon.json，如果没有配置过镜像该文件默认是不存的，在其中增加如下内容：
```json
{
  "registry-mirrors": ["https://y0qd3iq.mirror.aliyuncs.com"]
}
```
若不存在，可用vi进行编辑添加。

重启Docker服务
```shell script
server docker restart
```

查看是否生效：
```shell script
root@VM-0-10-ubuntu:/etc/docker# docker info|grep Mirrors -A 1
 Registry Mirrors:
  https://y0qd3iq.mirror.aliyuncs.com/
```

### 6. 使用容器

#### 1. 获取容器镜像
```shell script
docker pull ubuntu
```

#### 2. 启动
```shell script
$ docker run -it ubuntu /bin/bash
root@b3211sdsd:/# 
```
- -i: 交互式操作
- -t: 终端
- ubuntu: 镜像名称
- /bin/bash: 放在镜像名后面的是命令，这里我们希望有个交互式shell,因此用的是 /bin/bash

##### 退出终端
```shell script
root@b3211sdsd:/# exit
```

#### 3. 启动已停止的容器
> 可使用 docker ps -a 查看容器列表

```shell script
docker start xxxx
```
##### 后台运行容器: `-d`
```shell script
docker run -itd --name unubtn-test ubuntu /bin/bash
```
\* 加了 -d 参数默认不会进入容器，想要进入容器需要使用指令 `docker exec`

