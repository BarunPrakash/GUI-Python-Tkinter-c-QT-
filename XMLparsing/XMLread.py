# Designed By Barun 9 sept 2019
#productivity Trackers!!!


##########################################################
#!/usr/bin/python3
import xml.etree.ElementTree as ET
import subprocess
from datetime import date
#############################################################


debug = 0
########################################################
def xmlOperations(date ,noooflineCode):

	tree = ET.parse('Productivity.xml')
	root = tree.getroot()
#	debug=0
	if debug:
		print(date)
		print(noooflineCode)
	#find =root.find('timeSeries')
	#print(find.attrib)
	#root = ET.fromstring('Productivity.xml')


#	for variableParam in root.find('timeSeries').attrib['date']:
	for variableParam in root.findall('timeSeries'):
	#for rank in root.iter('variableParam'):
	#	new_rank = int(rank.text) + 12
	#	rank.text = str(new_rank)
	#	rank.set('updated', 'yes')
	#	print(variableParam)
		if debug:
			new_variableParam = int (variableParam.text) + noooflineCode
			variableParam.text =str(new_variableParam)
			variableParam.set ('updated','yes')
	
			tree.write('Productivity.xml')
		if(variableParam.attrib['date']  ==date):
			nl_lines = int(variableParam.find('noflines').text)+ noooflineCode
			variableParam.text =str(nl_lines)
			variableParam.set('update','yes')
			
	tree.write('Productivity.xml')

			
#			print(nl_lines)
			

	#	print (child.tag)
	#	print(child.attrib)
	#	print(root[0][1].text)




def ProcessFunctionforCompilation():
	call =subprocess.call(["gcc", "test.c"])
	lines =0 
	#call =subprocess.call("./a.out") 

	if ( call ): 
		today = date.today()
		lines = sum(1 for line in open('test.c'))
		print (lines)
	#print("Today's date:", today)
	#return lines
	return lines


##################################################################################
def main():

	nl_lines= ProcessFunctionforCompilation()
#	date =date.today()
	xmlOperations("1",nl_lines)



if __name__ == "__main__":
	main()	















