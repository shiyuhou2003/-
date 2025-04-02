<h1>爬虫基础学习（需要一点python基础）</h1>

```markdown
# 爬虫技术体系

- 1. 网络通讯基础  
  - HTTP/HTTPS协议  
    - 请求方法（GET/POST）  
    - 状态码（200、404、500等）  
    - 请求头（User-Agent、Cookie、Referer）  
  - TCP/IP三次握手  
  - WebSocket简介  

- 2. 爬虫基础概念  
  - 爬虫工作原理  
    - 请求→响应→解析→存储  
  - 合法性  
    - Robots协议  
    - 法律责任  
  - 爬虫分类  
    - 通用爬虫  
    - 聚焦爬虫  

- 3. 爬虫请求库  
  - Requests：基本HTTP请求  
  - Urllib：Python内置库  
  - Aiohttp：异步HTTP请求  
  - Selenium：模拟浏览器操作  

- 4. 数据提取技术  
  - 正则表达式（re）  
  - XPath  
    - 语法与lxml库  
  - BeautifulSoup（HTML/XML解析）  
  - PyQuery（jQuery风格解析）  

- 5. 多任务爬虫  
  - 多线程（Threading）  
  - 多进程（Multiprocessing）  
  - 协程（Asyncio）  
  - 任务队列（Celery）  

- 6. 自动化爬虫  
  - Selenium自动化  
    - 元素定位（ID/XPath/CSS选择器）  
    - 动态页面渲染  
  - Playwright（新一代自动化工具）  

- 7. 反爬虫处理  
  - 常见反爬手段：  
    - User-Agent验证  
    - IP封禁（代理IP池）  
    - 验证码（OCR/打码平台）  
    - 动态参数（JS加密）  
  - 应对策略：  
    - 随机请求头  
    - 代理IP轮换  
    - 模拟登录（Session/Cookie）  

- 8. MongoDB数据库  
  - 非关系型数据库特点  
  - 基本操作：  
    - 插入（insert_one/insert_many）  
    - 查询（find）  
    - 索引优化  
  - 与Python交互（PyMongo）  

- 9. Scrapy框架与Scrapy-Redis  
  - Scrapy核心组件：  
    - Spider、Pipeline、Middleware  
    - Item数据模型  
  - 分布式爬虫：  
    - Scrapy-Redis原理  
    - Redis队列管理  

- 10. Appium环境搭建（手机APP数据采集）  
  - 环境配置（JDK/Android SDK/Appium Server）  
  - 元素定位（UIAutomator）  
  - 模拟手势操作（滑动、点击）  

- 11. Fiddler抓包工具教程  
  - 抓取HTTP/HTTPS请求  
  - 过滤与断点调试  
  - 模拟低速网络  
  - 手机APP抓包配置  
```

