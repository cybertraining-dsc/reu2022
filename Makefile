IMAGE=tensorflow-2.8.0

.PHONY: book

image:
	cp ${IMAGE}.sif ${IMAGE}-cms.sif
	singularity exec ${IMAGE}-cms.sif pip install cloudmesh-common -U

sbatch:
	# cd experiment/${filename}; sbatch p8.sh
	cd experiment/${filename}; sbatch k80.sh
	# cd experiment/${filename}; sbatch a100.sh
	cd experiment/${filename}; sbatch v100.sh
	cd experiment/${filename}; sbatch p100.sh

grep:
	cd experiment/${filename}; grep '| total' *.log | cut -c -100 > time.txt

watch:
	watch squeue -u ${USER}

cat:
	cd experiment/${filename}; cat *.error *.log

book:
	cd book; make -f Makefile.docker all


bookmanager:
	cd ../bookmanager; make image


