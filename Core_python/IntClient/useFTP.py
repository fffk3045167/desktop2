import ftplib
import os
import socket


HOST = 'ftp.mozilla.org'
DIGN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (BlockingIOError, ConnectionResetError) as e:
        print('ERROR : cannot reach "{}"'.format(HOST))
        return
    print('*** Connected to host "{}"'.format(HOST))

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR : cannot login anonymously')  # anonymously 匿名地
        f.quit()
        return
    print('*** Logged in as "anonymously"')

    try:
        f.cwd(DIGN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "{}"'.format(DIGN))
        f.quit()
        return
    print('*** Changed to "{}" folder'.format(DIGN))

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print('ERROR: cannot read file "{}"'.format(FILE))
        os.unlink(FILE)
    else:
        print('*** Downloaded "{}" to CWD'.format(FILE))

    f.quit()


if __name__ == '__main__':
    main()
