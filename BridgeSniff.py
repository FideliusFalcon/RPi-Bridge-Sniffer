import yaml #PyYaml 
import os

def readYAML(fileName):
    with open(fileName, 'r') as stream:
        try:
            yamlDic = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return yamlDic
    
def writeYAML(fileName,yamlDic):
    with open(fileName, 'w') as outfile:
        yaml.dump(yamlDic, outfile, default_flow_style=False)

def CreateBridge(iface1,iface2,bridge):
    """A function that creates a bridge from the configuration in the yaml file"""
    command = "sudo brctl addbr", bridge
    os.system(command)
    command = "sudo ifconfig", iface1, "0.0.0.0 down"
    os.system(command)
    command = "sudo ifconfig", iface2, "0.0.0.0 down"
    os.system(command)
    command = "sudo brctl addif", bridge, iface1, iface2
    os.system(command)
    command = "sudo ifconfig", bridge, "up"
    os.system(command)
    command = "sudo ifconfig", iface1, "up"
    os.system(command)
    command = "sudo ifconfig", iface2, "up"
    os.system(command)
            
def StartSniff(fileName, number, bridge, counter):
    counter += 1
    writeYAML("config.yaml", yamlDic)

    os.system('sudo mkdir loot')
    command = "sudo tcpdump -i " + str(bridge) + " -w " + "loot/" + str(fileName) + "-" + str(number) + ".pcap"
    os.system(command)

def CreateConfig():
    yamlDic = readYAML("config.yaml")
    counter = yamlDic[1]["counter"]
    fileName = yamlDic[0]["config"]["filename"]
    bridge = yamlDic[0]["config"]["bridge"]
    iface1 = yamlDic[0]["config"]["iface1"]
    iface2 = yamlDic[0]["config"]["iface2"]
    counter = yamlDic[1]["counter"] = counter

    return counter, fileName, bridge, iface1, iface2
    

if __name__ == "__main__":
    counter, filename, bridge, iface1, iface2 = CreateConfig()
    CreateBridge(iface1, iface2, bridge)
    StartSniff(filename, counter, bridge, counter)