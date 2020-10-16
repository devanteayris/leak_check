# Credentials Leak Check
A tool to check if your domain or emails were involved within any service security breach, URL or pastebin.

## APIs Used
* DeHashed
* have i been pwned?

## Installation
Add repository:
```bash
git clone https://github.com/devanteayris/leak_check.git
```
Install dependencies with pip:
```bash
pip install -r requirements.txt
```
**Add your API keys to key.py or the tool will not work**
```python
HAVEIBEENPWNED_KEY = 'haveibeenpwnedkey'
DEHASHED_EMAIL = 'dehashedemail'
DEHASHED_KEY = 'dehashedkey'
```
## Usage
Open **emails.dat** and add one email per line that you want to check and then run the command:
```bash
python3 main.py
```
After all the emails are checked by the tool, you will be able to enter a **domain** of your choice to search for within the tool
## Examples
```bash
python3 main.py
```
Checking for any emails involved within any security breach
```text
========================================
[+] Count: 1/1 (100.0%)
[+] Emails leaked for now: 1/1 (100.0)
[+] Checking:
         -  test@gmail.com -> LEAKED
[+] Leaked sites: 261
[+] Details
        - 000webhost
        - 17Media
        - 17173
        - 2844Breaches
        - 500px
        - 7k7k
        - 8fit
        - 8tracks
        - AbuseWithUs
        - Adobe
        - AgusiQTorrents
        - Aipai
        - AKP
        - AnimeGame
        - Animoto
        - Apollo
        - Appartoo
        - Appen
        - Aptoide
```

Checking for any emails involved within public URL or pastebin
```text
Pastebin Search Upcoming.....
========================================
[+] Count: 1/1 (100.0%)
[+] Emails leaked for now: 1/1 (100.0)
[+] Checking:
         -  test@gmail.com -> LEAKED
[+] Leaks: 607
[+] Details
        - AdHocUrl                       http://siph0n.in/exploits.php?id=4370
        - AdHocUrl                       http://siph0n.in/exploits.php?id=4364
        - AdHocUrl                       http://siph0n.in/exploits.php?id=4369
        - AdHocUrl                       http://siph0n.in/exploits.php?id=1165
        - AdHocUrl                       http://siph0n.in/exploits.php?id=3762
        - AdHocUrl                       http://siph0n.in/exploits.php?id=3664
        - AdHocUrl                       http://siph0n.in/exploits.php?id=4025
        - AdHocUrl                       http://siph0n.in/exploits.php?id=3868
        - AdHocUrl                       http://siph0n.in/exploits.php?id=4054
        - AdHocUrl                       http://siph0n.in/exploits.php?id=3667
        - AdHocUrl                       http://siph0n.in/exploits.php?id=4138
        - AdHocUrl                       http://siph0n.in/exploits.php?id=4063
```
Checking for domain involved within any security breach
```text
========================================
Enter a Domain for Search: exampleeee.com
========================================
[+] Checking:
[+] Leaks: 6
[+] Victim: 1
         - Email: name@exampleeee.com -> LEAKED
         - Password: ravan631 -> LEAKED
         - Obtained From: Collections -> LEAKED
[+] Victim: 2
         - Email: name@exampleeee.com -> LEAKED
         - Password: ravan631 -> LEAKED
         - Obtained From: BreachCompilation -> LEAKED
[+] Victim: 3
         - Email: name@exampleeee.com -> LEAKED
         - Password: ravan631 -> LEAKED
         - Obtained From: AntiPublic -> LEAKED
[+] Victim: 4
         - Email: name@exampleeee.com -> LEAKED
         - Username: 576953675 -> LEAKED
         - Hashed Password: 0x8F4CD70DA713659AF854ECE00F508A33EEC3774F -> LEAKED
         - Obtained From: MySpace -> LEAKED
[+] Victim: 5
         - Email: example@exampleeee.com -> LEAKED
         - Username: asdghkodb -> LEAKED
         - Hashed Password: j1OYZKBFhcRBTf4dm2to5XMp10ny4i6p:82654e62866bfdf34ad30cd502845a9bc7db8466:25905460 -> LEAKED
         - Name: liv -> LEAKED
         - Obtained From: EyeEm -> LEAKED
[+] Victim: 6
         - Email: example@exampleeee.com -> LEAKED
         - Hashed Password: $2a$10$LsoAaTQEsqff/5esmGJA0.8SiEwFMKWZQUws.7IwSg2Ce7XCxLXfC -> LEAKED
         - Obtained From: Wanelo.com -> LEAKED
========================================
```
