## setting personal config for github purposes.
# git config --global user.name "ashuamit"
# git config --global user.email "ashuamit786@gmail.com"
# git config user.email "ashuamit786@gmail.com"
# git config user.name "ashuamit"



###A.Train by ordinary way
#1.dependencies
cd training
pip3 install -r requirements.txt

#2.training
cd training
python3 src/train.py experiments/mv2_cpm.cfg

#3.Run the follow command to evaluate the value of your PCKh.(evaluation)
python3 src/benchmark.py --frozen_pb_path=hourglass/model-360000.pb \
--anno_json_path=/root/hdd/ai_challenger/ai_challenger_valid.json \
--img_path=/root/hdd \
--output_node_name=hourglass_out_3




###B.using docker
# Train by nvidia-docker
# Build the docker by the following command:

cd training/docker
docker build -t single-pose .

or

docker pull edvardhua/single-pose

# Then run the following command to train the model:

nvidia-docker run -it -d \
-v <dataset_path>:/data5 -v <training_code_path>/training:/workspace \
-p 6006:6006 -e LOG_PATH=/root/hdd/trained/mv2_cpm/log \
-e PARAMETERS_FILE=experiments/mv2_cpm.cfg edvardhua/single-pose
