import os

def remove_in_dir(pth):
    files = os.listdir(pth)
    for f in files:
        full_pth = os.path.join(pth, f)
        if os.path.isdir(full_pth):
            remove_in_dir(full_pth)
        else:
            if os.path.splitext(full_pth)[-1].lower() == '.pkl':
                os.remove(full_pth)
    return 

remove_in_dir('./')
