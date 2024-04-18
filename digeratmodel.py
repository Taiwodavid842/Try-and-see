import pickle
def put_to_store(file_list):
	all_digerat={}
	all_digerat["david"]=file_list[0]
	all_digerat["melsy"]=file_list[1]
	all_digerat["Enoch"]=file_list[2]
	try:
        	with open('digerat.pickle', 'wb') as digerati:
            		pickle.dump(all_digerat, digerati)
	except IOError as ioerror:
        	print('file error:'+ str(ioerror))
	return(all_digerat)

def get_from_store():
	all_digerat={}
	try:
		with open('digerat.pickle', 'rb') as digerati:
			all_digerat=pickle.load(digerati)
	except IOError as ioerr:
		print('file error:'+ str(ioerr))
	return(all_digerat)

    
