[Me] 如何构建该项目的部署包以便在没有互联网连接的新 Windows 服务器中运行？

[python]：要在没有互联网访问的 Windows 服务器上部署此 FastAPI 项目，您需要创建一个包含所有必要文件和依赖项的离线部署包。以下是准备包并将其部署到服务器上的分步指南：

### 步骤 1：创建虚拟环境并安装依赖项
首先，在可以访问互联网的机器上创建一个虚拟环境并安装所需的软件包。

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 步骤 2 ：冻结已安装的软件包
创建一个requirements.txt包含所有依赖项的文件。
```bash
pip freeze > requirements.txt
```

### 步骤3：下载依赖项
用于pip将所需的包下载到本地目录中。

```bash
mkdir packages
pip download -r requirements.txt -d packages
```

### 步骤 4：准备部署包
创建一个包含项目文件、venv和下载的包的部署包。

```bash
mkdir deployment_package
cp -r data deployment_package/data
cp main.py deployment_package/
cp requirements.txt deployment_package/
cp -r packages deployment_package/packages
cp -r venv deployment_package/venv
```

### 步骤 5：将部署包传输到服务器
将目录传输deployment_package到目标 Windows 服务器。您可以使用 USB 驱动器、FTP 或任何其他文件传输方法。

### 步骤 6：在服务器上设置环境
在 Windows 服务器上，使用传输的文件设置环境。

1. 激活虚拟环境：

```cmd
cd path\to\deployment_package
venv\Scripts\activate
```

1. 安装依赖项：

```cmd
pip install --no-index --find-links=packages -r requirements.txt
```

### 步骤 7：运行 FastAPI 应用程序
在 Windows 服务器上启动 FastAPI 服务器。

```cmd
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 部署包结构回顾
deployment_package在将目录传输到服务器之前，请确保目录具有以下结构：

```
deployment_package/
│
├── data/
│   ├── example1.json
│   ├── example2.json
│   └── ...
│
├── main.py
├── requirements.txt
├── packages/
│   ├── fastapi-0.68.1-py3-none-any.whl
│   ├── uvicorn-0.15.0-py3-none-any.whl
│   └── ...
│
└── venv/
    ├── Scripts/
    ├── Lib/
    └── ...
```
此设置确保所有依赖项和环境都是独立的，从而允许应用程序在没有互联网访问的服务器上运行。

您想更详细地了解任何具体步骤吗？或者您还有其他问题吗？