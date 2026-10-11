# Evidence index

The current MOD is active experimental and not performance-qualified. Its
active mechanism admits and counts exact generation-bound, block-aligned
shared-prefix cohorts while leaving ordinary paged attention authoritative.

- `evidence/ISSUE13_SHARED_PREFIX_ATTENTION_CLOSURE.md` preserves the historical
  real-NPU component result and its negative decision.
- `evidence/on-off-preflight-20261010/RESULT.json` preserves the earlier inert
  admission rejection and is not an ON/OFF result.
- `evidence/ecpa-contract-20261011/` records the hash-bound Manager/host
  activation contract; it is non-performance evidence.

V250's 31.185% component P50 reduction failed correctness. V262's dedicated
correctness run passed, but its matched timing run failed correctness and every
endpoint missed the 20% crossover gate. The rejected kernels are not dispatched
by version 0.2.0. Candidate and projected-read counters are not device savings.
