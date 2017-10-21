import time
def get_current_sec():
	return time.time()

def get_real_time(t):
	t=time.localtime(t)
	year=str(t[0])
	month=str(t[1])
	if len(month)==1:
		month='0'+month
	day=str(t[2])
	if len(day)==1:
		day='0'+day
	hour=str(t[3])
	if len(hour)==1:
		hour='0'+hour
	minute=str(t[4])
	if len(minute)==1:
		minute='0'+minute
	second=str(t[5])
	if len(second)==1:
		second='0'+second
	return year+'-'+month+'-'+day+' '+hour+':'+minute+':'+second
