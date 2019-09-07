def crawl(files,indent=" "):
    
    for file in os.listdir(files):
        full_path=path.join(files,file)
        if  path.isfile(full_path):
            print(indent*5, file)
        else:
            print(indent,full_path)
            crawl(full_path)
            

crawl("/Users/Documents")  
