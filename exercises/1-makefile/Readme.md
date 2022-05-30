#### Makefile

In this exercise, we will automate the task of installing packages, linting, formatting and testing using Makefile.

1. Create a virutal environment.

```bash
python -m venv ~/practical-ops/exercise/1-makefile-exercise
```

2. Activate the virtual environment.

```bash
source ~/practical-ops/exercise/1-makefile-exercise/bin/activate
```

3. Continuous Integration using Makefile

```bash
make install
make lint
make format
make test
```

