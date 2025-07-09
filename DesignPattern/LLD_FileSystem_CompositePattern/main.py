from File import File
from Directory import Directory

if __name__=="__main__":
    
    file1 = File("root file")

    file2 = File("child1 file")
    file3 = File("child2 file")

    directory1 = Directory("root directory")

    directory2 = Directory("child1 directory")
    directory2.add(file2)
    directory2.add(file3)

    directory1.add(file1)
    directory1.add(directory2)

    # directory1.ls()
    print(directory1.search("child3 file"))

    