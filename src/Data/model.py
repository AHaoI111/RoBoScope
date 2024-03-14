from PySide6.QtGui import QStandardItemModel,QStandardItem,QIcon, QPixmap,QFont
import networkx as x
import os,pickle
from src.Data import Graph
class Graph2Model(QStandardItemModel):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.G = Graph.Graph(True)
        #self.node = 'Root'
        self.setHorizontalHeaderLabels([''])

        self.setupModel()


    def ChildNode(self,node,parent_Modelitem):
        #Node_infor = Graphy.get_node_info(self.G,node)
        #print(Node_infor)

        #self.appendRow(Modelitem)


        list_child = self.G.SubChild(node)
        if list_child:
            #print(parent_row)
            for child_node,child_name in list_child:
                Node_infor = self.G.get_node_info(child_node)

                child_Modelitem = QStandardItem(Node_infor['Data']['label'])
                child_Modelitem.setData(Node_infor)
                child_Modelitem.setEditable(False)
                #print(Node_infor)
                #if node == 'Root':
                #    self.appendRow(child_Modelitem)
                #else:
                parent_Modelitem.appendRow(child_Modelitem)
                self.ChildNode(child_node,child_Modelitem)
        return
    def setupModel(self):
        RootNode_list = self.G.RootNode()
        for node,node_name in RootNode_list:
            #Node_infor = Graphy.get_node_info(self.G, node)
            Modelitem = QStandardItem(node)
            Modelitem.setText(node_name)
            Modelitem.setData(self.G.get_node_info(node))
            Modelitem.setEditable(False)
            #print(Modelitem.data())
            self.ChildNode(node,Modelitem)
            self.appendRow(Modelitem)

    def get_item_data(self,index):
        node_info = self.itemFromIndex(index).data()['Data']
        currentModel = QStandardItemModel()
        currentModel.setHorizontalHeaderLabels(['键','值'])
        currentModel.setColumnCount(2)
        for key,value in node_info.items():
            #print(key,value)
            key_item = QStandardItem(key)
            key_item.setEnabled(False)
            value_item = QStandardItem(str(value))
            if key == 'Image':
                value_item.setEnabled(True)
                value_item.setEditable(False)
                value_item.setIcon(QPixmap('hand.png'))
                file_path_font = QFont()
                file_path_font.setBold(True)
                value_item.setFont(file_path_font)
            else:
                value_item.setEnabled(False)

            currentModel.appendRow([key_item,value_item])
        return currentModel
class Graph2Model_show(QStandardItemModel):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.G = Graph.Graph(True)
        #self.node = 'Root'
        self.setHorizontalHeaderLabels([''])

        self.setupModel()

    def ChildNode(self,node,parent_Modelitem):
        #Node_infor = Graphy.get_node_info(self.G,node)
        #print(Node_infor)

        #self.appendRow(Modelitem)


        list_child = self.G.SubChild(node)
        if list_child:
            #print(parent_row)
            for child_node,child_name in list_child:
                Node_infor = self.G.get_node_info(child_node)

                child_Modelitem = QStandardItem(Node_infor['Data']['label'])
                child_Modelitem.setData(Node_infor)
                child_Modelitem.setEditable(False)
                #print(Node_infor)
                #if node == 'Root':
                #    self.appendRow(child_Modelitem)
                #else:
                parent_Modelitem.appendRow(child_Modelitem)
                #self.ChildNode(child_node,child_Modelitem)
        return
    def setupModel(self):
        RootNode_list = self.G.RootNode()
        for node,node_name in RootNode_list:
            #Node_infor = Graphy.get_node_info(self.G, node)
            Modelitem = QStandardItem(node)
            Modelitem.setText(node_name)
            Modelitem.setData(self.G.get_node_info(node))
            Modelitem.setEditable(False)
            #print(Modelitem.data())
            self.ChildNode(node,Modelitem)
            self.appendRow(Modelitem)

    def get_item_data(self,index):
        node_info = self.itemFromIndex(index).data()['Data']
        currentModel = QStandardItemModel()
        currentModel.setHorizontalHeaderLabels(['键','值'])
        currentModel.setColumnCount(2)
        for key,value in node_info.items():
            #print(key,value)
            key_item = QStandardItem(key)
            key_item.setEnabled(False)
            value_item = QStandardItem(str(value))
            if key == 'Image':
                value_item.setEnabled(True)
                value_item.setEditable(False)
                value_item.setIcon(QPixmap('hand.png'))
                file_path_font = QFont()
                file_path_font.setBold(True)
                value_item.setFont(file_path_font)
            else:
                value_item.setEnabled(False)

            currentModel.appendRow([key_item,value_item])
        return currentModel
    def get_child_data(self,node):
        return self.G.SubChild_data(node)

#show data to scan dictionary and find data of every slide

class Graph2Model_slides(QStandardItemModel):
    def __init__(self,parent = None,files_fold='./data'):
        super().__init__(parent)
        
        self.files_fold = files_fold
        #self.node = 'Root'
        self.setHorizontalHeaderLabels([''])

        self.setupModel()

    def ChildNode(self,parent_Modelitem):
        #parent_code = parent_Modelitem.data['data']['Code']
        parent_node = parent_Modelitem.data()['ID']
        ChildNodes = self.G.SubChild(parent_node)
        for child_node,Child_Code in ChildNodes:
            Node_infor = self.G.get_node_info(child_node)
            child_Modelitem = QStandardItem(Child_Code)
            
            child_Modelitem.setData(Node_infor)
            child_Modelitem.setEditable(False)
            parent_Modelitem.appendRow(child_Modelitem)
            self.ChildNode(child_Modelitem)
   
    def SlideNode(self,file,parent_Modelitem):
        #Node_infor = Graphy.get_node_info(self.G,node)
        #print(Node_infor)
        self.G = Graph.Graph(file)
        #self.appendRow(Modelitem)
        #walk through data tree of slide  
        Rootnodes = self.G.RootNode()
        for node,_ in Rootnodes:
            Node_infor = self.G.get_node_info(node)
            
            parent_Modelitem.setData(Node_infor)
            #print(parent_Modelitem.data())
            self.ChildNode(parent_Modelitem)
        return
    def setupModel(self):
        
        if not os.path.exists(self.files_fold):
            print(self.files_fold)
            return
        for root, dirs, files in os.walk(self.files_fold):
            for file in files:
                if file.split('.')[1] == 'dat':
                   #Node_data ={'Code':file.split('.')[0]}
                   #self.add_node(Node_data)
                   slide_code = file.split('.')[0]
        #RootNode_list = self.G.RootNode()
        #for node,node_name in RootNode_list:
            #Node_infor = Graphy.get_node_info(self.G, node)
                   
                   Modelitem = QStandardItem(slide_code)
                   Modelitem.setText(slide_code)
                   datafile = self.files_fold + '/' + file
                   Modelitem.setData({'Code':slide_code,'file':datafile})
                   Modelitem.setEditable(False)
                   #print(Modelitem.data())
                   #self.SlideNode(slide_code,Modelitem)
                   self.appendRow(Modelitem)

    def get_item_data(self,index):
        node_info = self.itemFromIndex(index).data()['Data']
        currentModel = QStandardItemModel()
        currentModel.setHorizontalHeaderLabels(['键','值'])
        currentModel.setColumnCount(2)
        for key,value in node_info.items():
            #print(key,value)
            key_item = QStandardItem(key)
            key_item.setEnabled(False)
            value_item = QStandardItem(str(value))
            if key == 'Image':
                value_item.setEnabled(True)
                value_item.setEditable(False)
                value_item.setIcon(QPixmap('hand.png'))
                file_path_font = QFont()
                file_path_font.setBold(True)
                value_item.setFont(file_path_font)
            else:
                value_item.setEnabled(False)

            currentModel.appendRow([key_item,value_item])
        return currentModel
    def get_child_data(self,node):
        return self.G.SubChild_data(node) 