@echo off
echo "开始自动安装，请等待"
pip install -r requirements.txt
pip install .

echo "测试Qark是否安装成功"
qark --help

if %ERRORLEVEL% NEQ 0 echo "Qark 安装失败，请联系终端管理人员"

if %ERRORLEVEL%==0 echo "Qark 安装成功"

pause