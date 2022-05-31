# Rivanna 

Logging in to Rivanna via web interface

Documentation: <https://www.rc.virginia.edu/userinfo/rivanna/login/#web-based-access>

Login: <https://rivanna-portal.hpc.virginia.edu/>

UVA VPN: <https://in.virginia.edu/vpn>

Shell access: <https://rivanna-portal.hpc.virginia.edu/pun/sys/shell/ssh/rivanna.hpc.virginia.edu>

JupyterLab: <https://rivanna-portal.hpc.virginia.edu/pun/sys/dashboard/batch_connect/sys/jupyter_lab/session_contexts/new>

![UVA Login](images/uva-login.png)

**Figure:** UVA Login

The user must install Duo Mobile on smartphone to use as an 
authentication service to approve logins.

For security reasons we suggest never saving the password within
the browser autofill.

After logging in, you will receive an email through your UVA email
inbox to create an account on Rivanna. Once completing the sign-up
process, it will take around 1 hour for your account creation to be
finalized.

If connecting through SSH, then a VPN is required. Follow the
instructions to download UVA Anywhere at the following link:
<https://in.virginia.edu/vpn>

To log in to Rivanna, ensure you are connected to UVA Anywhere
and issue the following (make sure you replace `abc123` with your
UVA id):

```bash
you@yourcomputer$ ssh-copy-id abc123@rivanna.hpc.virginia.edu 
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
abc123@rivanna.hpc.virginia.edu's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'abc123@rivanna.hpc.virginia.edu'"
and check to make sure that only the key(s) you wanted were added.

you@yourcomputer$ ssh abc123@rivanna.hpc.virginia.edu
Last login: Tue May 31 11:55:43 2022
Authorized Use Only!
-bash-4.2$

```