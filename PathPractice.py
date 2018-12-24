from pathlib import Path
import pathlib
"""in order to access purepaths, has to import pathlib
if want to import path, one has to specifically call from pathlib to import path"""
#purepath and paths are different type of objects, one cannot use commands build for
#, say, purepath objects on path objects. Vice versa. 

#now I'm trying to take all file names into a list, 
#Make the list alphabet ordered based on file name
#stage 1 D 
def directory_fn(pathway:Path, file_list:list)->list:
    """If the path inputted is a directory, it will only list the files in that layer (unsorted)"""
    if pathway.is_dir():
        for x in list(pathway.iterdir()):
            if x.is_file():
                file_list.append(x)
    else: # if either location does not exist or is not a directory
        print ("ERROR")
    return(file_list)

# R
def recursive_fn(pathway:Path, file_list:list)->list:
    """This function takes all files into a lists who views the indicated path
    as parent (grandparent) (unsorted) """
    if pathway.is_dir(): #three conditions: directory, file, or dne
        for x in list(pathway.iterdir()):
            recursive_fn(x, file_list)
    elif pathway.is_file():
        file_list.append(pathway)
    else: #no anything
        pass
    return(file_list)

#if this function reaches a directory, it examines every single object in its same layer
#if it reaches a file, then it appended into a list

def sort_file_notpure(pathway: Path)-> str:
    """This is the key function to sort paths in lexiconological order"""
    pure = pathlib.PurePath(pathway)
    return(pure.name)

def stage1()->[Path]:
    whole_command = input()
    command = whole_command[0]
    error = True
    while error == True:
        if command in "DR":
            content = whole_command[2:]
            print (content)
            if command == "D":
                initial_list = directory_fn(Path(content),[])
            else:
                initial_list = recursive_fn(Path(content),[])
            if len(initial_list) == 0:
                pass
            else:
                error = False
        else:
            print ("ERROR, Try again")
            whole_command = input()
            command = whole_command[0]
        initial_list.sort(key = sort_file_notpure)
        for i in initial_list:
            print (i)
    return(initial_list)
#stage1 seems fine...for now
    
        
#stage2 A

#N
def name_match(Paths:[Path], name:str )->[Path]:
    """This function checks a list of path and return ones that matches the name indicated"""
    filtered = []
    for path in Paths:
        if pathlib.PurePath(path).name == name:
            filtered.append(path)
    return(filtered)

#E 
def extension_match(Paths:[Path], ext:str)->[Path]:
    """This function filters out all the files with indicated extensions(suffix)"""
    filtered = []
    for path in Paths:
        if pathlib.PurePath(path).suffix == ext:
            filtered.append(path)
            return(filtered)
        
#T Path.read_text() - if I run this function with, like a jpg file, it will run an error message
def text_match(Paths:[Path], text:str)->[Path]:
    """This function opens the file in given list of path, and filter any that contains matched content"""
    filtered = []
    for path in Paths:
        if pathlib.PurePath(path).suffix == ".txt" or ".py":
            if text in path.read_text():
                filtered.append(path)
    return(filtered)

#For now, have no idea how to get pass that. i.e. If error message, then idk :P

#>< Path.stat().st_size
def smaller_match(Paths:[Path], size:int)->[Path]:
    filtered = []
    for path in Paths:
        if path.stat().st_size <= size:
            filtered.append(path)
    return(filtered)

def bigger_match(Paths:[Path], size:int)->[Path]:
    filtered = []
    for path in Paths:
        if path.stat().st_size >=size:
            filtered.append(path)
    return(filtered)

def stage2(paths:[Path])->[Path]:
    whole_command = input()
    command = whole_command[0]
    while command != ("A" or "N" or"E" or "T" or "<" or ">"):
        whole_command = input("ERROR, try again")
        command = whole_command[0]
    if command == "A":
        return(paths)
    else:
        content = whole_command[2:]
        if command == "N":
            return(name_match(paths,str(content)))
        elif command == "E":
            return(extension_match(paths,str(content)))
        elif command == "T":
            return(text_match(paths,str(content)))
        elif command == "<":
            return(smaller_match(paths,int(content)))
        elif command == ">":
            return(bigger_match(paths,int(content)))
    

stage2(stage1())

#stage3
#F
def 
#D 
#T Path.open()




