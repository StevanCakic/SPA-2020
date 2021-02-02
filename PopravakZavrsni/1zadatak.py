# Napomena: vama je ostavljeno da testirate i eventualno odradite sitne ispravke u slucaju da ima gresaka

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
#a
    def dodaj(self, data):
        if self.root is None:      
            self.root = Node(data)  
        else:
            self._dodaj(data, self.root)
    
    def _dodaj(self, data, current_node):    
        if data["potrosnja"] < current_node.value["potrosnja"]:        
            if current_node.left is None:      
                current_node.left = Node(data)  
            else:
                self._insert(data, current_node.left)  
        elif data["potrosnja"] > current_node.value["potrosnja"]: 
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("The value is already in a tree")

    def dodaj_kupca(self):
        N = int(input("Unesi broj kupaca: "))
        brojac = 1
        while brojac<= N:
            naziv = input("Unesi naziv kupca: ")
            potrosnja = input("Unesi potrosnju: ")
            kupac = {"naziv_kupca":naziv,"potrosnja":potrosnja}
            if brojac == 1:
                stblo_pot = BinaryTree(kupac)
            else:
                stblo_pot.insert(kupac)
            brojac += 1
        print(stblo_pot.inorder_print(stblo_pot.root,""))
        print()
    
#b

    def _trazi(self, current_node, min_potrosnja):
        vr=[]
        if min_potrosnja > current_node.value['potrosnja'] and current_node.right:
            vr.append(current_node.value['ime'])
        elif min_potrosnja <= current_node.value['potrosnja'] and current_node.left:
            return self._find(current_node.left, min_potrosnja)      
        return vr

#c
    def max_portosnja(self, node):          
        current = node
        while current.right:              
            current = current.right       
        return current.value["ime"]
    
    def max(self):                    
        if self.root:
            return self.max_portosnja(self.root)
#d
    def inorder(self, start, traversal):    
        
        if start:                                                          
            traversal = self.inorder_print(start.left, traversal)  
            traversal += (str(start.value) + "->")                 
            traversal = self.inorder_print(start.right, traversal)  
        return traversal