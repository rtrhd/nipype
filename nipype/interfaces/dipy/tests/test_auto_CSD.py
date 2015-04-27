# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.dipy.reconstruction import CSD

def test_CSD_inputs():
    input_map = dict(b0_thres=dict(usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_bval=dict(mandatory=True,
    ),
    in_bvec=dict(mandatory=True,
    ),
    in_file=dict(mandatory=True,
    ),
    in_mask=dict(),
    out_fods=dict(),
    out_prefix=dict(),
    response=dict(),
    save_fods=dict(exists=True,
    usedefault=True,
    ),
    sh_order=dict(exists=True,
    usedefault=True,
    ),
    )
    inputs = CSD.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_CSD_outputs():
    output_map = dict(model=dict(),
    out_fods=dict(),
    )
    outputs = CSD.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

