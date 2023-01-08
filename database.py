import mysql.connector
from PIL import Image
from io import BytesIO

# connect to the database
db = mysql.connector.connect(
    host="192.168.178.35",
    user="mosk",
    passwd="timo22769",
    database="db_app"
)

# create a cursor
my_cursor = db.cursor()

# function to create table images
def create_table():
    # create the table with primary key id and image as a binary file
    my_cursor.execute("CREATE TABLE images (id INT AUTO_INCREMENT PRIMARY KEY, image LONGBLOB)")
    db.commit()

# function to open a picture as a binary file and store it in the database
def store_image_path(path):
    # open the picture
    with open(path, "rb") as file:
        # read the picture
        picture = file.read()
    # insert the picture into the database
    my_cursor.execute("INSERT INTO images (image) VALUES (%s)", (picture,))
    # commit the changes to the database
    db.commit()

# function to retrieve the picture from the database where id is == variable
def retrieve_and_convert_image(id, format, file=None):
    # retrieve the image
    my_cursor.execute("SELECT image FROM images WHERE id = %s", (id,))
    # fetch the image
    image = my_cursor.fetchone()[0]
    # open a new file to store the image (if specified)
    if file is not None:
        file.write(image)
    # open the image file and convert it to the specified format
    img = Image.open(BytesIO(image))
    with BytesIO() as f:
        img.save(f, format)
        # return the image data
        return f.getvalue()

def store_image_var(image, id=None):
    # insert the image into the database with the specified id (if given)
    if id is None:
        my_cursor.execute("INSERT INTO images (image) VALUES (%s)", (image,))
    else:
        my_cursor.execute("INSERT INTO images (id, image) VALUES (%s, %s)", (id, image))
    db.commit()



