import sys, argparse
from multiprocessing.dummy import Pool as ThreadPool
from ping3 import ping
from ipToList import ipToList

## 获取用户输入参数
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="set the number of concurrent thread.")
parser.add_argument("-f", help="set task type, 'ping' or 'tcp'.")
parser.add_argument("-ip", help="set ip address")
parser.add_argument("-w", help="set the name of saved file")
args = parser.parse_args()

cfg = {
    "numberOfConcurrent": args.n or 1,
    "taskType": args.f or 'ping',
    "ipStart": '',
    "ipEnd": '',
    "saveFileName": args.w
    }

if args.f == 'ping':
    tempList = args.ip.split('-')
    cfg['ipStart'] = tempList[0]
    cfg['ipEnd'] = tempList[1]
elif args.f == 'tcp':
    cfg['ipStart'] = args.ip
    cfg['ipEnd'] = ''

## 用户输入异常处理

## 处理请求函数
def testPing(address):
    print('ping address: ', address)
    pingResult = ping(address)
    if pingResult:
        return address
    else:
        return None

def testTCP(address):
    print('contact: ', address)
    return 2

## 启动线程
pool = ThreadPool(cfg['numberOfConcurrent'])
if cfg['taskType'] == 'ping':
    ## IP段转换成列表

    taskResults = pool.map(testPing, ipToList(cfg['ipStart'], cfg['ipEnd']))
elif cfg['taskType'] == 'TCP':
    print('tcp')

pool.close()
pool.join()

## 处理结果
result = []
if cfg['taskType'] == 'ping':
    for ip in taskResults:
        if ip:
            result.append(ip)

print('=================')
print("有效ip列表： ", result)