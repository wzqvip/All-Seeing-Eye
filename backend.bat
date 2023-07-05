python -m venv myenv
Set-ExecutionPolicy RemoteSigned
myenv\Scripts\activate
pip install -r requirements.txt
python openAI-api/framework/main.py