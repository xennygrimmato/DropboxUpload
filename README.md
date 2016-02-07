# DropboxUpload
Upload files on Dropbox from your terminal

1. Set up an app on Dropbox - https://www.dropbox.com/developers-v1/apps
2. Get the App Key and Secret.
3. Install the Dropbox Python API using: ``` pip install dropbox ```

Usage: ``` python dropbox_uploader.py FILEPATH DESTINATION ```

FILEPATH: The path of the file on your system that is to be uploaded.

DESTINATION: The path in your dropbox account where the file is to be uploaded.

For example, if you want to store your file with the name ```foo.txt```, the DESTINATION will be ```/foo.txt```.

Also, if you pass the DESTINATION as ```/dir_name/foo.txt```, the API will create a new directory with the name ```dir_name``` in your dropbox and copy your file with the name foo.txt inside that directory.

To contribute:

* Fork the repo.
* Make changes in a new branch.
* Create a Pull Request.

Suggestions/Issues/Bugs can be reported to: xennygrimmato (vstulsyan@gmail.com)