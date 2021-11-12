import subprocess


def displayInput(text, defaultValue):
	value = input(text+" (default="+defaultValue+") : ")
	if(value == ""):
		value=defaultValue

	return value


def menuExportDB():
	subprocess.run(["clear"])
	print("Export Database")

	host = displayInput("Masukan host", "localhost")
	port = displayInput("Masukan port", "27017")
	database = displayInput("Masukan database", "db")

	output = subprocess.run(["mongodump", "--host", host, "--port", port, "--db", database])
	print(output)

def menuImportDB():
	subprocess.run(["clear"])

	print("Import Database")

	host = displayInput("Masukan host", "localhost")
	port = displayInput("Masukan port", "27017")
	from_db = displayInput("Masukan nama database", "miti")
	target_db = displayInput("Masukan target database", "miti")

	# renamedb before import
	output = subprocess.run(["mv", "dump/"+from_db, "dump/"+target_db])

	# mongorestore
	output = subprocess.run(["mongorestore", "--host", host, "--port", port])
	print(output)	


print("MONGO-TOOLS-CLI")
print("=================")
print("PILIH MENU:")
print("1. Backup Database")
print("2. Restore Database")
print("3. Display Database")

menu = displayInput("Masukan No: ", "")

if(menu == "1"):
	menuExportDB()
elif(menu == "2"):
	menuImportDB()
elif(menu == "3"):
	print("display database")
else:
	print("menu tidak ada")