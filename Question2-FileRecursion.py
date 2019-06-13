
# coding: utf-8

# In[104]:


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
    
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    def _find_files(suffix, path):
        """supporting function that gets called recursively"""
        ## Use list_files global space variable to append data at all stack levels/depths
        
        for file in os.listdir(path):
            full_path=os.path.join(path,file)
            if os.path.isdir(full_path):
                _find_files(suffix, full_path)
            elif file.endswith(suffix):
                list_files.append(file)
        return 


    list_files=[]
    
    _find_files(suffix, path)
    return list_files


# In[105]:


print(find_files(".c","testdir"))
print(find_files(".h","testdir"))

