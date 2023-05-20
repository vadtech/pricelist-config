import xmlrpc.client
import base64
import os


# Odoo API authentication
url = "https://vad2.odoo.com"
db = "vadtech-odoo-main-3533917"
username = "innocent.mpasi@glace.com"
password = "Sanna@1#"


# Connect to the Odoo server
common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(url))
uid = common.authenticate(db, username, password, {})

# Connect to the Odoo API
models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))

# Update product image


# specify the path of the top-level folder
top_level_folder = "./images-for-odoo_2023-05-04_0656/"

# loop through all folders and subfolders
for root, dirs, files in os.walk(top_level_folder):
    for file in files:
        file_path = os.path.join(root, file)
        if file.endswith(".jpg"):
            # remove .jpg extension from the file name
            new_file_name = os.path.splitext(file)[0]
            # remove specified variables from new file name
            variables_to_remove = ('v2', 'e', '-v2', '-s' ,'-')
            for variable in variables_to_remove:
                new_file_name = new_file_name.replace(variable, '')
                product_id= models.execute_kw(db, uid, password, 'product.template', 'search_read',[[['default_code', '=', new_file_name]]], {'fields': ['id'], 'limit': 1})
                if product_id != []:
                    with open(file_path, 'rb') as f:
                        data = f.read()
                        img = base64.b64encode
                        encoded_image_data = base64.b64encode(data)
                        ImageSend = encoded_image_data.decode('ascii')
                    # Update product record with new image
                    product = models.execute_kw(db, uid, password, 'product.template', 'write', [[ product_id[0]['id']], {
                        'image_1920': ImageSend,
                    }])
                    print("-INFO- IMAGE UPLOADED!")
                else:
                    print("-WARNING- IMAGE NOT FOUND"+file_path)
