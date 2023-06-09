## END TO END ML PROJECT

1. Created Envirornment

```
conda create -p venv python==3.8
```



2. Activate Environment Variable

```
conda activate venv/
```

3. Create the requirements.txt and add the required libraries
```
pandas
numpy
matplotlib
seaborn
Flask
-e .
```

Here -e . will execute the Setupfile


4. Create Setup.py
```
from setuptools import find_packages,setup
from typing import List
HYPHON = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path,"r") as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]  
        if HYPHON in requirements:
            requirements.remove(HYPHON)
    return requirements

setup(
    name="GemPricePrediction",
    version="0.0.1",
    author="Chandan",
    author_email="chandannadve@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
```

5. Install the requirements.txt
```
pip install -r requirements.txt
```
6. Git Repository link
```
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ChandanNadve/gempricepro5.git
git push -u origin main
```