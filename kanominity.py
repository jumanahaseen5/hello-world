import MySQLdb

i=0;
flag=0


fo = open("supress.txt", "w")
fo.write( "");
fo.close()

# Open database connection
db = MySQLdb.connect("localhost","root","","anonymity" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
sql = "SELECT count(*) as cc FROM data2"
try:
    # Execute the SQL command
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
      tot = row[0]
except:
    print "Error: unable to fecth data"



print(tot)

totdata=tot

input_file="fields.txt"



f = open(input_file)
for line in f:
    line=line.rstrip()
    count=0

    sql = "SELECT distinct %s FROM data2 group by %s" % (line,line)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
          count=count+1;
    except:
        print "Error: unable to fecth data"


    print "%s ***** %s" % (count,line)  
    

    sql = "SELECT count(*) as cc,%s FROM data2 group by %s" % (line,line)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
          tot = row[0]
          data=row[1]
          print "%d %s %s %d" % (tot,data,line,count)
          kvalue=float(tot)/totdata
          if kvalue<=.10:
              fo = open("supress.txt", "a+")
              fo.write( "**** %s %s \n" % (data,line));
              fo.close()              
              print "%d ***** %s %d" % (tot,line,count)
          
          #totkvalue=totkvalue+kvalue
          print "K Value = %.10f" % (kvalue)
    except:
        print "Error: unable to fecth data"

    #print "Sum = %d" % (totkvalue)
    count=0
            







    
    print "%s" % (line)
    print "ddd"
f.close()






