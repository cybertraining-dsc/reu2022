import glob

script = '''
{name}:
	jupyter nbconvert {name}.ipynb --clear-output --output tmp_{name}.ipynb
	jupyter nbconvert --to python tmp_{name}.ipynb --output tmp_{name}.py
	fgrep -v "# In[ ]:" tmp_{name}.py > {name}.py
	rm -f tmp_{name}.ipynb tmp_{name}.ipynb.py
	@echo "-----------------------------------------------------------"
	-pycodestyle {name}.py
	@echo "-----------------------------------------------------------"
	-autopep8 {name}.py > tmp_{name}.py
	@echo "-----------------------------------------------------------"
	-pycodestyle tmp_{name}.py
	@echo "-----------------------------------------------------------"
'''
for file in glob.glob('*.ipynb'):
	print()
	name = file.replace('.ipynb', '')
	print(script.format(name=name))

for file in glob.glob('*.ipynb'):
	name = file.replace('.ipynb', '')
	print(name, end=' ')


