# ⛨ SHIELD
 a File Encryption Software with 2-Factor Authentication

---
### Motivation behind SHIELD
- We always have some sensitive documents in our computer, which can create massive problem if they go in wrong hand. One way to secure such files is by creating password protected archive like .zip. But, due to its popularity, it is often possible to bypass the password using some tool or simply by guessing or prying your password. Thus, an idea came to my mind to use 2-Factor Authentication in the encryption, so that intruder, even with the right password can't access those sensitive files.

### SHIELD in action
- In this example, we will see how SHIELD works...

#### ENCRYPTION:

  We will apply SHIELD in the folder below:
  
<img src="./Demo/Folder.PNG?raw=true" alt="folder before" width="50%">

1. First, fire up the SHIELD using 
```
python3 SHIELD1.0.py
```
A SHIELD menu will appear:

<img src="./Demo/S1.PNG?raw=true" alt="Menu" width="50%">

2. Now to ENCRYPT a file, we'll choose 1 and then a list of the files of that directory will appear.
3. After thet, to select our desired file, we will choose the list index from the list. 
4. After selecting the file, we have to put a password. The console will look something like this after this step.

<img src="https://user-images.githubusercontent.com/33586885/126453415-18a1c026-ec9d-4a28-8068-e60df3878450.png" alt="Password" width="50%">


5. After entering the password, SHIELD will generate a TOTP key and its corresponding QR CODE like this:

<img src="https://user-images.githubusercontent.com/33586885/126454632-364f29f1-ed8a-411b-a67f-92f607b30a55.png" alt="QR" width="60%">

6. We have to Scan the QR CODE using any authenticator app. For this Example, I'll use Google Authenticator:

<img src="https://user-images.githubusercontent.com/33586885/126455895-1ee2ecef-6126-4191-be80-88e378b067ab.png" alt="GoogleAuth" width="50%">

7. We have to enter the authentication code from the Google Authenticator to SHIELD first time to authenticate.

<img src="https://user-images.githubusercontent.com/33586885/126456354-48b67f2a-0cbc-4d1d-9eb2-01f3eb08264d.png" alt="GoogleAuthSuccess" width="50%">

After successful authentication, SHIELD will encrypt the file in .ef2 format using Multi-Layer Encryption.

<img src="https://user-images.githubusercontent.com/33586885/126456821-d0a78413-cab3-4726-b384-31aac7a0b696.png" alt="Folder After" width="50%">


#### DECRYPTION:

Now, we will decrypt our .ef2 file using SHIELD...

1. First Choose 2 From the SHIELD Menu to DECRYPT a file.
2. Now, select the .ef2 file using the file index mentioned above.
3. Enter your password.
4. Now enter the authentication code from the authenticator.

![Decrypt](https://user-images.githubusercontent.com/33586885/126458333-2825d6fd-c995-4267-93a0-43d7e2db7cec.png)

Voila, Your file is now decrypted.



