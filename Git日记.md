# Git学习笔记
---
### *前言*
#### Git是跟着廖雪峰老师的[教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000#0)学习的, 个人觉得教程很到位。另外，自己学习的初衷是实际应用，目的只是掌握工具。

## 1.环境配置
* 硬件环境：windows系统
* 软件:Git & powershell & github。windows 上git安装完之后提供git bash, git cmd和git gui三种shell供使用，自己想学习powershell所以折腾一番后选择了powershell。
* [git安装程序](https://git-scm.com/downloads); [git中文安装教程](https://blog.csdn.net/sishen47k/article/details/80211002)仅供参考，安装的时候基本一路默认; 通过powershell的模块posh-git就能实现git+powershell，百度的教程不太好，权作[参考](https://www.cnblogs.com/kreo/p/4685988.html)，实测直接管理员模式打开powershell后输入Install-Module posh-git命令即可，powershell会提示安装一个官方的扩展管理工具，然后就ok了
* 安装完初次使用时，需要输入以下代码以“自报家门”	

		git config --global user.name "your name"
		git config --global user.email "email address"
	

注意这里的name和email要换成自己的。
## 2.基础命令解释
版本库创建：版本库即repository,可以简单理解为一个git管理者的文件目录。创建一个版本库很简单，输入几行代码即可：

	...>cd d:/example //目录自己决定
	...>mkdir learngit  //名字自拟
	...>cd learingit
	...>git init
##

添加文件的基本操作：先创建文件，再add添加，然后commit提交即可：

	git add readme.txt
	git commit -m "add a file"

commit后的代码作用相当于给这次的commit加一个注释以便后面使用
####补充：Git管理的是修改，当你用git add命令后，在工作区的第一次修改被放入暂存区，准备提交，但是，在工作区的第二次修改并没有放入暂存区，所以，git commit只负责把暂存区的修改提交了，也就是第一次的修改被提交了，第二次的修改不会被提交。

##

`...>git status`
该命令可以查看仓库当前的状态，代码结果有三种

* changes not staged for commit：(stage也即暂存区,提示当前有未add的文件)
* changes to be committed:（文件处于stage,待commit）
* nothing to commit, working tree clean（工作区也即文件目录是干净的）

##

`...>git diff file_name`
git status显示内容有修改时可以查看具体的改动之处

`...>git diff HEAD -- file_name`
可以查看工作区和版本库master的区别 
##

`...>git log`
提示我们历史记录，显示提交日志，如果输入信息太多，可以加上如下参数：

`...>git log --pretty=oneline`
##

`...>git reset --hard HEAD^`	
把当前版本回退到上一个版本，--hard参数意义待补充， HEAD相当于只想当前版本的指针，其后的^有多少个就表示回退多少步（步数较多时可以改写成HEAD~n)

`...>git reset HEAD file-name` 该命令可以把已经add的修改撤销掉，**重新放回工作区**

`...>git reset --hard commit_ID`
该命令比上述命令使用更灵活，可以任意跳转，前提是知晓commit时的id, 结合可以记录每次命令的`...>git reflog`食用效果更佳。
##

`...>git checkout -- file_name`
该命令可以把未add的文件修改给**恢复到修改前，不管是修改还是删除等**，注意`--`这两个符号不能省略。
##

`...>rm file_name`命令或其他方式删除掉工作区中的文件后，可以选择恢复误删文件或从版本库中删除，恢复命令为`git checkout -- file_name`,从库中删除需键入命令：

	git add  file_name	//也可使用'git rm file_name
	git commit -m ".."

反之，

	git rm file
	git commit -m "..."
后工作区中的文件也会被干掉。


## 3.远程仓库
这一步骤涉及远程仓库（github 码云）的创建、ssh key的创建和添加到远程仓库以及。。。（待续）

*创建ssh key*:

	ssh-keygen -t rsa -C "youremail@example.com"
远程仓库创建以及ssh key的添加：基本操作

*将本地库与远程库关联*：（以github为例）
`git remote add origin https://github.com/Lidongde/learngit.git` 该命令中的origin只是一个远程库在本地的代称，可以但不建议修改

*将本地库的所有内容推送到远程库上（推送分支）*：

初次推送：`...>git push -u origin master`
其中origin为默认的远程库昵称，master为git本地库的**主分支**

一般推送：`...>git push origin master`

*从远程仓库clone*：
`...>git clone https://github.com/Lidongde/gitskills.git`

**注意克隆得到的本地仓库会出现在执行上述代码前所处的文件目录中**

*补充*：实际上，Git支持多种协议，默认的git://使用ssh，但也可以使用https等其他协议。使用https除了速度慢以外，还有个最大的麻烦是每次推送都必须输入口令，但是在某些只开放http端口的公司内部就无法使用ssh协议而只能用https。

##待续哦

## 4.分支（branch）操作


