@echo off
cls 

echo Deseja fazer o backup?
pause

cls

echo Fazendo backup . . . .
echo .

cd "D:\amonteiro\desktop"

mkdir Backup

cd "D:\amonteiro\desktop\minhas coisas"

xcopy /e /y "D:\amonteiro\desktop\minhas coisas\scripts" "D:\amonteiro\desktop\backup"
echo .
echo Copiando arquivos . . . .
echo .

cd "D:\amonteiro\desktop\backup"

echo Listando arquivos . . . .
echo.
dir

cd "D:\amonteiro\desktop\minhas coisas\scripts"
echo .
