
class Node:

    def __init__(self,edge):
        self.edge = edge
        self.children = {}

    def __repr__(self):
        return self.edge


class SuffixTree:


    def __init__(self,s):
        self.root = Node(None)
        self.edges = []
        self.suffix_add(s) 

    def __repr__(self):
        """Represent the Suffix tree by the edges"""
        return f"{self.edges}"

    def suffix_add(self, string): 
        """process each suffix in the string"""
        for i in range(0,len(string)):
            self.build(string[i:])
        self.edges = self.inorder(self.root)


    def build(self, s):

        curr = self.root
        j = 0

        while(j < len(s)):
            key = s[j]
            # check if current node has a child starting with first char 
            if key in curr.children:
                child = curr.children[key]
                edge = child.edge
                
                # check character by character if suffix matches the label of edge
                k = j
                edge_end = False
                while(k - j < len(edge)):

                    location = k - j

                    if(k == len(edge)):
                        # suffix comes short of the edge's length
                        edge_end = True
                        break
                    elif(s[k] == edge[location]):
                        # we keep checking for matching character in suffix with node edge
                        k += 1
                    else:
                        # missmatch
                        edge_end = True
                        break
                
                if edge_end:
                    # remaining part of suffix                 
                    s_remainder = s[k:]
                    keys = (key,s[k])
                    self.split_edge(curr, child, location, keys, s_remainder)
                    break
                else:
                    # child reached before suffix is exhausted
                    curr = child
                    j = k
            else:
                # if current node does not have child starting with first character in s
                node = Node(s[j:])
                curr.children[key] = node
                break


    def split_edge(self,curr,child,location,keys,s_remainder):
        #splittin of edge text left and right portion & key for new child link
        child_key = child.edge[location]
        left_edge = child.edge[:location] 
        right_edge = child.edge[location:]

        #creating left node with left part of edge stopping location index
        left_node = Node(left_edge)
        curr.children[keys[0]] = left_node

        #child node gets linked to curr (new node) right part of suffix
        child.edge = right_edge
        left_node.children[child_key] = child
        
        #node with remainder of suffix 
        remainderNode = Node(s_remainder)
        left_node.children[keys[1]] = remainderNode 


            
    def inorder(self,root): 
        """puts edges edge into a list"""
        
        if root: 

            for node in root.children.values(): 
                self.inorder(node)
                self.edges.append(node.edge)

        return self.edges


# ['A', 'T', 'AAATG$', 'G$', 'A', 'ATG$', 'TG$', 'T', 'AAATG$', 'G$', 'G$', '$']

def file_parser():  
    file = open("input","r")
    data = file.read().splitlines()

    string = ""

    for line in data:
        string += line

    if string[-1] != '$':
         string = string[:-1]

    file.close()
    return string

def output_write(edge_list): 

    file = open("output", "w")

    for edge in edge_list:
        file.write(edge + "\n")
    file.close()




#ATAAATG$
#BANANA
string = file_parser()
suffix = SuffixTree(string)
output_write(suffix.edges)
#print(suffix)

#print(suffix.root.children['A'].edge)

    