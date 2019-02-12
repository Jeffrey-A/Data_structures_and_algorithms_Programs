#Jeffrey Almanzar



from UI import UserInterface
class Euler_CT:

    def __init__(self):
        self.vertices =[]#strorages the vertices
        self.edges ={}  #store the edges
        self.UI = UserInterface() #Using the UserIterface class
        self.reason = None #will state the reason why the graph does not have a Euler circuit or trail
         
    def create_vertex(self,v):
        """post: creates the edges of the graph."""
        if v!="":
            self.vertices.append(v)
        
    def _create_dict(self):
        """post: creates a dictionary with the edges as a keys and an empty list as values."""
        for i in self.vertices:
            self.edges[i] = []
        
    def create_edge(self,v1,v2):
        """pre: the vertices are already created
        post: create the edges of the graph"""
        
        if len(self.edges)==0: #if the dictionary is empte, add the vertices
            self._create_dict()
            
        if v1 in self.vertices and v2 in self.vertices: # if v1 and v2 are valid verteices
            for i in self.edges:
                if i == v1 and v2 not in self.edges[i] : 
                   self.edges[i].append(v2)#append v2 to the value of the key v1. 
                   self.edges[v2].append(i) #append v1 to the value of the key v2.
                   #it allow me to know the degree of each vertex later
                   return True
                
    def get_degree(self,v):
        """pre: all vertices and adges must be already created. v is a valid vertex.
        post: return the degree of vertex v."""
        if v in self.edges:
            return len(self.edges[v])
        
    def has_circuit(self):
        """post: returns true if the graph has an auler circut or returns False otherwise."""
        for i in self.edges:
            if (self.get_degree(i) == 0) or (self.get_degree(i)% 2!= 0): #If one vertex is not connected or has an odd degree
                self.reason = "The graph do not have an Euler Circuit, " +"deg("+i+") is odd or 0."
                return False
        if len(self.vertices)==0:
            self.reason = "The graph do not have an Euler Circuit, not vertices or edges found."
            return False
            
        else:
            self.reason =True
            return True
    
    def has_trail(self):
        """post: returns true if the graph has an auler trail or returns False otherwise."""
        odd = 0
        for i in self.edges:
            if (self.get_degree(i)% 2!= 0): #If a vertex  has an odd degree
                odd +=1
        if odd ==2: #Only two vertices can have odd degrees, in order to have aN Euler trail
            self.reason =True
            return True
        else:
            self.reason = "The graph do not have an Euler trail. Must be exactly 2 veritices with odd degree"
            return False

    def display(self):
        """pre: all vertices and edges must be created.
        post:Displays all the information to the console: vertices, edges, degrees..."""
        print()
        print("Undirected Graph:")
        self.UI.display_vertices(self.vertices)#display vertices
        
        #display edges
        self.UI.display_edges(self.edges)
        
        #display degrees
        print("Degrees:")
        for i in self.edges:
            self.UI.display_degree(i,self.get_degree(i))
            
        self.UI.display_facts() #display when an undireted graph has an Euler circuit or trail
        self.has_circuit()
        self.UI.result(self.reason,"Euler Circuit")
        self.has_trail()
        self.UI.result(self.reason,"Euler Trail")

    def get_file_info(self):
        """post: get the information from the file and storages all the vertices and edges."""
        userfile = input("Type the name of the file(graph.txt): ")
        file = open(userfile,"r")
        info = {}
        x =0

        while True:#read all the lines
            line = file.readline()
            if line =="": #end of the file
                break
            info[x] =line
            x+=1 #new key

        #I am expecting two lines in the file only   
        for i in info:
            if i ==0:
                for vertex in info[i]:
                    if vertex.isalpha() or vertex.isdigit():
                        self.create_vertex(vertex)
            elif i == 1:
                for edge in info[i].split():
                    self.create_edge(edge[1],edge[3])
            else:
                print("INVALID INPUT FOUND IN THE FILE!!")

    def test_one_graph(self):
        input_type = self.UI.get_input_type()
        if input_type == '1':
            
            #getting vertices
            vertices = self.UI.get_vertex() 
            for i in vertices:
                if i !="":
                    self.create_vertex(i)
                    
            #getting edges        
            edges = self.UI.get_edges() 
            for i in edges:
                self.create_edge(i[0],i[1])

            #display
            self.display()

        else:
            self.get_file_info() #get the file name, and storages the vertices and edges
            self.display()
        
                   
    def main(self):
        """controls the whole app."""
        self.UI.intro() #introduction
        self.test_one_graph() #test one graph

        while True:
            user = input("Want to try another graph?  y/n --> ")
            if user[0] !='y':
                print()
                print("Thank you!!")
                break
            self.vertices.clear()
            self.edges.clear()
            self.test_one_graph()
        
        
            
    
