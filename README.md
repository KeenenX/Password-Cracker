<h1>🔐 Password Cracker – (Ashley Madison)</h1>

 ### [YouTube Demonstration](https://youtube.com/@KeenenX)

<h2>Description</h2>

This script checks if a given password appears in a known list of leaked passwords (from the Ashley Madison data breach) using MD5 hashing. It downloads the password list from GitHub and compares hashes line-by-line. If a match is found, it alerts that the password is compromised
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python 3.13.3</b> 

<h2>Environments Used </h2>

- <b>Windows 11</b>

<h2>Program walk-through:</h2>

<p align="center">
📸 Step 1: Import Required Libraries: <br/>
<img src="https://i.imgur.com/VoXSZ5Y.png" height="80%" width="80%" alt="Password Cracker Steps"/>
<br /> 💬 "We import the hashlib module to hash passwords using MD5, and urllib.request to fetch the leaked password file directly from a URL."
<br />
<br /> 
 
 <br />
📸 Step 2: Define the URL for the Leaked Password List
<br/>
<img src="https://i.imgur.com/jaV3iAb.png" height="80%" width="80%" alt="Password Cracker Steps"/>
<br /> 💬 "We define the URL pointing to the leaked password list in plaintext format, and open it with urllib. This returns a stream we can read line by line."
<br />
<br /> 
 


<br />
📸 Step 3: Hash the Password You Want to Check
<br/>
<img src="https://i.imgur.com/4MYpxaA.png" height="80%" width="80%" alt="Password Cracker Steps"/>
<br /> 💬 "We define the password to check (booomer), encode it in UTF-8, strip whitespace, and hash it using MD5. The hash will be compared to the hashes of all leaked passwords."
<br />
<br /> 
 


<br />
📸 Step 4: Loop Through the Leaked Passwords
<br/>
<img src="https://i.imgur.com/8DqBe8Z.png" height="80%" width="80%" alt="Password Cracker Steps"/>
<br />💬 "We iterate through each line in the downloaded file. Each line (a password) is decoded to UTF-8, stripped of whitespace, and hashed using MD5 for comparison."
<br />
<br /> 
 


<br />
📸 Step 5: Compare the Hashes
<br/>
<img src="https://i.imgur.com/l8c7Oaa.png" height="80%" width="80%" alt="Password Cracker Steps"/>
<br /> 💬 "If the hash of the user-defined password matches a hash from the leaked list, we print a warning message and exit the script using quit()."
<br />
<br /> 
 


 <br />
📸 Step 6: Final Message If No Match is Found  <br/>
<img src="https://i.imgur.com/OskpIVM.png" height="80%" width="80%" alt="Password Cracker Steps"/>
<br /> 💬 "If the password is not found in the leaked list, the script prints a reassuring message indicating it’s not among the known compromised passwords."
<br />
<br /> 
 


 <br />

</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
