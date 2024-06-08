## AI Instruction
[The Chat with AI](https://chatgpt.com/share/ef180ed2-43cc-42d8-88e2-8f665b7b01c4)

```
pip install -r requirements.txt
uvicorn main:app --reload
```

## Build project release package

- Step 1: Create a Virtual Environment and Install Dependencies
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```
- Step 2: Freeze the Installed Packages `pip freeze > requirements.txt`
- Step 3: Download the Dependencies
```
mkdir packages
pip download -r requirements.txt -d packages
```
- Step 4: Prepare the Deployment Package
```
mkdir deployment_package
cp -r data deployment_package/data
cp main.py deployment_package/
cp requirements.txt deployment_package/
cp -r packages deployment_package/packages
cp -r venv deployment_package/venv
```
- Step 5: Transfer the Deployment Package to the Server
Transfer the `deployment_package` directory to the target Windows server. You can use a USB drive, FTP, or any other file transfer method

- Step 6: Set Up the Environment on the Server
```
cd path\to\deployment_package
venv\Scripts\activate

pip install --no-index --find-links=packages -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 8000


```
