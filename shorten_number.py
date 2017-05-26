def shorten_number(suffixes, base):
	print 3

filter1 = shorten_number(['','k','m'] ,1000)
filter1('234324') # '234k'
filter1('98234324') # '98m'
filter1([1,2,3]) # '[1, 2, 3]'
filter1('') # ''
filter1('32424234223') # '32424m'


filter2 = shorten_number(['','KB','MB','GB'],1024)
filter2('32') # '32'
filter2('2100') # '2KB'
filter2('pippi') # 'pippi'
filter2('2100k') # '2100k'
filter2('1073741823') # '1023MB'