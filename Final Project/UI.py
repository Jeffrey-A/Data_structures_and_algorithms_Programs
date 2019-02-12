#Jeffrey Almanzar

class UserInterface:
    """Display information to the console."""
    
    def __init__(self):
        self.Input_type= 0

    def intro(self):
        """post: prints an introduction of the app."""
        print("---------------------------------------------------------------------------")
        print("*                    Euler Circuit and Trail                              *")
        print("---------------------------------------------------------------------------")
        print("Input sources:")
        print("\t1.Keybord")
        print("\t2.File")
        
        
    def get_input_type(self):
        """post: gets the input source and returns it."""
        
        while True:
            self.Input_type = input("Please indicate the input source (1 or 2): ")
            
            if self.Input_type == '1' or self.Input_type=='2':
                return self.Input_type
                break
            else:
                print("Invalid input!!")
                   
        
    def get_vertex(self):
        """post: gets all the vertices and returns them."""
        user = input("Type all the vertices separated by commas a,b,...,v: ")
        vertices = user.split(",")
        return vertices
    
    def get_edges(self):
        """post: gets all the edges and returns them."""
        
        print("Type all the edges one by one hit enter when done:")
        edges =[]
        while True:
            user = input("(a,b)--> a,b: ")
            if user =="":
                break
            if (user[0].isalpha() or user[0].isdigit())  and (user[2].isalpha() or user[2].isdigit()): #the verties can be letters all numbers
                edges.append((user[0],user[2]))
        return edges
        
    def display_vertices(self,vertices):
        """post: prints the vertices to the console."""
        print("Vertices:",end="  ")
        ver =''
        for i in vertices:
            ver = ver+i+","
        print(ver[:len(ver)-1])

    def display_degree(self,v,n):
        """post: prints the degree of each vertex."""
        print("\tdeg("+v+") =",n)

    def display_edges(self,edges):
        """post: prints the edges."""
        print("Edges:",end="  ")
        edge =''
        for i in edges:
            for j in edges[i]:
                if "("+j[0]+","+i[0]+")" not in edge:
                    edge = edge+"("+i[0]+","+j[0]+"),"
        print(edge[:len(edge)-1])
        
    def display_facts(self):
        """post: prints when the graph has an Euler circuit or trail according to zybook."""
        print()
        print("Facts:")
        print("1.Euler circuit:")
        print("\tIf an undirected graph G is connected and every vertex in G has an even degree, then G has an Euler circuit.")
        print("2.Euler trail:")
        print("\tAn undirected graph G has an Euler trail if and only if G is connected and has exactly two vertices with odd degree.")
        print()
        print("Assuming the graph is undirected and connected:")
    
    def result(self,reason,Cir_or_trail):
        """pre: reason is a boolean or a string, Cir_or_trail is a string.
        post: prints if Cir_or_trail has an Euler circuit al trail."""
        if reason ==True:
            print("The graph has an",Cir_or_trail+".")
        else:
            print(reason)
        
        

