LOCATION=https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/main/content/en/modules/notebooks
# LOCATION=https://raw.githubusercontent.com/cybertraining-dsc/reu2022/main/code/deeplearnning

# %.ipynb : %.py
# jupyter nbconvert $(foreach file, *.ipynb, $(basename ${file})) --clear-output --output tmp.ipynb
# jupyter nbconvert --to python tmp.ipynb --output tmp.py
# fgrep -v "# In[ ]:" tmp.py > $(basename ${file}).py
# rm -f tmp.ipynb tmp.py

PHONY := $(wildcard *.py)
NOTEBOOKS = E534_Higgs_Discovery_A E534_Higgs_Discovery_B E534_Higgs_Discovery_C E534_Higgs_Discovery_D example_mlp_mnist google_colab_mnist_example mlp_mnist mnist_autoencoder mnist_cnn mnist_lstm mnist_mlp_with_lstm mnist_rnn mnist_with_distributed_training mnist_with_pytorch python_warmup

all: requirements $(NOTEBOOKS)


#download:
# 	curl -o google_colab_mnist_example.ipynb ${LOCATION}/google_colab_mnist_example.ipynb
# 	curl -o mlp_mnist.ipynb ${LOCATION}/mlp_mnist.ipynb
# 	curl -o mnist_autoencoder.ipynb ${LOCATION}/mnist_autoencoder.ipynb
# 	curl -o mnist_cnn.ipynb ${LOCATION}/mnist_cnn.ipynb
# 	curl -o mnist_lstm.ipynb ${LOCATION}/mnist_lstm.ipynb
# 	curl -o mnist_mlp_with_lstm.ipynb ${LOCATION}/mnist_mlp_with_lstm.ipynb
# 	curl -o mnist_rnn.ipynb ${LOCATION}/mnist_rnn.ipynb
# 	curl -o mnist_with_distributed_training.ipynb ${LOCATION}/mnist_with_distributed_training.ipynb
# 	curl -o mnist_with_pytorch.ipynb ${LOCATION}/mnist_with_pytorch.ipynb
# 	curl -o python_warmup.ipynb ${LOCATION}/python_warmup.ipynb



example_mlp_mnist:
	jupyter nbconvert example_mlp_mnist.ipynb --clear-output --output tmp_example_mlp_mnist.ipynb
	jupyter nbconvert --to python tmp_example_mlp_mnist.ipynb --output tmp_example_mlp_mnist.py
	fgrep -v "# In[ ]:" tmp_example_mlp_mnist.py > example_mlp_mnist.py
	rm -f tmp_example_mlp_mnist.ipynb tmp_example_mlp_mnist.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle example_mlp_mnist.py
	@echo "-----------------------------------------------------------"
	-autopep8 example_mlp_mnist.py > tmp_example_mlp_mnist.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_example_mlp_mnist.py
	@echo "-----------------------------------------------------------"



google_colab_mnist_example:
	jupyter nbconvert google_colab_mnist_example.ipynb --clear-output --output tmp_google_colab_mnist_example.ipynb
	jupyter nbconvert --to python tmp_google_colab_mnist_example.ipynb --output tmp_google_colab_mnist_example.py
	fgrep -v "# In[ ]:" tmp_google_colab_mnist_example.py > google_colab_mnist_example.py
	rm -f tmp_google_colab_mnist_example.ipynb tmp_google_colab_mnist_example.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle google_colab_mnist_example.py
	@echo "-----------------------------------------------------------"
	-autopep8 google_colab_mnist_example.py > tmp_google_colab_mnist_example.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_google_colab_mnist_example.py
	@echo "-----------------------------------------------------------"



mlp_mnist:
	jupyter nbconvert mlp_mnist.ipynb --clear-output --output tmp_mlp_mnist.ipynb
	jupyter nbconvert --to python tmp_mlp_mnist.ipynb --output tmp_mlp_mnist.py
	fgrep -v "# In[ ]:" tmp_mlp_mnist.py > mlp_mnist.py
	rm -f tmp_mlp_mnist.ipynb tmp_mlp_mnist.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle mlp_mnist.py
	@echo "-----------------------------------------------------------"
	-autopep8 mlp_mnist.py > tmp_mlp_mnist.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_mlp_mnist.py
	@echo "-----------------------------------------------------------"



mnist_autoencoder:
	jupyter nbconvert mnist_autoencoder.ipynb --clear-output --output tmp_mnist_autoencoder.ipynb
	jupyter nbconvert --to python tmp_mnist_autoencoder.ipynb --output tmp_mnist_autoencoder.py
	fgrep -v "# In[ ]:" tmp_mnist_autoencoder.py > mnist_autoencoder.py
	rm -f tmp_mnist_autoencoder.ipynb tmp_mnist_autoencoder.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle mnist_autoencoder.py
	@echo "-----------------------------------------------------------"
	-autopep8 mnist_autoencoder.py > tmp_mnist_autoencoder.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_mnist_autoencoder.py
	@echo "-----------------------------------------------------------"



mnist_cnn:
	jupyter nbconvert mnist_cnn.ipynb --clear-output --output tmp_mnist_cnn.ipynb
	jupyter nbconvert --to python tmp_mnist_cnn.ipynb --output tmp_mnist_cnn.py
	fgrep -v "# In[ ]:" tmp_mnist_cnn.py > mnist_cnn.py
	rm -f tmp_mnist_cnn.ipynb tmp_mnist_cnn.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle mnist_cnn.py
	@echo "-----------------------------------------------------------"
	-autopep8 mnist_cnn.py > tmp_mnist_cnn.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_mnist_cnn.py
	@echo "-----------------------------------------------------------"



mnist_lstm:
	jupyter nbconvert mnist_lstm.ipynb --clear-output --output tmp_mnist_lstm.ipynb
	jupyter nbconvert --to python tmp_mnist_lstm.ipynb --output tmp_mnist_lstm.py
	fgrep -v "# In[ ]:" tmp_mnist_lstm.py > mnist_lstm.py
	rm -f tmp_mnist_lstm.ipynb tmp_mnist_lstm.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle mnist_lstm.py
	@echo "-----------------------------------------------------------"
	-autopep8 mnist_lstm.py > tmp_mnist_lstm.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_mnist_lstm.py
	@echo "-----------------------------------------------------------"



mnist_mlp_with_lstm:
	jupyter nbconvert mnist_mlp_with_lstm.ipynb --clear-output --output tmp_mnist_mlp_with_lstm.ipynb
	jupyter nbconvert --to python tmp_mnist_mlp_with_lstm.ipynb --output tmp_mnist_mlp_with_lstm.py
	fgrep -v "# In[ ]:" tmp_mnist_mlp_with_lstm.py > mnist_mlp_with_lstm.py
	rm -f tmp_mnist_mlp_with_lstm.ipynb tmp_mnist_mlp_with_lstm.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle mnist_mlp_with_lstm.py
	@echo "-----------------------------------------------------------"
	-autopep8 mnist_mlp_with_lstm.py > tmp_mnist_mlp_with_lstm.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_mnist_mlp_with_lstm.py
	@echo "-----------------------------------------------------------"



mnist_rnn:
	jupyter nbconvert mnist_rnn.ipynb --clear-output --output tmp_mnist_rnn.ipynb
	jupyter nbconvert --to python tmp_mnist_rnn.ipynb --output tmp_mnist_rnn.py
	fgrep -v "# In[ ]:" tmp_mnist_rnn.py > mnist_rnn.py
	rm -f tmp_mnist_rnn.ipynb tmp_mnist_rnn.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle mnist_rnn.py
	@echo "-----------------------------------------------------------"
	-autopep8 mnist_rnn.py > tmp_mnist_rnn.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_mnist_rnn.py
	@echo "-----------------------------------------------------------"



mnist_with_distributed_training:
	jupyter nbconvert mnist_with_distributed_training.ipynb --clear-output --output tmp_mnist_with_distributed_training.ipynb
	jupyter nbconvert --to python tmp_mnist_with_distributed_training.ipynb --output tmp_mnist_with_distributed_training.py
	fgrep -v "# In[ ]:" tmp_mnist_with_distributed_training.py > mnist_with_distributed_training.py
	rm -f tmp_mnist_with_distributed_training.ipynb tmp_mnist_with_distributed_training.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle mnist_with_distributed_training.py
	@echo "-----------------------------------------------------------"
	-autopep8 mnist_with_distributed_training.py > tmp_mnist_with_distributed_training.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_mnist_with_distributed_training.py
	@echo "-----------------------------------------------------------"



mnist_with_pytorch:
	jupyter nbconvert mnist_with_pytorch.ipynb --clear-output --output tmp_mnist_with_pytorch.ipynb
	jupyter nbconvert --to python tmp_mnist_with_pytorch.ipynb --output tmp_mnist_with_pytorch.py
	fgrep -v "# In[ ]:" tmp_mnist_with_pytorch.py > mnist_with_pytorch.py
	rm -f tmp_mnist_with_pytorch.ipynb tmp_mnist_with_pytorch.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle mnist_with_pytorch.py
	@echo "-----------------------------------------------------------"
	-autopep8 mnist_with_pytorch.py > tmp_mnist_with_pytorch.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_mnist_with_pytorch.py
	@echo "-----------------------------------------------------------"



python_warmup:
	jupyter nbconvert python_warmup.ipynb --clear-output --output tmp_python_warmup.ipynb
	jupyter nbconvert --to python tmp_python_warmup.ipynb --output tmp_python_warmup.py
	fgrep -v "# In[ ]:" tmp_python_warmup.py > python_warmup.py
	rm -f tmp_python_warmup.ipynb tmp_python_warmup.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle python_warmup.py
	@echo "-----------------------------------------------------------"
	-autopep8 python_warmup.py > tmp_python_warmup.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_python_warmup.py
	@echo "-----------------------------------------------------------"


# *.py: *.ipynb
# 	jupyter nbconvert mlp_mnist.ipynb --clear-output --output tmp.ipynb
# 	jupyter nbconvert --to python tmp.ipynb --output tmp.py
# 	fgrep -v "# In[ ]:" tmp.py > mlp_mnist.py
# 	rm -f tmp.ipynb tmp.py
# 	@echo "-----------------------------------------------------------"
# 	-pycodestyle mlp_mnist.py
# 	@echo "-----------------------------------------------------------"
# 	-autopep8 mlp_mnist.py > tmp.py
# 	@echo "-----------------------------------------------------------"
# 	-pycodestyle tmp.py
# 	@echo "-----------------------------------------------------------"



convert:
	jupyter nbconvert E534_Higgs_Discovery_A.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > E534_Higgs_Discovery_A.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert E534_Higgs_Discovery_B.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > E534_Higgs_Discovery_B.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert E534_Higgs_Discovery_C.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > E534_Higgs_Discovery_C.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert E534_Higgs_Discovery_D.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > E534_Higgs_Discovery_D.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert google_colab_mnist_example.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > google_colab_mnist_example.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert mlp_mnist.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > mlp_mnist.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert mnist_autoencoder.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > mnist_autoencoder.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert mnist_cnn.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > mnist_cnn.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert mnist_lstm.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > mnist_lstm.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert mnist_mlp_with_lstm.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > mnist_mlp_with_lstm.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert mnist_rnn.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > mnist_rnn.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert mnist_with_distributed_training.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > mnist_with_distributed_training.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert mnist_with_pytorch.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > mnist_with_pytorch.py
	rm -f tmp.ipynb tmp.py

	jupyter nbconvert python_warmup.ipynb --clear-output --output tmp.ipynb
	jupyter nbconvert --to python tmp.ipynb --output tmp.py
	fgrep -v "# In[ ]:" tmp.py > python_warmup.py
	rm -f tmp.ipynb tmp.py

requirements:
	pip install -r requirements.txt
