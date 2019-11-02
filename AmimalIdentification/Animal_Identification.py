import collections
def getList():
    conditionList=[]
    conclutionList=[]
    with open('data.txt',encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            line=line.strip('\n')
            if  line:
                dataList = line.split(' ')
                conditionList.append(dataList[:-1])
                conclutionList.append(dataList[-1])
    return conditionList,conclutionList

def getTopology(conditionList:list,conclutionList:list):
    topology=collections.OrderedDict()
    inIndex=[]
    for i in conditionList:
        sum=0
        for  j in i:
            if j in conclutionList: sum+=conclutionList.count(j)
        inIndex.append(sum)
        #print(inIndex)
    #构建条件与结论的有序字典
    while(len(inIndex)!=inIndex.count(-1)):
        for i,ind in enumerate(inIndex):
            if ind==0: 
                topology[tuple(conditionList[i])]=conclutionList[i]
                #print(topology)
                inIndex[i]=-1
                for j,conditionItem in enumerate(conditionList):
                    if(conclutionList[i] in conditionItem ): inIndex[j]-=1
    return topology
def isJinI(j ,i):
    for k in j:
        if k not in i: return False
    return True

def getInfer(topology:collections.OrderedDict,inputList:list) :
    flag=False
    progress=""
    for i in topology:
        if isJinI(i,inputList):
            progress+="由{condition}推导出{conclution}\n".format(condition=i,conclution=topology[i])
            final=topology[i]
            flag=True
        inputList.append(topology[i])
    if flag==True:
        progress+="最终推导出：{conclution}".format(conclution=final)
    else:progress="条件不足，无法推导"
    return progress
def action(text):
        inputList=text.split(" ")
        conditionList,conclutionlist=getList()
        topology=getTopology(conditionList,conclutionlist)
        progress=getInfer(topology,inputList)
        return progress
# if __name__=="__main__":action()