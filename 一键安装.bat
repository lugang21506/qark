@echo off
echo "��ʼ�Զ���װ����ȴ�"
pip install -r requirements.txt
pip install .

echo "����Qark�Ƿ�װ�ɹ�"
qark --help

if %ERRORLEVEL% NEQ 0 echo "Qark ��װʧ�ܣ�����ϵ�ն˹�����Ա"

if %ERRORLEVEL%==0 echo "Qark ��װ�ɹ�"

pause