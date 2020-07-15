"""
1,拓扑排序序列
2，构建字典,和一个逆向字典，查询一个地点在原来里出现过，而在逆向字典key中没有出现，则就是出发点
"""
def printResult(inputs):
    reverseInput = {k:v for v,k in inputs.items()}
    # for k,v in inputs.items():
    #     reverseInput[v] =  k
    start = None

    # 找起点
    for k,v in inputs.items():
        if k not in reverseInput:
            start = k
            break

    if start == None:
        print("输入不合理")
        return

    # 从起点开始遍历
    to = inputs[start]
    print(start+"->"+to)
    start = to
    to = inputs[to]
    while to != None:
        print(","+start+"->"+to)
        start = to
        to = inputs.get(to,None)
        # 字典的get方法，相比dict[k]多了一个默认值，如果没找到返回None

if __name__ == "__main__":
    input = dict()
    input["西安"] = "成都"
    input["北京"] = "上海"
    input["大连"] = "西安"
    input["上海"] = "大连"
    printResult(input)