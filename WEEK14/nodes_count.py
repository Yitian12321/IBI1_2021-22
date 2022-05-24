from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt

#All child nodes of one node is needed and its further child nodes is needed as well.
#Calculate the number of parent nodes of the child nodes.
#This function can get the id  of parent nodes
def find_parent_nodes(node_id, parent_ids):
    immediate_ids = node_family[node_id]
    for immediate_id in immediate_ids:
        parent_ids.add(immediate_id) 
        find_parent_nodes(immediate_id, parent_ids)

#Open the XML file.
xmlDOM = xml.dom.minidom.parse("go_obo.xml")
collection = xmlDOM.documentElement
terms = collection.getElementsByTagName("term")

#creat two dictionary to store the terms and overall
node_family = {}
result_overall = {}

#All nodes of each term is needed to get
#The data will be stored in the node_family.
for term in terms:
    node_id = term.getElementsByTagName("id")[0].childNodes[0].data
    immediate_ids = []
    for is_a in term.getElementsByTagName("is_a"):
        immediate_ids.append(is_a.childNodes[0].data)
    node_family[node_id] = immediate_ids
    result_overall[node_id] = 0

#Calculate the parent nodes of each child node.
for key in node_family.keys():
    parent_ids = set()
    find_parent_nodes(key, parent_ids)
    for parent_id in parent_ids:
        result_overall[parent_id] += 1 #The number of all child nodes is same as each parent node.

#Draw distribution plots of overall result
plt.boxplot(result_overall.values(), vert=True, whis=1.5, showbox=True, showcaps=True, showfliers=True)
plt.title('The distribution of child nodes across each GO term')
plt.xlabel("All terms in the GO")
plt.ylabel("number of 'translation' childNodes of terms")
plt.show()



#Get the list of terms associated with 'translation'.
term_list = []
for term in terms:
      defstr_text = term.getElementsByTagName("defstr")[0].childNodes[0]
      if 'translation' in defstr_text.data:
          term_list.append(term)

#Selected nodes with translation in the node_family
node_list = []
for term in term_list:  
    node_id = term.getElementsByTagName("id")[0].childNodes[0].data 
    node_list.append(node_id)

result_translation = []
for node in node_list:
      result_translation.append(result_overall[node])

#Draw the distribution plots of terms related to translation
plt.boxplot(result_translation, vert=True, whis=1.5, showbox=True, showcaps=True, showfliers=True)
plt.title('The distribution of child nodes across each GO term ')
plt.xlabel("Terms relevant to translation")
plt.ylabel("number of 'translation' childNodes of terms")
plt.show()


#Calculate the average
average_overall= sum(result_overall.values())/len(result_overall.values())
average_translation= sum(result_translation)/len(result_translation)

#print the results
print("Each term of overall Gene Ontology have", average_overall, "child nodes on average.")
print("Each translation term have", average_translation, "child nodes on average.")

if average_overall > average_translation:
   print("The 'translation' terms have more child nodes than the overall Gene Ontology terms.")
else:
   print("The overall Gene Ontology terms have more child nodes than the 'translation' terms.")

#Result
#Each term of overall Gene Ontology have 12.08177017321504 child nodes on average.
#Each translation term have 13.486486486486486 child nodes on average.
#The overall Gene Ontology terms have more child nodes than the 'translation' terms.

#In this task, I used to feel confused and got help from my classmates Mr.Deng, Mr.Tu.Thanks for their help.
