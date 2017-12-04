# django-blog
一个以 Django 作为框架搭建的个人博客。

博客主页 www.stopfollow.com

查看博客建站历程，可以访问 www.stopfollow.com/timeline/

博客主要功能：
- 用户认证
- 文章分类、标签云、文章内容页
- 文章评论、回复、被@之后收到信息推送通知
- 全文搜索功能
- Timeline
- RSS博客订阅
- 网站地图
- 实用工具

主要特点：
- 前端采用bootstrap3 ，博客完全响应式
- 文章内容采用markdown语法支持，简洁明了
- 博客支持emoji表情
- 评论采用ajax提交，被人@之后收到网页提醒和信息推送
- 由haystack和jieba分词支持的强大的全文搜索功能
- 用户认证支持第三方账号（微博、Github）登录

使用方法：
1. 直接从Github上克隆一份代码到本地
2. 按照requirements.txt的依赖库按照需要的依赖（建议在虚拟环境下）
3. 在虚拟环境下进入django_blog目录，运行
```python
python manage.py runserver --settings=django_blog.settings_dev
```
4. 浏览器中输入http://127.0.0.1:8000/即可运行博客




