# coding:utf8

class HtmlOutputer(object):

	def __init__(self):
		self.alldata = []

	def collect_datas(self,datas):
		if datas is None or len(datas) == 0:
			return
		for data in datas:
			self.collect_data(data)

	def collect_data(self,data):
		if data is None:
			return
		self.alldata.append(data)


	def output_html(self):
		fout = open('output.html','w')
		fout.write('<!DOCTYPE html>')
		fout.write("<html>")

		fout.write('<head>')
		fout.write('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
		fout.write('<link rel="stylesheet" href="./index.css">')
		fout.write('</head>')
	
		fout.write("<body>")
		fout.write("<table>")

		for data in self.alldata:
			fout.write("<tr>")
			
			#fout.write("<td>%s</td>"% data['url'] )
			fout.write("<td><h1>%s</h1></td>"% data['title'].encode('utf-8') )
			data['grade'] = data['grade'].encode("utf-8")  

			if data['grade']!='' and float(data['grade']) >= 9.0:
				fout.write("<td><strong class='best'>%s</strong></td>"% data['grade'].encode('utf-8') )
			elif data['grade']!='' and float(data['grade']) >= 8.0:
				fout.write("<td><strong class='better'>%s</strong></td>"% data['grade'].encode('utf-8') )
			elif data['grade']!='' and float(data['grade']) >= 7.0:
				fout.write("<td><strong class='good'>%s</strong></td>"% data['grade'].encode('utf-8') )
			elif data['grade']!='' and float(data['grade']) >= 6.0:
				fout.write("<td><strong class='normal'>%s</strong></td>"% data['grade'].encode('utf-8') )
			elif data['grade']!='' and float(data['grade']) == 0.0:
				fout.write("<td><strong class='nograde'>%s</strong></td>"% data['grade'].encode('utf-8') )
			else:
				fout.write("<td><strong class='bad'>%s</strong></td>"% data['grade'].encode('utf-8') )



			fout.write("</tr>")

		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")

		print "finished"

