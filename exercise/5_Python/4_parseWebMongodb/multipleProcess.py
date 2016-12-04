import multiprocessing
import time

def run(fn):
    time.sleep(1)
    # fn: 函数参数是数据列表的一个元素
    print(fn*fn)
    return fn*fn

if __name__ == "__main__":
    testFL = [1, 2, 3, 4, 5, 6]
    print('单进程顺序执行:') #顺序执行(也就是串行执行，单进程)
    startTime = time.time() #开始计时,time1
    for fn in testFL:
        run(fn)
    endTime1 = time.time() #开始计时,time2,单进程计算结束
    print('单进程所花时间为: {}'.format(endTime1-startTime))

    print('开始创建多进程,并行执行')
    pool = multiprocessing.Pool() #创建拥有多个进程数量的进程池,注:Pool()中没有填入参数表示由计算机自动计算创建几个进程
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    rl = pool.map(run,testFL)
    pool.close() #关闭进程池，不再接受新的进程
    pool.join() #主进程阻塞等待子进程的退出
    endTime2 = time.time() #开始计时,time3,多进程计算结束
    print('多进程所花事件为: {}'.format(endTime2-endTime1))
    print(rl)





