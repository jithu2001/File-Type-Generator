File Type Generator - Readme
Overview
File Type Generator is a program designed to monitor a pre-set directory in a Windows system and classify files copied into it based on their types. The program acts as a staging area for users who frequently copy files of types such as PNG, MP3, JPEG, and PDF, all of which are tailless and lack file extensions. The service/program automatically organizes these files into designated directories for each file type, ensuring that the copied files acquire the appropriate file extensions.

Features
Set the Staging Directory: The program allows users to set up a staging directory where they can copy the files for classification.

Set the Target Directories: Users have the flexibility to choose and set the target directories for each file type. The files will be organized automatically into the respective directories based on their types.

Usage
Prerequisites: The program requires the installation of Python and the python-magic library to identify file types based on their content. Make sure to have these dependencies installed on your system.

Configuration:

Open the file_type_generator.py script in any code editor.
Modify the source_directory variable to set the staging directory where files will be copied for classification.
Update the destination_directory variable to specify the target directory where files of different types will be organized.
Running the Program:

Once the configuration is set, save the changes and run the script using Python.
The program will now continuously monitor the staging directory for new files.
When you copy a file into the staging directory, the program will automatically classify and move it to the appropriate target directory based on its type.
Supported File Types:

The program supports the following file types:

PNG (Portable Network Graphics) images
MP3 (MPEG Audio Layer III) audio files
JPEG (Joint Photographic Experts Group) images
PDF (Portable Document Format) files


Note
The program is designed to run indefinitely and continuously monitor the staging directory for new files. It will automatically classify and move files to the target directories.
Make sure to keep the program running as long as you want the file classification process to continue.
Remember to handle any additional file types or extensions that you might need in the future by updating the get_file_type() function.
Disclaimer: While the program was initially developed for a Windows system, it should work on other systems too, as long as the prerequisites are met. The choice of system or programming language is not restricted. You can use the program on your preferred operating system and with the Python interpreter of your choice.

Feel free to contribute, enhance, or modify the program based on your specific requirements or use cases. Happy file organization!
