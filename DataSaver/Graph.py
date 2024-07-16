# -*- encoding: utf-8 -*-
"""
@Description:
用于存储数据的方式
@File    :   Graph.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""

import networkx as nx
import os,datetime
import pickle
import uuid
#global G
#每一张玻片保存一个数据文件
class Graph_slide():
    #初始化图对象，如果新建，参数for_example指明是否加入示例数据
    def __init__(self,Code):
        self.G = nx.DiGraph()
        Node_data ={'Code':Code}
        self.add_node(Node_data)
 
    def save(self,path):
        with open(path, 'wb') as f:
            pickle.dump(self.G, f)
    #新增节点，第一个参数为字典，其中Code为关键字，必填。第二个参数为新增节点的父节点，如果新增根节点，不填入第二个参数
    def add_node(self,Node_Data,parent_node = ''):
        Node_ID = str(uuid.uuid4()) # 生成一个 UUID
        self.G.add_nodes_from([(Node_ID,Node_Data)])
        if parent_node !='':
            self.G.add_edge(parent_node,Node_ID)
        return Node_ID
    def get_IDfromCode(self,code):
        node_list = nx.get_node_attributes(self.G, "Code")

        for key,value in node_list.items():

            if value == code:
                return key
        return 'Not find ID from '+code
    def set_attr_node(self,node,attr_dict):
        for key,value in attr_dict.items():
            self.G.nodes[node][key] = value
        return True
    def get_node_info(self,node):
        #return nx.get_node_attributes(G,"Name")[node]
        #获取节点的信息（字典结构）
        node_data = self.G.nodes[node]
        #增加ID
        node_info = {}
        node_info['ID'] = node
        node_info['Data'] = node_data
        return node_info
#全部玻片数据放入同一个目录，每个玻片数据文件Code.dat
class Graph():
    #初始化图对象，如果新建，参数for_example指明是否加入示例数据
    def __init__(self,datafile):

        if os.path.exists(datafile):
            with open(datafile, 'rb') as f:
                self.G = pickle.load(f)
        #else:
        #    self.G = nx.DiGraph()
            #G.add_node('Root', Name='Root')
        #    if for_example:
        #        self.example('Root')
                  

    def example(self,parent_node):
        if parent_node == 'Root':
            #一级节点，病患玻片
            Code_list = ['2304181110','2304181111','2304181112','2304181113']
            Label_list = ['张毅','王铁','刘曼','李晓']
            for i in range(0, 3):
                #unique_id = str(uuid.uuid4())  # 生成一个 UUID
                data = {}
                data['Code'] = Code_list[i]
                data['label'] = Label_list[i]
                root_id = self.add_node(data)

                unique_id = self.example(root_id)
                #self.G.add_nodes_from([(unique_id, data)])
        else:
            # 二级节点
            code_list = ['低倍20x', '高倍100x']
            for Code in code_list:
                data = {}
                parent_code = self.get_node_info(parent_node)['Data']['Code']
                new_data = {}
                new_data['new_attr'] = '新增属性'
                self.set_attr_node(parent_node,new_data)
                #print(parent_code)
                #print(self.get_IDfromCode(parent_code))
                data['Code'] = parent_code+'_'+Code
                data['label'] = Code
                PP_code = self.add_node(data,parent_node)
                #self.G.add_node(unique_id, Code = Code,Name=Code)
                #self.G.add_edge(parent_node, unique_id)
                #三级节点
                for j in range(0,3):
                    #c_unique_id = str(uuid.uuid4())  # 生成一个 UUID
                    data={}
                    data['Code'] = 'Img20230713100'+str(j)
                    data['label'] = data['Code']
                    data['Date'] = str(datetime.date.today())
                    data['Pos']  = '(0,'+str(j)+')'
                    data['Desc'] = '区域扫描'
                    data['Image'] = 'D:\python_note\GUI\DataMan\TB00018.jpg'
                    #bbox: x,y,w,h
                    data['bbox']  = [(201,100,50,50),(101,102,50,50)]
                    data['Annotation'] = ['上皮细胞','白细胞']
                    unique_id = self.add_node(data,PP_code)
                    #self.G.add_nodes_from([(c_unique_id, data)])
                    #self.G.add_edge(unique_id, c_unique_id)

        return unique_id
    def SubChild(self,node):
        #global G
        node_list = []
        Name = nx.get_node_attributes(self.G, "Code")
        nl = sorted(self.G.neighbors(node))
        if len(nl) > 0:
            for nbr in nl:
                node_list.append((nbr,Name[nbr]))
        return node_list
    def SubChild_data(self,node):
        node_list = []
        nl = sorted(self.G.neighbors(node))
        if len(nl) > 0:
            for nbr in nl:
                node_list.append(self.get_node_info(nbr))
        return node_list
    def RootNode(self):
        node_list = []
        node_degree = self.G.in_degree()
        node_degree_0 = list(filter(lambda nd:nd[1]==0,node_degree))
        Name = nx.get_node_attributes(self.G, "Code")
        #    #print(node_degree_0[0][0])
        #nl = [nd[0] for nd in node_degree_0]
        for node,_ in node_degree_0:
        #node = node_degree_0[0][0]
            #print('root:'+node)
            node_list.append((node,Name[node]))
        return node_list
    def save(self,path):
        with open(path, 'wb') as f:
            pickle.dump(self.G, f)
    #新增节点，第一个参数为字典，其中Code为关键字，必填。第二个参数为新增节点的父节点，如果新增根节点，不填入第二个参数
    def add_node(self,Node_Data,parent_node = ''):
        Node_ID = str(uuid.uuid4()) # 生成一个 UUID
        self.G.add_nodes_from([(Node_ID,Node_Data)])
        if parent_node !='':
            self.G.add_edge(parent_node,Node_ID)
        self.save()
        return Node_ID
    def get_IDfromCode(self,code):
        node_list = nx.get_node_attributes(self.G, "Code")

        for key,value in node_list.items():

            if value == code:
                return key
        return 'Not find ID from '+code
    def set_attr_node(self,node,attr_dict):
        for key,value in attr_dict.items():
            self.G.nodes[node][key] = value
        return True
    def get_node_info(self,node):
        #return nx.get_node_attributes(G,"Name")[node]
        #获取节点的信息（字典结构）
        node_data = self.G.nodes[node]
        #增加ID
        node_info = {}
        node_info['ID'] = node
        node_info['Data'] = node_data
        return node_info