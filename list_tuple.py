list=[("web-server","192.168.1.1","frontend"),
      ("app-server","192.168.1.2","backend"),
      ("db-server","192.168.1.3","database")]
for i in list:
    print("name:{0} and IP:{1} and server:{2}".format(i[0],i[1],i[2]))