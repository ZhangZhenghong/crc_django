#!/usr/bin/python
# coding=utf-8

#从NCBI下载XML文件, display setting 选info,输出选择file->XML,然后 运行该脚本即可
import xml.dom.minidom
import sys
print(len(sys.argv))
if(len(sys.argv) < 2):
	print("Usage: python Scriptname file_name")
	exit()

fout=open(sys.argv[1]+".result.txt", "w")

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse(sys.argv[1])
rootnode = DOMTree.documentElement
 
for taxon in rootnode.childNodes:
	if taxon.nodeType == 1:
		for strain in taxon.childNodes:
			if strain.nodeType == 1:
				if strain.tagName == 'TaxId':
					print(strain.childNodes[0].data, end="\t")
					fout.write(strain.childNodes[0].data + "\t")
				if strain.tagName == 'Lineage':
					print(strain.childNodes[0].data, end="\n")
					fout.write(strain.childNodes[0].data + "\n")

#print(root.getElementsByTagName('Lineage')[1].childNodes[0].data)

