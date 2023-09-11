from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon, QPixmap, QFont
import networkx
import UI.Data.Graph as Graph


class Graph2Model(QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.G = Graph.Graph(True)
        # self.node = 'Root'
        self.setHorizontalHeaderLabels([''])

        self.setupModel()

    def ChildNode(self, node, parent_Modelitem):
        # Node_infor = Graphy.get_node_info(self.G,node)
        # print(Node_infor)

        # self.appendRow(Modelitem)

        list_child = self.G.SubChild(node)
        if list_child:
            # print(parent_row)
            for child_node, child_name in list_child:
                Node_infor = self.G.get_node_info(child_node)

                child_Modelitem = QStandardItem(Node_infor['Data']['label'])
                child_Modelitem.setData(Node_infor)
                child_Modelitem.setEditable(False)
                # print(Node_infor)
                # if node == 'Root':
                #    self.appendRow(child_Modelitem)
                # else:
                parent_Modelitem.appendRow(child_Modelitem)
                self.ChildNode(child_node, child_Modelitem)
        return

    def setupModel(self):
        RootNode_list = self.G.RootNode()
        for node, node_name in RootNode_list:
            # Node_infor = Graphy.get_node_info(self.G, node)
            Modelitem = QStandardItem(node)
            Modelitem.setText(node_name)
            Modelitem.setData(self.G.get_node_info(node))
            Modelitem.setEditable(False)
            # print(Modelitem.data())
            self.ChildNode(node, Modelitem)
            self.appendRow(Modelitem)

    def get_item_data(self, index):
        node_info = self.itemFromIndex(index).data()['Data']
        currentModel = QStandardItemModel()
        currentModel.setHorizontalHeaderLabels(['键', '值'])
        currentModel.setColumnCount(2)
        for key, value in node_info.items():
            # print(key,value)
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

            currentModel.appendRow([key_item, value_item])
        return currentModel


class Graph2Model_show(QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.G = Graph.Graph(True)
        # self.node = 'Root'
        self.setHorizontalHeaderLabels([''])

        self.setupModel()

    def ChildNode(self, node, parent_Modelitem):
        # Node_infor = Graphy.get_node_info(self.G,node)
        # print(Node_infor)

        # self.appendRow(Modelitem)

        list_child = self.G.SubChild(node)
        if list_child:
            # print(parent_row)
            for child_node, child_name in list_child:
                Node_infor = self.G.get_node_info(child_node)

                child_Modelitem = QStandardItem(Node_infor['Data']['label'])
                child_Modelitem.setData(Node_infor)
                child_Modelitem.setEditable(False)
                # print(Node_infor)
                # if node == 'Root':
                #    self.appendRow(child_Modelitem)
                # else:
                parent_Modelitem.appendRow(child_Modelitem)
                # self.ChildNode(child_node,child_Modelitem)
        return

    def setupModel(self):
        RootNode_list = self.G.RootNode()
        for node, node_name in RootNode_list:
            # Node_infor = Graphy.get_node_info(self.G, node)
            Modelitem = QStandardItem(node)
            Modelitem.setText(node_name)
            Modelitem.setData(self.G.get_node_info(node))
            Modelitem.setEditable(False)
            # print(Modelitem.data())
            self.ChildNode(node, Modelitem)
            self.appendRow(Modelitem)

    def get_item_data(self, index):
        node_info = self.itemFromIndex(index).data()['Data']
        currentModel = QStandardItemModel()
        currentModel.setHorizontalHeaderLabels(['键', '值'])
        currentModel.setColumnCount(2)
        for key, value in node_info.items():
            # print(key,value)
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

            currentModel.appendRow([key_item, value_item])
        return currentModel

    def get_child_data(self, node):
        return self.G.SubChild_data(node)
