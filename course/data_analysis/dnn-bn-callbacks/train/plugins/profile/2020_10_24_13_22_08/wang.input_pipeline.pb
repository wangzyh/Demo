	��ZD�@��ZD�@!��ZD�@	%�\���?%�\���?!%�\���?"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$��ZD�@
����?A��e@YZ�$�9�?*	q=
ף�N@2F
Iterator::Model	�p��?!�x�ެE@)�2SZK�?1	�E��:@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat�Y5��?!1!�V�?@)GUD��?1���m�9@:Preprocessing2U
Iterator::Model::ParallelMapV2��:TS��?!�8�TD1@)��:TS��?1�8�TD1@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate�X���?!l�Ӕ�0@)��x!~?1A�nZ(@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor�#����n?!����@)�#����n?1����@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip������?! �W!SL@),����n?1�ؚL��@:Preprocessing2�
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice��v� �g?!0{)o�@)��v� �g?10{)o�@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap���a�7�?!�&��n�2@)�t><K�Q?1��S]��?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 1.1% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9%�\���?#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	
����?
����?!
����?      ��!       "      ��!       *      ��!       2	��e@��e@!��e@:      ��!       B      ��!       J	Z�$�9�?Z�$�9�?!Z�$�9�?R      ��!       Z	Z�$�9�?Z�$�9�?!Z�$�9�?JCPU_ONLYY%�\���?b 