_base_ = "./mot_challenge_det.py"

data_root = 'data/crowdhuman/'

train_dataloader = dict(
    batch_size=2,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='annotations/crowdhuman_train.json',
        data_prefix=dict(img='train/'),
        metainfo=dict(classes=('pedestrian', )),
        filter_cfg=dict(filter_empty_gt=True, min_size=32),
        pipeline=train_pipeline))
val_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='annotations/crowdhuman_val.json',
        data_prefix=dict(img='val/'),
        metainfo=dict(classes=('pedestrian', )),
        test_mode=True,
        pipeline=test_pipeline))
val_evaluator = dict(
    type='CocoMetric',
    ann_file=data_root + 'annotations/crowdhuman_val.json',
    metric='bbox',
    format_only=False)
