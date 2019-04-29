import json
import sys

def main():
    args = sys.argv

    target=args[1]

    f = open("data.json", 'r')

    json_data = json.load(f) 
#DEBUG    print(json_data[0])
#DEBUG    print("{}".format(json.dumps(json_data,indent=4)))

    outlist=[]
    ec2list=[]
    cidr=[]
    for instance in json_data:
        if instance["data"]["type"] == "subnet":
            #print(instance["data"]["name"])
            #print("{}".format(json.dumps(instance["data"],indent=4)))
            #print("{}".format(json.dumps(instance["data"]["node_data"],indent=4)))
            #print(instance["data"]["name"]," subnetId:",instance["data"]["node_data"]["SubnetId"]," arn:",instance["data"]["id"])
            cidr.append({'name':instance["data"]["name"],'id':instance["data"]["id"],'subnet':instance["data"]["node_data"]["SubnetId"]})
            #print("debug",cidr[-1]['name'])
            outlist.append(instance)
        elif instance["data"]["type"] == "ec2":
            #print(instance["data"]["name"])
            ec2list.append(instance)
#            print("{}".format(json.dumps(instance["data"]["node_data"]["NetworkInterfaces"],indent=4)))
        else:
            outlist.append(instance)

#    print("CIDR: ",cidr)

    for this_cidr in cidr:
        #print("this_cidr:",this_cidr)
        if target in this_cidr['name']:
            target_subnet=this_cidr['subnet']
            target_arn=this_cidr['id']

    #print("target subnet:",target_subnet)
    #print("target arn:",target_arn)
    #print("outlist",outlist)
    #print("ec2list",ec2list)

    for ec2 in ec2list:
        #print("ec2:",ec2['data']['name'])
        #print("ec2:  nics:",ec2['data']['node_data']['NetworkInterfaces'])
        #for nic in ec2[]
        #print("       parent(before):",ec2['data']['parent'])
        for this_nic in ec2['data']['node_data']['NetworkInterfaces']:
            #print("       this_nic:",this_nic['PrivateIpAddress'],'/',this_nic['SubnetId'])
            if this_nic['SubnetId'] == target_subnet:
                ec2['data']['parent']=target_arn
        #print("       parent(after):",ec2['data']['parent'])
    fw = open('data.json','w')
    outlist += ec2list

    json.dump(outlist,fw,indent=4)

if __name__=='__main__':
    main()
