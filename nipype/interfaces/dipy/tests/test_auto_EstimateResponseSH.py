# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.dipy.reconstruction import EstimateResponseSH

def test_EstimateResponseSH_inputs():
    input_map = dict(b0_thres=dict(usedefault=True,
    ),
    fa_thresh=dict(usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_bval=dict(mandatory=True,
    ),
    in_bvec=dict(mandatory=True,
    ),
    in_evals=dict(mandatory=True,
    ),
    in_file=dict(mandatory=True,
    ),
    in_mask=dict(),
    out_prefix=dict(),
    response=dict(),
    save_glyph=dict(usedefault=True,
    ),
    )
    inputs = EstimateResponseSH.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_EstimateResponseSH_outputs():
    output_map = dict(glyph_file=dict(),
    response=dict(),
    )
    outputs = EstimateResponseSH.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

