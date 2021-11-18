import dropbox

class TransferData:
        def __init__(self,access_token):
            self.access_token = access_token

        def upload_file(self,file_from,file_to):
            dbx = dropbox.Dropbox(self.access_token)
            f = open(file_from,'rb')
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.A8g6rfvAqXyOGOgnk95jww2JWW93JdNYSYaXhNjfd6NJw3_ppSCcG5tNJF4_FTwLoEvHmkAfWkmfkuwSaBcV9Zb_PZJkLVieCMnOU-8lXHnvPzRaNIEUDafPG7PRxXmcCVHlXME'
    transferData = TransferData(access_token)
    file_from = input('Enter the file path to tranfer:')
    file_to = input('Enter the file path to upload in dropbox:')
    transferData.upload_file(file_from,file_to)
    print('file has been moved')

main()    