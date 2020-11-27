How to parse files
==================

1. Download the <a href="https://drive.google.com/file/d/1iGUyZs62cGkaetY9COsGGQoS_R0Y9Io6/view?usp=sharing" download target="_blank">parserUUID2int.exe</a>
2. Copy source files in the same directory.
3. Run the parserUUID2int.exe

Development
===========
1.  Download and install git.
    ```
    https://git-scm.com/downloads
    ```
2.  Choose your projects directory (like C:/Users/YourName/projects)   
3.  Clone the github project 'sergey-untilov/parserUUID2int'
    ```
    git clone https://github.com/sergey-untilov/parserUUID2int.git
    ```
4.  Choose project directory
    ```
    cd parserUUID2int
    ```
5.  Download and install Python 2.7.17.
    ```
    https://www.python.org/downloads/release/python-2717
    ```
6.  Install virtualenv.
    ```
    pip install virtualenv
    ```
7.  Setup a virtual environment for Python.
    ```
    virtualenv env
    ```
8.  Activate virtual environment.
    ```
    activate.cmd
    ```
9.  Copy source files into parserUUID2int\inp\ directory.
10. Run the programm.
    ```
    run.cmd
    ```
11. Output files will be in outp\ directory.

12. To make executable file for Windows run
    ```
    build.cmd
    ```
    That makes the dist\parserUUID2int.exe file.
