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

### self mv2_cpm.py
[Train]
model: 'mv2_cpm'
checkpoint: '/media/ashuamit/bothOS/linux/datasets/poseEstimationForMobileDetails/self/models/mv2_cpm_batch-16_lr-0.001_gpus-1_192x192_experiments-mv2_cpm'
datapath: '/media/ashuamit/bothOS/linux/datasets/our_dataset/dataset_face_with_labels/'
imgpath: '/root/hdd/'
visible_devices: '1'
multiprocessing_num: 16
max_epoch: 10
lr: '0.001'
batchsize: 16
decay_rate: 0.95
input_width: 192
input_height: 192
n_kpoints: 14
scale: 2
identify_occlusion: False
modelpath: '/root/hdd/trained/mv2_cpm_tiny/models'
logpath: '/root/hdd/trained/mv2_cpm_tiny/log'
num_train_samples: 27000
per_update_tensorboard_step: 500
per_saved_model_step: 2000
pred_image_on_tensorboard: False
