# rich2d-1-snake
A clone of the classic arcade game Snake implemented using
the Rich2D engine

## Dependencies
This project depends on Rich2D
( https://github.com/rdouglascanada/rich2d )

## Build
To compile the project into an executable, install 
[pyinstaller](https://pyinstaller.org/en/stable/installation.html)
and then run

`pyinstaller -F src/main.py --noconsole --name snake.exe --distpath releases`

