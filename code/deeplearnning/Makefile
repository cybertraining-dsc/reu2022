LOCATION=https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/main/content/en/modules/notebooks

all: requirements download convert

download:
	curl -o E534_Higgs_Discovery_A.ipynb ${LOCATION}/E534_Higgs_Discovery_A.ipynb
	curl -o E534_Higgs_Discovery_B.ipynb ${LOCATION}/E534_Higgs_Discovery_B.ipynb
	curl -o E534_Higgs_Discovery_C.ipynb ${LOCATION}/E534_Higgs_Discovery_C.ipynb
	curl -o E534_Higgs_Discovery_D.ipynb ${LOCATION}/E534_Higgs_Discovery_D.ipynb
	curl -o google_colab_mnist_example.ipynb ${LOCATION}/google_colab_mnist_example.ipynb
	curl -o mlp_mnist.ipynb ${LOCATION}/mlp_mnist.ipynb
	curl -o mnist_autoencoder.ipynb ${LOCATION}/mnist_autoencoder.ipynb
	curl -o mnist_cnn.ipynb ${LOCATION}/mnist_cnn.ipynb
	curl -o mnist_lstm.ipynb ${LOCATION}/mnist_lstm.ipynb
	curl -o mnist_mlp_with_lstm.ipynb ${LOCATION}/mnist_mlp_with_lstm.ipynb
	curl -o mnist_rnn.ipynb ${LOCATION}/mnist_rnn.ipynb
	curl -o mnist_with_distributed_training.ipynb ${LOCATION}/mnist_with_distributed_training.ipynb
	curl -o mnist_with_pytorch.ipynb ${LOCATION}/mnist_with_pytorch.ipynb
	curl -o python_warmup.ipynb ${LOCATION}/python_warmup.ipynb

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
	pip install nbconvert
	pip install ipython
	pip install -r requirements.txt
