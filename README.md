formscrub
=========

used to quickly delete yucky values from plists

To use:

Unless you're into editing your /etc/paths and chmod +x'ing all the things, just download the script and whenever you have a .plist file you want to edit, enter this into Terminal:

    python formscrub.py filename
    
This will go through the file and remove the values you want to delete, then re-save it.

=========

If you really want to run this from everywhere - if you don't feel like constantly dropping the files you want to edit in the same folder as the script, or if you don't want to type path/to/my/plist.file over and over, you'll need to do the following things:

1) Find the file in Terminal and enter this command:

    chmod +x formscrub.py
    
2) Go to your home directory and enter: (requires sudo password)

    sudo nano /etc/paths
    
3) Once the editor is up, go to the bottom of the file, type in this, and save it:

    PATH=$PATH:/directory/to/formscrub.py

You should now be able to just run the script from anywhere in the Terminal. In this way, you can just go to where your actual file is sitting in your computer and enter

    formscrub.py myfile
    
...and it should Just Work. If not, Google is your friend. :)

=========

At present, it just looks for a default value. Later versions will allow you to not only name the value you want to eliminate from the imported .plist file, but also give you the option of saving the file under a different name.
