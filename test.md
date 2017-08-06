
测试数据：
going to start sesssion
Username:book
Password:book123

    ------------- Welcome [book] login fortress machine -------------

[<1 -- David>, <1 -- Jack>, <2 -- Tom>, <2 -- Lucy>, <3 -- Tom>]
[bj_group, sh_group]
z.	ungroupped hosts (5)
0.	bj_group (4)
1.	sh_group (2)
[book]:0
------ Group: bj_group ------
  0.	David@ubuntu test(192.168.31.110)
  1.	Jack@ubuntu test(192.168.31.110)
  2.	Tom@server1(192.168.31.102)
  3.	Lucy@server1(192.168.31.102)
----------- END -----------
[(b)back, (q)quit, select host to login]:2
host: <2 -- Tom>
*** Connecting...
/usr/local/Python3.6.0/lib/python3.6/site-packages/paramiko/client.py:711: UserWarning: Unknown ssh-rsa host key for 192.168.31.102: b'bbd3d79e885af9f91c5a10bd7fbead2c'
  key.get_fingerprint())))
<paramiko.Transport at 0xb672ffec (cipher aes128-ctr, 128 bits) (active; 1 open channel(s))>
*** Here we go!

--logs: [<models.model_v2.AuditLog object at 0xb6532f4c>]
Last login: Mon Jun 19 01:31:02 2017 from 192.168.31.102
[Tom@centos67 ~]$ lscmd->: ls
                             --logs: [<models.model_v2.AuditLog object at 0xb6532f4c>, <models.model_v2.AuditLog object at 0xb6770f8c>]

a.txt  hello.txt  name  test
[Tom@centos67 ~]$ pwdcmd->: pwd
                               --logs: [<models.model_v2.AuditLog object at 0xb672daac>]

/home/Tom
[Tom@centos67 ~]$ cd test/cmd->: cd tes	t/
                                          --logs: [<models.model_v2.AuditLog object at 0xb672d2ac>]

[Tom@centos67 test]$ lscmd->: ls
                                --logs: [<models.model_v2.AuditLog object at 0xb67286cc>]

[Tom@centos67 test]$ exitcmd->: exit
                                    --logs: [<models.model_v2.AuditLog object at 0xb630fe2c>]

logout

*** EOF
[(b)back, (q)quit, select host to login]:q^H
[(b)back, (q)quit, select host to login]:b
z.	ungroupped hosts (5)
0.	bj_group (4)
1.	sh_group (2)
[book]:1
------ Group: sh_group ------
  0.	Tom@server1(192.168.31.102)
  1.	Lucy@server1(192.168.31.102)
----------- END -----------
[(b)back, (q)quit, select host to login]:b
z.	ungroupped hosts (5)
0.	bj_group (4)
1.	sh_group (2)
[book]:z
------ Group: ungroupped hosts ------
  0.	David@ubuntu test(192.168.31.110)
  1.	Jack@ubuntu test(192.168.31.110)
  2.	Tom@server1(192.168.31.102)
  3.	Lucy@server1(192.168.31.102)
  4.	Tom@server2(192.168.31.100)
----------- END -----------
z.	ungroupped hosts (5)
0.	bj_group (4)
1.	sh_group (2)
[book]:3
no this option..
z.	ungroupped hosts (5)
0.	bj_group (4)
1.	sh_group (2)
[book]:0
------ Group: bj_group ------
  0.	David@ubuntu test(192.168.31.110)
  1.	Jack@ubuntu test(192.168.31.110)
  2.	Tom@server1(192.168.31.102)
  3.	Lucy@server1(192.168.31.102)
----------- END -----------
[(b)back, (q)quit, select host to login]:3
host: <2 -- Lucy>
*** Connecting...
<paramiko.Transport at 0xb67a47ac (cipher aes128-ctr, 128 bits) (active; 1 open channel(s))>
*** Here we go!

--logs: [<models.model_v2.AuditLog object at 0xb672faac>]
[Lucy@centos67 ~]$ lscmd->: ls
                              --logs: [<models.model_v2.AuditLog object at 0xb672faac>, <models.model_v2.AuditLog object at 0xb632d9ec>]

[Lucy@centos67 ~]$ touch notifycmd->: touch notify
                                                  --logs: [<models.model_v2.AuditLog object at 0xb672dd6c>]

[Lucy@centos67 ~]$ ls -alhcmd->: ls -alh
                                        --logs: [<models.model_v2.AuditLog object at 0xb632d54c>]

×ÜÓÃÁ¿ 24K
drwx------. 3 Lucy Lucy 4.0K 8ÔÂ   6 16:29 .
drwxr-xr-x. 7 root root 4.0K 8ÔÂ   6 16:27 ..
-rw-r--r--. 1 Lucy Lucy   18 7ÔÂ  24 2015 .bash_logout
-rw-r--r--. 1 Lucy Lucy  176 7ÔÂ  24 2015 .bash_profile
-rw-r--r--. 1 Lucy Lucy  124 7ÔÂ  24 2015 .bashrc
drwxr-xr-x. 2 Lucy Lucy 4.0K 11ÔÂ 12 2010 .gnome2

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
:qcmd->: :q
           --logs: [<models.model_v2.AuditLog object at 0xb672dd6c>]
[Lucy@centos67 ~]$ cmd->:
                          --logs: [<models.model_v2.AuditLog object at 0xb632d98c>]

[Lucy@centos67 ~]$ exitcmd->: exit
                                  --logs: [<models.model_v2.AuditLog object at 0xb6532dac>]

logout

*** EOF
[(b)back, (q)quit, select host to login]:b
z.	ungroupped hosts (5)
0.	bj_group (4)
1.	sh_group (2)
[book]:0
------ Group: bj_group ------
  0.	David@ubuntu test(192.168.31.110)
  1.	Jack@ubuntu test(192.168.31.110)
  2.	Tom@server1(192.168.31.102)
  3.	Lucy@server1(192.168.31.102)
----------- END -----------
[(b)back, (q)quit, select host to login]:
[(b)back, (q)quit, select host to login]:b
z.	ungroupped hosts (5)
0.	bj_group (4)
1.	sh_group (2)
[book]:0
------ Group: bj_group ------
  0.	David@ubuntu test(192.168.31.110)
  1.	Jack@ubuntu test(192.168.31.110)
  2.	Tom@server1(192.168.31.102)
  3.	Lucy@server1(192.168.31.102)
----------- END -----------
[(b)back, (q)quit, select host to login]:1
host: <1 -- Jack>
*** Connecting...
/usr/local/Python3.6.0/lib/python3.6/site-packages/paramiko/client.py:711: UserWarning: Unknown ssh-ed25519 host key for 192.168.31.110: b'b020fac3a4b87b95d5fee4993395212f'
  key.get_fingerprint())))
<paramiko.Transport at 0xb67333ec (cipher aes128-ctr, 128 bits) (active; 1 open channel(s))>
*** Here we go!

--logs: [<models.model_v2.AuditLog object at 0xb633878c>]
Welcome to Ubuntu 16.04.2 LTS (GNU/Linux 4.4.0-62-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Jack@ubuntu:~$ lscmd->: ls
                          --logs: [<models.model_v2.AuditLog object at 0xb633878c>, <models.model_v2.AuditLog object at 0xb633852c>]

Jack@ubuntu:~$ touch book.txtcmd->: touch book.txt
                                                  --logs: [<models.model_v2.AuditLog object at 0xb678430c>]

Jack@ubuntu:~$ lscmd->: ls
                          --logs: [<models.model_v2.AuditLog object at 0xb672d60c>]

book.txt
Jack@ubuntu:~$ pwdcmd->: pwd
                            --logs: [<models.model_v2.AuditLog object at 0xb672d10c>]

/home/Jack
Jack@ubuntu:~$ exitcmd->: exit
                              --logs: [<models.model_v2.AuditLog object at 0xb678430c>]

logout

*** EOF
[(b)back, (q)quit, select host to login]:q
[root@centos67 bin]#

