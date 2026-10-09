from pathlib import Path

from vllm_hust_ext.manifest import activation_blocker, load_manifest

import stateaxis_shared_prefix_attention


def test_descriptor_is_discoverable_but_not_activatable() -> None:
    manifest = load_manifest(
        Path(stateaxis_shared_prefix_attention.__file__).with_name(
            "vllm-hust-extension-v0.3.json"
        )
    )
    assert manifest.bundle_id == "org.vllm-hust.stateaxis-shared-prefix-attention"
    assert manifest.schema_version == "0.3-experimental"
    assert activation_blocker(manifest) is not None
