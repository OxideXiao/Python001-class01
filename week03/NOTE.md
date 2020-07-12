学习笔记
1. Scrapy底层框架=》twisted， 异步编程

2. f字符串 args传元组 -》 args = ('asdf',) 不是字符串

3. 多进程程序调试是一个难点

4. 通过python 文件名.py调用的程序的话，支持从if __name__ = '__main__'开始 --> 即独立运行时，__name__的值等于’__main__‘

5. 多进程问题：
	a.数据通信问题。正常的变量赋值是在进程自身的堆栈中实现的。跨进程时，堆栈信息是不能传递的
		解决方式： 队列、管道、共享内存

	b.资源竞争问题。枷锁机制

6. queue.get方法 两个参数 blocked, timeout. 当blocked = true（默认）时若队列为空，则阻塞当前进程等待数据进来。若等待时间超过timeout（默认none）值，则抛出queue.Empty异常
blocked= fales时，直接读取数据。若没数据，抛出queue.Empty

7. queue.put 两个参数 blocked， timeout。当blocked = true时,若队列已满则阻塞当前进程，若超哥timeout设置的值，则抛出queue.Full.
blocked - false是，直接存放数据对象。若队列已满，抛出queue.Full

8. queue.join() 阻塞至队列中所有的元素都被接收和处理完毕。当条目添加到队列的时候，未完成任务的计数就会增加。当未完成计数为0时，接触阻塞
queue.task_done() 未完成计数减一

9. 锁不保证顺序，锁是保证资源的抢占

10. 阻塞非阻塞-》调用方、同步和异步 -》被调用方

11. 一个进程占用一个逻辑cpu、多个线程运行在一个进程上

12. 并发与并行， 类似多线程的是并发；多进程的是并行；
并发：无论上一个开始执行的任务是否完成，当前任务都可以开始执行
并行：有多个任务执行单元，从物理上就可以多个任务一起执行

13. 几种锁的种类：lock，rlock，condition，semaphore，event，timer

14. 原始锁处于 "锁定" 或者 "非锁定" 两种状态之一。它被创建时为非锁定状态。它有两个基本方法， acquire() 和 release() 。当状态为非锁定时， acquire() 将状态改为 锁定 并立即返回。当状态是锁定时， acquire() 将阻塞至其他线程调用 release() 将其改为非锁定状态，然后 acquire() 调用重置其为锁定状态并返回。 release() 只在锁定状态下调用； 它将状态改为非锁定并立即返回。如果尝试释放一个非锁定的锁，则会引发 RuntimeError  异常。

集中操作对锁的影响
||非锁定时|锁定时|
|----------|-------|-----------------------------|
|acquire() | 获得锁 | 阻塞知道锁被释放，然后返回并获得锁|
|release() |error|释放锁|
|conditon.wait() |error|释放锁并阻塞等待notify唤醒；唤醒后且锁被释放时，返回并获得锁|
|condition.notify()|error|唤醒wait的线程|

15. thread.setDaemon(True) 设置线程为守护线程。终端关闭了也依然运行

16. GIL锁：多线程在I/O密集型的工作中有用，计算密集型的一般