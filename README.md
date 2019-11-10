# Find Path In Raster
A QGIS Plugin for finding a path between two points in a raster

### 

#### QGIS Python API

Official documents:   https://www.qgis.org/pyqgis/master/ 

An example:  https://www.qgistutorials.com/en/docs/3/building_a_python_plugin.html 

* The Plugin has been created, just put it into QGIS python plugins directory

* Plugin Builder and Plugin Reloader can be installed in QGIS Plugins

  

#### Pybind11

Plan to use pybind11 to wrap C++ in this python plugin. 

Documents:  https://pybind11.readthedocs.io/en/stable/ 

Pass ND arrays with Numpy:  https://codeday.me/bug/20181003/281971.html 



Install: `pip install pybind11 `

Compile: need 2 versions

Note: In tutorials, installing pybind11 with pip also works. 

Windows .dll

Tutorial:   https://www.jb51.net/article/164588.htm 

##### Linux .so

Tutorial:  https://zhuanlan.zhihu.com/p/52619334 

Compile options: -shared -fPIC \`python3 -m pybind11 --includes\` 

For single .cpp, it can be :  g++ -O3 -Wall -std=c++11 -shared -fPIC \`python3 -m pybind11 --includes\` shortest_path.cpp -o shortest_path\`python3-config --extension-suffix\`

