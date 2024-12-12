## Getting started edit docs

### Linux venv

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Documentation

Go to folder docs `cd webapp/docs`

The `source` folder contains all the files (.rst) for compiling documentation

    .
    ├── Makefile
    ├── README.md
    ├── make.bat
    ├── requirements.txt
    ├── server_docs.py
    └── source
        ├── conf.py
        ├── index.rst
        └── usage
            └── overview.rst

To compile, run the command. If there are any changes in the `source` files, you will need to compile again

    make html

And start a small server to display html

    python server_docs.py

documentation is available at the link `http://127.0.0.1:8000/index.html`