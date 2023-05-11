version = [1, 0]
version = [str(i) for i in version]
import basic
import sys
import os
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)
fileRun = sys.argv[0]
timesKeyBoardInterrupt = 0
if sys.argv[0].find(".py"):
    if len(sys.argv) >= 2:
        fileRun = sys.argv[1]
    else:
        fileRun = None
if fileRun:
    if fileRun.strip() == "":
        print("Couldn't find file")
    else:
        # figure out if file even exists
        try:
            # check if fileRun includes a ./ if not add it at the beginning
            if fileRun.find("./") == -1:
                fileRun = "./" + fileRun
                
            f = open(fileRun, "r")
            entireText = f.read()
            # get the file name without extension
            fileName = fileRun.split("/")[-1]
            
            # if fileRun.find(".ddl") == -1:
            #     print("\033[93mIt is recommended to use the .ddl file extension!\033[0m")
            result, error = basic.run(f'<{fileName}>', entireText)
            f.close()
        except FileNotFoundError:
            currentDirectory = os.path.abspath(os.getcwd())
            print(f"{currentDirectory}: can't open file, most likely can't be found.")
            exit()

    if error:
        print(error.as_string())
    # elif result:
    # 	if len(result.elements) == 1:
    # 		print(repr(result.elements[0]))
    # 	else:
    # 		print(repr(result))
else:
    
    print("Denny Dynamic Language (DDL) v"+".".join(version))
    print("Type 'exit() or quit()' to stop all executions")
    print("Type 'run(\"filename\")' to run a file")
    print("Type 'help()' to get help")
    print("Type 'help(\"function\")' to get help for a function")
    while True:
        try:
            text = input('>>> ')
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            timesKeyBoardInterrupt += 1
            if timesKeyBoardInterrupt >= 3:
                print("Exiting...")
                break
            continue
        if text.strip() == "":
            continue
        timesKeyBoardInterrupt = 0
        result, error = basic.run('<stdin>', text)

        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
