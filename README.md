
git clone https://github.com/surath1/machine-learning-llm.git
cd machine-learning-llm
code .
python template.py (update file and folder strecture for 1st time)

pip install -r requirement.txt (all python library)

pip install --upgrade gdown

pip install --upgrade --no-cache-dir gdown  ( fix the issue : ModuleNotFoundError: No module named 'gdown' )

git add .
git commit -m "folder strecture created for llm model"
git push origin main
git status
git ls-files --modified
 
--conda command-----------
conda env list
conda list
python --version
conda env

conda create -n llm-youtube python==3.8 -y
conda activate llm-youtube

---misc-----------
For a specific path: 
    -- conda create -p /path/my_env python=X.Y  /// conda env remove -p /path/my_env
For a specific name: 
    --conda create -n my_env python=X.Y /// conda env remove -n my_env

