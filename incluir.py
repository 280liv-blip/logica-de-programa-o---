from conecao import conectar

nome= input("digite um nome para incluir: ")

con = conectar ()
cursor = con.cursor ()

cursor.execute ("SELECT * FROM  nome WHERE nome = %s ",(nome))
resultado = cursor.fetchone ()

if resultado :
    print ("nome ja existe.")
else :
    cursor.execute ("INSERT INTO nomes (nome) VALUES (%s)", (nome))
    con.commit ()
    print ("nome inserido com sucesso !")

cursor.close()
con.close ()
