import plotly 
import sys
if len(sys.argv)<3:
	print('Enter username as first argument and api key as second argument and run the script again!')
else:
	username=sys.argv[1]
	api_key=sys.argv[2]
	plotly.tools.set_credentials_file(username=username, api_key=api_key)