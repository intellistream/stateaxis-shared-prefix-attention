# stateaxis-shared-prefix-attention

Extension ID: `org.vllm-hust.stateaxis-shared-prefix-attention`

Generation-bound admission and evidence boundary for exact shared-prefix
attention cohorts, split from StateAxis issue #13.

Version `0.2.0` is Manifest 0.3 active experimental, default-off, and can only
be enabled through vLLM-HUST Extension Manager/ECPA. It detects and counts
decode rows that share the same physical state generation, have equal context
length, and end on a 128-token block boundary. It does not extend state
lifetime. Unsupported batches keep ordinary paged attention.

The current revision is deliberately `telemetry_only`: it does not dispatch the
historical V250/V262 device kernels. V250 showed a 31.185% component P50
reduction but failed correctness. V262 passed a separate correctness run, then
failed correctness in matched timing and missed the 20% crossover gate at every
endpoint. Candidate counts and projected avoided row-token reads are not HBM or
online performance measurements. The five frozen preregistration/result files
are vendored under `evidence/historical-real-npu-component-gates/` with
repo-local SHA-256 checks. A service ON/OFF run of version 0.2.0 would measure
telemetry overhead rather than the rejected device acceleration.

## Install and validate

```bash
python -m pip install -e '.[test]'
pytest -q
vllm-hust-ext extension inspect org.vllm-hust.stateaxis-shared-prefix-attention
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension check org.vllm-hust.stateaxis-shared-prefix-attention
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext run --dry-run -- /bin/true
```

Omitting the MOD is the OFF arm and leaves StateAxis unchanged. The ON arm is
not performance-qualified until a new exact device path and matched fresh
service repetitions pass the benchmark gates.

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
