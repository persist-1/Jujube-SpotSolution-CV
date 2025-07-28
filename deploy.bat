@echo off
REM 检查requirements.txt是否存在
if not exist "requirements.txt" (
    echo 错误：未找到requirements.txt文件
    pause
    exit /b 1
)

REM 检查虚拟环境目录
if exist "venv\" (
    echo 检测到现有虚拟环境
    choice /c YN /m "是否删除现有虚拟环境并重建？(Y=删除重建/N=更新依赖)"
    if errorlevel 2 goto UPDATE
    if errorlevel 1 goto RECREATE
) else (
    goto CREATE
)

:RECREATE
rmdir /s /q venv

:CREATE
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo 虚拟环境已创建并安装依赖
pause
exit /b 0

:UPDATE
call venv\Scripts\activate
pip install --upgrade -r requirements.txt
echo 虚拟环境依赖已更新
pause