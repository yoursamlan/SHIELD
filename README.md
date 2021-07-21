# ⛨ SHIELD
 a File Encryption Software with 2-Factor Authentication

---
### Motivation behind SHIELD
- We always have some sensitive documents in our computer, which can create massive problem if they go in wrong hand. One way to secure such files is by creating password protected archive like .zip. But, due to its popularity, it is often possible to bypass the password using some tool or simply by guessing or prying your password. Thus, an idea came to my mind to use 2-Factor Authentication in the encryption, so that intruder, even with the right password can't access those sensitive files.

### SHIELD in action
- In this example, we will see how SHIELD works...
  We will apply SHIELD in the folder below:
  
![FolderBefore](./Demo/Folder.PNG?raw=true)

1. First, fire up the SHIELD using 
```
python3 SHIELD1.0.py
```
A SHIELD menu will appear:

![menu](./Demo/S1.PNG?raw=true)

2. Now to ENCRYPT a file, we'll choose 1 and then a list of the files of that directory will appear.
3. After thet, to select our desired file, we will choose the list index from the list. 
4. After selecting the file, we have to put a password. The console will look something like this after this step.
![pass](https://user-images.githubusercontent.com/33586885/126453415-18a1c026-ec9d-4a28-8068-e60df3878450.png)
5. 
