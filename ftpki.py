import ftplib

ftp = ftplib.FTP('test.rebex.net')
logowanie = ftp.login('demo', 'password')
print(logowanie)
# katalog = ftp.nlst()
katalog = ftp.nlst('pub/example')
print(katalog)
# plik = ftp.retrbinary('RETR readme.txt', open('README.log', 'wb').write)
plik = ftp.retrbinary('RETR pub/example/KeyGenerator.png', open('plik.png', 'wb').write)
