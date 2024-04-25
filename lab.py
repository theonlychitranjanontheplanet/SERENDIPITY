vector = [1, 2, 3, 4]  # Example list

from embedding import get_embedding


vector_str = ','.join(map(str, vector)) #converts to 1,2,3,4
# Split the string by commas to get a list of substrings


number_list_str = vector_str.split(',')
# Convert each string in the list to an integer
back_to_list = [int(num) for num in number_list_str]

######################################################################################


# import mysql.connector

# mydb = mysql.connector.connect(
#     host= "localhost",
#     user="root",
#     passwd="Bro123@bruh",
#     database="serendipity"
# )


# mycursor=mydb.cursor()

# mycursor.execute("SELECT * FROM memory")

# myresult=mycursor.fetchall()

# for row in myresult:
#     print(row)


#0.016388215124607086


if(0.016388215124607086 == 0.016388215124607086):
    print("YES!!")