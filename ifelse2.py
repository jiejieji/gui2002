


friend = ['Korkai','Khorkai','Khorkwai']


friend2 = {'Korkai':'เด็กชายก.ไก่',
			'Khorkai':'เด็กชายข.ไข่'}
			
visitor = 'Korkai'


if visitor in friend or visitor.title() in friend:
	print('เป็นเพือนลุงเอง เชินมาได้')
	if visitor in friend2 or visitor.title() in friend2:
		print('สวัสดี' + friend2[visitor.title()])
	else:
		print('สวัสดีคุนลูกค้า')	




else:
	print('เอ้ย! คุนเป็นไคร ไม่มีชื่อในเมมเบอร์')	