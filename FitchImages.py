#Abdullah. Twitter: @Techn_new
import cv2
import schedule
import pyodbc
import io
from PIL import Image
import cv2
import os
import numpy as np

def get_image_blob(connection_prd):
    print("Fetching Image...")
    #Write your query here
    sql1 = "select top(100) from table;"
    cursor = connection_prd.cursor()
    cursor.execute(sql1)
    rows = cursor.fetchall()
    print("images fetched")
    print(type(rows))
    
    for row in rows:
        process_image(connection_prd, row)


def process_image(connection, row):
    print("Processing...")
    #convert image type 
    imageBytes = cv2.imdecode(np.fromstring(row.Content, np.uint8), cv2.IMREAD_COLOR)
    image_shape = imageBytes.shape
    #write them to the folder
    cv2.imwrite("{0}\\image.jpeg".format(folder), imageBytes)
    print("Photo was saved to the folder!!")
    

folder = "C:\\Users\\user\\Desktop\\folder path"

print("Creating prd connection...")
#opening the database connection
connection_prd = pyodbc.connect("DRIVER={}))
print("Prd connection created.")



try:
    get_image_blob(connection_prd)
except Exception as ex:
    connection_dev.rollback()
    print("Excepton is: ")
    print(ex)
    print("Failed to save image to folder ")
finally:
    #closing database connection.
    connection_prd.cursor().close()
    connection_prd.close()
    print("connections are closed")
