__base__ = ['./bytetrack_yolox_x_8xb4-80e_crowdhuman-mot20train_test-mot20test.py']

test_evaluator = dict(
    type='NAJMetrics',
    postprocess_tracklet_cfg=[
        dict(type='InterpolateTracklets', min_num_frames=5, max_num_frames=20)
    ],
    format_only=True,
    outfile_prefix='./mot_20_test_res')
