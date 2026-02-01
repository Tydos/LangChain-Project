curl -L -o dataset.zip https://www.kaggle.com/api/v1/datasets/download/shubhammaindola/harry-potter-books
unzip dataset.zip
rm dataset.zip
ls *.txt > index.txt