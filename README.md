# robotframework-redislibrary
## robotframework-redislibrary 新增了哪些功能
* 新增了string、list、hash、set、sorted set等数据类型的set和get方法。
* 新增了连接redis时的身份验证。
* 采用pool连接方式。
## 说明
* 本项目仅供参考使用。
* 本项目是在 https://github.com/nottyo/robotframework-redislibrary.git 的基础上进行的二次开发，感谢其作者：Traitanit Huangsri。
* 使用过程中有任何bug都可以提出来，互相交流，非常感谢。
## 安装
```python
pip install tox
pip install coverage
pip install robotframework==3.0
pip install redis==2.10.5
pip install deco
python setup.py install
```
## 感谢
* 再次感谢原作者：Traitanit Huangsri，以及其提供的项目：https://github.com/nottyo/robotframework-redislibrary.git 。