import json

def main():
    f = open("data.json", 'r')

    #ココ重要！！
    json_data = json.load(f) #JSON形式で読み込む
#DEBUG    print(json_data[0])
#DEBUG    print("{}".format(json.dumps(json_data,indent=4)))
#    name_list = ["honoka","eri","kotori","umi","rin","maki","nozomi","hanayo","niko"]
#    for name in name_list:
#        print("{0:6s} 身長：{1}cm BWH: ".format(name,json_data[name]["height"]),end="\t")
#        for i in range(len(json_data[name]["BWH"])):
#            print("{}".format(json_data[name]["BWH"][i]),end="\t")
#        print()

    outlist=[]
    ec2list=[]
    cidr=[]
    for instance in json_data:
        if instance["data"]["type"] == "subnet":
            print(instance["data"]["name"])
            #print("{}".format(json.dumps(instance["data"],indent=4)))
            #print("{}".format(json.dumps(instance["data"]["node_data"],indent=4)))
            #print(instance["data"]["name"]," subnetId:",instance["data"]["node_data"]["SubnetId"]," arn:",instance["data"]["id"])
            cidr.append({'name':instance["data"]["name"],'id':instance["data"]["id"],'subnet':instance["data"]["node_data"]["SubnetId"]})
            #print("debug",cidr[-1]['name'])
            outlist.append(instance)
        elif instance["data"]["type"] == "ec2":
            print(instance["data"]["name"])
            ec2list.append(instance)
#            print("{}".format(json.dumps(instance["data"]["node_data"]["NetworkInterfaces"],indent=4)))
        else:
            outlist.append(instance)

    print("CIDR: ",cidr)

    #print("outlist",outlist)
    #print("ec2list",ec2list)

    fw = open('data2.json','w')
    outlist += ec2list

    json.dump(outlist,fw,indent=4)
if __name__=='__main__':
    main()
