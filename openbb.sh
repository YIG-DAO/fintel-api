conda create -n obb python=3.10 -y
conda activate obb
pip install openbb
pip install "openbb[optimization]"
pip install "openbb[prediction]"