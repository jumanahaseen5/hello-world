import MySQLdb

i=0;
flag=0

fo = open("supressl.txt", "w")
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

dfield="insulin"

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
          print "%d %s %s " % (tot,data,line)



          sql2 = "SELECT count(*) as cc,%s FROM data2 where %s='%s' group by %s" % (dfield,line,data,dfield)
          try:
              cursor.execute(sql2)
              results2 = cursor.fetchall()
              for row2 in results2:
                  lval=float(row2[0])/tot
                  fo = open("supressl.txt", "a+")
                  if row2[1]=='Down':
                      fo.write( "%s +++++ %s \n" % (row2[0],row2[1]));
                      fo.close()  
                  print "%s +++++ %s" % (row2[0],row2[1])
                  print "L Diversity = %.2f  %s %s %s" % (lval,dfield,data,line)
                  print "******"
              
                
          except:
              print "Error: unable to fecth data"



          
          

















          
          #totkvalue=totkvalue+kvalue
          
    except:
        print "Error: unable to fecth data"

    #print "Sum = %d" % (totkvalue)
    count=0
            







    
    print "%s" % (line)
    print "ddd"
f.close()






