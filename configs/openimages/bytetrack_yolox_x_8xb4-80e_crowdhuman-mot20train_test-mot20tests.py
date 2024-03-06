_base_ = ['./bytetrack_yolox_x_8xb4-80e_crowdhuman-mot20train_test-mot20test.py']

test_evaluator = dict(
    type='MOTChallengeMetrics',
    metric=['HOTA', 'CLEAR', 'Identity'],
    format_only=True,
    outfile_prefix='./mot_20_test_res')
