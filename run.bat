@echo off
REM 检查虚拟环境是否存在
if not exist "venv\Scripts\activate" (
    echo 虚拟环境不存在，请先运行 deploy.bat 创建
    pause
    exit /b 1
)

REM 激活虚拟环境并运行主程序
call venv\Scripts\activate
python main.py
pause