学习笔记
1. 设置代理时想为上周的猫眼爬虫设置代理ip，直接套用了课上的程序逻辑发现一直无效。经过排查发现针对http和https的请求是需要做不同的处理的.因此猫眼的https请求设置代理ip以目前学习到的内容可能还无法处理？
请测试，通过修改请求协议为http可以确认http的proxy是能生效的，就是请求会被拒绝。因为还要测试其他功能如存mysql，因此先继续使用猫眼的爬虫。

2. 配置mysql请求时, 应将用户名等连接信息写在单独的文件中，再在连接数据库时引用，从而实现配置文件的解耦

3. request-header需要加的信息，除了'User-Agent'、'Referer'以外，碰到过的一些网站还需要加： 'x-requested-with'、'x-source'、'Origin'、'Host'

4. requests.Session方法返回的对象可以为其发出的所有请求保持同一个cookie。便于后续模拟同一个用户发出信息的场景

5. 关于中间件：对于DOWNLOADER_MIDDLEWARES，在request前端，数值越小的越先被调用；在response阶段，数字越大的越先被调用

