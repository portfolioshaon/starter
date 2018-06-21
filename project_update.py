import os,subprocess,urllib,webbrowser

def cmd(command):
    cmd = subprocess.Popen(command, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    stdout, stderr = cmd.communicate('dir c:\\')
    print stdout
    
print("Checking if need initialization...")
if not os.path.exists("prm"):
    
    repon = raw_input("Repository name:")
    repol = raw_input("Repository link:")
    print("Repository link: "+ repol)
    os.makedirs("prm")

    fh = open("prm/project.log","w")
    lines_of_text = "[initialized]\n[remotename:"+repon+"]\n[remotelink:"+repol+"]"
    fh.write(lines_of_text) 
    fh.close()

    fh = open("prm/query.txt","w")
    lines_of_text = "Queries for sloving Issues\n"
    fh.write(lines_of_text) 
    fh.close()

    fh = open("prm/README.md","w")
    lines_of_text = "# "+repon+"\n## Download\nFor downloading use\n       git clone "+repol
    fh.write(lines_of_text) 
    fh.close()

    cmd("git init")
    cmd("git add .")
    cmd("git remote add "+repon+" "+repol)

print(".....")
print("\"update\" - for updating project to repository")
print("\"git\" - for using git")
print("\"query\" - for using google")

command = raw_input("Give me a Command:")

if command == "git" :
    command=""

    print("Retriving project remotename...")
    with open("prm/project.log", "r") as f:
        data = f.readlines()
  
    for c in data:
        print c
        if "remotename" in c:
            start = c.find('[remotename:') + len('[remotename:')
            end = c.find(']', start)
            repon = c[start:end]
            print("Retrived project name: %s"%repon)
        elif "remotelink" in c:
            start = c.find('[remotelink:') + len('[remotelink:')
            end = c.find(']', start)
            repon = c[start:end]
            print("Retrived project link: %s"%repol)


    print(".....")
    print("\"push\" - for pushing your update to remote git")
    print("\"pull\" - ")
    command = raw_input("Give me a Command:")

    if command == "push" :
        command = ""

	umes = raw_input("Commit Message:")
	print("Pushing...")
	cmd("git add .")
	cmd("git commit -m \""+umes+"\"")
	cmd("git push -u "+repon+" master")
elif command == "update" :
    command = ""
    
    print("Retriving project remotename...")
    with open("prm/project.log", "r") as f:
        data = f.readlines()
  
    for c in data:
        print c
        if "remotename" in c:
            start = c.find('[remotename:') + len('[remotename:')
            end = c.find(']', start)
            repon = c[start:end]
            print("Retrived project name: %s"%repon)
        elif "remotelink" in c:
            start = c.find('[remotelink:') + len('[remotelink:')
            end = c.find(']', start)
            repon = c[start:end]
            print("Retrived project link: %s"%repol)

        
    umes = raw_input("Commit Message:")
    print("Pushing...")
    cmd("git add .")
    cmd("git commit -m \""+umes+"\"")
    cmd("git push -u "+repon+" master")

elif command == "query" :
    command = ""

    query=raw_input("Write query, we will pass it to google:")

    fh = open("prm/query.txt","a")
    fh.write(query+"\n")
    fh.close()

    webbrowser.open("https://www.google.com/search?q="+urllib.quote_plus(query))
'''
echo off
setlocal EnableDelayedExpansion
echo Checking if need initialization...
if not exist prm (
	SET /P repon=Repository name:
	SET /P repol=Repository link:
	echo "Ripo Link: !repol!"

	mkdir prm
	echo [initialized] > prm/project.log
	echo [remotename:!repon!] >> prm/project.log
        echo [remotelink:!repol!] >> prm/project.log
	echo "Queries for sloving Issues" > prm/query.txt	
	echo # !repon! > README.md
	echo ## Download >> README.md
	echo For downloading use >> README.md
	echo        git clone !repol! >> README.md


	git init
	git add .
	git remote add !repon! !repol!
)

echo .....
echo "git" - for using git
echo "query" - for using google
SET /p  command=Give me a Command:

IF "%command%" == "git" (
	SET command=

	echo Retriving project remotename...
	FOR /F "tokens=1* delims=[]" %%a in (prm/project.log) do (
		Echo.%%a | findstr /C:"remotename">nul && (
		
			set line=%%a
			set repon=!line:remotename:=!
			Echo Remotename retrived : !repon!
	
		) || (
		    rem Echo remote name cannot retrive
		)
	)

	echo .....
	echo "push" - for pushing your update to remote git
	echo "pull" - 
	SET /p command=Give me a Command:

	IF "!command!" == "push" (
		SET command=

		SET /P umes=Commit Message:
		echo Pushing...
		git add .
		git commit -m "!umes!"
		git push -u !repon! master
	)

) ELSE IF "%command%" == "query" (
	SET command=

	SET /p query=Write query, we will pass it to google:
	echo !query! >> prm/project.log

	set "URLPATH=!query!"
	set "URLPATH=!URLPATH:\=/!"
	set "URLPATH=!URLPATH: =%%20!"
	start https://www.google.com/search?q=!URLPATH!

	endlocal
	endlocal

)
'''
